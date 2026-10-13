import AppKit
import ApplicationServices
import Darwin

// Usage: screen-share SSH_ALIAS [WIDTH HEIGHT]. SSH supplies the host and user;
// credentials stay in Screen Sharing's Keychain, never in this helper.
struct Failure: Error, CustomStringConvertible { let description: String }
func fail(_ message: String) throws -> Never { throw Failure(description: message) }
func run(_ executable: String, _ args: [String]) throws -> String {
    let process = Process(), output = Pipe(), errors = Pipe()
    process.executableURL = URL(fileURLWithPath: executable)
    process.arguments = args; process.standardOutput = output; process.standardError = errors
    try process.run()
    let data = output.fileHandleForReading.readDataToEndOfFile()
    let error = errors.fileHandleForReading.readDataToEndOfFile()
    process.waitUntilExit()
    guard process.terminationStatus == 0 else {
        try fail(String(data: error, encoding: .utf8) ?? "Command failed")
    }
    return String(data: data, encoding: .utf8) ?? ""
}
func attribute(_ element: AXUIElement, _ key: String) -> AnyObject? {
    var value: CFTypeRef?
    return AXUIElementCopyAttributeValue(element, key as CFString, &value) == .success ? value : nil
}
func children(_ element: AXUIElement) -> [AXUIElement] {
    attribute(element, kAXChildrenAttribute) as? [AXUIElement] ?? []
}
func descendants(_ element: AXUIElement, depth: Int = 0) -> [AXUIElement] {
    guard depth < 8 else { return [] }
    return [element] + children(element).flatMap { descendants($0, depth: depth + 1) }
}
func waitUntil(_ seconds: Double, _ condition: () throws -> Bool) throws {
    let deadline = Date().addingTimeInterval(seconds)
    repeat {
        if try condition() { return }
        Thread.sleep(forTimeInterval: 0.3)
    } while Date() < deadline
    try fail("Timed out waiting for Screen Sharing. Check its sign-in or connection dialog, then run again.")
}

let args = Array(CommandLine.arguments.dropFirst())
func main() throws {
    guard args.count == 1 || args.count == 3 else { try fail("Usage: screen-share SSH_ALIAS [WIDTH HEIGHT]") }
    let alias = args[0]
    guard !alias.hasPrefix("-"), alias.range(of: #"^[A-Za-z0-9._-]+$"#, options: .regularExpression) != nil else { try fail("Invalid SSH alias") }
    let cache = FileManager.default.urls(for: .cachesDirectory, in: .userDomainMask)[0].appendingPathComponent("screen-share")
    try FileManager.default.createDirectory(at: cache, withIntermediateDirectories: true)
    let lock = Darwin.open(cache.appendingPathComponent(alias + ".lock").path, O_CREAT | O_RDWR, 0o600)
    guard lock >= 0 else { try fail("Could not create launch lock") }
    defer { Darwin.close(lock) }
    guard flock(lock, LOCK_EX | LOCK_NB) == 0 else { try fail("A screen-sharing launch is already running for this host") }
    let width = args.count == 3 ? Int(args[1]) ?? 0 : 3440
    let height = args.count == 3 ? Int(args[2]) ?? 0 : 1440
    guard width > 0, height > 0, width <= 3840, height <= 2160 else { try fail("Resolution must fit within 3840×2160") }
    guard AXIsProcessTrusted() else { try fail("Enable Accessibility for Tinycast in System Settings → Privacy & Security → Accessibility, then run again.") }
    let config = try run("/usr/bin/ssh", ["-G", alias])
    func sshValue(_ key: String) throws -> String {
        guard let line = config.split(separator: "\n").first(where: { $0.hasPrefix(key + " ") }) else { try fail("SSH config is missing \(key)") }
        return String(line.dropFirst(key.count + 1))
    }
    let host = try sshValue("hostname"), user = try sshValue("user")
    let sshArgs = ["-o", "BatchMode=yes", "-o", "ConnectTimeout=8", "-o", "ServerAliveInterval=5", "-o", "ServerAliveCountMax=2", alias]
    // Fail before opening a session if the remote helper is unavailable.
    _ = try run("/usr/bin/ssh", sshArgs + ["test -x /opt/homebrew/bin/displayplacer"])
    let previous = NSWorkspace.shared.frontmostApplication
    let bundleID = "com.apple.ScreenSharing"
    var activated = false
    defer {
        if activated, let previous, previous.bundleIdentifier != bundleID { previous.activate(options: []) }
    }
    func session() -> AXUIElement? {
        guard let app = NSRunningApplication.runningApplications(withBundleIdentifier: bundleID).first else { return nil }
        let root = AXUIElementCreateApplication(app.processIdentifier)
        var windows = attribute(root, kAXWindowsAttribute) as? [AXUIElement] ?? []
        // Fullscreen session windows may be omitted from AXWindows.
        for key in [kAXMainWindowAttribute, kAXFocusedWindowAttribute] {
            if let value = attribute(root, key), CFGetTypeID(value) == AXUIElementGetTypeID() { windows.append(value as! AXUIElement) }
        }
        return windows.first { window in
            let title = attribute(window, kAXTitleAttribute) as? String ?? ""
            let url = attribute(window, kAXDocumentAttribute) as? String ?? ""
            let isTarget = title == alias || title.hasPrefix(alias + " –") || title == host || url.contains(alias + "%20") || url.contains(alias + ".vncloc")
            return isTarget && descendants(window).contains { (attribute($0, kAXRoleAttribute) as? String) == "AXSharedScreen" }
        }
    }
    if session() == nil, let app = NSRunningApplication.runningApplications(withBundleIdentifier: bundleID).first {
        // AppKit can omit a fullscreen window from AXWindows when its
        // connections browser is key. The Window menu still lists the session.
        let root = AXUIElementCreateApplication(app.processIdentifier)
        if let value = attribute(root, kAXMenuBarAttribute), CFGetTypeID(value) == AXUIElementGetTypeID() {
            let menu = value as! AXUIElement
            if let item = descendants(menu).first(where: {
                let title = attribute($0, kAXTitleAttribute) as? String ?? ""
                return (attribute($0, kAXRoleAttribute) as? String) == kAXMenuItemRole &&
                    (title == alias || title.hasPrefix(alias + " (") || title == host)
            }) {
                activated = true
                app.activate(options: [])
                AXUIElementPerformAction(item, kAXPressAction as CFString)
                Thread.sleep(forTimeInterval: 0.5)
            }
        }
    }
    if session() == nil {
        var components = URLComponents()
        components.scheme = "vnc"; components.host = host; components.user = user
        components.queryItems = [URLQueryItem(name: "quality", value: "high"), URLQueryItem(name: "numVirtualDisplays", value: "1")]
        guard let url = components.url else { try fail("Invalid Screen Sharing URL") }
        _ = try run("/usr/bin/open", ["-g", url.absoluteString])
    }
    try waitUntil(45) { session() != nil }
    guard let window = session() else { try fail("Session disappeared") }
    // Apple's Screen Sharing virtual display has this serial (0x6d767300).
    // Require exactly one; never change physical monitors or another display.
    func remoteDisplay() throws -> (resolution: String, scaling: Bool) {
        let listing = try run("/usr/bin/ssh", sshArgs + ["/opt/homebrew/bin/displayplacer list"])
        let blocks = listing.components(separatedBy: "Persistent screen id:").dropFirst()
        let virtual = blocks.filter { $0.contains("Serial screen id: s1836479232\n") }
        guard virtual.count == 1, let block = virtual.first else { try fail("Expected one Apple Screen Sharing virtual display. Use High Performance with 1 Virtual Display.") }
        guard let line = block.components(separatedBy: "\n").first(where: { $0.hasPrefix("Resolution: ") }) else { try fail("Remote display resolution unavailable") }
        return (String(line.dropFirst(12)), block.contains("Scaling: on\n"))
    }
    func dynamicButton() throws -> AXUIElement {
        guard let button = descendants(window).first(where: {
            (attribute($0, kAXDescriptionAttribute) as? String) == "Dynamic Resolution" ||
            (attribute($0, kAXHelpAttribute) as? String) == "Dynamic Resolution"
        }) else { try fail("Dynamic Resolution control is unavailable. Use a High Performance session.") }
        return button
    }
    func setDynamic(_ enabled: Bool) throws {
        let button = try dynamicButton()
        let on = (attribute(button, kAXValueAttribute) as? NSNumber)?.boolValue ?? false
        if on != enabled {
            guard AXUIElementPerformAction(button, kAXPressAction as CFString) == .success else { try fail("Could not change Dynamic Resolution") }
            Thread.sleep(forTimeInterval: 0.3)
        }
    }
    let expected = "\(width)x\(height)"
    let existing = try remoteDisplay()
    let existingDynamic = (attribute(try dynamicButton(), kAXValueAttribute) as? NSNumber)?.boolValue == true
    if existing.resolution == expected && !existing.scaling &&
        (attribute(window, "AXFullScreen") as? NSNumber)?.boolValue == true &&
        existingDynamic {
        print("\(alias) already ready at \(width)×\(height) in its fullscreen Space.")
        return
    }
    activated = true
    NSRunningApplication.runningApplications(withBundleIdentifier: bundleID).first?.activate(options: [])
    AXUIElementPerformAction(window, kAXRaiseAction as CFString)
    Thread.sleep(forTimeInterval: 0.5)
    // Reset sizing after changing the remote display's Retina mode.
    try setDynamic(false)
    Thread.sleep(forTimeInterval: 0.5)
    let display = try remoteDisplay()
    if display.scaling {
        guard display.resolution.range(of: #"^\d+x\d+$"#, options: .regularExpression) != nil else { try fail("Invalid remote display resolution") }
        _ = try run("/usr/bin/ssh", sshArgs + ["/opt/homebrew/bin/displayplacer 'id:s1836479232 res:\(display.resolution) scaling:off'"])
    }

    let fullscreen = (attribute(window, "AXFullScreen") as? NSNumber)?.boolValue ?? false
    if !fullscreen {
        guard AXUIElementSetAttributeValue(window, "AXFullScreen" as CFString, kCFBooleanTrue) == .success else { try fail("Could not enter full screen") }
    }
    try waitUntil(8) { (attribute(window, "AXFullScreen") as? NSNumber)?.boolValue == true }
    Thread.sleep(forTimeInterval: 1.0)
    try setDynamic(true)
    var verified = false
    for attempt in 0..<3 {
        // A new High Performance session can finish its display negotiation
        // after the window appears. Reapply only while the size is incorrect.
        if attempt > 0 {
            NSRunningApplication.runningApplications(withBundleIdentifier: bundleID).first?.activate(options: [])
            AXUIElementPerformAction(window, kAXRaiseAction as CFString)
            try setDynamic(false)
            Thread.sleep(forTimeInterval: 0.5)
            let current = try remoteDisplay()
            if current.scaling {
                guard current.resolution.range(of: #"^\d+x\d+$"#, options: .regularExpression) != nil else { try fail("Invalid remote display resolution") }
                _ = try run("/usr/bin/ssh", sshArgs + ["/opt/homebrew/bin/displayplacer 'id:s1836479232 res:\(current.resolution) scaling:off'"])
            }
            Thread.sleep(forTimeInterval: 0.5)
            try setDynamic(true)
        }
        let deadline = Date().addingTimeInterval(4)
        repeat {
            let result = try remoteDisplay()
            if result.resolution == expected && !result.scaling { verified = true; break }
            Thread.sleep(forTimeInterval: 0.5)
        } while Date() < deadline
        if verified { break }
    }
    guard verified else { try fail("The remote display did not reach \(expected). Run this command from the matching ultrawide monitor, then retry.") }

    // macOS may briefly visit the new fullscreen Space. Return focus to the
    // app that was active when the launcher command began; leave the session live.
    print("\(alias) ready at \(width)×\(height) in its fullscreen Space.")
}
do {
    try main()
} catch {
    fputs("\(error)\n", stderr)
    exit(1)
}

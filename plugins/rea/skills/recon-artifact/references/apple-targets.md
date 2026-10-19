# Apple artifact and runtime investigation

Use for an IPA, app bundle, Mach-O, framework/shared cache, crash report, or
identified Apple process. Turn the supplied target into an evidence-backed
feature path; choose the next operation from what the artifact actually exposes.

## Resolve the input and available capabilities

- IPA: list archive members first; identify `Payload/*.app/Info.plist` and embedded
  frameworks/extensions. Extract selected files to a fresh analysis directory
  with an archive reader that rejects traversal paths and escaping symlinks.
- `.app` or framework: read `CFBundleExecutable` from its actual `Info.plist`;
  resolve framework version symlinks. Do not guess the executable from the name.
- Crash report: begin with process path, platform, image UUIDs, architecture,
  loaded-image addresses, and implicated stack frame. Distinguish simulator
  processes from host services using process path and device coalition.
- Runtime/process identifier: resolve the exact process and loaded image first.
  If only a bundle identifier is supplied, discover a matching installed app on
  the selected device or simulator; do not choose another task's device.
- Framework/cache: determine its OS build and architecture. Search matching
  public source or symbols before reconstructing already documented behavior.

Inspect exposed REA capabilities and their schemas. Prefer a purpose-built
operation when it supplies the required evidence. Discover installed fallbacks:

```sh
command -v file shasum plutil codesign xcrun unzip strings
xcrun --find otool
xcrun --find nm
xcrun --find dwarfdump
xcrun --find swift-demangle
xcrun --find lldb
command -v class-dump frida frida-ps
```

Missing tools select another evidence route; they are not a reason to install a
toolchain automatically. Check installed help before using version-specific flags.

## Establish identity before interpreting code

The examples below are read-only. Replace quoted placeholders with verified
absolute paths; issue only the commands relevant to the current question.

```sh
unzip -l '/absolute/path/Target.ipa'
plutil -p '/absolute/path/Target.app/Info.plist'
file '/absolute/path/executable'
shasum -a 256 '/absolute/path/executable'
xcrun dwarfdump --uuid '/absolute/path/executable'
xcrun otool -hv '/absolute/path/executable'
xcrun otool -l '/absolute/path/executable'
xcrun otool -L '/absolute/path/executable'
codesign -d --entitlements :- '/absolute/path/Target.app'
```

Record bundle/version/build, file hash, per-slice UUID and architecture, and
platform from build/version load commands. ARM64 alone does not distinguish a
device build from an Apple Silicon simulator build. Keep their findings separate.
Inspect encryption load commands (`cryptid`, region offset/size) before trusting
code bytes. Nonzero encryption status limits static interpretation of that
region; continue with resources, imports, metadata outside it, and any accessible
matching runtime. State exactly which code remains unavailable.

For crashes, match image UUID and architecture before symbolication or address
translation. With runtime address A, loaded image base L, and preferred image
base P, the unslid address is A - L + P. Resolve its containing segment/section;
a virtual address is not a file offset. Use segment mappings to derive an offset
only when the address lies in file-backed bytes. Reject mismatched dSYMs/builds.

## Trace the requested behavior

Start from its concrete anchor: a UI string/resource, log message, public API,
crash frame, file key, request field, or observed callback. Build a short chain:
trigger → dispatch → transformation → framework/storage/IPC → visible result.

```sh
xcrun nm -nm '/absolute/path/executable'
strings -a '/absolute/path/executable'
xcrun otool -ov '/absolute/path/executable'
xcrun swift-demangle '$sObservedMangledSymbol'
```

Filter outputs to the feature and follow references using available REA or
disassembler operations. Record image, address, caller/callee, relevant constants,
and unresolved dispatch. Resource names or strings are leads, not proof that a
function executes. Inspect bundle plists, localized strings, storyboards/nibs,
and extracted assets where they establish the trigger or presentation contract.

- Objective-C: correlate class/category metadata, selector references, and
  implementation addresses. Recover receiver and selector at message sends;
  account for dynamic receiver types instead of treating a selector as one callee.
- Swift: demangle available symbols and use type metadata and call-site evidence.
  Track direct, vtable, witness-table, closure, thunk, and async dispatch when
  encountered. Stripping/inlining may erase source boundaries; follow constants,
  imports, and dataflow rather than inventing a missing source function.
- ABI: recover arguments/results from both caller and callee. Swift aggregate
  lowering, indirect results, context/self, generics, and ownership can invalidate
  a decompiler's C-like signature. A register can hold one part of a value.
  Do not assume every Swift class is Objective-C or every Swift thunk bridges it.
- Framework: follow the specific imported API into the matching framework image.
  If it belongs to a shared cache, use an available extractor compatible with that
  cache version, preserving image provenance. Do not hardcode one cache location.
- IPC: if the framework forwards work, identify service name, message construction,
  fields, response handling, and server handler when accessible. Record Mach/XPC
  and entitlement boundaries. A client stub alone does not establish server logic;
  unavailable server evidence stays unresolved rather than prompting a bypass.

## Select a discriminating runtime observation

When the matching runtime is accessible, capture loaded-image identity and slide
before relating its addresses to static results. In an existing LLDB session:

```text
image list -o -f
image dump sections
image lookup -a 0xOBSERVED_ADDRESS
thread backtrace
```

Choose a narrow breakpoint or instrumentation probe only after stating the
hypothesis it tests, expected input, and distinguishing outputs. Use the observed
module/symbol/address and actual ABI. Prefer passive arguments/results/backtraces
over calling unknown functions or changing return values. Attaching, breakpoints,
and instrumentation may affect timing; record that limitation in the result.

No attach/debug capability, incompatible platform, or encrypted code: continue
static tracing, inspect matching symbols/public source, or construct a small
offline experiment that distinguishes remaining interpretations. Label simulator
observations as simulator evidence; reproduce on a matching device before making
device-specific claims. Do not reset devices or weaken signing as a routine step.

Finish with the supported feature path, reproducible evidence, recovered boundary
contract, and the smallest next observation for each material unknown. Pass this
map to reconstruction/verification with original-artifact results as the oracle.

## Sources and scope

The target-driven workflow above is an independent synthesis. [Apriorit's iOS
article](https://www.apriorit.com/dev-blog/how-to-reverse-engineer-an-ios-app)
inspired its six routes: available source, artifact acquisition, simulator
evidence, crash localization, internal frameworks, and daemon boundaries.
Use the [Swift calling convention](https://github.com/swiftlang/swift/blob/main/docs/ABI/CallingConvention.rst)
for signature lowering and ownership, and [Apple's symbolication guidance](https://developer.apple.com/documentation/xcode/adding-identifiable-symbol-names-to-a-crash-report)
for matching crash images and symbols. Verify target-specific layouts and
tool support; tutorial examples do not establish universal runtime behavior.

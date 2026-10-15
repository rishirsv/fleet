# Platforms

## Contents

- [Apple interfaces](#apple-interfaces)
- [App icons](#app-icons)
- [Lazy SwiftUI collections](#lazy-swiftui-collections)

## Apple interfaces

Confirm the target platform, OS range, SDK, and existing components before
choosing an API.

Keep navigation and conventional actions recognizable. Put distinctive imagery,
voice, typography, and color primarily into content; customize a functional
control only for a concrete need. For Liquid Glass interfaces, use system
materials for navigation instead of imitating them with browser blur recipes.

Custom fonts must support Dynamic Type and reflow. Custom icons keep
platform-specific meanings, including sharing. Test light and dark appearances;
keep logos from displacing useful content.

Choose which toolbar actions remain visible as a window narrows and which move
into an overflow menu. Test actual resizing across window sizes, and inspect
inactive windows as well as focused ones. Use current framework facilities
where they meet the requirement in place of hard-coded dimensions.

On iPad and Mac, use a toolbar search field for search across split-view
columns or results in the detail area; a sidebar field searches that sidebar's
content. A dedicated destination suits app-wide discovery. On iPhone, consider
bottom search placement for reachability. Distinguish a discovery tab from an
entry that immediately opens the keyboard; cancellation dismisses keyboard
input.

## App icons

Keep editable layers and relative positions. Preview the icon with the
platform's actual renderer at small and large sizes, and check it on device
across appearance modes and backgrounds. Check recognition from shape and
contrast without relying on hue. Inspect layer overlap, translucency, and
refraction together, and adapt composition to the platform's icon shape. Keep
the source artwork layered so the system can apply its material effects.

## Lazy SwiftUI collections

Off-screen layout is estimated, so an absolute content offset is not a stable
item identity. Use visible-item relationships for behavior tied to what people
see.

Store selection and editing state that must persist outside temporary row-local
state. Prepare a reasonable row layout before appearance so heights do not
change during scrolling. Filter the data instead of hiding individual views
with conditional output. Check transforms near the visible boundary so
virtualization does not remove content that still appears on screen.

Test scrolling away and back, resizing, mixed row sizes, and navigation to a
distant item.

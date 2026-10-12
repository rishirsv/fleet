# Motion

Use motion to explain change, maintain spatial continuity, give feedback, or
express the interface's character. Preserve established motion conventions when
refining a product. A still screenshot cannot specify timing or behavior.

## Give motion a job

Identify the trigger, what changes, and what the user should understand. Routine
controls should respond promptly; expressive sequences can take more time when
attention to the sequence is part of the experience. Consider repetition: an
entrance that delights once can obstruct a frequently used task.

Default to immediate hover and selection feedback for repeatedly traversed rows,
menus, and tabs, and for frequent keyboard actions. Animate when continuity
explains a meaningful change. Highlights should follow the current pointer or
focus position without delay as the user moves across neighboring items.

Keep unsolicited movement selective. Animate the relationship that matters
instead of giving every section the same entrance. Preserve immediate access to
content and controls, and add no artificial waiting to make an operation seem
substantial.

## Choreograph the change

For a sequence with several stages, describe those stages before tuning
individual elements: what leads, what follows, which elements move together, and
what the final state is. Keep timing and spatial values named and easy to
adjust. Simple feedback needs no storyboard or stage controller.

Anchor menus and expanding surfaces to their source. Preserve identity through
movement, resizing, and shared elements. Make exit paths understandable in
relation to entry; follow the product's navigation model when forward and
backward movement have different meanings. Make exits quieter than entrances.

Use stagger to communicate order or grouping, and bound the total delay so long
lists do not make later items wait. Keep necessary content visible while
decorative animations finish. Coordinate by state or animation completion when
one stage depends on another; independent timers can drift or fire after the
user leaves.

## Choose timing and physics

Choose timing by distance, element size, urgency, and frequency of use. Roughly
100–150ms for small animated feedback and 200–350ms for compact transitions are
starting points for tuning. Larger sequences may need longer; exits should clear
the way promptly without becoming abrupt.

Use duration-based easing for a controlled transition with known endpoints. Use
springs when they improve retargeting, gesture release, or continuous movement.
Tune settling time and overshoot deliberately; bounce can express character but
should not make controls feel imprecise. Choose springs or a particular curve
per transition.

Spring parameters differ by library and platform. Confirm units and parameter
meaning before transferring values; duration and bounce do not convert directly
to stiffness and damping.

## Handle interruption and gestures

Retarget from the currently rendered position. Carry velocity when the animation
system supports it. Rapid toggles, reversal, and repeated activation should
converge on the latest requested state without snaps, queued animations, or
delayed callbacks restoring an old state.

During direct manipulation, track input without easing behind it. Preserve the
grab offset and support cancellation. At release, use position and velocity to
choose a destination consistent with platform behavior, then continue smoothly
into settling motion. Bound resistance and snapping so edges remain
understandable. Keep scrolling and competing gestures usable, and provide
alternatives for essential gesture-only actions.

Separate product state from animated presentation. Define when an exiting
element stops accepting input, where focus moves, and when it can be removed.
Finish or cancel cleanup correctly even if motion is interrupted or disabled.

## Respect motion preferences

Provide a reduced-motion treatment that preserves the state change: often an
immediate update or brief fade in place of translation, zoom, parallax, or
repeated oscillation. Apply it to both CSS and scripted animation. Respond to
preference changes while the interface is open where supported.

Keep progress and completion understandable without spatial motion. Avoid
flashing and provide control over prolonged automatic movement. Coordinate
optional sound or haptics with the causal event and respect their separate
settings.

## Implement

Use the simplest mechanism that supports the behavior: CSS for local state
transitions, a scripted timeline for sequencing, or the project's animation
system for gestures and springs. Prefer transforms and opacity for spatial
effects where they fit, and measure layout, paint, blur, and large-layer costs
on the target device. Use temporary layer hints only when they solve an
observed problem. For native interfaces, use the platform's animation, gesture,
accessibility, and lifecycle facilities.

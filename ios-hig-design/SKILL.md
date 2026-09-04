---
name: ios-hig-design
description: Design iPhone/iPad/SwiftUI interfaces around Apple platform conventions, safe areas, Dynamic Type, VoiceOver, system navigation, materials, and semantic colors.
---
Use for native iOS/iPadOS/SwiftUI UI work or HIG compliance review.

1. Prefer native controls and platform navigation patterns before custom replacements.
2. Respect safe areas, home indicator, Dynamic Island/notch, keyboard, rotation, split view, and device classes relevant to the app.
3. Use Dynamic Type and layouts that survive larger accessibility text sizes without clipping critical content.
4. Use semantic system colors/materials where appropriate so light/dark/high-contrast behavior remains coherent.
5. Give every interactive control a meaningful accessibility label/value/hint when native semantics are insufficient.
6. Keep touch targets comfortable and do not place destructive actions where accidental activation is likely.
7. Use sheets, alerts, navigation stacks, tab bars, toolbars, and context menus according to task depth and platform expectations.
8. Support VoiceOver reading order and focus behavior deliberately.
9. Avoid imitating another platform's navigation merely for cross-platform visual sameness.
10. Validate on representative devices and with accessibility settings enabled.

Platform familiarity is part of usability: custom design should extend iOS conventions, not fight them.

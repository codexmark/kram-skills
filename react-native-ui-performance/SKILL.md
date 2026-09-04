---
name: react-native-ui-performance
description: Build responsive React Native interfaces with disciplined list rendering, image handling, navigation, animation, and native-feeling interaction performance.
---
Use for React Native/Expo mobile UI performance and interaction work.

1. Optimize the interaction path first: taps, gestures, scrolling, keyboard, navigation transitions.
2. Use performant list primitives for large collections and provide stable keys/item measurements when the chosen library benefits from them.
3. Avoid unnecessary re-renders of list rows and expensive inline object/function churn in hot paths when profiling shows impact.
4. Size and cache images appropriately; do not decode huge assets for small surfaces.
5. Keep animations on compositor/native-friendly properties when possible and respect reduced-motion/accessibility preferences.
6. Design for safe areas, keyboard avoidance, touch targets, text scaling, screen readers, and orientation changes.
7. Prefer native platform conventions for navigation and controls unless a custom interaction has a strong product reason.
8. Handle offline/loading/error states explicitly; mobile networks are part of the UX.
9. Test on lower-end representative hardware, not only emulators or flagship devices.
10. Treat Expo/OTA constraints as deployment architecture, not a styling concern.

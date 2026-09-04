---
name: web-ui-quality-gate
description: Final web-interface gate for accessibility, keyboard behavior, responsive integrity, forms, states, navigation, and browser-visible quality.
---
Use this late in the UI workflow, after design and usability corrections, to decide whether a web interface is ready to ship.

## Gate areas

### Accessibility
- semantic HTML first;
- every control has an accessible name;
- labels remain persistent;
- focus is visible and not obscured;
- all essential operations work by keyboard;
- color is never the sole status signal;
- contrast meets the project's accessibility baseline;
- custom dialogs, menus, tabs, comboboxes, and grids follow recognized keyboard/focus patterns;
- reduced-motion preferences are respected;
- 200% zoom and narrow reflow do not destroy task completion.

### States and feedback
Verify applicable states explicitly:
- loading;
- populated;
- empty;
- no results;
- submitting/processing;
- success;
- error;
- retryable failure;
- disabled/read-only.

A local operation must not block the whole application without reason.

### Forms
- preserve entered data on validation/server failure;
- errors appear at the field and/or summary when appropriate;
- errors explain correction, not merely invalidity;
- duplicate submissions are prevented;
- required/optional conventions are consistent;
- destructive actions use proportional confirmation.

### Navigation and context
- browser back/forward behaves predictably;
- important navigable state is reflected in the URL when appropriate;
- filters, search, sort, pagination, and important tabs survive expected navigation;
- deep links open meaningful states;
- breadcrumbs and page titles do not contradict each other.

### Responsive quality
Check at least one narrow phone, tablet/narrow desktop, and wide desktop. Do not accept horizontal whole-page scrolling or desktop layouts merely squeezed smaller.

### Performance-visible UX
- click feedback is immediate;
- skeletons reserve realistic space;
- no avoidable layout jumps;
- heavy secondary features are not loaded eagerly without reason;
- long operations communicate progress or ongoing status.

## Output

Report only actionable findings, preferably as `file:line` or `route/component` when source locations are known. Classify each as `blocker | major | minor`.

The gate fails if any blocker remains or if a major accessibility/task-completion issue is knowingly left without an explicit accepted exception.

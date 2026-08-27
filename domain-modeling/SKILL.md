---
name: domain-modeling
description: Model the domain's real rules in types first, so invalid states are unrepresentable.
---
When designing data structures or APIs:

1. Name things what the domain calls them — the user's vocabulary, not the implementation's.
2. Make invalid states unrepresentable: if two fields cannot both be set, that is two types (or a sum type), not a comment.
3. Parse, don't validate: convert raw input into a rich type once, at the boundary; everything past the boundary trusts the type.
4. Keep IDs, quantities and units distinct types when confusing them would be a real bug.
5. Model behavior where the data is — a struct everyone else reaches into is a domain concept that never got its methods.

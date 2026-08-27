---
name: diagnosing-bugs
description: Binary-search a failure to its cause with evidence at each step, before touching any fix.
---
For any bug or unexplained failure:

1. Observe: capture the exact error, the exact input, the exact environment. Verbatim, not paraphrased.
2. Localize: binary-search the failure — halve the input, disable half the path, add one probe at the midpoint. Each step must produce evidence that shrinks the search space.
3. Explain: state the mechanism ("X happens because Y at file:line") and make a prediction ("removing Z should change the symptom to W").
4. Confirm the prediction BEFORE writing the fix. A fix without a confirmed mechanism is a guess wearing a suit.

Never fix the symptom site if the mechanism lives upstream.

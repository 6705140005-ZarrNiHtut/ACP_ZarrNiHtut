# Assignment 03 — CHANGES

**Name:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  **Student ID:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

This is the written part of your submission. Explain **what you changed and why**, then record your **prompt log**. Keep before/after snippets to a line or two.

\---

## 1 · What I changed

One row per change. Name the OOP concept and say how you checked the behaviour was unchanged.

|#|Code smell in the original|What I changed it to|OOP concept applied|How I verified behaviour was unchanged|
|-|-|-|-|-|
|1|*Products, orders and items were stored as tuples/lists.*|*Created Product, OrderItem, Customer, and Order objects. OrderItem has a Product; Order has a Customer and many OrderItem objects.*|Classes / composition|Ran `python Assignment\\\\\\\\\\\\\\\_03.py` → PASS|
|2|*Quantity and other state had no constructor validation.*|*Constructors validate names, prices, categories, customer names, quantities, customers, and order items.*|Encapsulation|Ran the self-test and checked the constructors.|
|3|Repeated if tier == ... chains calculated discounts and points.|Created Customer, Silver, Gold, and Platinum subclasses with polymorphic discount\_rate() and inherited points() using each tier's multiplier.|Inheritance / polymorphism|Ran the self-test → PASS and checked each tier class.|
|4|calc() mixed calculations with receipt printing.|Order.subtotal(), discount(), tax(), total(), and points() return values; receipt() handles only receipt text.|Separation of concerns / pure methods|Ran the self-test → PASS and verified calculation methods contain no printing.|
|5|Magic numbers and a leftover global were used.|Added named constants such as TAX\_RATE, DISCOUNT\_THRESHOLD, BULK\_QTY\_THRESHOLD, and POINTS\_DIVISOR; the refactored code does not use global.|Clean code / constants|Ran the self-test → PASS.|

## 2 · Short reflection (4–6 sentences)

Which change improved the code the most, and why? Where did keeping the behaviour identical force you to be careful?

> The biggest improvement was changing the repeated membership-tier conditions into subclasses because each tier now contains its own discount behaviour. The Order class also became easier to understand because it is responsible for order calculations while the receipt method handles presentation. Composition makes the relationships clear: an order has a customer and order items, and each item has a product. I had to be careful not to change any business rules, especially the discount threshold, bulk discount, tax, and points calculation. I verified the final result with the provided self-test, which printed PASS - behaviour is unchanged. Your refactor is safe.

\---

## 3 · Prompt log (Level 2 — required)

Record **every** prompt where AI helped. If you wrote a part yourself, say so in one row. AI-shaped code with an empty log does **not** meet the Level-2 policy.

|#|My prompt to the AI|What it suggested (summary)|Accept / reject / edited|How I checked it|
|-|-|-|-|-|
|1|*“Do this class assignment” and provided the Assignment 03 files.*|*Refactor the legacy store into classes while preserving the exact output, including Product, OrderItem, Customer subclasses, Order, constants, and separate receipt printing.*|Edited and verified the generated code.|Ran the provided self-test and got PASS.|
|2|“Complete the assignment using the provided requirements.”|Use inheritance/polymorphism for membership tiers, composition for Order and OrderItem, constructor validation, pure calculation methods, and named constants.|Accepted with edits where needed to match the assignment exactly.|Compared the self-test output against the legacy golden output.|
|3|“Make sure the assignment passes.”|Tested the completed Python file against the built-in behaviour lock.|Accepted.|python Assignment\_03\_completed.py printed PASS.|

**Ownership statement.** *By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*

\---

## 4 · Before-you-submit checklist

* \[ ] `python Assignment\\\\\\\\\\\\\\\_03.py` prints **PASS**.
* \[ ] No tuples / parallel lists left — products, orders, and items are objects.
* \[ ] No `if tier == ...` chains — tiers are a class family.
* \[ ] Calculation methods **return** values and do not `print`; printing is separate.
* \[ ] Constructors validate state; no leftover `global`; magic numbers are named.
* \[ ] The change table and reflection above are filled in.
* \[ ] The prompt log is complete and the ownership statement is signed.


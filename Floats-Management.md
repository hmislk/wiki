# CareCode HIMS: Floats Management

## Overview

**Floats** in CareCode HIMS represent **cash or monetary advances** exchanged between users outside of standard billing operations. They serve two purposes:

1. **Providing seed money** (float) to a cashier at the beginning of a shift.
2. **Temporary monetary exchanges** between users during operations (e.g., lending money for change).

Unlike bill payments, floats are **not tied to any department or patient transaction** but are **fully accounted within the drawer** system.

---

## 1. Characteristics of Floats

* Floats are:

  * **Not linked to any bill**
  * **Not linked to any department**
* Every float is a **user-to-user transfer**, with:

  * Sender (giver)
  * Receiver (taker)
  * Timestamp
  * Amount

---

## 2. Types of Float Transactions

### a. **Receiving Float Before Shift**

* A cashier may **receive a float at the start of a shift** from:

  * Main cashier
  * Accounts staff
  * Another authorised user
* This amount is **added to the drawer** at the time of receipt.

### b. **Float Transfers During Shift**

* Users can **lend or transfer float** during the shift:

  * Example: Cashier A gives change to Cashier B.
* These amounts are also immediately **reflected in both drawers**.

### c. **Returning Float at Shift End**

* Any remaining float received (and not handed over) must be:

  * **Returned during shift handover**
  * Deducted from the sender's drawer at that time

---

## 3. Drawer Integration

* Float transactions **directly affect the drawer balance**:

  * **Receiving float** increases the drawer.
  * **Giving float** decreases the drawer.
  * This ensures **real-time reconciliation** of cash on hand.
* At shift handover, the float total is considered part of the drawer and is **accounted for separately from bill collections**.

---

## 4. Access and Audit

* All float transactions are **audited** with:

  * Sender and receiver details
  * Amount and timestamp
  * Remarks (if applicable)

* Float history is available via:

  * **User-level views** for their own shifts
  * **Manager-level reports** for cross-user analysis

---

## 5. Use Cases

| Scenario                                | Drawer Effect                      |
| --------------------------------------- | ---------------------------------- |
| Receiving float from another user       | Increases receiver’s drawer        |
| Handing float to another user           | Decreases sender’s drawer          |
| Returning unused float at shift closure | Deducted from drawer automatically |



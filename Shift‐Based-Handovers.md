# CareCode HIMS: Shift-Based Handovers

## Overview

CareCode HIMS introduces a secure **shift-based handover mechanism** that ensures all payments collected during a cashier's shift are properly verified, documented, and handed over to an authorised person before the shift ends. The system ties every cashier’s financial activity to their active shift, with no transactions permitted outside an active session (unless explicitly configured).

---

## 1. Shift Sessions

### Starting a Shift

* **Mandatory (by default)**: Users must start a shift to enable transaction capabilities.
* Starting a shift activates the **user’s drawer** and links it to one or more departments as bills are processed.
* This can be disabled by configuration, but is enabled by default to enforce accountability.

---

## 2. Ending a Shift & Handover Requirements

At the end of a shift, a cashier is **required to hand over all funds and transfer activity** before closing.

### What is Handed Over:

* **Payments collected during the shift**:

  * Each bill payment is linked to a specific **department**.
* **Float transfers** received during the shift.
* Together, these match the **current drawer balance**.

---

## 3. Handover Workflow

### Step-by-Step Process:

1. **Shift Details Preview**:

   * Shift date
   * Department(s)
   * Bill counts and totals
   * Payment method breakdown (cash, credit card slips, cheques, bank transactions, IOUs)

2. **Physical Verification**:

   * User manually confirms possession of all non-cash payment instruments.

3. **Enter Cash Denominations**:

   * Denomination-wise cash input is required for reconciliation.

4. **Select Receiver**:

   * Cashier selects a valid user (Bulk Cashier, Main Cashier, or Accounts user).

5. **Submit Handover**:

   * Once submitted:

     * The **sender’s drawer is immediately deducted**.
     * The **receiver’s drawer remains unchanged** until accepted.
     * A separate **handover record** is created.

---

## 4. Receiving a Handover

* Receivers are notified via in-system alerts.
* Each handover must be **individually reviewed and accepted or rejected**.
* They must:

  * Cross-verify cash and other payment slips
  * Accept or reject based on correctness

### On Acceptance:

* The receiver’s drawer is updated.
* Full audit record is saved.

### On Rejection:

* Sender is notified.
* Drawer balance is rolled back accordingly.
* The handover is cancelled and must be reattempted.

---

## 5. Handling Multiple Shifts

* A user may **handover multiple shifts**:

  * Their own earlier sessions
  * Shifts of other users (if allowed)
* **Each shift is handed over as one handover. Multiple handovers per shift is possible.**.
* Receivers maintain a **queue of pending handovers**, each processed independently.

---

## 6. History & Reporting

### For Cashiers:

* View of all past handovers (given or received)
* Status: Pending, Accepted, Rejected
* Access to drawer reconciliation reports

### For Managers:

* Summary reports by department, user, and date
* Analysis of:

  * Shift durations
  * Payment patterns
  * Outstanding or rejected handovers

---

## System Design Notes

* All bills, float transfers, and handovers are linked to departments for precise reporting.
* Drawer balance = shift collections + float transfers – handovers
* Every handover includes:

  * User and receiver identities
  * Timestamp
  * Payment method breakdown
  * Optional remarks

---

## Limitations

* Currently, **managers cannot override or reassign** handovers.
* Rejected handovers must be re-initiated by the original sender.

[Back](https://github.com/hmislk/hmis/wiki/Financial-Management)

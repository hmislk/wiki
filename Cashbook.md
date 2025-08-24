# 🧾 Cashbook in CareCode HIMS

## Overview

The **Cashbook** in CareCode HIMS is a central financial log that records monetary movements resulting from shift handovers, deposits, and reconciliations. It ensures traceability, auditability, and transparency across all levels of operation—**institution**, **site**, and **department**—by linking every transaction to its source.

---

## 🔍 Structure of a Cashbook Entry

Each **cashbook entry** is created under the following structure:

| Field             | Description                                                        |
| ----------------- | ------------------------------------------------------------------ |
| **User**          | The cashier or staff who performed the handover                    |
| **Department**    | The department from which the payment originated                   |
| **Site**          | Derived from the department                                        |
| **Institution**   | Derived from the department                                        |
| **Date**          | Entry date (shifts spanning multiple days are split automatically) |
| **Amount**        | Total of all payment modes for that shift handover                 |
| **Payment Modes** | A breakdown (e.g., Cash, Card, Cheque, eWallet, IOUs)              |

> 🔄 **Note:** Cashbook entries are **only created once per transaction**, even if amounts are re-handovered between users later.

---

## 🧑‍💼 When Entries Are Created

Cashbook entries are generated in the following events:

### ✅ Shift Handover

* Each shift handover creates a **new cashbook entry**.
* The system splits entries if a shift spans across calendar days.
* One entry per user, per department, per day.

### ✅ Bank Deposits / Safe Deposits

* When funds are deposited to bank or safe, a separate entry is added.
* These entries allow downstream tracking of fund movements from drawer to secure holding.

---

## ❌ When Entries Are Not Created

* **User-to-user float or re-handover** transactions do **not** create new cashbook entries.
* The payment is only recorded **once**, at the point of the **original shift handover**.

---

## 🧾 Reporting

The system provides comprehensive reporting views based on the cashbook:

### 1. **Individual Cashbook View**

* View of cashbook entries per user
* Shift-by-shift breakdown
* Payment method breakdown

### 2. **Department Cashbook**

* Aggregated entries per department
* Used for internal audits and departmental financial summaries

### 3. **Site Cashbook**

* Combined cash movements across all departments operating at the same site

### 4. **Institution Cashbook**

* Aggregated view across all sites and departments under a legal entity

Each report supports date range filtering, payment method summarisation, and user-based access permissions.

---

## 💡 Best Practices

* Ensure all **shift handovers are accepted** before relying on cashbook totals.
* Float movements should be reconciled using drawer-level reports, not cashbook.
* Use institution and site cashbooks for **financial audits and bank reconciliations**.

---

[🔙 Back to Financial Management](https://github.com/hmislk/hmis/wiki/Financial-Management)



[Back](https://github.com/hmislk/hmis/wiki)

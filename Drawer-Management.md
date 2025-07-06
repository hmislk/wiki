# CareCode HIMS: Drawer Management

## Overview

The **Drawer** in CareCode Hospital Information Management System (HIMS) replicates a real-world cashier drawer. It tracks and manages all physical and non-physical forms of payments received by a cashier. This system ensures accurate financial reconciliation and enforces accountability and transparency for each cashier’s transactions.

---

## Key Concepts

### 1. **Definition**

A **Drawer** represents a virtual container holding all monetary transactions processed by a cashier. It includes various forms of payments:

* Cash
* Credit Card slips
* Cheques
* Other approved payment methods

Each user can operate **only one drawer** at any given time.

---

### 2. **Transactions & Bills**

* Drawers receive payments when patients are provided services or goods.
* Each **Bill** belongs to a specific **Department** but its **payment is recorded** in the cashier’s drawer.
* Therefore, a **drawer can reflect payments from multiple departments**, even though the drawer itself has no department reference.

---

### 3. **Float Transfers**

* Cashiers can hand over part of their drawer balance to:

  * Another user (e.g., during shift changes)
  * A **bulk cashier** or **accounting department** for safekeeping or further processing.
* Such **float transfers** reduce the drawer balance accordingly.

---

### 4. **Drawer Adjustments**

* Only **system administrators** can manually adjust drawer balances.
* All such adjustments are **audited** with proper logs and trails.
* Adjustments help reconcile mismatches or correct errors.

---

### 5. **Drawer Balance and Reconciliation**

* The system enforces that the **drawer balance in software must match the actual physical drawer** contents.
* It double-checks the accuracy by calculating:

  * Total value of **bills settled**
  * **Returns**
  * **Cancellations**
  * Across **all departments** handled by the cashier

---

### 6. **Views and Reporting**

#### For Cashiers:

* **Current Drawer View**: Displays the current drawer status, **categorized by payment method**.
* **Drawer History**: Allows the user to view historical balances and transactions for audit or verification purposes.

#### For Managers:

* Managers can **view drawers of other users** to monitor balances and ensure accountability.


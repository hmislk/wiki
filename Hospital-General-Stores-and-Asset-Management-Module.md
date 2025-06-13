# Hospital General Stores and Asset Management Module

## Introduction

The Hospital General Stores and Asset Management module is designed to manage the full lifecycle of non-clinical inventory and physical assets across the hospital. It handles procurement, disbursement, usage, and maintenance of consumables (like gloves or detergents), stationeries, medical sundries, and fixed assets such as furniture and medical equipment. By maintaining accurate stock levels and detailed traceability, it supports efficient hospital operations, accountability, and transparency.

---

## Administration

This foundational setup governs the metadata essential for managing items and transactions.

* **Items:** Define all items handled in stores, including consumables and capital assets.
* **Categories:** Organise items into logical categories to simplify searching, reporting, and analytics.
* **Suppliers & Manufacturers:** Maintain updated records of vendors and manufacturers for procurement, warranty tracking, and source referencing.

---

## Store Procurement

Supports item acquisition workflows with approval, tracking, and validation mechanisms.

* **Orders:**

  * Create purchase orders for items.
  * Submit for approval or cancel as needed.
* **Goods Receipt Note (GRN):**

  * Record the physical receipt of ordered goods.
  * Validate quantities and conditions before acceptance.
* **Direct Purchase:**

  * Used when items are procured immediately without a formal order.
* **Returns and Cancellations:**

  * **GRN Return:** Return goods due to damage, defects, or over-supply.
  * **GRN Cancellation:** Void GRN records that were issued erroneously.
  * **Direct Purchase Cancellation / Return:** Revoke direct purchases and optionally return items to vendors.

---

## Disbursement

Facilitates the internal transfer of inventory across hospital units or departments.

* **Request from Units:**

  * Units raise requests for stock items (stationery, cleaning supplies, etc.).
* **Issue to Requests:**

  * Approved requests are fulfilled and issued from stock.
* **Transfer to Other Units:**

  * Move items directly from one unit or store to another.
* **Accept Goods on Receive:**

  * Target units confirm receipt of items, updating both sending and receiving inventories.
* **Returns and Cancellations:**

  * **Cancel Issue to Request:** Roll back mistakenly issued items.
  * **Return from Units:** Units return unused or over-issued items.

---

## Discard and Consumption

Handles deduction of items from inventory for valid non-transfer reasons.

* **Direct Issue:**

  * Issue items without request—typically for immediate operational use.
* **Consumption:**

  * Log general usage (e.g., cleaning agents used by housekeeping).
* **Discard:**

  * Record items disposed of due to expiry, damage, or contamination.
* **Returns and Cancellations:**

  * **Cancel Direct Issue / Consumption / Discard:** Revoke records made in error.
  * **Return Direct Issue:** Register returns for mistakenly issued direct issues.

---

## Patient-Related Issuing

Enables controlled stock usage at the point of care, integrated with inpatient and outpatient modules.

* **Issue to Inpatients:**

  * Record item usage per admitted patient, tied to the ward or bed.
* **Issue to Outpatients:**

  * For items consumed during procedures or visits.
* **Request for Inpatients:**

  * Consultants or nurses request items for specific patients.
* **Returns and Cancellations:**

  * **Cancel Patient Issue / Request:** Correct errors or reversals.
  * **Return Patient Issue:** Return unused items back to stores.

---

## Asset Management / Inventory

Manages physical capital items with maintenance and lifecycle tracking.

* **Asset Registration:**

  * Register furniture, medical equipment, electronics, etc., with full specifications.
* **Service Scheduling:**

  * Create recurring or ad hoc maintenance schedules.
* **Repair Logs:**

  * Track breakdowns, repair work, and vendors involved.
* **Replacements:**

  * Record when an asset is retired and replaced, including links to new asset records.
* **Asset Transfer:**

  * Track when an asset is reassigned to another department or location.
* **Discard and Disposal:**

  * Mark assets as discarded after depreciation or obsolescence, with audit trail.

---

## Reports and Analytics

This section provides insights into usage patterns, stock movement, consumption, asset status, and financial tracking.

* **Stock Balance Reports:** Current inventory levels by item, category, or location.
* **Item Movement Reports:** Detailed history of receipts, issues, returns, and discards.
* **Procurement Reports:** Order status, supplier-wise analysis, and GRN summaries.
* **Disbursement Reports:** What was issued to each unit or patient.
* **Asset Reports:** Inventory of all assets with status (active, under repair, discarded).
* **Consumption Trends:** Time-based reports showing usage rates of key items.
* **Expiry Reports:** Lists items nearing expiry for proactive action.
* **Financial Reports:** Value of stock on hand, procured, or consumed during a period.
* **Audit Trails:** Full history of edits, deletions, and movements for governance.



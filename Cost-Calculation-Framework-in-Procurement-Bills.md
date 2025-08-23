# Cost Calculation Framework in Procurement Bills

This article documents how costs, discounts, taxes, and expenses are recorded and calculated in procurement bills within the HMIS system. It describes both the financial rules and the technical safeguards that ensure consistency, auditability, and correctness.

---

## 1. Core Entities

* **Bill**
  Represents a procurement transaction. Stores bill-level inputs and calculated aggregates.
  Related entity: `BillFinanceDetails`.

* **BillItem**
  Represents each item/pack in the bill. Stores basic user inputs.
  Related entities: `BillItemFinanceDetails`, `PharmaceuticalBillItem`.

* **BillFinanceDetails**
  Stores derived bill-level values (gross, net, totals).

* **BillItemFinanceDetails**
  Stores detailed rates and totals for each line, including both user inputs and calculated values.

* **PharmaceuticalBillItem**
  Records unit/pack details and ties BillItem to stock/medicine catalogue. One-to-one with BillItem for pharmacy.

---

## 2. User Inputs

### Bill Level

* `billDiscount`
* `billTax`
* `billExpensesIncluded` (capitalizable into cost)
* `billExpensesExcluded` (not included in cost)

### Bill Item Level

* `qty` (purchased quantity in units/packs)
* `freeQty` (bonus units/packs at zero price)
* `purchaseRate` (PR)
* `lineDiscountRate` (DR)
* `lineTaxRate` (TR)
* `lineExpenseRate` (ER)
* `retailRate` (RSR)
* `wholesaleRate` (WSR)

---

## 3. Calculated Values

### Line Calculations

* **LineGrossRate** = PR

* **LineNetRate** = PR + TR + ER – DR

* **LineCostRate** = (LineNetTotal ÷ (QtyInUnits + FreeQtyInUnits))

  * Always per unit
  * For packs, multiply by `unitsPerPack` if needed

* **LineGrossTotal** = PR × Qty

* **LineDiscount** = DR × Qty

* **LineTax** = TR × Qty

* **LineExpense** = ER × Qty

* **LineNetTotal** = Gross + Tax + Expense – Discount

### Allocation of Bill Values

Bill-level values (discounts, taxes, expenses) are distributed across items **proportional to each item’s LineNetTotal**.

* FreeQty is excluded from allocation base.
* Stored separately as:

  * `billDiscountValue`
  * `billExpenseValue`
  * `billTaxValue`
  * `billNetValue`

### Final Item Totals

* **GrossTotal** = LineGrossTotal
* **TotalDiscount** = LineDiscount + Allocated BillDiscount
* **TotalTax** = LineTax + Allocated BillTax
* **TotalExpense** = LineExpense + Allocated BillExpense
* **NetTotal** = LineNetTotal + BillNetValue

Per-unit rates = Total ÷ Qty.

---

## 4. Stock Valuation

* **Cost Rate** = (Paid Value ÷ (Qty + FreeQty))
* **ValueAtRetailRate** = RSR × (Qty + FreeQty)
* **ValueAtWholesaleRate** = WSR × (Qty + FreeQty)
* **ValueAtPurchaseRate** = PR × (Qty + FreeQty)
* **ValueAtCostRate** = CostRate × (Qty + FreeQty)

⚠️ Always use **Cost Rate** for inventory valuation and COGS. Never use PR × stock if FreeQty is present, as it overstates value.

---

## 5. Sign Conventions

* **Stock Inflow** = Positive qty
* **Stock Outflow** = Negative qty
* **Expenditure** = Negative value
* **Income** = Positive value

---

## 6. Implementation Safeguards

1. **Pack vs Unit Consistency**

   * Persist a snapshot of `unitsPerPack` and tax regime in each BillItemFinanceDetails.
   * Prevents catalogue changes from altering historical bills.

2. **Allocation Precision**

   * Allocate with high-precision decimal.
   * Round only at currency precision.
   * Distribute rounding remainders deterministically (largest remainder first).
   * Log allocations for audit.

3. **Policy Toggles**

   * Inclusive vs exclusive tax.
   * Bill expense capitalizable vs not.
   * Persist these flags at Bill level.

4. **Edge Cases**

   * **Returns**: reverse with historical cost rate.
   * **Donations**: record zero cost unless fair-value policy applies.
   * **Mixed AMPs/AMPPs**: calculate in units internally.

5. **One-to-One Guarantees**

   * Enforce that each `BillItem` has exactly one `PharmaceuticalBillItem` (pharmacy) or one `PatientInvestigation` (lab).
   * Use DB unique constraints and data-repair routines.

6. **Idempotence**

   * Calculation = pure function of persisted inputs.
   * Re-running must not alter previous results.
   * Stamp each bill with `calculationPolicyVersion`.

---

## 7. Audit & Transparency

* **Order of Operations**
  Document exact calculation sequence and rounding points.
* **Test Suite**
  Maintain canonical sample bills (with freeQty, mixed packs, returns) with expected outputs.
* **Why Panel**
  Expose in UI: for any BillItem, show inputs, allocated values, and rounding logic.


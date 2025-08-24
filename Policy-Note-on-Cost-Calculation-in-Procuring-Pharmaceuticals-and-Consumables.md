## 1. Purpose

This note outlines the standard method of calculating costs in pharmaceutical and consumable procurement, ensuring accuracy, transparency, and compliance with hospital financial management practices.

## 2. Bill and Bill Items

Each purchase is documented in a **Bill**, which may contain multiple **Bill Items**.

* **Bill-level values**: Discounts, taxes, and expenses that apply to the full bill.
* **Item-level values**: Rates and totals that apply to individual items or packs.
* Bill-level values are proportionally distributed across bill items, but not re-summed into the bill to avoid circular dependencies.

## 3. Bill-Level Financial Inputs

User inputs recorded at the Bill level include:

* **Bill Discount**
* **Bill Tax**
* **Bill Expenses included in costing** (e.g., freight, insurance)
* **Bill Expenses not included in costing** (e.g., administrative charges)

## 4. Bill-Level Calculated Values

* **Gross Total** = Sum of Line Net Totals
* **Net Total** = Gross Total + Bill Tax + Bill Expenses (included in costing) – Bill Discount

## 5. Item-Level Financial Inputs

Each Bill Item may be recorded in units (AMP) or packs (AMPP). Inputs include:

* Quantity (Qty)
* Free Quantity (additional free stock)
* Purchase Rate (per unit or pack)
* Line Discount Rate
* Line Tax Rate
* Line Expense Rate (e.g., freight, handling applied at line level)
* Retail Rate (for sales)
* Wholesale Rate (for bulk sales)

## 6. Item-Level Calculated Values

* **Line Gross Rate** = Purchase Rate
* **Line Net Rate** = Gross Rate + Tax – Discount
* **Line Cost Rate** = Net Rate ÷ Quantity (always calculated per unit, with packs converted into units)

Totals:

* **Line Gross Total** = Purchase Rate × Qty
* **Line Discount** = Discount Rate × Qty
* **Line Tax** = Tax Rate × Qty
* **Line Expense** = Expense Rate × Qty
* **Line Net Total** = Gross Total + Tax + Expense – Discount

## 7. Allocation of Bill-Level Values

Bill-level values are distributed across Bill Items **proportionally to each item’s Line Net Total**.

* Free quantities are excluded from allocation (as overheads apply only to paid quantities).

Allocated values include:

* Bill Discount Value
* Bill Expense Value
* Bill Tax Value

## 8. Final Totals for Each Item

* **Gross Total** = Line Gross Total
* **Total Discount** = Line Discount + Allocated Bill Discount
* **Total Tax** = Line Tax + Allocated Bill Tax
* **Total Expense** = Line Expense + Allocated Bill Expense
* **Net Total** = Line Net Total + Allocated Bill Net Value

Corresponding per-unit rates are calculated by dividing these totals by the quantity.

## 9. Stock Valuation

* Stock must always be valued at the **Cost Rate**, not Purchase Rate.
* Free quantities are included when calculating cost per unit, as they dilute the effective unit cost.
* Example:

  * Purchased: 1,000 units @ Rs. 10 each + 100 units free
  * Payment = Rs. 10,000
  * Stock = 1,100 units
  * **True Cost Rate** = 10,000 ÷ 1,100 = Rs. 9.09 per unit
  * Using Purchase Rate × Stock (1,100 × 10) would incorrectly value stock at Rs. 11,000.

## 10. Sign Conventions

* **Stock inflow** = Positive quantity
* **Stock outflow** = Negative quantity
* **Expenditure** = Negative value
* **Income** = Positive value

---

✅ This structure provides a clear and auditable costing framework, suitable for application in hospital pharmacies, stores, and finance divisions. It ensures that:

* Procurement costs are correctly allocated,
* Free stock is properly accounted for, and
* Stock valuations remain accurate for decision-making, pricing, and reporting.



[Back](https://github.com/hmislk/hmis/wiki)

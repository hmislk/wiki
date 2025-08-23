## Purchase Structure

In the procurement of pharmaceuticals and consumables, cost calculation is critical to ensure accuracy and transparency in financial management. The following structure outlines the process:

### Bill & Bill Items

Each purchase is documented in a bill containing multiple bill items. Each bill item corresponds to an individual item or pack. There are values directly related to the Bill or Bill Items. The sum of Bill Item values may be recorded at the bill level. Also, bill-level values may be proportionally divided among bill items and recorded at Bill Item level. Care must be taken to avoid circular dependencies in recording the values.

### Bill

There are values recorded at the Bill level related to costing.

#### User Inputs useful for costing

* Bill Discount
* Bill Tax
* Bill Expenses included for costing
* Bill Expenses not included for costing

#### Calculated values related to Bill

* Sum of Line Net Totals
* Sum of Line Discounts
* Sum of Line Taxes
* Gross Total (= sum of Line Gross Totals)
* Net Total (= sum of Line Net Totals + Bill Tax + Bill Expenses included for costing – Bill Discount)

Please note that the bill net total already reflects line discounts, line taxes, and line expenses through their contribution to the Line Net Total.

#### Backend Entities used to record data

* Bill
* BillFinanceDetails

---

### Bill Items

Each bill item consists of:

* **Item**: The individual item (AMP) or pack (AMPP). Different methods are used in costing calculations depending on whether the item is AMP (units) or AMPP (packs).

#### User inputs that contribute to costing

* **Quantity (Qty)**: Number of units/packs purchased.
* **Free Quantity**: Additional units/packs provided at no charge.
* **Purchase Rate (PR)**: Rate at which the item is purchased (per unit for AMP, per pack for AMPP).
* **Line Discount Rate (DR)**
* **Line Tax Rate (TR)**
* **Line Expense Rate (ER)**
* **Retail Rate (RSR)**
* **Wholesale Rate (WSR)**

#### Calculated values (line-level, not user-editable)

##### Rates

* **Line Gross Rate** = Purchase Rate.
* **Line Net Rate** = Line Gross Rate + Line Tax Rate + Line Expense Rate – Line Discount Rate.
* **Line Cost Rate** = Line Net Total ÷ Quantity in Units. Always recorded in units. If needed for a pack, multiply by units per pack.

##### Totals

* **Line Gross Total** = PR × Qty
* **Line Discount** = DR × Qty
* **Line Tax** = TR × Qty
* **Line Expense** = ER × Qty
* **Line Net Total** = Line Gross Total + Line Tax + Line Expense – Line Discount

---

### Values Calculated from Bill-Related Inputs

Bill-level values (discount, tax, expenses) are divided proportionally to the line net totals of each line. These are then divided by quantities to get per-unit rates. Free quantities are not included in this distribution. These allocated values are not summed again to form bill totals, to avoid circular dependency.

##### Allocated Values per Line

* **Bill Discount Value**
* **Bill Expense Value**
* **Bill Tax Value**
* **Bill Gross Value** = zero
* **Bill Net Value** = Bill Expense Value + Bill Tax Value – Bill Discount Value

##### Allocated Rates per Line

* **Bill Discount Rate** = Bill Discount Value ÷ Qty
* **Bill Expense Rate** = Bill Expense Value ÷ Qty
* **Bill Tax Rate** = Bill Tax Value ÷ Qty
* **Bill Gross Rate** = zero
* **Bill Net Rate** = Bill Net Value ÷ Qty

---

### Total Line Values

Calculated as line values + allocated bill values:

* **Gross Total** = Line Gross Total
* **Total Discount** = Line Discount + Bill Discount Value
* **Total Tax** = Line Tax + Bill Tax Value
* **Total Expense** = Line Expense + Bill Expense Value
* **Net Total** = Line Net Total + Bill Net Value

### Total Line Rates

Calculated as totals ÷ Qty:

* **Gross Rate**
* **Total Discount Rate**
* **Total Tax Rate**
* **Total Expense Rate**
* **Net Rate**

---

### Valuation for Decision-Making

* **Value At Retail Rate** = RSR × (Qty + Free Qty)
* **Value At Wholesale Rate** = WSR × (Qty + Free Qty)
* **Value At Purchase Rate** = PR × (Qty + Free Qty)
* **Value At Cost Rate** = CR × (Qty in Units + Free Qty in Units)

---

### Bill Item Related Entities

* **BillItem**: Basic user inputs.
* **BillItemFinanceDetails**: Stores user inputs and calculations, including pack size in units and rates.
* **PharmaceuticalBillItem**: Records mainly in units; not generally used for user inputs.

---

### Sign Conventions

* Rates/discounts are positive.
* Stock going out = negative quantity.
* Stock coming in = positive quantity.
* Money spent = negative value.
* Money earned = positive value.

---

## Programming Logic

### When a user changes a line-related input

1. Update values in `BillItem` or `BillItemFinanceDetails`.
2. Update pack/unit conversions.
3. Recalculate line values.
4. Update bill-level aggregates that depend on line values.
5. Do **not** redistribute bill-level values at this stage.

### When a user changes a bill-related input

1. Update the input in `Bill` or `BillFinanceDetails`.
2. Recalculate bill-level values.
3. Redistribute bill-level values proportionally to bill items.
4. Recalculate bill item total values (line + bill allocations).


Here’s the add-on section you can paste at the end. It explains exactly **where** each value should be assigned (Bill vs BillFinanceDetails) and **when** to read/write them, without changing your variable names.


## Assignment: Bill vs BillFinanceDetails

All **user‑entered bill inputs** live on `Bill` and are the single source of truth. All **calculated bill‑level numbers** live on `BillFinanceDetails` and are never edited directly by users.

### A. User inputs (authoritative fields → Bill)

Assign these on create/edit and bind UI directly to `Bill`:

* Bill Discount → `Bill`
* Bill Tax → `Bill`
* Bill Expenses included for costing → `Bill`
* Bill Expenses not included for costing → `Bill`
* Policy flags that affect interpretation (e.g., tax inclusive/exclusive, whether expenses are capitalizable) → `Bill`

Read them from `Bill` whenever you recalculate lines or allocations. Do not duplicate these as editable fields in `BillFinanceDetails`. If you keep cached copies in `BillFinanceDetails` for performance, overwrite them on every recompute and never expose them for editing.

### B. Line‑driven aggregates (calculated → BillFinanceDetails)

After recalculating all lines (in `BillItemFinanceDetails`) and before/after allocation, write these **computed** totals to `BillFinanceDetails`:

* Sum of Line Gross Totals (pre‑allocation) → `BillFinanceDetails`
* Sum of Line Net Totals (pre‑allocation) → `BillFinanceDetails`
* Sum of Line Discounts, Sum of Line Taxes, Sum of Line Expenses (pre‑allocation) → `BillFinanceDetails`
  These are pure aggregates of line math, used as the allocation base and for audit. They are recomputed, not edited.

### C. Allocation results rolled up (calculated → BillFinanceDetails)

Once you distribute bill‑level inputs to lines and store each line’s allocated values in `BillItemFinanceDetails`, roll them back up and assign to `BillFinanceDetails`:

* Allocated Bill Discount Total = Σ per‑line allocated bill discount → `BillFinanceDetails`
* Allocated Bill Tax Total = Σ per‑line allocated bill tax → `BillFinanceDetails`
* Allocated Bill Expense Total = Σ per‑line allocated bill expense → `BillFinanceDetails`
* Rounding remainder note/flag (if any) → `BillFinanceDetails`
  These totals are derived from line allocations; they must equal the original Bill inputs within rounding tolerance. Do not write these back into `Bill`.

### D. Final bill totals for reporting (calculated → BillFinanceDetails)

After allocation and final per‑line totals are known, compute bill‑level reporting numbers and assign to `BillFinanceDetails`:

* Bill Gross Total = Σ Line Gross Total → `BillFinanceDetails`
* Bill Discount Total = Σ (Line Discount + Allocated Bill Discount) → `BillFinanceDetails`
* Bill Tax Total = Σ (Line Tax + Allocated Bill Tax) → `BillFinanceDetails`
* Bill Expense Total = Σ (Line Expense + Allocated Bill Expense) → `BillFinanceDetails`
* Bill Net Total = Σ (Line Net Total + Bill Net Value per line) → `BillFinanceDetails`
  These are the numbers to show on printed bills/reports. They are not a new set of inputs.

### E. Save/approve sequence (where writes happen)

1. User edits bill inputs → write to `Bill`.
2. Recalculate all lines → write to `BillItemFinanceDetails`.
3. Aggregate pre‑allocation line sums → write to `BillFinanceDetails`.
4. Allocate bill inputs to lines → write allocated amounts to each `BillItemFinanceDetails`.
5. Aggregate allocated totals and final bill totals → write to `BillFinanceDetails`.
6. On approve/post, read the **Cost Rate** for stock valuation from line results and post inventory/GL. Do not modify `Bill`.

### F. Reads (who consumes what)

* UI forms and validations read bill inputs from `Bill`.
* Allocation engine reads bill inputs from `Bill` and line bases from `BillItemFinanceDetails`.
* Reports/prints read final totals from `BillFinanceDetails`; line detail from `BillItemFinanceDetails`.



[Back](https://github.com/hmislk/hmis/wiki)

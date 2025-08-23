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


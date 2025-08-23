# Costing Logic: Triggers, Order of Operations, and Actions

## A. Notation & Entities

* Bill → `Bill`, details in `BillFinanceDetails` (BFD)
* Line → `BillItem`, details in `BillItemFinanceDetails` (BIFD)
* Pharma line snapshot → `PharmaceuticalBillItem` (PBI) with `unitsPerPack`
* “QtyInUnits” means `qty × unitsPerPack` for AMPP; for AMP it equals `qty`.

---

## B. Core Formulas (used by multiple steps)

1. **LineGrossRate** = `purchaseRate`
2. **LineNetRate** = `purchaseRate + lineTaxRate + lineExpenseRate – lineDiscountRate`
3. **LineGrossTotal** = `purchaseRate × qty`
4. **LineDiscount** = `lineDiscountRate × qty`
5. **LineTax** = `lineTaxRate × qty`
6. **LineExpense** = `lineExpenseRate × qty`
7. **LineNetTotal** = `LineGrossTotal + LineTax + LineExpense – LineDiscount`
8. **QtyInUnits** =

   * AMPP: `qty × unitsPerPack`
   * AMP: `qty`
   * `freeQtyInUnits` defined likewise
9. **LineCostRate (per unit)** = `(LineNetTotal ÷ (QtyInUnits + FreeQtyInUnits))`
10. **Allocation Base** = `LineNetTotal` (free quantities excluded from base)
11. **Allocated amounts** per line = `(LineNetTotal ÷ Σ LineNetTotal of the bill) × (bill‑level amount)`
12. **Final per-line totals**

* `TotalDiscount = LineDiscount + AllocBillDiscount`
* `TotalTax = LineTax + AllocBillTax`
* `TotalExpense = LineExpense + AllocBillExpense`
* `GrossTotal = LineGrossTotal`
* `NetTotal = LineNetTotal + (AllocBillTax + AllocBillExpense – AllocBillDiscount)`

13. **Per-line rates** (display) = corresponding totals ÷ `qty` (not including free).
14. **Stock Valuation CostRate** = `(Σ(LineNetTotal) + Σ(AllocBillTax + AllocBillExpense – AllocBillDiscount)) ÷ (Σ(QtyInUnits + FreeQtyInUnits))`.

Rounding: compute with high‑precision decimal; round to currency at the **last step of each level** (line totals; then bill totals). Distribute any allocation rounding remainder by largest fractional part.

---

## C. Global Invariants (validate on every save/approve)

* Exactly one PBI per pharmacy `BillItem`; error if 0 or >1.
* For lab/collection items: exactly one `PatientInvestigation` per relevant `BillItem`.
* Snapshot values (`unitsPerPack`, tax regime, inclusive/exclusive flags) must exist on BIFD/PBI.
* Signs: in‑stock = +qty; out‑stock = –qty; expenditure = negative value; income = positive.
* Idempotence: Re-running calculations with the same inputs must produce identical BIFD/BFD.

---

## D. Event Matrix — “What to do when …”

### D1) User changes a **line‑level input**

Inputs: `qty`, `freeQty`, `purchaseRate`, `lineDiscountRate`, `lineTaxRate`, `lineExpenseRate`, AMPP↔AMP selection.
**Actions (in order):**

1. Ensure PBI exists (pharmacy) and snapshot `unitsPerPack` is present; refresh `QtyInUnits/freeQtyInUnits`.
2. Recompute **line calculations** using Section B (1–9). Write to BIFD.
3. **Do NOT** recalculate or redistribute bill‑level allocations yet (they depend on all lines).
4. Recompute **bill aggregates driven by lines** in BFD (Σ LineGrossTotal, Σ LineNetTotal, etc.).
5. If **any bill‑level input** (discount/tax/expense) is non‑zero, go to D3 to reallocate; else stop.

   * Rationale: allocation base changed with this line; allocations must be refreshed.

### D2) User deletes a **line**

**Actions:**

1. Remove/retire BIFD and associated PBI/PI as per domain rule.
2. Recompute bill aggregates (Σ across remaining lines).
3. Re‑run **allocation** across remaining lines (D3).
4. Recompute final line totals and BFD.

### D3) User changes a **bill‑level input**

Inputs: `billDiscount`, `billTax`, `billExpensesIncluded`, `billExpensesExcluded`, or tax inclusive/exclusive flag.
**Actions (in order):**

1. Persist bill‑level input(s) to `Bill`/BFD; confirm policy flags snapshot on `Bill`.
2. Ensure **all lines have up‑to‑date LineNetTotal** (if not, recompute D1 for affected lines).
3. Compute **Allocation Base** = Σ `LineNetTotal` for all lines (exclude free qty).
4. Allocate `billDiscount`, `billTax`, and `billExpensesIncluded` to each line:

   * `alloc = baseShare × billAmount` (Section B‑11), round and reconcile remainder.
   * Write to BIFD fields (allocated discount/tax/expense).
5. For each line, recompute **Final Item Totals** and per‑line rates (Section B‑12, B‑13).
6. Update BFD **Net Total** using line totals (no circular re‑sum of allocations back to bill inputs).
7. Recompute **Stock Valuation CostRate** (Section B‑14) if this bill affects inventory valuation.

### D4) User toggles **AMP ↔ AMPP** or changes **unitsPerPack**

**Actions:**

1. Snapshot `unitsPerPack` to BIFD/PBI.
2. Recompute `QtyInUnits/freeQtyInUnits`.
3. Recompute **line calculations** (B 1–9).
4. Recompute bill aggregates; then **reallocate bill‑level values** (D3).
5. Update final line totals and BFD.

### D5) User changes **inclusive/exclusive tax** policy on the bill

**Actions:**

1. Persist policy flag on `Bill`.
2. Reinterpret `lineTaxRate`/`purchaseRate` as per policy, recompute **all lines** (B 1–9).
3. Recompute bill aggregates → **reallocate** (D3) → finalize.

### D6) Approving/Posting the bill (finalize)

**Pre‑checks:**

* All invariants hold (one PBI/PI per line, non‑null snapshots, no negative `qty` on procurement, etc.).
* Allocations exist and sum to bill inputs within rounding tolerance.
  **Actions:**

1. Lock bill; re-run full compute path (lines → bill aggregates → allocations → totals).
2. Persist final BIFD and BFD with policy/version stamp and rounding notes.
3. Post inventory: increase stock by `(QtyInUnits + FreeQtyInUnits)` at **CostRate**.
4. Post GL entries according to mapping (inventory, creditors/cash, taxes, discounts, capitalized expenses).

### D7) Returns/Credit Notes for a received bill

**Actions:**

1. Identify original line(s) and **use their historical CostRate** and historical allocation proportions.
2. Create return line(s) with negative quantities; reverse **both** line components and their allocated bill components proportionally.
3. Recompute bill aggregates of the return document; do **not** recalc original bill.
4. Post inventory decrease at historical CostRate; post GL reversals.

### D8) Donations / zero‑price receipts

**Actions:**

1. If policy = zero‑cost: set CostRate = 0; still compute quantities.
2. If policy = fair‑value capitalization: set valuation amount; fill BIFD “valuation source”; CostRate = valuation ÷ (QtyInUnits + FreeQtyInUnits).
3. Post inventory accordingly; no creditors.

### D9) Editing a **historical bill**

**Actions:**

1. Disallow edits after posting unless a **revision** document pattern is used (debit/credit notes).
2. If edit is permitted: recalc using the **original policy/version snapshot** stored on the bill to avoid reinterpretation with new rules.
3. Recompute and re‑post differences only.

---

## E. Save‑Time Validation Checklist (fail fast)

* Missing or multiple PBI/PI for lines that require them.
* `unitsPerPack` null for AMPP.
* Negative or zero `qty` for procurement (except returns).
* Allocation remainder not reconciled to zero at bill level.
* Sum of allocated components ≠ bill inputs (beyond rounding tolerance).
* Stock valuation recomputed and consistent with line totals.

---

## F. Suggested Function Boundaries (idempotent)

* `recalculateLine(BillItem bi)` → updates BIFD for that line (B 1–9)
* `recalculateBillAggregates(Bill bill)` → writes BFD Σ of line‑driven values
* `allocateBillValuesToLines(Bill bill)` → writes allocated amounts to each BIFD
* `recalculateLineFinalTotals(BillItem bi)` → applies Section B‑12/13
* `recalculateStockValuation(Bill bill)` → computes Section B‑14 for inventory posting
* `validateBill(Bill bill)` → runs invariant and rounding checks
* `finalizeAndPost(Bill bill)` → D6 sequence (locks, recompute, persist, post)

Each function must be a pure function of persisted inputs; no hidden state. Calling the whole pipeline twice must yield identical numbers.



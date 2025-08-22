This document outlines the semantics and usage of each field within the `BillItemFinanceDetails` entity of the CareCode HIMS. This class captures the financial calculations per bill item, covering entered values, computed rates, and allocations from the overall bill.

Bill - 
Subclass(BilledBill, CancelledBill, RefundBill, PreBill)
BillType - 

BillTypeAtomic

total, netTotal, discount
(Minus when money goes out)

StockBill - Depricate
BillFinanceDetails -



## 1. **Units and Packs**

* **Ampp / Vmpp items**: User-entered quantities are in *packs*. System stores pack values directly, and unit values are calculated as:

  ```
  quantityByUnits = quantity × unitsPerPack
  ```
* **Amp / Vmp items**: Quantities are entered and stored in *units*. No further conversion required.
* **All fields labeled with `ByUnits`** store unit values, regardless of the item type.

## 2. **Rates and Totals**

Each financial component (gross, net, discount, tax, cost, expense) is tracked at 3 levels:

| Level | Prefix Used | Notes                                                                 |
| ----- | ----------- | --------------------------------------------------------------------- |
| Line  | `line*`     | Calculated directly from user input per bill item                     |
| Bill  | `bill*`     | Portion of bill-level value allocated to this line (e.g. tax/expense) |
| Total | `total*`    | Final value = line + bill allocation                                  |

**Application Order**:
`line → bill → total`

If there are no bill-level values, then:
`lineTotal = total`

## 3. **Rate vs Value Conventions**

* `rate` fields always represent the **rate per entered quantity** (i.e., per pack or per unit depending on the item).
* `value = rate × quantity`

### Examples:

* `lineGrossRate × quantity = lineGrossTotal`
* `lineNetRate × quantity = lineNetTotal`

## 4. **Cost Rate**

* `lineCostRate` is calculated in **units** for all items.
* Formula:

  ```java
  lineCostRate = totalPurchaseValueInUnits / (quantityInUnits + freeQuantityInUnits)
  ```
* This is **explicitly** calculated and assigned in the controller; it is **not** derived within the entity.

## 5. **Return Handling**

* Returns are processed as **new bills** with their own `BillItemFinanceDetails`.
* Original quantities returned are stored in:

  * `returnQuantity`, `returnFreeQuantity`, `totalReturnQuantity`
* Return rates **may differ** from original bill rates.
* Only returned quantities are stored and **accumulated** after each return.

## 6. **Profit Margin**

* Calculated in the controller.
* Common formula:

  ```java
  profitMargin = valueAtRetailRate - valueAtCostRate
  ```

## 7. **Allocation of Bill Components**

* Bill-level expenses, taxes, and discounts (e.g., transport, promotional discounts) are **not linked to individual items**.
* They are proportionally allocated to each item based on:

  ```java
  proportion = lineNetTotal / sum(lineNetTotal of all items)
  ```
* This applies to:

  * `billDiscount`, `billExpense`, `billTax`
  * And their respective rate fields

[Back](https://github.com/hmislk/hmis/wiki/Code-Concepts-for-Developers)

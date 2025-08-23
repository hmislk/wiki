## Purchase Structure

In the procurement of pharmaceuticals and consumables, cost calculation is critical to ensure accuracy and transparency in financial management. The following structure outlines the process:

### Bill & Bill Items
Each purchase is documented in a bill containing multiple bill items. Each bill item corresponds to an individual item or pack. There are values directly related to Bill or Bill Items. The sum of Bill Item Values may be recorded at the bill level. Also, the bill level values may be proportionally divided among bill items and recorded at Bill Item Level. But we have make sure that there are not circular dependencies in recording the values. 

### Bill
There are values recorded at the Bill level related to costing.

#### User Inputs useful for costing are as follows.
* Bill Discount
* Bill Tax
* Bill Expenses, those are included for costing
* Bill Expenses, those are NOT included for costing

#### The calculated values related to Bill are as follows
* Sum of Line Net Totals
* Sum of Line Discounts
* Sun of Line Taxes
* Gross Total (=sum of Line Net Totals)
* Net Total (=sum of Line Net Total + Bill Tax + Bill Expenses, those are included for costing - Bill Discount)

Please note that the bill net total includes line discounts, line taxes, and line discounts as they contribute to the Line Net Total

#### The backend Entities used to record data are as follows
* Bill
* BillFinanceDetails 


### Bill Items
Each bill item consists of:
- **Item**: The individual item (AMP) or pack (AMPP). There is totally different methods used in costing calculations, depending on the selection is a AMP(by Units) or AMPP(by Packs)

#### The user inputs that contribute to costing as as follows
- **Quantity (Qty)**: The total number of units/packs purchased. The user can change this.
- **Free Quantity**: Additional units provided at no charge in units/packs. The user can change this.
- **Purchase Rate (PR)**: The rate at which the item is purchased. It is for a Unit in case of AMP or for a Pack in case of AMPP.
- **Line Discount Rate (DR)**: Discount rate applicable to the specific line item unit/pack.  It is for a Unit in case of AMP or for a Pack in case of AMPP.
- **Line TAX Rate (TR)**: Tax rate applicable to the specific line item unit/pack.  It is for a Unit in case of AMP or for a Pack in case of AMPP.
- **Line Expense Rate (ER)**: Expense rate applicable to the specific line item unit/pack.  It is for a Unit in case of AMP or for a Pack in case of AMPP.
- **Retail Rate (RSR)**: The price at which the item is sold to retail customers.  It is for a Unit in case of AMP or for a Pack in case of AMPP.
- **Wholesale Rate (WSR)**: The price for wholesale transactions.  It is for a Unit in case of AMP or for a Pack in case of AMPP.

#### The calculated values, only considering the line inputs, are as follows. These values are not available to the user to change directly.
- **Line Gross Rate**: In procurement bills, the Purchase rate is the Line Gross Rate. It is for a pack if the selected item is a AMPP. It is for a unit of the selected item is an AMP.
- **Line Net Rate**: In procurement bills, the line net rate is calculated by Line Gross Rate (ie Purchase rate in Procurement Bills) + Line Tax Rate - Line Discount Rate. It is for a pack if the selected item is an AMPP. It is for a unit of the selected item is an AMP.
- **Line Cost Rate**: The calculated cost per unit. The user can NOT directly change it. It is calculated. This is ALWAYS calculated for a unit. This is calculated by the Line Net Rate divided by the Quantity in Units. If the same item is purchased in packs or units, this should be the same. While handling AMPPs, if the line cost rate is required for a pack, we have to multiply the line cost rate by the Units per Pack.

- **Line Gross Total**: In procurement bills, the Purchase Value is the Line Gross Rate. It is calculated by `PR × Qty`
- **Line Discount**: The Discount for a Line. It is calculated by `DR × Qty`
- **Line TAX**: The TAX for a Line. It is calculated by `TR × Qty`
- **Line Expense**: The TAX for a Line. It is calculated by `TR × Qty`
- **Line Net Total**: The net total of line values. It is calculated from Line Gross Total + Line Tax + Line Expense - Line Discount

- **Purchase Gross Value**: Computed as `PR × Qty`
- **Bill Discount for Line**: Proportion of the total bill discount applicable to the line item
- **Bill Tax for Line**: Proportion of the bill tax applicable to the line item
- **Line Tax**: Tax applied specifically to the item line
- **Total Discount**: Summation of all applicable discounts

- **Value At Retail Rate**: Computed as `PR × Qty`
- **Value At Purchase Rate**: Proportion of the total bill discount applicable to the line item
- **Value At Cost Rate**: Proportion of the bill tax applicable to the line item
- **Value At Wholesale Rate**: Tax applied specifically to the item line


##### Rate Breakdown
- **Line Discount Rate**: Discount applied at the line level
- **Line Tax Rate**: Tax rate for the line item
- **Bill Tax Rate for Line**: Tax rate applied to the total bill that affects the line item
- **Bill Discount Rate for Line**: Proportion of the total bill discount affecting the line item

#### Purchase Net Value
The net value of the purchase is calculated as:
`Purchase Net Value = (PR - (Line Discount Rate + Bill Discount Rate for Line)) × Qty`

### Example Calculation
**AMP: Zaart 50**  
- **Quantity**: 1000 units
- **Free Quantity**: 100 units
- **Purchase Rate (PR)**: 10
- **Retail Sale Rate (RSR)**: 12.50
- **Purchase Cost**: `1000 × 10 = 10,000`
- **Cost Rate**: `10,000 / 1100`

### Post-Purchase Considerations
#### Stock Management
- No differentiation is made between purchased and free quantity.
- **Purchase Value Calculation**: `Purchase Rate × Qty`
- **Retail Sale Value Calculation**: `Retail Rate × Qty`

#### Stock Valuation Issue
If stock quantity is **1100**, the purchase value calculated by stock * PR:
`1100 × 10 = 11,000` **(Incorrect Calculation)**

**Ideal Purchase Value Calculation:**
`Stock × Cost Rate`


[Back](https://github.com/hmislk/hmis/wiki/Pharmaceutical-Logistics)



















Cost Calculation in Procuring Pharmaceuticals and Consumables

Purchase 
   Bill
        Bill Items
               Item (Individual Item - AMP / Pack - AMPP )
                     Qty
                     Purchase Rate 
                     Cost Rate
                     Free Qty
                     Retail Rate
                     Wholesale Rate
                     Purchase Gross Value (PR X qty)
                     Line Discount
                     Bill Discount for Line
                     Bill Tax for Line
                     Line Tax
                     Total Discount

                     Line Discount Rate
                     Line Tax Rate 
                     Bill Tax Rate for Line
                     Bill Discount Rate for Line
                    
                     Purchase Net Value = (PR - (Line Discount Rate + Bill Discount Rate for Line)) * Qty

                     

Ex.
AMP
Zaart 50 > Qty 1000, Free Qty 100, PR - 10, RSR - 12.50 - Purchase Cost - 10,000, Cost Rare (10,000 / 1100)

After Purchase
      Stock (No differentiation of qty and free qty)
      Purchase Value - Purchase rate * Qty
      Retail Sale Value - Retail rate * Qty

Stock - 1100
Purchase Value when calculated by Qtock * PR - 1100 * 10 = 11,000 > Wrong
Ideal Purchase Value - Stock * Cost Rate




                     

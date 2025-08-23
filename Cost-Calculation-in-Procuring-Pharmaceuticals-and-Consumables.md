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

##### Rates directly related to the Line that are Calculated 
- **Line Gross Rate**: In procurement bills, the Purchase rate is the Line Gross Rate. It is for a pack if the selected item is a AMPP. It is for a unit of the selected item is an AMP.
- **Line Net Rate**: In procurement bills, the line net rate is calculated by Line Gross Rate (ie Purchase rate in Procurement Bills) + Line Tax Rate - Line Discount Rate. It is for a pack if the selected item is an AMPP. It is for a unit of the selected item is an AMP.
- **Line Cost Rate**: The calculated cost per unit. The user can NOT directly change it. It is calculated. This is ALWAYS calculated for a unit. This is calculated by the Line Net Rate divided by the Quantity in Units. If the same item is purchased in packs or units, this should be the same. While handling AMPPs, if the line cost rate is required for a pack, we have to multiply the line cost rate by the Units per Pack.

#### Values directly related to the Line that are Calculated 
- **Line Gross Total**: In procurement bills, the Purchase Value is the Line Gross Rate. It is calculated by `PR × Qty`
- **Line Discount**: The Discount for a Line. It is calculated by `DR × Qty`
- **Line TAX**: The TAX for a Line. It is calculated by `TR × Qty`
- **Line Expense**: The TAX for a Line. It is calculated by `TR × Qty`
- **Line Net Total**: The net total of line values. It is calculated from Line Gross Total + Line Tax + Line Expense - Line Discount

#### Values Calculated from Bill Related Values
The values directly related to the Bill, but not the lines, also have an impact on the cost of items. They also need to be taken into consideration for costing. The bill-related values are divided proportionally to the line net totals of each line. These values that were calculated from the bill values are then divided by quantities to get the rates. Here, free quantities are not taken into consideration. These values are not agained summed to get any bill related value as then there will be a circular dependancy.

##### Values in Bill Items coming from Bill Values
- **Bill Discount Value**: The component of a line that comes from the Bill Discount
- **Bill Expense Value**: The component of a line that comes from the Bill Expense
- **Bill Tax Value**: The component of a line that comes from the Bill Tax
- **Bill Gross Value**: Kept without any calculation as it is zero.
- **Bill Net Value**: The component is calculated from Bill Expense Value + Bill Tax Value - Bill Discount Value

##### Rates in Bill Items coming from Bill Values
- **Bill Discount Rate**: The Bill Discount value of a line divided by 'qty'
- **Bill Expense Rate**: The Bill Expense value of a line divided by 'qty'
- **Bill Tax Rate**: The Bill Tax value of a line divided by 'qty'
- **Bill Gross Rate**: Kept without any calculation as it is zero.
- **Bill Net Rate**: The Bill Net value of a line divided by 'qty'

#### Total Line Values - These are calculated by adding values from Line values directly related to the Line and the line values that are calculated from Bill Values
- **Gross Total**: Line Gross Total + Bill Gross Total - As Bill Gross Total is zero, Gross Total = Line Gross Total
- **Total Discount**: Line Discount + Bill Discount
- **Total TAX**: Line Tax + Bill Tax
- **Total Expense**: Line Tax + Bill Tax
- **Net Total**: Line Net Total + Bill Net Total

#### Total Line Rates - These are calculated by dividing the respective line total value by the quantity
- **Gross Rate**: Gross Total divide by Quantity
- **Total Dicount Rate**: Total Discount divide by Quantity
- **Total Tax Rate**: Total Tax divide by Quantity
- **Total Expense Rate**: Total Expense divide by Quantity
- **Net Rate**: Net Total divide by Quantity

#### The value of items needs to be valued at different rates for decision-making. So these are calculated and recorded. These are calculated by multiplying the respective line total value by the quantity
- **Value At Retail Rate**: Computed as `RSR × (Qty+Free QTY)`
- **Value At Wholesale Rate**: Computed as `WSR × (Qty+Free QTY)`
- **Value At Purchase Rate**: Computed as `PR × (Qty+Free QTY)`
- **Value At Cost Rate**: Computed as `CR × (Qty in Units +Free QTY in Units)`

#### Bill Item Related Entities
BillItem Entity - records basic data as the user entered
BillItemFinanceDetails - records basic data as user-entered or calculated. Pack Size in Units, rates in Units and Packs (when relevant) are recorded there.
PharmaceuticalBillItem - This is not usually used to capture user inputs. It mainly records in units (unless the variable says packs). 

Positive and Negatives. The rates/discounts are positive. If the stock go out, the quantities should be negative. If stocks come in quantities should be recorded as positives. When money is spent, values should be negative. If money is earned, values should be positive.


## Programming Logic

### When a user changes a line-related input
First, we have to identify where the user inputs are recorded. For bill-related items, the details may be recorded to Bill Item Finance Details or Bill Item. We are not usually using the Pharmaceutical Bill Item to record user inputs. Once the variables where the user inputs are initially recorded are identified, the variables that record the same value need to be updated. Then pack/unit-related values need to be updated. This will involve BillItem, BillItemFinanceDetails and PharmaceuticalBillItem.
As the change of user inputs for a line has an effect on the calculated values for the lines, the line values need to be calculated with updated user inputs.
Then, the bill level values that directly depend on the line level values need to be updated.
The values of the bill that are dependent on the above values are required to be changed.

At this stage, we should not redistribute bill-level values to lies as nothing happens to them when the user changes line-level values.

### When a user changes a bill-related input
The place where the user input is recorded has to be identified. That user input may be recorded at different entities. We have to update them first.
The bill level calculations need to be done.
Then these values need to be distributed to the bill Items proportionally.
Then, the bill item level total values need to be calculated. Here, the directly bill item-related values should NOT be changed. Only bill-related values and total values should be changed. The totalling of bill values is also not necessary to get bill level values as it is not happening here.




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




                     

**Cost Calculation in Procuring Pharmaceuticals and Consumables**

### Purchase Structure

In the procurement of pharmaceuticals and consumables, cost calculation is critical to ensure accuracy and transparency in financial management. The following structure outlines the process:

#### Bill
Each purchase is documented in a bill containing multiple bill items. Each bill item corresponds to an individual item or pack.

##### Bill Items
Each bill item consists of:
- **Item**: The individual item (AMP) or pack (AMPP)
- **Quantity (Qty)**: The total number of units purchased
- **Purchase Rate (PR)**: The rate at which the item is purchased
- **Cost Rate**: The calculated cost per unit
- **Free Quantity**: Additional units provided at no charge
- **Retail Rate (RSR)**: The price at which the item is sold to retail customers
- **Wholesale Rate**: The price for wholesale transactions
- **Purchase Gross Value**: Computed as `PR × Qty`
- **Line Discount**: Discount applicable to the specific line item
- **Bill Discount for Line**: Proportion of the total bill discount applicable to the line item
- **Bill Tax for Line**: Proportion of the bill tax applicable to the line item
- **Line Tax**: Tax applied specifically to the item line
- **Total Discount**: Summation of all applicable discounts

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




                     

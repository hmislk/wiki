Bills, Bill Items, Bill Fees, Bill Sessions

Bill
   billFees
   billItems
   billSession
   singleBillSession
   singleBillItem


Item
   Service
   Medicines
   Investigation
   Radiology
   ServiceSession
   List<Fee> .. ItemFee

List<BillItem>
   billFees
   billSession
   Referance to Item - Service / Medicine / ServiceSession


List<BillFee>
 Refer to Bill, BillItem, Fee(ItemFee)
  

BillSession






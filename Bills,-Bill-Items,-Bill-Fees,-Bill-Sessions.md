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


Pre Bill - 
1. Appoint = Cash Tx - PaidBill - Self Referral - CHANNEL_BOOKING_WITH_PAYMENT, CHANNEL_BOOKING_WITH_PAYMENT_ONLINE - Paid Bill - Same
2. Appointment = No Cash - CHANNEL_BOOKING_WITHOUT_PAYMENT - Paid Bill - CHANNEL_PAYMENT_FOR_BOOKING_BILL





Billed Bill







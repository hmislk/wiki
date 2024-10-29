Order or a Bill

Attributes-
* Patient attributes. And patient object content all the patient details.
* Bill date
* Bill time
* Bill number
* Total price
* Payment method

Bill - Parent Class
Sub Classes
*   PreBill - 
*   BilledBill - has a referance to cancelleBill as CancelBill
*   CancelleBill - when a BilledBill is cancelled, a new cancelledBill is created, has a referance called BilledBill
*   ReturnBill - 






[Back](https://github.com/hmislk/hmis/wiki/Knowledgebase)

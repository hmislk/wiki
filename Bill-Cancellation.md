Bill cancellation

Selct the BilledBill to Cancel

Verifications
* Not cancelled before
* Not returned at any stage, If needed, returns should be cancelled before Bill Bill Cancellation
* Drawer balance (Need to check For Cash, IOU. NOT needed to be checked for Cards, Patient Deposits, etc)
* Check Preferences based criteria like Duration after Original Billing

Create New CancellationBill
copy BilledBill values
invert values like gross total, discount, netTotal, tax, sum of hospital fee, staff fee
replaces coped values with current values - ex. creator, createdAt, etc
reference to BilledBill

Create New Cancellation Bill's Bill Item
for each bill Item needs a new 



















[Back](https://github.com/hmislk/hmis/wiki/Knowledgebase)
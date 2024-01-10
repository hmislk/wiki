# Introduction to the Order/Bill Concept in CareCode HMIS
In CareCode HMIS, the term 'Order' is synonymous with 'Bill'. This concept is a cornerstone of patient service management, encompassing the range of services or tests requisitioned for a patient during a single visit to the OPD department. Each order or bill represents a complete record of patient interactions, capturing both the clinical and financial aspects of care provision.

# The Structure and Composition of Orders/Bills
At the heart of an order/bill is the aggregation of multiple 'Order Items/Bill Items'. Each item represents a specific service or test provided to the patient. This modular approach ensures detailed tracking of patient services, ranging from simple consultations to complex diagnostic tests. The order/bill thus serves as a comprehensive record, reflecting the totality of care and services rendered during the patient's visit.

# Types of OPD Orders/Bills in CareCode HMIS
CareCode HMIS classifies OPD orders/bills into two primary categories based on their payment structure:

## Immediate Payment Orders
These orders are settled at the time of service delivery. They are typical in scenarios where services are provided, and payment is processed immediately.
## Deferred Payment Orders
In these cases, the order is generated, but the payment is postponed, often collected later by a cashier. This system is particularly relevant for patients who might undergo multiple or ongoing services before the final billing.

# Institutional Dynamics in Order Processing
Every order item is intrinsically linked to specific institutional parameters: the 'fromInstitution/toInstitution', where the user is logged, and 'toInstitution/toDepartment', where the service is or will be rendered. These parameters not only ensure accuracy in service delivery but also facilitate seamless inter-departmental coordination within the healthcare setup.
[Details](https://github.com/hmislk/hmis/wiki/Institutional-Dynamics-in-OPD-Order-Processing)

# Batch Bills Versus Individual Bills
In CareCode HMIS, the concept of 'Batch Bills' plays a pivotal role in billing management:

When all order items pertain to a single department, a single batch bill along with an individual bill is generated.
Conversely, if the order items span across multiple departments, one batch bill references multiple individual bills. This system ensures that each department's services are accurately documented and billed.

# Printing and Displaying Orders/Bills
The system's flexibility extends to the printing and display of bills:

## Single Bill Scenario
When a single bill is generated, only this bill is displayed and printed, with no reference to the batch bill.
## Multiple Bill Scenario
In cases where multiple bills are produced, both the batch bill and all individual bills are displayed and printed. The batch bill provides a consolidated view, including total payments and tendered amounts in case of cash transactions.

[Back](https://github.com/hmislk/hmis/wiki/OPD)


## Overview

This section outlines the Object-Oriented Design for the Bills/Orders system component of CareCode Health Management Information System (HMIS). The design focuses on encapsulating entities like bills, items, fees, and services into a structured and modular format, enabling efficient management and scalability.

## Entities and Their Relationships
1. Bill
Attributes: billID, billDate, totalAmount, status, patient, etc.
Methods: calculateTotal(), etc.

2. BillItem
Attributes: item, quantity, price, etc.
Relationships: Linked to Item (Investigation/Service).
Methods: calculateItemTotal(), etc.

3. BillFees
Attributes: fee, type (e.g., institution, facility use), amount, etc.
Methods: getFeeDetails(), etc.

4. BillComponents
This is a composite entity encapsulating different aspects of a bill.

5. BillPayments
paymentID, amount, paymentMethod, date, etc.

6. BillSessions: sessionID, sessionType, duration,

7. BillExpenses: expenseID, description, amount, etc.

8. Item
Attributes: itemID, name, code, category (Investigation/Service), etc.

Subclasses:
Investigation: specificAttributes (e.g., labTestType)
Services: specificAttributes (e.g., serviceType)
InpatientService: additionalAttributes (e.g., roomType)
TheatreService: additionalAttributes (e.g., equipmentUsed)
PharmaceuticalItem: additionalAttributes (e.g., dosageForm)

[Back](https://github.com/hmislk/hmis/wiki/Design-Documentation)
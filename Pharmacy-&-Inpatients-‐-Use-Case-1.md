Use Case 1: **Drug Issue to Inpatient with Ward-Based Stock Management**
**Description**:
This use case describes the process of issuing drugs to an inpatient from the ward's stock, recording the stock reduction, and updating the patient's bill immediately. The process is managed by the ward staff, typically a nurse, through a computerized system.

Actors:
Primary Actor: Ward Staff (Nurse)
Secondary Actors: Pharmacy Department, Billing Department
Precondition:
The nurse has a valid user account and is logged into the system.
Computers are available in the ward for accessing the system.
The ward has a designated stock of drugs.
The drug stock is not assigned to any specific inpatient but is available for all inpatients in the ward.
Trigger:
A doctor prescribes medication to an inpatient, triggering the need to issue drugs from the ward stock.

Main Flow:
Authentication: The ward staff (nurse) logs into the system using their user credentials.
Drug Selection: The nurse selects the prescribed drug from the ward's stock list available in the system.
Stock Verification: The system checks the availability of the drug in the ward's stock.
Drug Issuance:
a. If the drug is available, the nurse issues the required quantity to the inpatient.
b. The system automatically updates the ward's stock, reducing the quantity issued.
Billing Update: The system immediately adds the charges for the issued drugs to the total bill of the patient, which will be settled after discharge.
Confirmation: The nurse confirms the drug issuance, and the system logs the transaction for record-keeping and auditing purposes.
Postconditions:
The inpatient receives the required medication.
The ward's drug stock is updated to reflect the reduction.
The patient's bill is updated to include the charges for the issued drugs.
A record of the transaction is securely stored in the system.
Requirements:
User accounts for ward staff (nurses) with appropriate access privileges.
Computers with internet access in the ward for accessing the system.
A reliable and secure system for managing stock and billing.
Assumptions:
The system is functioning correctly and is accessible at the time of drug issuance.
The ward staff is trained and competent in using the system.
Notes:
The system should have robust security measures to protect sensitive patient and drug stock information.
Regular audits and stock checks should be conducted to ensure the accuracy of the system's data.
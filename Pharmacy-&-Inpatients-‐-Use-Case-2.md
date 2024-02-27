# Use Case 2: Drug Issue to Inpatient with Manual Request to Pharmacy

### Description:

This use case describes the process of issuing drugs to an inpatient when there are no user accounts for ward staff or computers in the ward. The process involves manually creating a drug request for the patient and sending it to the pharmacy, where the request is processed, and drugs are issued.


### Actors:

**Primary Actor:** Ward Staff (Nurse)

**Secondary Actors:** Pharmacy Staff, Billing Department

### Precondition:

The ward staff (nurse) has access to the required forms for manually creating drug requests.

The pharmacy has a designated stock of drugs.

The drug stock is not assigned to any specific inpatient but is available for all inpatients in the pharmacy.

### Trigger:

A doctor prescribes medication to an inpatient, triggering the need to issue drugs from the pharmacy stock.

### Main Flow:

**Manual Request Creation:** The ward staff (nurse) manually fills out a drug request form for the prescribed medication for the inpatient.

**Request Dispatch:** The completed form is sent from the ward to the pharmacy.

**Authentication:** Pharmacy staff log into the system using their user credentials.

**Drug Selection:** Pharmacy staff select the prescribed drug from the pharmacy's stock list available in the system.

**Stock Verification:** The system checks the availability of the drug in the pharmacy's stock.

**Drug Issuance:**

a. If the drug is available, the pharmacy staff issues the required quantity to the inpatient.

b. The system automatically updates the pharmacy's stock, reducing the quantity issued.

**Billing Update:** The system immediately adds the charges for the issued drugs to the total bill of the patient, which will be settled after discharge.

**Confirmation:** Pharmacy staff confirm the drug issuance and the system logs the transaction for record-keeping and auditing purposes.

### Postconditions:

The inpatient receives the required medication.

The pharmacy's drug stock is updated to reflect the reduction.

The patient's bill is updated to include the charges for the issued drugs.

A record of the transaction is securely stored in the system.

### Requirements:

User accounts for pharmacy staff with appropriate access privileges.

Computers with internet access in the pharmacy for accessing the system.

A secure method for transporting the manual drug request forms from the ward to the pharmacy.

### Assumptions:

The system is functioning correctly and is accessible at the time of drug issuance.

The pharmacy staff is trained and competent in using the system.

### Notes:

The manual process of creating and sending drug requests is prone to errors and delays; hence, a protocol should be in place to handle discrepancies and ensure the timely delivery of medications.

Regular audits and stock checks should be conducted to ensure the accuracy of the system's data.

Both use cases aim to ensure efficient and accurate drug issuance to inpatients, with the key difference being the presence or absence of digital resources at the ward level.

[Back](https://github.com/hmislk/hmis/wiki/Inpatient-Pharmaceutical-Management)





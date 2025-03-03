### **Bill Cancellation Process in CareCode HIS**

The bill cancellation process in CareCode HIS follows a structured workflow to ensure accuracy, validation, and proper referencing. Below is a step-by-step description of the process.

---

#### **Selecting the BilledBill for Cancellation**
1. Identify the specific `BilledBill` to cancel.
2. Ensure the following verifications are completed before proceeding:

   - **Not Cancelled Previously:** Confirm that the bill hasn’t been cancelled already.
   - **No Returns Recorded:** If returns exist, they must be cancelled first before proceeding with the bill cancellation.
   - **Drawer Balance Check:** Ensure that for payments made in cash or IOU, the drawer balance is checked. This step is not required for payments made via cards, patient deposits, etc.
   - **Preference-Based Criteria:** Validate the cancellation request based on configured criteria, such as the allowed duration after the original billing.

---

#### **Creating a New CancellationBill**
1. **Copy Values from the Original BilledBill:**
   - Clone all relevant attributes of the `BilledBill` into the new `CancellationBill`.

2. **Invert Financial Values:**
   - Convert values such as:
     - Gross Total  
     - Discount  
     - Net Total  
     - Tax  
     - Sum of Hospital Fees  
     - Sum of Staff Fees  
   - Inversion ensures that the cancellation bill reflects negative amounts.

3. **Replace Certain Values:**
   - Update creator, creation timestamp (`createdAt`), and any other relevant metadata to reflect the current cancellation action.

4. **Add a Reference to the Original BilledBill:**  
   - The new `CancellationBill` will maintain a reference back to the cancelled `BilledBill`.

5. **Update References in the Original BilledBill:**  
   - Save the newly created `CancellationBill` with updated references in the original `BilledBill`.

---

#### **Creating Bill Items for the CancellationBill**
1. For each item listed under the original `BilledBill`, create a corresponding bill item for the `CancellationBill`.
2. Ensure that the cancellation bill items follow the same logic as the parent `CancellationBill`:
   - Copy original item values.
   - Invert necessary values.
   - Replace metadata like creator and timestamps.
   - Add appropriate references to the original `BilledBill` and the new `CancellationBill`.

---

#### **Creating Bill Fees for the CancellationBill Items**
1. For each fee associated with the original bill items, create a corresponding fee entry for the cancellation bill items.
2. Apply the same process followed for creating the `CancellationBill`:
   - Copy and invert fee values.
   - Replace relevant metadata.
   - Maintain references between the original `BilledBill`, the new `CancellationBill`, the respective bill items, and their associated fees.

---

#### **Handling Payments for the CancellationBill**
1. **Invert Payments:**  
   - Reverse the payment values recorded in the original `BilledBill`.

2. **Modify Payment Methods if Required:**  
   - Use a new payment method if necessary. For instance, if a card payment is being refunded, the patient may receive cash instead.

---

#### **Updating the Drawer Balance**
1. Reflect the cancelled amounts in the drawer to ensure the balance stays accurate.

---

#### **Preparing for Print**
1. Prepare the necessary details for printing the `CancellationBill`, ensuring all references, fees, and payments are correctly reflected.













[Back](https://github.com/hmislk/hmis/wiki/Knowledgebase)
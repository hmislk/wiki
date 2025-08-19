# Pharmacy Configuration and Privileges

This section describes the configuration options and privileges required for managing pharmacy-related pages. It is intended for **System Administrators**.

---

## Inpatient Medication Management

### Direct Issue to BHTs

**Page:** `/inward/pharmacy_bill_issue_bht.xhtml`
**Navigation:** Menu ▸ Pharmacy ▸ Inpatient Medication Management ▸ Direct Issue to BHTs

**Configuration Options:**

* Display Total Stock when listing medicines for Inpatients
* Medicine Identification Codes Used
* Nursing IP Billing – Show Rate and Value
* Pharmacy Bill Support for Native Printers
* Pharmacy Inward Direct Issue Bill is FiveFiveCustom3
* Pharmacy Inward Direct Issue Bill is PosHeaderPaper

**Privileges Required:**

* PharmacyDirectIssueToBht
* NursingIPBillingViewRates

---

### Reprint Inpatient Direct Issues

**Page:** `/inward/pharmacy_reprint_bill_sale_bht.xhtml`
**Navigation:** Menu ▸ Pharmacy ▸ Inpatient Medication Management ▸ Search Inpatient Direct Issues by Item ▸ Reprint

**Configuration Options:**

* Nursing IP Billing – Show Rate and Value
* Pharmacy Inward Direct Issue Bill is FiveFiveCustom3
* Pharmacy Inward Direct Issue Bill is PosHeaderPaper

**Privileges Required:**

* InwardCheck / InwardUnCheck
* ShowInwardFee
* NursingIPBillingViewRates

---

## Disposal

### Issue

**Page:** `/pharmacy/pharmacy_issue.xhtml`
**Navigation:** Menu ▸ Pharmacy ▸ Disposal ▸ Issue

**Configuration Options:**

* Consumption – Show Rate and Value

**Privileges Required:**

* PharmacyDisposalIssue
* ConsumptionViewRates
* ChangeReceiptPrintingPaperTypes

---

## Disbursement

### Request

**Page:** `/pharmacy/pharmacy_transfer_request.xhtml`
**Navigation:** Menu ▸ Pharmacy ▸ Disbursement ▸ Request

**Configuration Options:**

* Stock Request – Show Rate and Value

**Privileges Required:**

* PharmacyDisbursementRequest
* StockRequestViewRates
* Developers

---

### Direct Issue

**Page:** `/pharmacy/pharmacy_transfer_issue.xhtml`
**Navigation:** Menu ▸ Pharmacy ▸ Disbursement ▸ Direct Issue

**Configuration Options:**

* Stock Transaction – Show Rate and Value
* Pharmacy Transfer Issue Bill is POS Paper with details
* Pharmacy Transfer Issue Bill is POS Paper with header
* Pharmacy Transfer Issue Bill is Template

**Privileges Required:**

* PharmacyDisbursementDirectIssue
* StockTransactionViewRates
* Developers

---

### Issued List

**Page:** `/pharmacy/pharmacy_transfer_issued_list.xhtml`
**Navigation:** Menu ▸ Pharmacy ▸ Disbursement ▸ Receive

**Configuration Options:**

* (none)

**Privileges Required:**

* PharmacyDisbursementRecieve

---

### Receive from List

**Page:** `/pharmacy/pharmacy_transfer_receive.xhtml`
**Navigation:** Menu ▸ Pharmacy ▸ Disbursement ▸ Receive ▸ Receive (from list)

**Configuration Options:**

* Report Font Size of Item List in Pharmacy Disbursement Reports
* Pharmacy Transfer Receive Bill is Template

**Privileges Required:**

* PharmacyTransferViewRates
* ChangeReceiptPrintingPaperTypes
* Developers

---

## Retail Transactions

### Sale by Batch

**Page:** `/pharmacy/pharmacy_bill_retail_sale.xhtml`
**Navigation:** Menu ▸ Pharmacy ▸ Retail Transactions ▸ Sale by Batch

**Configuration Options:**

* Find Last Sale Rate of Medicines in Retail Sale
* Display Total Stock when listing medicines for Retail Sale
* Medicine Identification Codes Used
* Enable label printing for pharmacy medicines
* Pharmacy Bill Support for Native Printers
* Pharmacy Retail Sale Bill formats: PosPaper / PosPaper with items / PosPaper (prabodha) / FiveFivePaper / PosHeaderPaper / FiveFiveCustom3

**Privileges Required:**

* PharmacySale
* ChangeReceiptPrintingPaperTypes

---

### Sale for Cashier

**Page:** `/pharmacy/pharmacy_bill_retail_sale_for_cashier.xhtml`
**Navigation:**

* Menu ▸ Pharmacy ▸ Retail Transactions ▸ Sale for cashier
* Menu ▸ Opd Issue ▸ Opd Issue For Cashier

**Configuration Options:**

* Create Token At Pharmacy Sale For Cashier
* Allow Tendered Amount for pharmacy sale for cashier
* Pharmacy Bill Support for Native Printers
* Enable token system in sale for cashier
* Pharmacy Sale for Cashier Token Bill is Pos paper
* Pharmacy Sale for Cashier Bill is Pos paper
* Pharmacy Retail Sale Bill is PosHeaderPaper
* Pharmacy Sale for cashier Bill is FiveFiveCustom3

**Privileges Required:**

* PharmacySaleForCashier
* ChangeReceiptPrintingPaperTypes
* PharmacySale

---

[[← Back to Pharmacy Administration](https://github.com/hmislk/hmis/wiki/Pharmacy-Administration)](https://github.com/hmislk/hmis/wiki/Pharmacy-Administration)


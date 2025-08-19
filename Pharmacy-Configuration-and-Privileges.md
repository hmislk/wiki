Pharmacy Configuration and Privileges

Pharmacy Page Details
/inward/pharmacy_bill_issue_bht.xhtml
Navigation Path: Menu ▸ Pharmacy ▸ Inpatient Medication Management ▸ Direct Issue to BHTs

Configuration Options Used:

Display Total Stock when listing medicines for Inpatients

Medicine Identification Codes Used

Nursing IP Billing – Show Rate and Value

Pharmacy Bill Support for Native Printers

Pharmacy Inward Direct Issue Bill is FiveFiveCustom3

Pharmacy Inward Direct Issue Bill is PosHeaderPaper

Privileges Required:

PharmacyDirectIssueToBht (menu)

NursingIPBillingViewRates (rate display)

Composite Components:
bill:bhtDetail,
phe:issueBill,
phi:saleBill_five_five_1,
phe:A4_paper_with_headings,
phi:inward_direct_issue_bill_five_five_custom_3,
phi:saleBill_Header_Inward

/inward/pharmacy_reprint_bill_sale_bht.xhtml
Navigation Path: Menu ▸ Pharmacy ▸ Inpatient Medication Management ▸ Search Inpatient Direct Issues by Item ▸ Reprint

Configuration Options Used:

Nursing IP Billing – Show Rate and Value

Pharmacy Inward Direct Issue Bill is FiveFiveCustom3

Pharmacy Inward Direct Issue Bill is PosHeaderPaper

Privileges Required:

InwardCheck / InwardUnCheck (controls)

ShowInwardFee (view bill items)

NursingIPBillingViewRates (rate display)

Composite Components:
ph:issueBill,
phi:saleBill_five_five,
phi:inward_direct_issue_bill_five_five_custom_3,
phi:saleBill_Header_Inward

/pharmacy/pharmacy_issue.xhtml
Navigation Path: Menu ▸ Pharmacy ▸ Disposal ▸ Issue

Configuration Options Used: Consumption – Show Rate and Value

Privileges Required:

PharmacyDisposalIssue (menu)

ConsumptionViewRates (rate display)

ChangeReceiptPrintingPaperTypes (paper selection)

Composite Components:
ph:history,
ph:pharmacy_issue_receipt

/pharmacy/pharmacy_transfer_request.xhtml
Navigation Path: Menu ▸ Pharmacy ▸ Disbursement ▸ Request

Configuration Options Used: Stock Request – Show Rate and Value

Privileges Required:

PharmacyDisbursementRequest (menu)

StockRequestViewRates (rate display)

Developers (show all bill formats)

Composite Components:
ph:history,
ph:pharmacy_transfer_request_receipt

/pharmacy/pharmacy_transfer_issue.xhtml
Navigation Path: Menu ▸ Pharmacy ▸ Disbursement ▸ Direct Issue

Configuration Options Used:

Stock Transaction – Show Rate and Value

Pharmacy Transfer Issue Bill is POS Paper with details

Pharmacy Transfer Issue Bill is POS Paper with header

Pharmacy Transfer Issue Bill is Template

Privileges Required:

PharmacyDisbursementDirectIssue (menu)

StockTransactionViewRates (rate display)

Developers (show all bill formats)

Composite Components:
ph:history,
ph:transferIssue,
ph:transferIssue_detailed,
ph:saleBill_Header_Transfer,
ph:pharmacy_transfer_issue_receipt

/pharmacy/pharmacy_transfer_issued_list.xhtml
Navigation Path: Menu ▸ Pharmacy ▸ Disbursement ▸ Receive

Configuration Options Used: (none observed)

Privileges Required: PharmacyDisbursementRecieve (menu)

Composite Components: (none used)

/pharmacy/pharmacy_transfer_receive.xhtml
Navigation Path: Menu ▸ Pharmacy ▸ Disbursement ▸ Receive ▸ Receive (from list)

Configuration Options Used:

Report Font Size of Item List in Pharmacy Disbursement Reports

Pharmacy Transfer Receive Bill is Template

Privileges Required:

PharmacyTransferViewRates

ChangeReceiptPrintingPaperTypes

Developers (debug options)

Composite Components:
ph:history,
ph:transferReceive,
ph:transfeRecieve_detailed,
ph:pharmacy_transfer_receive_receipt

/pharmacy/pharmacy_bill_retail_sale.xhtml
Navigation Path: Menu ▸ Pharmacy ▸ Retail Transactions ▸ Sale by Batch

Configuration Options Used:

Find Last Sale Rate of Medicines in Retail Sale

Display Total Stock when listing medicines for Retail Sale

Medicine Identification Codes Used

Enable label printing for pharmacy medicines

Pharmacy Bill Support for Native Printers

Pharmacy Retail Sale Bill formats (PosPaper, PosPaper with items, PosPaper(prabodha), FiveFivePaper, PosHeaderPaper, FiveFiveCustom3)

Privileges Required:

PharmacySale (menu)

ChangeReceiptPrintingPaperTypes

Composite Components:
phi:pharmacy_instruction_label,
pa:creditCard / patient_deposit / ewallet / cheque / slip / multiple_payment_methods,
phi:saleBill_without_item / saleBill / saleBill_prabodha / saleBill_five_five / saleBill_Header / sale_bill_five_five_custom_3

/pharmacy/pharmacy_bill_retail_sale_for_cashier.xhtml
Navigation Paths:

Menu ▸ Pharmacy ▸ Retail Transactions ▸ Sale for cashier

Menu ▸ Opd Issue ▸ Opd Issue For Cashier

Configuration Options Used:

Create Token At Pharmacy Sale For Cashier

Allow Tendered Amount for pharmacy sale for cashier

Pharmacy Bill Support for Native Printers

Enable token system in sale for cashier

Pharmacy Sale for Cashier Token Bill is Pos paper

Pharmacy Sale for Cashier Bill is Pos paper

Pharmacy Retail Sale Bill is PosHeaderPaper

Pharmacy Sale for cashier Bill is FiveFiveCustom3

Privileges Required:

PharmacySaleForCashier (menu)

ChangeReceiptPrintingPaperTypes

PharmacySale (switching sale modes)

Composite Components:
phi:saleBill_five_five_token,
phi:saleBillToken,
phi:saleBill_for_Cashier,
phi:saleBill_five_five_for_Cashier,
phi:saleBill_Header,
phi:sale_bill_five_five_custom_3

[Back](https://github.com/hmislk/hmis/wiki/Pharmacy-Administration)
How to Create a Printing Page

The system has several receipts / bills to print
OPD Bills, Pharmacy Retail Sale Bills

The different installations have different printers, paper sizes and configuration

A new method is introduced to handle the customization

CSS styles are stored as configuration options. THey are loaded at the onset of the application. If a value is not set. the default values are created.

Sample

`@Named`
`@ApplicationScoped`
`public class ConfigOptionApplicationController implements Serializable {`

    `@PostConstruct`
    `public void init() {`
        `loadApplicationOptions();`
    `}`

    `public void loadApplicationOptions() {`
        `applicationOptions = new HashMap<>();`
        `List<ConfigOption> options = getApplicationOptions();`
        `for (ConfigOption option : options) {`
            `applicationOptions.put(option.getOptionKey(), option);`
        `}`
        `loadEmailGatewayConfigurationDefaults();`
        `loadPharmacyConfigurationDefaults();`
        `loadPharmacyIssueReceiptConfigurationDefaults();`
    `}`

    `private void loadPharmacyIssueReceiptConfigurationDefaults() {`
        `getLongTextValueByKey("Pharmacy Issue Receipt CSS",`
                `".receipt-container {\n"`
                `+ "    font-family: Verdana, sans-serif;\n"`
                `+ "    font-size: 12px;\n"`
                `+ "    color: #000;\n"`
                `+ "}\n"`
                `+ ".receipt-header, .receipt-title, .receipt-separator, .receipt-summary {\n"`
                `+ "    margin-bottom: 10px;\n"`
                `+ "}\n"`
                `+ ".receipt-institution-name {\n"`
                `+ "    font-weight: bold;\n"`
                `+ "    font-size: 16px;\n"`
                `+ "    text-align: center;\n"`
                `+ "}\n"`
                `+ ".receipt-institution-contact {\n"`
                `+ "    text-align: center;\n"`
                `+ "    font-size: 11px;\n"`
                `+ "}\n"`
                `+ ".receipt-title {\n"`
                `+ "    text-align: center;\n"`
                `+ "    font-size: 14px;\n"`
                `+ "    font-weight: bold;\n"`
                `+ "    text-decoration: underline;\n"`
                `+ "}\n"`
                `+ ".receipt-details-table, .receipt-items-table, .receipt-summary-table {\n"`
                `+ "    width: 100%;\n"`
                `+ "    border-collapse: collapse;\n"`
                `+ "}\n"`
                `+ ".receipt-items-header {\n"`
                `+ "    font-weight: bold;\n"`
                `+ "    border-bottom: 1px solid #ccc;\n"`
                `+ "}\n"`
                `+ ".item-name, .item-qty, .item-rate, .item-value {\n"`
                `+ "    padding: 4px;\n"`
                `+ "    text-align: left;\n"`
                `+ "}\n"`
                `+ ".item-qty, .item-rate, .item-value {\n"`
                `+ "    text-align: right;\n"`
                `+ "}\n"`
                `+ ".summary-label {\n"`
                `+ "    font-weight: bold;\n"`
                `+ "}\n"`
                `+ ".summary-value {\n"`
                `+ "    text-align: right;\n"`
                `+ "    font-weight: bold;\n"`
                `+ "}\n"`
                `+ ".total-amount {\n"`
                `+ "    font-size: 14px;\n"`
                `+ "    font-weight: bold;\n"`
                `+ "}\n"`
                `+ ".receipt-cashier {\n"`
                `+ "    margin-top: 20px;\n"`
                `+ "    text-align: right;\n"`
                `+ "    text-decoration: overline;\n"`
                `+ "}"`
        `);`
    `}`

`}`



This is a sample receipt composite component.

`<?xml version='1.0' encoding='UTF-8' ?>`
`<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">`
`<html xmlns="http://www.w3.org/1999/xhtml"`
      `xmlns:cc="http://xmlns.jcp.org/jsf/composite"`
      `xmlns:f="http://xmlns.jcp.org/jsf/core"`
      `xmlns:h="http://xmlns.jcp.org/jsf/html"`
      `xmlns:ui="http://xmlns.jcp.org/jsf/facelets">`


    `<!-- INTERFACE -->`
    `<cc:interface>`
        `<cc:attribute name="bill" type="com.divudi.core.entity.Bill"/>`
    `</cc:interface>`

    `<!-- IMPLEMENTATION -->`
    `<cc:implementation>`

        `<style>`
            `<h:outputText escape="false"`
            `value="#{configOptionApplicationController.getLongTextValueByKey('Pharmacy Issue Receipt CSS')}"/>`
        `</style>`


        `<h:outputText escape="false"`
                      `value="#{configOptionApplicationController.getLongTextValueByKey('Pharmacy Issue Receipt Header')}"/>`

        `<div class="receipt-container">`
            `<div class="receipt-header">`
                `<div class="receipt-institution-name">`
                    `<h:outputLabel value="#{cc.attrs.bill.department.printingName}" />`
                `</div>`
                `<div class="receipt-institution-contact">`
                    `<h:outputLabel value="#{cc.attrs.bill.department.address}" /><br />`
                    `<h:outputLabel value="#{cc.attrs.bill.department.telephone1}" />`
                    `<h:outputLabel value=" #{cc.attrs.bill.department.telephone2}" /><br />`
                    `<h:outputLabel value="#{cc.attrs.bill.department.fax}" />`
                `</div>`
            `</div>`

            `<div class="receipt-title">`
                `<h:outputLabel value="Pharmacy Issue Receipt" />`
            `</div>`

            `<div class="receipt-separator"><hr /></div>`

            `<div class="receipt-bill-details">`
                `<table class="receipt-details-table">`
                    `<!-- Table rows for bill metadata -->`
                    `<tr>`
                        `<td><h:outputLabel value="Date" styleClass="label" /></td>`
                        `<td><h:outputLabel value=":" /></td>`
                        `<td>`
                            `<h:outputLabel value="#{cc.attrs.bill.createdAt}">`
                                `<f:convertDateTime pattern="dd/MM/yy" />`
                            `</h:outputLabel>`
                            `<h:outputLabel value="#{cc.attrs.bill.createdAt}">`
                                `<f:convertDateTime timeZone="Asia/Colombo" pattern="#{sessionController.applicationPreference.shortTimeFormat}" />`
                            `</h:outputLabel>`
                        `</td>`
                        `<td><h:outputLabel value="BHT No" rendered="#{cc.attrs.bill.patientEncounter.bhtNo ne null}" /></td>`
                        `<td><h:outputLabel value=":" rendered="#{cc.attrs.bill.patientEncounter.bhtNo ne null}" /></td>`
                        `<td><h:outputLabel value="#{cc.attrs.bill.patientEncounter.bhtNo}" rendered="#{cc.attrs.bill.patientEncounter.bhtNo ne null}" /></td>`
                    `</tr>`
                    `<tr>`
                        `<td><h:outputLabel value="Invoice No" styleClass="label" /></td>`
                        `<td><h:outputLabel value=":" /></td>`
                        `<td colspan="4"><h:outputLabel value="#{cc.attrs.bill.deptId}" /></td>`
                    `</tr>`

                    `<h:panelGroup rendered="#{cc.attrs.bill.invoiceNumber ne null}">`
                        `<tr>`
                            `<td><h:outputLabel value="Request No" styleClass="label" /></td>`
                            `<td><h:outputLabel value=":" /></td>`
                            `<td colspan="4"><h:outputLabel value="#{cc.attrs.bill.invoiceNumber}" /></td>`
                        `</tr>`
                    `</h:panelGroup>`

                    `<tr>`
                        `<td><h:outputLabel value="Payment Method" styleClass="label" rendered="#{cc.attrs.bill.paymentMethod ne null}" /></td>`
                        `<td><h:outputLabel value=":" rendered="#{cc.attrs.bill.paymentMethod ne null}" /></td>`
                        `<td><h:outputLabel value="#{cc.attrs.bill.paymentMethod}" rendered="#{cc.attrs.bill.paymentMethod ne null}" /></td>`
                    `</tr>`

                    `<tr>`
                        `<td><h:outputLabel value="Payment Scheme" styleClass="label" rendered="#{cc.attrs.bill.paymentScheme.printingName ne null}" /></td>`
                        `<td><h:outputLabel value=":" rendered="#{cc.attrs.bill.paymentScheme.printingName ne null}" /></td>`
                        `<td><h:outputLabel value="#{cc.attrs.bill.paymentScheme.printingName}" rendered="#{cc.attrs.bill.paymentScheme.printingName ne null}" /></td>`
                    `</tr>`

                    `<tr>`
                        `<td><h:outputLabel value="Patient Name" styleClass="label" rendered="#{cc.attrs.bill.patient.person.nameWithTitle ne null}" /></td>`
                        `<td><h:outputLabel value=":" rendered="#{cc.attrs.bill.patient.person.nameWithTitle ne null}" /></td>`
                        `<td colspan="4"><h:outputLabel value="#{cc.attrs.bill.patient.person.nameWithTitle}" rendered="#{cc.attrs.bill.patient.person.nameWithTitle ne null}" /></td>`
                    `</tr>`

                    `<tr>`
                        `<td><h:outputLabel value="Staff Name" styleClass="label" rendered="#{cc.attrs.bill.toStaff.person.nameWithTitle ne null}" /></td>`
                        `<td><h:outputLabel value=":" rendered="#{cc.attrs.bill.toStaff.person.nameWithTitle ne null}" /></td>`
                        `<td colspan="4"><h:outputLabel value="#{cc.attrs.bill.toStaff.person.nameWithTitle}" rendered="#{cc.attrs.bill.toStaff.person.nameWithTitle ne null}" /></td>`
                    `</tr>`

                    `<h:panelGroup rendered="#{cc.attrs.bill.toDepartment ne null}">`
                        `<tr>`
                            `<td><h:outputLabel value="To Unit" styleClass="label" /></td>`
                            `<td><h:outputLabel value=":" /></td>`
                            `<td colspan="4"><h:outputLabel value="#{cc.attrs.bill.toDepartment.name}" /></td>`
                        `</tr>`
                    `</h:panelGroup>`

                    `<h:panelGroup rendered="#{cc.attrs.bill.toInstitution ne null}">`
                        `<tr>`
                            `<td><h:outputLabel value="Company" styleClass="label" /></td>`
                            `<td><h:outputLabel value=":" /></td>`
                            `<td colspan="4"><h:outputLabel value="#{cc.attrs.bill.toInstitution.name}" /></td>`
                        `</tr>`
                    `</h:panelGroup>`

                    `<h:panelGroup rendered="#{cc.attrs.bill.comments ne null}">`
                        `<tr>`
                            `<td><h:outputLabel value="Comment" styleClass="label" /></td>`
                            `<td><h:outputLabel value=":" /></td>`
                            `<td colspan="4"><h:outputLabel value="#{cc.attrs.bill.comments}" /></td>`
                        `</tr>`
                    `</h:panelGroup>`

                `</table>`
            `</div>`

            `<div class="receipt-separator"><hr /></div>`

            `<div class="receipt-items-section">`
                `<table class="receipt-items-table">`
                    `<thead>`
                        `<tr>`
                            `<th class="item-name">Item</th>`
                            `<th class="item-qty">Qty</th>`
                            `<th class="item-rate">Rate</th>`
                            `<th class="item-value">Value</th>`
                        `</tr>`
                    `</thead>`
                    `<tbody>`
                        `<ui:repeat value="#{cc.attrs.bill.billItems}" var="bip">`
                            `<tr>`
                                `<td class="item-name">`
                                    `<h:outputLabel value="#{bip.searialNo+1} - #{bip.item.name}" />`
                                `</td>`
                                `<td class="item-qty">`
                                    `<h:outputLabel value="#{bip.qty}">`
                                        `<f:convertNumber pattern="#,##0.00" />`
                                    `</h:outputLabel>`
                                `</td>`
                                `<td class="item-rate">`
                                    `<h:outputLabel value="#{bip.pharmaceuticalBillItem.retailRate}">`
                                        `<f:convertNumber pattern="#,##0.00" />`
                                    `</h:outputLabel>`
                                `</td>`
                                `<td class="item-value">`
                                    `<h:outputLabel value="#{bip.pharmaceuticalBillItem.retailRate * bip.qty}">`
                                        `<f:convertNumber pattern="#,##0.00" />`
                                    `</h:outputLabel>`
                                `</td>`
                            `</tr>`
                        `</ui:repeat>`
                    `</tbody>`
                `</table>`
            `</div>`

            `<div class="receipt-separator"><hr /></div>`

            `<div class="receipt-summary">`
                `<table class="receipt-summary-table">`
                    `<tr>`
                        `<td class="summary-label">Total</td>`
                        `<td class="summary-value">`
                            `<h:outputLabel value="#{cc.attrs.bill.total}" styleClass="total-amount">`
                                `<f:convertNumber pattern="#,##0.00" />`
                            `</h:outputLabel>`
                        `</td>`
                    `</tr>`
                    `<h:panelGroup rendered="#{cc.attrs.bill.discount ne 0.0}">`
                        `<tr>`
                            `<td class="summary-label">Discount</td>`
                            `<td class="summary-value">`
                                `<h:outputLabel value="#{-cc.attrs.bill.discount}">`
                                    `<f:convertNumber pattern="#,##0.00" />`
                                `</h:outputLabel>`
                            `</td>`
                        `</tr>`
                        `<tr>`
                            `<td class="summary-label">Net Total</td>`
                            `<td class="summary-value">`
                                `<h:outputLabel value="#{cc.attrs.bill.netTotal}">`
                                    `<f:convertNumber pattern="#,##0.00" />`
                                `</h:outputLabel>`
                            `</td>`
                        `</tr>`
                    `</h:panelGroup>`
                    `<tr>`
                        `<td class="summary-label">Number of Items</td>`
                        `<td class="summary-value">`
                            `<h:outputLabel value="#{cc.attrs.bill.billItems.size()}">`
                                `<f:convertNumber pattern="#,##0.00" />`
                            `</h:outputLabel>`
                        `</td>`
                    `</tr>`
                `</table>`
            `</div>`

            `<div class="receipt-cashier">`
                `<h:outputLabel value="Cashier : #{cc.attrs.bill.creater.name}" />`
            `</div>`
        `</div>`

        `<h:outputText escape="false"`
                      `value="#{configOptionApplicationController.getLongTextValueByKey('Pharmacy Issue Receipt Footer')}"/>`




    `</cc:implementation>`
`</html>`


It is called from the relavant page like below


`                        <h:panelGroup   id="gpBillPreview" >`
                            `<phi:pharmacy_issue_receipt bill="#{pharmacyIssueController.printBill}"/>`
                        `</h:panelGroup>`




[Back](https://github.com/hmislk/hmis/wiki/Developer-Manual)
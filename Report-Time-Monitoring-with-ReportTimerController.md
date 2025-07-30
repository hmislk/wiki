# Overview
In order to track and monitor the time taken for report generation in the system, a utility class called ReportTimerController has been introduced. This allows automatic logging of:

* Start time
* End time
* Executing user
* Report type and name

The captured data is saved in the ReportLog entity, which can later be used for audit, performance optimization, or debugging.

## 📁 Location
com.divudi.bean.common.ReportTimerController

## 🔍 Purpose
Encapsulates the logic required to:

* Log the start time of a report
* Execute the report generation logic
* Log the end time and save the report duration

# How to Integrate with a Report Processing Method
## 🔧 Step-by-Step Guide
* Find the file where the report is exis(Eg:/pharmacy/bin_card.xhtml)
* Find the processing button and go to the method in action: (Eg:action="#{pharmacyErrorChecking.processBinCard()}")
* Wrap the report processing logic inside 
> **reportTimerController.trackReportExecution(() -> {**
> **--------**
> **---------**
> **}, PharmacyReports.PHARMACY_BIN_CARD, sessionController.getLoggedUser());**

* ### Updated Method with Time Monitoring

```public void processBinCard() {```
        ```reportTimerController.trackReportExecution(() -> {```
            ```binCardEntries = stockHistoryController.findBinCardDTOs(fromDate, toDate, null, department, item);```

            ```if (configOptionApplicationController.getBooleanValueByKey("Pharmacy Bin Card - Hide Adjustment Bills in Bin Card",true)) {```
                ```List<BillType> bts = new ArrayList<>();```
                ```bts.add(BillType.PharmacyAdjustmentSaleRate);```

                ```Iterator<PharmacyBinCardDTO> iterator = binCardEntries.iterator();```
                ```while (iterator.hasNext()) {```
                    ```PharmacyBinCardDTO dto = iterator.next();```
                    ```if (dto.getBillType() != null && bts.contains(dto.getBillType())) {```
                        ```iterator.remove();```
                    ```}```
                ```}```
            ```}```

        ```}, PharmacyReports.PHARMACY_BIN_CARD, sessionController.getLoggedUser());```
    ```}```

*###  Specify the appropriate PharmacyReports enum type as the second argument.
To enable identification of report types, ensure your report type is declared in the PharmacyReports enum (or your respective module enum).
`package com.divudi.core.data.reports;`

`public enum PharmacyReports implements IReportType {`
    `PHARMACY_BIN_CARD("Pharmacy Bin Card"),;`
    
    `private final String displayName;`

    `PharmacyReports(String displayName) {`
        `this.displayName = displayName;`
    `}`

    `@Override`
    `public String getDisplayName() {`
        `return displayName;`
    `}`

    `@Override`
    `public String getReportType() {`
        `return this.getClass().getSimpleName();`
    `}`

    `@Override`
    `public String getReportName() {`
        `return this.name();`
    `}`
`}`

### Please use the respective file for creating enum (Eg: Bin card is a pharmacy report because of that i used the PharmacyReports.java File to create it's enum)
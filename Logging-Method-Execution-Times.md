## 🕒 Logging Method Execution Times

### 📘 Introduction

The `trackReportExecution()` wrapper method in `ReportTimerController` helps log the time taken for report generation and other expensive operations. However, when this is applied before **validation checks** (like user permissions, null checks, or bill status), it may record misleading logs or even cause errors.

This guide explains **how to safely log execution times only when the operation is truly performed**, and how to persist those logs asynchronously.

---

### ✅ When to Avoid `trackReportExecution()`

Avoid wrapping entire methods like this:

```java
public void generateReport() {
    reportTimerController.trackReportExecution(() -> {
        if (!userHasAccess()) {
            JsfUtil.addErrorMessage("Access denied");
            return;
        }
        performReportGeneration();
    }, reportType, "Controller.methodName", user);
}
```

The above logs even when the report logic is skipped due to validation.

---

### ✅ Safe Pattern: Manual Logging with Start/End

Use this structure instead:

```java
public void generateBarcodesForSelectedBill(Bill bill) {
    // Validate first
    if (bill == null || bill.isCancelled()) {
        JsfUtil.addErrorMessage("Invalid bill");
        return;
    }

    // Start timing only after validation
    Date startTime = new Date();
    ReportLog log = new ReportLog(reportType, reportName, user, startTime, null);
    Future<ReportLog> futureLog = reportTimerController.getReportLogAsyncService().logReport(log);
    ReportLog savedLog = null;

    try {
        savedLog = futureLog.get();  // Wait for the async creation
        performBarcodeGeneration(bill);
    } catch (Exception e) {
        Logger.getLogger(getClass().getName()).log(Level.SEVERE, "Error during report generation", e);
    } finally {
        if (savedLog != null) {
            savedLog.setEndTime(new Date());
            reportTimerController.getReportLogAsyncService().logReport(savedLog); // Async update
        }
    }
}
```

---

### ✅ `performBarcodeGeneration()` Example

Move your business logic into a helper method:

```java
public void generateBarcodesForSelectedBill(Bill billForBarcode) {
    selectedBillBarcodes = new ArrayList<>();
    billBarcodes = new ArrayList<>();
    setCurrentBill(billForBarcode);

    if (billForBarcode == null) {
        JsfUtil.addErrorMessage("No Bills Selected");
        return;
    }

    if (billForBarcode.isCancelled()) {
        JsfUtil.addErrorMessage("This Bill is Already Cancelled");
        return;
    }

    // Start manual timing
    Date startTime = new Date();
    ReportLog reportLog = new ReportLog(CommonReports.LAB_DASHBOARD, "LaboratoryManagementController.generateBarcodesForSelectedBill", sessionController.getLoggedUser(), startTime, null);
    Future<ReportLog> futureLog = reportTimerController.getReportLogAsyncService().logReport(reportLog);
    ReportLog savedLog = null;

    try {
        savedLog = futureLog.get();

        BillBarcode bb = new BillBarcode(billForBarcode);
        List<PatientSampleWrapper> psws = new ArrayList<>();
        List<PatientSample> pss = patientInvestigationController.prepareSampleCollectionByBillsForPhlebotomyRoom(billForBarcode, sessionController.getLoggedUser());
        StringBuilder sampleIDs = new StringBuilder();

        if (pss != null) {
            for (PatientSample ps : pss) {
                PatientSampleWrapper ptsw = new PatientSampleWrapper(ps);
                psws.add(ptsw);
                if (!sampleIDs.toString().contains(ps.getIdStr())) {
                    sampleIDs.append(ps.getIdStr()).append(" ");
                }
            }
        }

        for (PatientInvestigationWrapper piw : bb.getPatientInvestigationWrappers()) {
            if (billForBarcode.getStatus() == PatientInvestigationStatus.ORDERED) {
                piw.getPatientInvestigation().setBarcodeGenerated(true);
                piw.getPatientInvestigation().setBarcodeGeneratedAt(new Date());
            }

            String[] idsToAdd = sampleIDs.toString().trim().split("\\s+");
            String existingSampleIds = piw.getPatientInvestigation().getSampleIds();
            for (String id : idsToAdd) {
                if (!existingSampleIds.contains(id)) {
                    existingSampleIds += " " + id;
                }
            }

            if (billForBarcode.getStatus() == PatientInvestigationStatus.ORDERED) {
                piw.getPatientInvestigation().setBarcodeGeneratedBy(sessionController.getLoggedUser());
                piw.getPatientInvestigation().setStatus(PatientInvestigationStatus.SAMPLE_GENERATED);
            }

            piw.getPatientInvestigation().setSampleIds(existingSampleIds.trim());
            patientInvestigationFacade.edit(piw.getPatientInvestigation());
        }

        if (billForBarcode.getStatus() == PatientInvestigationStatus.ORDERED) {
            billForBarcode.setStatus(PatientInvestigationStatus.SAMPLE_GENERATED);
        }

        billFacade.edit(billForBarcode);
        bb.setPatientSampleWrappers(psws);

        billBarcodes.add(bb);
        selectedBillBarcodes = billBarcodes;
        listingEntity = ListingEntity.VIEW_BARCODE;

    } catch (Exception e) {
        // handle exception
    } finally {
        Date endTime = new Date();
        if (savedLog != null) {
            savedLog.setEndTime(endTime);
            reportTimerController.getReportLogAsyncService().logReport(savedLog);
        }
    }
}

```

---

### 🧠 Design Highlights

| Concern                         | Addressed via                            |
| ------------------------------- | ---------------------------------------- |
| User or input validation        | Done **before** starting timer           |
| Thread-safe & async persistence | `@Asynchronous` `ReportLogAsyncService`  |
| Proper closure                  | `finally` ensures end time is logged     |
| Audit DB separation             | Uses `hmisAuditPU` via `ReportLogFacade` |

---

### 🛠 Required Components

* `ReportLog`
* `ReportLogFacade` (with `@PersistenceContext(unitName = "hmisAuditPU")`)
* `ReportLogAsyncService` with:

```java
@Asynchronous
public Future<ReportLog> logReport(ReportLog log) {
    if (log.getId() == null) {
        reportLogFacade.create(log);
    } else {
        reportLogFacade.edit(log);
    }
    return CompletableFuture.completedFuture(log);
}
```

---

### 📍 Where to Use

* Report generation (PDF, Excel, Dashboards)
* Heavy DB queries
* Long-running patient/pharmacy/lab logic

---

### ✅ Summary

Wrap only the **core execution logic** after validations. This guarantees meaningful logs and avoids noise from early-exit or failed conditions.


[Back](https://github.com/hmislk/hmis/wiki/Code-Conventions)

# Introduction to LIMS

LIMS is capable of handling virtually any number of tests or investigations. The configuration can be changed so that all the institutions/departments of the system share the same set of investigations or each department have a separate set of investigations. Each investigation can have properties like category, name, printing name, department, and so on. The total charge for an investigation depends on different fees related to each investigation. Each investigation can have a report format. The report format is the key point in data managed by the test. It dictates the data captured during the analysis, how to automate, how to generate reference ranges depending on the age and sex and how the hard copy be generated. When the automation is not available, the data entry to results of tests performed on each patient has made it easy by entering [possible values for fields] of data capture. The reference ranges can be configured initially so that they will be added to the report with the start of the result entering depending on the age and sex. The calculations can be designed initially so that at the point of data entry to reports, the calculations are performed by the LIMS. Once an order is made for a certain test, it may be necessary to issues a different test result for the same order, for example, it may be a WBC/DC that is requested, yet some occasion, it may be necessary to issue an FBC instead. This facility can be managed through replacable investigations.
 
The LIMS daily routine starts with the ordering process. Tests may be ordered from OPD or Wards.
A bill will be generated with details of the order along with a barcode. At the phlebotomy area, a computer with a barcode reader will identify the order and [generate stickers](https://github.com/hmislk/hmis/wiki/LIMS-Sampling) needed to be pasted in each container. The samples are then [received at the relevant laboratory](https://github.com/hmislk/hmis/wiki/LIMS-Receiving-Samples-at-the-Lab). When required, the MLT can print [worksheets](https://github.com/hmislk/hmis/wiki/LIMS-Printing-Worksheets).

Automated tests will order tests and get results from the analyzers through bi-directional communication. Tests not automated need to be searched by criteria like name, id, etc. and enter data. When data is entered automatically or manually, the results needed to be approved to printing a hard copy. Depending on the configuration, an SMS and/or Email will be sent to the patient with a link to the report.

Once a report is approved by an authorized user, no more data entry for the report is possible. If the report needed to be changed, authorized users can cancel the authorization. After the cancellation, data can be entered again. Depending on the configuration, the lab manager will get an email for each cancellation of an authorisation. 

When handing over the hard copies, it can be marked in the system. As the signature is inserted to the report during authorization, even collecting centres located away from the lab, can print hard copies and handover to patients.

Patients can click on the link in the SMS and view the report. If email is given, the patient will get a pdf file of the report as an attachment. The patient can also view the reports through the Mobile App or Web Portal for the patients. Web portal and the mobile app allow the patient to see charts plotted with serial results when appropriate. 

An analysis of different aspects of the lab performance is available through the Menu > Lab > Summeries.


[Back](https://github.com/hmislk/hmis/wiki/LIMS)


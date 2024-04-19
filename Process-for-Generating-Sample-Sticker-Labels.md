# Introduction
This page explains of the methodology used for generating sample sticker labels for laboratory tests. 

# Process Overview
When a set of investigations is ordered for a patient, such as for "Patient Buddhika," who requires tests like ESR, FBC, UFR, Lipid Profile, TSH, Liver Profile, and CRP, the HMIS determines how many and what types of samples are necessary. This determination is based on pre-configured data for each test, which includes the type of tube, specimen required, analyzer used, and the department involved.

# Example Case
For illustrative purposes, let's examine the case of Patient Buddhika, who requires multiple tests:

## Tests Ordered: 
ESR, FBC, UFR, Lipid Profile, TSH, Liver Profile, CRP.
The system uses the following pre-configured data for each test:

## Tube:
ESR: Sodium Citrate Tube
FBC: EDTA Tube
UFR, Lipid Profile, TSH, Liver Profile, CRP: Plain Tube

## Specimen:
FBC: Whole Blood
UFR: Urine
Lipid Profile, TSH, Liver Profile, 
CRP: Serum

## Analyzer:
UFR: Manual
FBC: 5 Part Haematological Analyzer
Lipid Profile, Liver Profile, CRP: Biochemistry Analyzer
TSH: Hormonal Analyzer

# Label Generation Procedure
The HMIS will generate the necessary labels for the collected samples based on the pre-configured settings. The number of unique samples and hence labels needed for Patient Buddhika's tests is four, determined as follows:

* FBC: EDTA Tube with Whole Blood using a 5-part Haematological Analyzer.
* UFR: Plain Tube with Urine, analyzed manually.
* Lipid Profile, Liver Profile, CRP: Plain Tube with Serum using a Biochemistry Analyzer.
* TSH: Plain Tube with Serum using a Hormonal Analyzer.

## JSON Configuration and ZPL Code Generation
For each of these labels, the system generates JSON data which can be used to print labels. Below is an example of the JSON configuration for these labels:

## json

`{`
  `"Barcodes": [`
    `{"insid": "L/28885", "tube": "EDTA Tube", "tests": "Full Blood Count (FBC) - ", "sex": "Male", "name": "BUDDHIKA ARIYARATNE", "deptid": "NPL/1", "billDate": "18 Apr 24", "id": "41835812", "barcode": "41835812", "age": "48 years"},`
    `{"insid": "L/28885", "tube": "Plain Tube", "tests": "Urine Full Report (UFR) - ", "sex": "Male", "name": "BUDDHIKA ARIYARATNE", "deptid": "NPL/1", "billDate": "18 Apr 24", "id": "41835817", "barcode": "41835817", "age": "48 years"},`
    `{"insid": "L/28885", "tube": "Plain Tube", "tests": "CRP (C-Reactive Protein), TSH, Lipid Profile, Liver Profile - ", "sex": "Male", "name": "BUDDHIKA ARIYARATNE", "deptid": "NPL/1", "billDate": "18 Apr 24", "id": "41835815", "barcode": "41835815", "age": "48 years"},`
    `{"insid": "L/28885", "tube": "Sodium Citrate Tube", "tests": "ESR - ", "sex": "Male", "name": "BUDDHIKA ARIYARATNE", "deptid": "NPL/1", "billDate": "18 Apr 24", "id": "41835810", "barcode": "41835810", "age": "48 years"}`
  `]`
`}`

This JSON configuration leads to the generation of ZPL code for label printing, ensuring that each label is correctly formatted and contains all necessary patient and test information for accurate sample identification and tracking.

# Conclusion
The automated generation of sample sticker labels by the HMIS plays a critical role in maintaining accuracy and efficiency in the laboratory testing process. 
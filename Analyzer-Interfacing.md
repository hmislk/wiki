Analyzer Interfacing

Module - Lab (LIMS)

## Analyzers Type - 
* Biochemistry (SGOT, SGPT, Serum Creatinine)
* Haematology - (FBC)
* Hormonal - TSH, Ferritin
* Electrolyte - Na, K, Cl, Ca
* Other - HbA1C

## Communication Method
Unidirectional
Bidrecrection

# Physical Connection
* TCP/IP
* Comport

# Standards
* ASTM (V1, V2)
* HL7
* FHIR

LIMS Characters
* Analyzer
* Department Analyzer


When an order is placed for a patient > Patient Investigation Objects are created for Investigations
Lipid Profile > one Patient Investigation
Liver Profile > One Patient Investigation

Patient Sample
Created at the time of Barcode Generation
Container *
Components of an Investigation
(Analyzer *)
(Department *)

Examples of Having Components - Blood Sugar Series - FBS/ Post Break Fast, Pre Lunch, Post Lunch, Pre Dinner. Post Dinner

Patient Sample Run





Phlebotomy
Barcode Generation








[Back](https://github.com/hmislk/hmis/wiki/LIMS-Knowledgebase)
Path: Administration > Manage Pricing > Upload Fees > Upload to add Department Fees by Item Code

Using this feature, fees can be uploaded per department, therefore allowing two different departments at the same site to have different fees. To enable this, firstly, options must be turned on to allow department-specific fees.

The Excel sheet that is uploaded should be in the following format.

Column | Field           | Required  | Comments
A      | Item Code       | Mandatory |
B      | Fee             | Mandatory |
C      | Foreigner Fee   | Optional  | If not given, takes the Fee value as the Foreigner Fee Value
D      | Fee Type        | Optional  | If not given, takes the 'OwnInstitution' as type
E      | Institution     | Optional  | If not given, take logged Institution
F      | Department      | Optional  | If not given, take logged Institution
G      | Speciality      | Optional  | If not given, ignored
H      | Staff           | Optional  | Give without title. If not given, ignored

<img width="1932" height="1293" alt="screencapture-qa-carecode-org-qa1-faces-admin-pricing-upload-to-add-department-fees-by-item-code-xhtml-2025-07-23-08_18_34" src="https://github.com/user-attachments/assets/2f97248c-4e46-4759-8b0f-8e28179abe80" />

Then select Choose File and select the file that needs to be uploaded. Then select Upload and add fee values, followed by Save Imported Values. Here, all the valid imports and invalid imports will be displayed along with the reason for the invalid import.



[Back](https://github.com/hmislk/hmis/wiki/Manage-Pricing)

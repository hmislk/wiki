# Authentication and Authorization Mechanism

Implementation of a secure login system requiring credentials for access.
The system will authenticate users based on their login details and assign authorization levels according to their roles within the hospital.

# Role-Based Access Control (RBAC)

Comprehensive RBAC functionality to define, assign, and manage user roles and permissions with granularity.
Ability to assign and limit privileges specifically tailored to the role or user, ensuring users have access only to the functionalities necessary for their job.

# Department-Specific Access

Users will have the capability to log into one or more assigned departments, with access rights varying based on the department(s) selected during login.
The system will allow for the dynamic adjustment of user privileges based on the department context to ensure relevant access.

# Administrative Controls

Administrative users will have the ability to define roles, assign users to departments, and set specific privileges for each role or user.
Provision for the creation of an unlimited number of roles to accommodate the diverse functions and responsibilities within the hospital.
Department Selection at Login

During the login process, users will be required to select their department from a list of assigned departments. Access privileges will be automatically adjusted to reflect the selected department's permissions, ensuring users operate within their authorized scope.
Audit Trail and Logging

Every action performed within the system will be logged to create a comprehensive audit trail. This includes login attempts, data access, modifications, and any other significant actions.
The logging functionality will support auditing purposes, enabling the tracking of user activities for security, compliance, and operational integrity.

[Back](https://github.com/hmislk/hmis/wiki/Functions)
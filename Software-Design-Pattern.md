MVC (Model-View-Controller) is a common software design pattern used to separate concerns in an application. It improves maintainability, scalability, and testability.

Model:
Handles the data and business logic.
It manages database records, calculations, and rules.
Example: Java classes with JPA entities managing patient data.

View:
Handles the presentation layer (UI).
It displays data from the Model to the user.
Example: JSF (XHTML pages) showing patient details.

Controller:
Handles user input and updates the Model and View.
It processes actions like form submissions and commands.
Example: Managed Beans in JSF handling button clicks.

Flow:
User interacts with the View → Controller processes the action → Model updates → View refreshes with new data.

MVC helps keep the code organised and makes future changes easier.
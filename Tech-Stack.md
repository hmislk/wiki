
# The Core and the Web Application

### Language
- **[Java](https://github.com/hmislk/hmis/wiki/Java)**

### IDE
- **Apache NetBeans 16**: 

### Database
- **MySQL 8**: 

### Frameworks
- **Java Server Faces (JSF) 2.3**: Provides a framework for building server-side user interfaces.

### Framework Components
- **PrimeFaces 14.0.6**: Offers advanced UI frameworks for JSF applications, as specified in the latest Maven `pom.xml`.

### Building Tool
- **[Apache Maven](https://github.com/hmislk/hmis/wiki/Mevan)**: Manages project builds and dependencies.

### JDBC Driver
- **MySQL Connector/J 8.0.30+**: 

### Persistence Framework
- **JPA (Java Persistence API)**

### Persistence Provider
- **EclipseLink 2.5**: Provides advanced JPA functionalities. (ORM)

### Application Server
- **Payara 5**: A modern and fully-supported server environment for Java EE applications.

## Middleware and Utilities

### LIMS Analyzer Middleware
- **C#:** Utilized for developing middleware applications interfacing with laboratory instruments.

### Bill and Barcode Printing
- **JavaSE**: Manages printing functionalities in a standard Java environment.

### Web Services
- **RESTful**: Employs RESTful web services for interoperable machine-to-machine interaction.

## Development and Maintenance

### Version Control
- **Git**: Manages source code versions.
- **GitHub**: Hosts the source code repository and tracks issues.

### Issue Tracking
- **GitHub Issue Tracker**: Monitors and resolves issues throughout the software lifecycle.

## Dependencies
Updates and current libraries used are detailed in the Maven `pom.xml` configuration. Noteworthy dependencies include:
- **HAPI FHIR**: Integrates FHIR-based standards for healthcare interoperability.
- **Apache POI**: Manages Microsoft document files.
- **Jackson and Gson**: Handle JSON processing.
- **Joda-Time, Commons libraries, Barcode4j, iText**: Provide support for time handling, utility functions, barcode generation, and PDF creation, respectively.

### Maven POM Highlights
The project’s Maven POM file specifies dependencies, plugins, and repositories essential for the development and deployment of the application. This includes settings for compatibility with Java 8, despite using newer library versions, to ensure broad compatibility and stability.

[Back](https://github.com/hmislk/hmis/wiki/Developer-Manual)
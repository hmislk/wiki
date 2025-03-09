**Title:**  
**Overview of Java Editions and Usage in CareCode**

**Article:**  

### 1. Java Editions  
Java is available in different editions, each designed for specific types of applications:

- **Java SE (Standard Edition):**  
  Core Java platform used for general-purpose applications. Includes basic libraries, tools, and APIs required to develop desktop and simple server applications.

- **Java ME (Micro Edition):**  
  Designed for embedded and mobile devices with limited resources, such as feature phones and IoT devices.

- **Java EE (Enterprise Edition):**  
  Now known as **Jakarta EE** (formerly **J2EE**), designed for developing large-scale, distributed, and enterprise-level applications. Provides APIs for web services, servlets, EJB, and more. [Java EE vs J2EE vs Jakarta EE](https://www.baeldung.com/java-enterprise-evolution#:~:text=Actually%2C%20the%20Eclipse%20Foundation%20legally,voted%20and%20picked%3A%20Jakarta%20EE.)

### 2. Usage in CareCode  
At **CareCode**, we use **Java EE (J2EE)** for developing our **Core** and **API** layers. This allows us to build scalable, secure, and multi-user enterprise applications with features such as:

- RESTful APIs.  
- Transaction management.  
- Security handling.  
- Database integrations.

### 3. Server and Client Environment  

- The **Application Server** runs the **JVM (Java Virtual Machine)** and the **JDK/JRE**, hosting the deployed Java EE application and handling client requests.

- **Clients** (users accessing the system) do not need to have **JRE** installed on their machines. They only require:  
  - An internet connection.  
  - A modern web browser.  

Clients interact with the system through standard web interfaces (such as HTML/JS), while all business logic executes on the server.



[Back](https://github.com/hmislk/hmis/wiki/Java)
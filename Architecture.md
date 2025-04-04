**Single-Tier Architecture:**  
All components (user interface, business logic, and data storage) run in a single system or application. There is no separation between layers.  
Example: A desktop application like Microsoft Access where the user interface, processing, and database are within one system.

**Two-Tier Architecture:**  
The application is divided into two layers:  
1. Client Tier (Presentation Layer) – user interface and basic validation.  
2. Server Tier (Data Layer) – database server handling data storage and queries.  
Example: A client application (like a desktop app) directly communicating with a database (such as MySQL).

**Three-Tier Architecture:**  
The application is divided into three layers:  
1. Presentation Tier – user interface.  
2. Business Logic Tier – processes data and applies rules.  
3. Data Tier – manages data storage and retrieval.  
Example: A web application with a front-end (HTML/JS), back-end server (Java EE), and a database (MySQL).

**Multi-Tier Architecture:**  
Extends the three-tier model by adding more specialised layers, such as:  
- Security Layer  
- Caching Layer  
- API Layer  
- Integration Layer  
This improves scalability, flexibility, and maintenance in large systems.

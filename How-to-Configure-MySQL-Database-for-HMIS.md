# How to Configure MySQL Database for HMIS

This guide explains how to configure the MySQL database for the HMIS application. It includes steps for setting up the MySQL JDBC Driver, configuring a JDBC connection pool, and creating a JDBC resource in the Payara server.

## Prerequisites

Ensure that you have the following:

- MySQL Server installed and running
- Payara Server installed and running
- MySQL JDBC Driver (`mysql-connector-java-version-bin.jar`)

## Step 1: Install MySQL JDBC Driver

1. Copy the `mysql-connector-java-version-bin.jar` file into the `lib` directory of your Payara server.


`   cp /path/to/mysql-connector-java-version-bin.jar /path/to/payara/glassfish/domains/domain1/lib/`


2. Replace `/path/to/mysql-connector-java-version-bin.jar` with the path to your MySQL JDBC Driver, and `/path/to/payara/` with the path to your Payara installation.

3. Restart the Payara server to load the new JDBC driver.


`/path/to/payara/bin/asadmin stop-domain`
`/path/to/payara/bin/asadmin start-domain`


## Step 2: Create JDBC Connection Pool

1. In the Payara admin console (typically `http://localhost:4848`), navigate to `Resources > JDBC > JDBC Connection Pools`.

2. Click `New...` to create a new connection pool.

3. Enter the following details:

   - Pool Name: Enter the name of your connection pool (for example, `HMISPool`).
   - Resource Type: Select `javax.sql.DataSource`.
   - Database Driver Vendor: Select `MySQL`.

4. Click `Next`.

5. In the `Additional Properties` section, enter the following:

   - ServerName: Enter the hostname of your MySQL server (for example, `localhost`).
   - DatabaseName: Enter the name of your database.
   - User: Enter your MySQL username.
   - Password: Enter your MySQL password.
   - URL: Enter your JDBC URL. This should look something like `jdbc:mysql://localhost:3306/your_database?useSSL=false&allowPublicKeyRetrieval=true`. Replace `localhost` with your MySQL server's hostname, `3306` with your MySQL server's port, and `your_database` with the name of your database.

6. Click `Finish` to create the connection pool.

## Step 3: Create JDBC Resource

1. In the Payara admin console, navigate to `Resources > JDBC > JDBC Resources`.

2. Click `New...` to create a new JDBC resource.

3. Enter the JNDI Name as specified in your `persistence.xml` file (for example, `jdbc/HMIS`) and select the Pool Name as created in the previous step (`HMISPool`).

4. Click `OK` to create the JDBC resource.

Your Payara server is now configured to use your MySQL database. You should be able to deploy and run your HMIS application.

[Back](https://github.com/hmislk/hmis/wiki)

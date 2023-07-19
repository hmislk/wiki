
# How to Install and Run a Cloned Repository

This guide will walk you through the process of cloning a specific branch from the [HMIS](https://github.com/hmislk/hmis) repository, building the Java application with Maven, and deploying it on a Payara server.

## Prerequisites

Ensure that you have a Virtual Machine (VM) with the following software installed and configured:

Java Development Kit (JDK)
MySQL JDBC Driver
Payara server

## Step 1: Clone the Repository
First, you need to clone the desired branch from the HMIS repository. Replace branch_name with the name of the branch you want to clone:

`git clone --branch branch_name https://github.com/hmislk/hmis.git emr1`

This will clone the branch into a directory named emr1.

## Step 2: Navigate to the Project Directory
Change your current directory to the newly cloned project:

`cd emr1`

## Step 3: Build the Project with Maven
From the root directory of the project (where the pom.xml file is located), build the project using Maven:

`mvn clean package`

This will compile the code, run any tests, and package the application into a .war file. The resulting file will be located in the target subdirectory.

Step 4: Deploy the Application to Payara
Copy your .war file to the autodeploy directory of your Payara server. Replace your-artifact.war with the name of your .war file:


`cp target/your-artifact.war /path/to/payara/glassfish/domains/domain1/autodeploy/`

Payara will automatically deploy any applications placed in the autodeploy directory.

## Troubleshooting
If you encounter any issues during the deployment, check Payara's server logs for error messages. The logs are typically located at /path/to/payara/glassfish/domains/domain1/logs/server.log.
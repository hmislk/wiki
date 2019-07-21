For the development and testing purposes, you can easily clone the project and run with the help of NetBeans.

For MS-Windows

Download a database like [MySQL](https://dev.mysql.com/downloads/mysql/) or [MariaDB](https://downloads.mariadb.org/) and install it following instructions. Make sure to have a user with a password with all privileges. Configuration of the database is stated [elsewhere](https://github.com/hmislk/hmis/wiki/Database-Configuration).

Download the [Netbeans with JDK bundle](https://www.oracle.com/technetwork/java/javase/downloads/jdk-netbeans-jsp-3413139-esa.html) and install following instructions. Install all JavaEE plugins.

Download [glassfish 4.1.2](http://download.oracle.com/glassfish/4.1.2/release/glassfish-4.1.2.zip) server and unzip to a folder. 

Open Netbeans and configure the glassfish server and MySQL. Clone the project with Netbeans. Locate the persistance.xml and configure database. 

Run the project and the web application will start in a browser window.

For Ubuntu
First, update the system by following commands


`sudo apt-get update`

`sudo apt-get upgrade`


Install MySQL (or MariaDB)

`sudo apt install mysql-server`

Configure MySQL access with following command. Follow defaults.

`sudo mysql_secure_installation`

Then log as the su

`sudo mysql`

You will get the mySQL command prommt. Create a new user and grant all privileges as below. Then grant all privileges as below.

`CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';`
`CREATE USER 'sss'@'localhost' IDENTIFIED BY 'Bud7NilB';`
`GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';`








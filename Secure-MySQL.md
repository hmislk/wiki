# Secure MySQL\MariaDB

Secure MySQL\MariaDB access with the following command. Follow defaults.

`sudo mysql_secure_installation`

Then log as the su

`sudo mysql`

You will get the MySQL command prompt. Create a new user and grant all privileges as below. Then grant all privileges as below.

`CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';`

`GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'localhost';`

[Back](https://github.com/hmislk/hmis/wiki)

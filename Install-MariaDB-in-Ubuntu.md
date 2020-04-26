First, update the system by following commands

`sudo apt-get update`

`sudo apt-get upgrade`

Install MariaDB

`sudo apt install mariadb-server mariadb-client`

`sudo mysql_secure_installation`

`sudo mysql`

`GRANT ALL ON *.* TO 'admin'@'localhost' IDENTIFIED BY 'password' WITH GRANT OPTION;`

`FLUSH PRIVILEGES;`

`exit;`


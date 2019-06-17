# Database Configuration


## Setting up Lower Case Table Names
When the database is running in a Linux environment, MySQL or MariaDB table names are case sensitive by default. The web application access database through JPA, which requires case insensitive table names. Before running the application, need to set the MySQL or MariaDB setting to allow case insensitive table names. If is done as follows.

### MariaDB
The MariaDB has different levels of configuration files. The MariaDB/MySQL tools read configuration files in the following order:
* Edit "/etc/mysql/mariadb.cnf" to set global defaults,
* Edit "/etc/mysql/conf.d/*.cnf" to set global options.
* Edit "/etc/mysql/mariadb.conf.d/*.cnf" to set MariaDB-only options.
* Edit "~/.my.cnf" to set user-specific options.

If the same option is defined multiple times, the last one will apply.

You need to have super user privileges to change the first three files. Open the file with an editor like [nano](https://github.com/hmislk/hmis/wiki/Installing-Nano).

Edit the "/etc/mysql/mariadb.cnf" file

`sudo nano /etc/mysql/my.cnf`

Create the following two lines at the end of the comments of the file.

'[mysqld]

lower_case_table_names=1'

Save the file and restart mySQL or MariaDB by

'sudo service mysql restart'

Afterword the table names will be case insensitive.









First, update the system by following commands

`sudo apt-get update`

`sudo apt-get upgrade`

Install MariaDB

`sudo apt-get install software-properties-common`

`sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8`
`sudo add-apt-repository "deb [arch=amd64,arm64,ppc64el] http://mariadb.mirror.liquidtelecom.com/repo/10.4/ubuntu $(lsb_release -cs) main"`

`sudo apt update`

`sudo apt -y install mariadb-server mariadb-client`

This is how VNC Server is installed in Ubuntu 18.04 LTS

sudo apt update

sudo apt upgrade

sudo apt-get install ubuntu-desktop gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal

sudo apt update

sudo apt upgrade

sudo apt-get install vnc4server

vncserver

sudo nano ~/.vnc/xstartup






`#!/bin/sh`

`# Uncomment the following two lines for normal desktop:`
`# unset SESSION_MANAGER`
`# exec /etc/X11/xinit/xinitrc`
``
`[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup`
`[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources`
`xsetroot -solid grey`
`vncconfig -iconic &`
`x-terminal-emulator -geometry 80x24+10+10 -ls -title "$VNCDESKTOP Desktop" &`
`x-window-manager &`
``
`gnome-panel &`
``
`gnome-settings-daemon &`
``
`metacity &`
``
`nautilus &`


`$ chmod 700 ~/.vnc/xstartup`


For Details visit this [Link](https://portal.databasemart.com/kb/a381/how-to-install-ubuntu-desktop-and-vnc-server-on-ubuntu-server14_04.aspx)

[Back](https://github.com/hmislk/hmis/wiki/Deployment-in-a-Development-Environment)
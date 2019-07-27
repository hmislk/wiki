Install Gnome Desktop. (To save resources, you can install XFace instead of Gnome)

`sudo apt install ubuntu-gnome-desktop gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal`

`sudo systemctl enable gdm`

`sudo systemctl start gdm`

Install a VNC Server

`sudo apt install tightvncserver`

Run VNC Server for the first time to create the password and startup script.

`vncserver`

Give password and kill the VNC Instance.

`vncserver -kill :1`

If nano, a text editor, is not installed, you have to install it before editing the startup script.

`sudo apt-get install nano`

Edit the startup script 

`nano ~/.vnc/xstartup `

Make sure the following contents are there in the startup script.

`#!/bin/sh`

`export XKL_XMODMAP_DISABLE=1`
`unset SESSION_MANAGER`
`unset DBUS_SESSION_BUS_ADDRESS`

`[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup`
`[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources`
`xsetroot -solid grey`
`vncconfig -iconic &`

`gnome-panel &`
`gnome-settings-daemon &`
`metacity &`
`nautilus &`
`gnome-terminal &`


Start the VNC Server. Use your screen resolution. 

`vncserver -geometry 1600x900`




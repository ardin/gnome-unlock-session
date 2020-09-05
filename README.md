# GNOME-unlock-session

## General notes


Are you tired continuously entering password when your home workstation is locked?

I am. 

Thus, this program unlock your workstation by pressing **SUPER+U** without additional credentials.

I don't recommend this in sensitive environments or where someone can apply "Mortal Combat" combination.



# Installation

## Installation

**Fedora 32**

* dnf copr enable ardin/gnome-unlock-session -y
* dnf install gnome-unlock-session -y

**CentOS 8**

* yum install yum-plugin-copr -y
* yum copr enable ardin/gnome-unlock-session -y
* yum install gnome-unlock-session -y

**From repo**
sudo pip install evdev
sudo dnf install python3-libevdev
sudo cp gnome-unlock-session.service /usr/lib/systemd/system/
sudo cp gnome-unlock-session /usr/bin
sudo chmod +x /usr/bin/gnome-unlock-session
sudo systemctl enable gnome-unlock-session
sudo systemctl start gnome-unlock-session



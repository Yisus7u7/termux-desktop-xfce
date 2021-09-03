#!/bin/bash

cd $HOME
rm -rf .vnc/
wget https://github.com/Yisus7u7/termux-desktop-xfce/releases/download/4.0.2/datar.tar.xz
tar -xvf ./datar.tar.xz
rm ./datar.tar.xz
wget https://github.com/Yisus7u7/termux-desktop-xfce/releases/download/kde/breeze-cursor-theme_5.20.5-4_all.deb
apt install ./breeze-cursor-theme_5.20.5-4_all.deb
rm breeze-cursor-theme_5.20.5-4_all.deb
wget https://github.com/Yisus7u7/termux-desktop-xfce/releases/download/arc/termux-arc-gtk-theme_20210412_all.deb
apt install ./termux-arc-gtk-theme_20210412_all.deb
rm termux-arc-gtk-theme_20210412_all.deb
rm ~/.vnc/*.pid
rm ~/.vnc/*.log
rm ~/.vnc/passwd 
chmod +x ~/.vnc/xstartup 



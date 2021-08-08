#!/bin/bash

cd $HOME
rm -rf .vnc/
wget https://github.com/Yisus7u7/termux-desktop-xfce/releases/download/4.0.2/data.tar.xz
tar -xvf data.tar.xz
rm data.tar.xz
wget https://github.com/Yisus7u7/termux-desktop-xfce/releases/download/kde/breeze-cursor-theme_5.20.5-4_all.deb
apt install ./breeze-cursor-theme_5.20.5-4_all.deb
rm breeze-cursor-theme_5.20.5-4_all.deb


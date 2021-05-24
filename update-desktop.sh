#!/bin/bash

clear 

echo "Updating desktop, please wait"

sleep 5

#install new packages

pkg up
git pull

#configuring update

rm -rf $PREFIX/bin/music
rm -rf $PREFIX/startdesktop 
cp -rf $HOME/termux-desktop-xfce/music $PREFIX/bin
cp -rf $HOME/termux-desktop-xfce/startdesktop $PREFIX/bin
rm -rf $HOME/.config.old 
cp -rf $HOME/.config $HOME/.config.old 
rm -rf $HOME/.config 
cp -rf $HOME/termux-desktop-xfce/.config $HOME
cp -rf $HOME/termux-desktop-xfce/README.desktop $HOME/Desktop
cp -rf $HOME/termux-desktop-xfce/.icons/* $HOME/.icons/
cp -rf $HOME/termux-desktop-xfce/.themes/* $HOME/.themes/
cp -rf $HOME/termux-desktop-xfce/backgrounds/* $HOME/backgrounds/

clear 

echo "update finished, enjoy!"

exit

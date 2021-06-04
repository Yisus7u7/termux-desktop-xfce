#!/bin/bash

clear 

echo "Updating desktop, please wait"

#install new packages

pkg up
git pull

clear

#configuring update

echo "backing up files and adding new config files"

rm -rf $PREFIX/bin/music
rm -rf $PREFIX/startdesktop 
cp -rf $HOME/termux-desktop-xfce/music $PREFIX/bin
cp -rf $HOME/termux-desktop-xfce/startdesktop $PREFIX/bin
rm -rf $HOME/.config.old 
mv -f $HOME/.config $HOME/.config.old 
cp -rf $HOME/termux-desktop-xfce/.config $HOME
cp -rf $HOME/termux-desktop-xfce/README.desktop $HOME/Desktop
cp -rf $HOME/termux-desktop-xfce/.icons/* $HOME/.icons/
cp -rf $HOME/termux-desktop-xfce/.themes/* $HOME/.themes/
cp -rf $HOME/termux-desktop-xfce/backgrounds/* $HOME/backgrounds/

echo "update finished, enjoy!"

exit

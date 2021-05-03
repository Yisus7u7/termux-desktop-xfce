#!/bin/bash

clear 

echo "Updating desktop, please wait"

rm -rf $PREFIX/bin/music

rm -rf $PREFIX/startdesktop 

cp -rf $HOME/termux-desktop-xfce/music $PREFIX/bin

cp -rf $HOME/termux-desktop-xfce/startdesktop $PREFIX/bin

rm -rf $HOME/.config.old 

cp -rf $HOME/.config $HOME/.config.old 

rm -rf $HOME/.config 

cp -rf $HOME/termux-desktop-xfce/.config $HOME

clear 

echo "update finished, enjoy!"

exit

#!/bin/bash

clear 

#this script will configure a graphical user interface 
#(xfce4) in termux
#creator: @Yisus7u7v

echo -e """

\e[1;33mTermux Desktop\e[1m 
   \e[1;31mby \e[4;36mYisus7u7\e[4m \e[1m


"""

cd $HOME

echo -e '\e[1;36m installing packages, it is necessary  \e[1m'
echo -e '''
\e[1;31m Download speed depends on
 your internet connection \e[1m'''

sleep 3

clear

echo -e '\e[1;36m installing xfce4 and basic apps...\e[1m'

sleep 1 

pkg update && pkg upgrade
pkg install -y x11-repo 
pkg install -y xfce4 xfce4-taskmanager dosbox xfce4-terminal python-tkinter htop neofetch loqui vim-gtk the-powder-toy galculator xorg-xhost mpv ristretto xfce4-whiskermenu-plugin xfce4-clipman-plugin xarchiver tigervnc geany geany-plugins gtk3 gtk2 mtpaint leafpad hexchat netsurf recordmydesktop feh
clear

echo -e '\e[1;31mSetting up vnc server ...\e[1m'

sleep 3

#setting folders

rm -rf $HOME/.vnc
mv $HOME/.config $HOME/.config.old
rm -rf $HOME/.icons
rm -rf $HOME/.themes
mv ./music $PREFIX/bin/music

#installing dotfiles

clear
echo "Wait a sec...."
cp -rf $HOME/termux-desktop-xfce/music $PREFIX/bin
cp -rf $HOME/termux-desktop-xfce/startdesktop $PREFIX/bin
cp -rf $HOME/termux-desktop-xfce/backgrounds $HOME
cp -rf $HOME/termux-desktop-xfce/.icons $HOME
cp -rf $HOME/termux-desktop-xfce/.themes $HOME
cp -rf $HOME/termux-desktop-xfce/.vnc $HOME
cp -rf $HOME/termux-desktop-xfce/.config $HOME
mkdir $HOME/Desktop 
mkdir $HOME/Downloads 
mkdir $HOME/Templates 
mkdir $HOME/Public 
mkdir $HOME/Documents 
mkdir $HOME/Pictures 
mkdir $HOME/Video
cp -rf $HOME/termux-desktop-xfce/README.desktop $HOME/Desktop
termux-setup-storage
ln -s $HOME/storage/music $HOME/Music 

bash $HOME/.icons/install-papirus.sh

read -p "\e[1; Do you want to compile extra plugins on-device??[y/n]" in

if [[ $in -eq y]]
then
    bash compile-install.sh
    echo -e """\e[1;32menjoy!!
    To start the vnc server, use the command: vncserver or startdesktop to stop it, use the command: vncserver -kill: 1 Replace the: 1 with the port on which the vnc service is running\e[1m"""

else
echo -e """\e[1;32menjoy!!
To start the vnc server, use the command: vncserver or startdesktop to stop it, use the command: vncserver -kill: 1 Replace the: 1 with the port on which the vnc service is running\e[1m"""
exit

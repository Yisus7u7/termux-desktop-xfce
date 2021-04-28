#!/bin/bash

clear 

#this script will configure a graphical user interface 
#(xfce4) in termux
#creator: @Yisus7u7v
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

pkg install -y xfce4 xarchiver tigervnc geany gtk3 python-tkinter leafpad hexchat netsurf xfce4-terminal recordmydesktop feh mtpaint dosbox

pkg install -y loqui vim-python htop neofetch

pkg install -y neovim 

pkg install -y vim-gtk

pkg install -y mpv mtpaint feh dosbox pulseaudio the-powder-toy htop galculator xorg-xhost

clear

echo -e '\e[1;31mSetting up vnc server ...\e[1m'

sleep 3
#setting folders
rm -rf $HOME/.vnc

mv $HOME/.config $HOME/.config.old

rm -rf $HOME/.icons

rm -rf $HOME/.themes

mv music $PREFIX/bin/music

#installing dotfiles

clear

echo "espere un momento...."

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

termux-setup-storage

cd $HOME

ln -s $HOME/storage/music Music 

mkdir $HOME/Music

cd $HOME/.icons

bash install-papirus.sh 

cd $HOME

echo -e """\e[1;32menjoy!!
To start the vnc server, use the command: vncserver or startdesktop to stop it, use the command: vncserver -kill: 1 Replace the: 1 with the port on which the vnc service is running\e[1m"""

exit



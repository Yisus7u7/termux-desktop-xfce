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

pkg install -y xfce4 

pkg install -y xfce4-taskmanager

pkg install -y xfce4-whiskermenu-plugin

pkg install -y xfce4-clipman-plugin

pkg install -y xarchiver 

pkg install -y tigervnc 

pkg install -y geany 

pkg install -y geany-plugins

pkg install -y gtk3 gtk2 mtpaint

pkg install -y leafpad hexchat 

pkg install -y netsurf recordmydesktop 

pkg install -y feh 

pkg install -y dosbox

pkg install -y xfce4-terminal

pkg install -y python-tkinter 

pkg install -y htop 

pkg install -y neofetch

pkg install -y loqui

pkg install -y neovim 

pkg install -y vim-gtk

pkg install -y the-powder-toy 

pkg install -y galculator 

pkg install -y xorg-xhost

pkg install -y mpv 

pkg install -y tumbler

pkg install -y ristretto

pkg install -y 

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



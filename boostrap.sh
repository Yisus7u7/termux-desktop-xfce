#this script will configure a graphical user interface
#(xfce4) in termux
#creator: @Yisus7u7
#Maintainer: st0rmc4non
cd $HOME

echo -e '\e[1;36m Installing necessary packages...  \e[1m'
echo -e '''
\e[1;31m Download speed depends on
 your internet speed \e[1m'''

sleep 3

clear

echo -e '\e[1;36m Upgrading Packages...\e[1m'

apt update && apt upgrade -y
clear

echo -e '\e[1;36m Installing Prequisites...\e[1m'

sleep 3
apt install -y wget x11-repo
rm $PREFIX/etc/apt/sources.list.d/termux-desktop-xfce.list
wget -P $PREFIX/etc/apt/sources.list.d https://raw.githubusercontent.com/Yisus7u7/termux-desktop-xfce/gh-pages/termux-desktop-xfce.list
apt update

sleep 3

clear

echo -e '\e[1;36m Installing the XFCE Desktop Environment\e[1m'
sleep 3
apt install -y xfce4 tigervnc xfce4-goodies termux-desktop-xfce breeze-cursor-theme ttf-microsoft-cascadia
sleep 3

clear

echo -e '\e[1;36m Installing applications you might use...\e[1m'

apt install -y otter-browser geany hexchat cantata audacious-plugins audacious leafpad pavucontrol-qt kvantum polybar xfce-theme-manager netsurf lynx
sleep 3

clear

echo -e '\e[1;36m Grabbing wallpapers...\e[1m'
sleep 3
wget https://github.com/Yisus7u7/termux-desktop-xfce/releases/download/desktop-5.0.3/data.tar.xz
tar -xvf data.tar.xz
rm data.tar.xz
clear

echo -e '\e[1;36m FIX: XStartup\e[1m'
sleep 3
wget https://github.com/Yisus7u7/termux-desktop-lxqt/releases/download/data/termux_desktop_lxqt_data.tar.xz
tar -xvf termux_desktop_lxqt_data.tar.xz
rm data.tar.xz
sleep 3
clear

echo " Finalizing..."
sleep 3
rm -rf $HOME/.backup
mkdir $HOME/.backup
mv $HOME/.config $HOME/.backup
mv $HOME/.vnc $HOME/.backup
cd $HOME
mkdir $HOME/Desktop
mkdir $HOME/Downloads
mkdir $HOME/Templates
mkdir $HOME/Public
mkdir $HOME/Documents
mkdir $HOME/Pictures
mkdir $HOME/Videos
ln -s $HOME/storage/music Music
cd $HOME
mv $PREFIX/share/kvantum/* $PREFIX/share/Kvantum
clear

echo -e """\e[1;32menjoy!!
To start the vnc server, use the command: vncserver to stop it, use the command: vncserver -kill: 1 Replace the: 1 with the port on which the vnc service is running\e[1m"""

exit

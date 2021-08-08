#!/bin/python3

from os import system
from colorama import Back, Fore, init, Style
from time import sleep

init(autoreset=True)

AZUL = Fore.BLUE
VERDE = Fore.GREEN
AMARILLO = Fore.YELLOW
AZULREY = Fore.CYAN
MORADO = Fore.MAGENTA
BRILLO = Style.BRIGHT
RESET = Style.RESET_ALL

PKGSMAIN = "wget mpv-x xfce4 geany thunar geany-plugins leafpad zenity libnotify xfce4-whiskermenu-plugin xfce4-clipman-plugin xorg-xhost uget ristretto galculator arqiver pinentry-gtk mtpaint lximage-qt lxqt-notificationd lxtask loqui mate-settings-daemon mate-terminal"

DIRS = "~/Desktop ~/Documents ~/Downloads ~/Public ~/Videos ~/Templates ~/Pictures"

def main():
	system('pkg update -y')
	system('pkg upgrade -y')
	print(BRILLO + MORADO + "==> Termux-Desktop-xfce", RESET + AMARILLO + BRILLO + "by", RESET + AZULREY + BRILLO + "Yisus7u7")
	print(BRILLO + AZUL + "Installing the desktop, push enter to continue")
	input(BRILLO + VERDE + ">> ")
	system('yes | pkg install' + PKGSMAIN + " -y")
	
	print(BRILLO + MORADO + "==> ", RESET + BRILLO + VERDE + "Clean unnecessary files from disk")
	sleep(3)
	system('rm -rf ~/.cache/*')
	system('apt clean && apt autoremove')
	system('cd ~/termux-desktop-xfce')
	
	print(BRILLO + MORADO + "==> ", BRILLO + VERDE + "Setting directories for installation")
	system('termux-setup-storage')
	system('rm -rf ~/.config.old ~/.icons ~/.themes ~/.profile')
	system('mv ~/.config ~/.config.old')
	system('mkdir -p ' + DIRS)
	system('ln -s ~/storage/music ~/Music')
	
	print(BRILLO + MORADO + "Installing data...")
	system('cp ~/termux-desktop-xfce/data.tar.xz ~/data.tar.xz')
	system('cd $HOME')
	system('tar -xvf ./data.tar.xz')
	system('rm ./data.tar.xz')
	system('wget https://github.com/Yisus7u7/termux-desktop-xfce/releases/download/kde/breeze-cursor-theme_5.20.5-4_all.deb')
	system('apt install ./breeze-cursor-theme_5.20.5-4_all.deb')
	system('rm ./breeze-cursor-theme_5.20.5-4_all.deb')
	system('rm $PREFIX/bin/startdesktop'), system('rm $PREFIX/bin/stopdesktop')
	system('cp ~/termux-desktop-xfce/startdesktop $PREFIX/bin')
	system('cp ~/termux-desktop-xfce/stopdesktop $PREFIX/bin')
	
	print(BRILLO + AZULREY + "To start the vnc server, use the command: vncserver or startdesktop to stop it, use the command: stopdesktop")
	
	
	
main()

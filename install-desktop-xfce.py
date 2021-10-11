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

ENABLE_X_REPO="pkg install -y x11-repo"
PKGSMAIN = "wget mpv-x xfce4 geany thunar geany-plugins featherpad zenity libnotify xfce4-whiskermenu-plugin xfce4-clipman-plugin xorg-xhost uget ristretto galculator arqiver pinentry-gtk mtpaint lximage-qt lxqt-notificationd xfce4-taskmanager loqui audacious qt5-qtbase-gtk-platformtheme kvantum qt5ct otter-browser tigervnc"
DIRS = "$HOME/Desktop $HOME/Documents $HOME/Downloads $HOME/Public $HOME/Videos $HOME/Templates $HOME/Pictures"

def main():
	system('pkg update -y')
	system('pkg upgrade -y')
	print(BRILLO + MORADO + "==> Termux-Desktop-xfce", RESET + AMARILLO + BRILLO + "by", RESET + AZULREY + BRILLO + "Yisus7u7")
	print(BRILLO + AZUL + "Installing the desktop, push enter to continue")
	input(BRILLO + VERDE + ">> ")
	system('yes | pkg install' + PKGSMAIN + " -y")
	
	print(BRILLO + MORADO + "==> ", RESET + BRILLO + VERDE + "Clean unnecessary files from disk")
	sleep(3)
	system('rm -rf $HOME/.cache/*')
	system('apt clean && apt autoremove')
	
	print(BRILLO + MORADO + "==> ", BRILLO + VERDE + "Setting directories for installation")
	system('termux-setup-storage')
	system('rm -rf $HOME/.config.old $HOME/.icons $HOME/.themes $HOME/.profile')
	system('mv $HOME/.config $HOME/.config.old')
	system('mkdir -p ' + DIRS)
	system('ln -s $HOME/storage/music $HOME/Music')
	
	print(BRILLO + MORADO + "Installing data...")
	system('bash ./postins.sh')
	system('rm $PREFIX/bin/startdesktop'), system('rm $PREFIX/bin/stopdesktop')
	system('cp ~/termux-desktop-xfce/startdesktop $PREFIX/bin')
	system('cp ~/termux-desktop-xfce/stopdesktop $PREFIX/bin')
	
	print(BRILLO + AZULREY + "To start the vnc server, use the command: vncserver or startdesktop to stop it, use the command: stopdesktop")
	
	
system('pkg update -y')
system(ENABLE_X_REPO)	
main()

# termux-desktop-xfce
Set up a beautiful xfce desktop in termux 

## Requirements

No root permissions required

Android 7, 8, 9, 10, 11 or 12

Termux : https://f-droid.org/en/packages/com.termux/

1 GB of ram minimum, 2 GB recommended 
1 GB of space 
A vnc client with which to connect, you can use this

https://play.google.com/store/apps/details?id=com.realvnc.viewer.android

You can also use xserver-xsdl, bvnc pro or kali-Kex

> Note: the play store termux is unmaintained and does not receive updates, 
do not use it, it is deprecated, use the one from the link above 

# What is it?

This is an advanced configuration of termux x11, rich in features to be highly functional, 
good looking, highly customizable and with very good optimization, this was inspired by @WMCB-Tech 's [dotfiles](https://github.com/WMCB-Tech/dotfiles) and from @adi1090x 's [termux-desktop](https://github.com/adi1090x/termux-desktop) , resulting in a highly useful and optimized desktop. 

# Screenshots:

> current version: 4.0.2 Arc update 

![escritorio](./fotos/desktop.png)
![escritorio](./fotos/desktop2.png)
![escritorio](./fotos/desktop3.png)
![escritorio](./fotos/desktop5.png)
![escritorio](./fotos/desktop6.png)


> Note: The following images are from older versions of the project 
 

![escritorio](./fotos/desktop7.png)

> Note: This desktop runs under termux natively, it is not a proot distribution

# Take a look at the pre-installed utilities

### Task Manager and music player

![task](./fotos/task.png)
![music](./fotos/music1.png)
![music_player](./fotos/play_music.png)

### Surf the web, edit your files with Gvim, leafpad, and chat on irc channels with hexchat

![image1](./fotos/web-and-mail.png) 
![image2](./fotos/chat_vim_text-editor.png) 

### Write code with autocompletion and syntax highlighting with geany

![Geany](./fotos/geany.png)

### Play retro games or run windows 1, 2 or 3 on dosbox emulator

![xarchiver](./fotos/xarchiver.png)
![install-doom](./fotos/install_doom.png)
![doom men�?](./fotos/playdoom-menu.png)
![play_doom](./fotos/play_doom.png)

### Less apps ?, I have made a configuration to run the apps of a proot distro in termux native desktop. An example:

```
./start-ubuntu.sh
apt install firefox
export DISPLAY=:1
firefox 
```

### You can run proot apps without problems

![firefox](./fotos/proot-firefox.png) 
![libreoffice_load](./fotos/proot-libreoffice.png) 
![libreoffice_app](./fotos/proot-libreoffice2.png) 

# Installation

! Only in termux

```bash
cd $HOME
pkg update && pkg upgrade 
pkg install git wget python
pip install colorama
git clone --depth 1 https://github.com/Yisus7u7/termux-desktop-xfce
cd termux-desktop-xfce
chmod +x *.sh *.py
python3 ./install-desktop-xfce.py
```

After that just have a cup of coffee... the script will do its job 

# Usage

```
startdesktop 
```

Or 

```
vncserver -listen tcp 
```

To start the vnc server, connect to localhost: 1 Or the port indicated by the terminal.
Any error, question or suggestion, report it in:
https://github.com/Yisus7u7/termux-desktop-xfce/issues


I hope you like this little work, don't forget to leave your 🌟 and share: 3 

You can donate to this little project in PayPal

https://www.paypal.me/JesusChapman 

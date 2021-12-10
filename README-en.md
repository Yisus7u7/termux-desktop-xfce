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
good looking, highly customizable and with very good optimization, this was inspired by @Manjaro [manjaro-site](https://manjaro.org) and from @adi1090x 's [termux-desktop](https://github.com/adi1090x/termux-desktop) , resulting in a highly useful and optimized desktop. 

# Screenshots:

> current version: 5.0.3 update 

![escritorio](./fotos/desktop.png)
![escritorio](./fotos/desktop2.png)
![escritorio](./fotos/desktop3.png)
![escritorio](./fotos/desktop5.png)
![escritorio](./fotos/desktop6.png)
![escritorio](./fotos/chat_and_youtube.png)

# Themes

Aside from the above screenshots, there are many
more themes you can change from settings, too
other wallpapers

![graphite](./fotos/theme1)
![Colliod](./fotos/theme2)

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
curl -sLf https://raw.githubusercontent.com/Yisus7u7/termux-desktop-xfce/main/boostrap.sh | bash
```

After that just have a cup of coffee... the script will do its job 

# Usage
Run:

```bash
vncserver -listen tcp 
```

To start the vnc server, connect to localhost: 1 Or the port indicated by the terminal.
Any error, question or suggestion, report it in:
https://github.com/Yisus7u7/termux-desktop-xfce/issues


I hope you like this little work, don't forget to leave your 🌟 and share: 3 

You can donate to this little project in PayPal

https://www.paypal.me/JesusChapman 

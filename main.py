#! /data/data/com.termux/files/usr/bin/python
import os
from os   import system as sys
from os   import chdir  as cd
from sys  import argv
from time import sleep

try :
    import colorama
except ModuleNotFoundError :
    sleep(1)
    sys(' echo -e "\033[1;35m ERROR     : \033[1;32m Module colorama Not Found " ')
    sleep(3)
    sys('echo -e "\033[1;35m FETCHING  : \033[1;32m colorama "')
    sys(' pip install colorama ')
    sys(' echo -e "\033[0m"')
    
# -- BEING COLORS --
from colorama import *    
init(autoreset=True)
Green   = Fore.GREEN   + Style.BRIGHT
Red     = Fore.RED     + Style.BRIGHT
Yellow  = Fore.YELLOW  + Style.BRIGHT
Blue    = Fore.BLUE    + Style.BRIGHT
Magenta = Fore.MAGENTA + Style.BRIGHT
Cyan    = Fore.CYAN    + Style.BRIGHT
# -- END   COLORS --
f_v = '0'
try :
    x11=open("/data/data/com.termux/files/usr/etc/apt/sources.list.d/x11.list")
except FileNotFoundError :
    sleep(1)
    print(Magenta + " ERROR      : " + Green + " Mirror x11 Not Found")
    sleep(3)
    print(Magenta + " INSTALLING : " + Green + " x11")
    sleep(1)
    sys('pkg install -y x11-repo')

class install :
    def xfce(version,url):
        PKG = "wget mpv-x xfce4 geany thunar geany-plugins featherpad zenity libnotify xfce4-whiskermenu-plugin xfce4-clipman-plugin xorg-xhost uget ristretto galculator arqiver pinentry-gtk mtpaint lximage-qt lxqt-notificationd xfce4-taskmanager loqui audacious qt5-qtbase-gtk-platformtheme kvantum qt5ct otter-browser tigervnc"
        DIR = "$HOME/Desktop $HOME/Documents $HOME/Downloads $HOME/Public $HOME/Videos $HOME/Templates $HOME/Pictures"

        print(Magenta+"\t   TERMUX - DESKTOP \n")
        sleep(1)
        print(Magenta+" ENVIRONMENT : "+Cyan  + "XFCE")
        sleep(0.3)
        print(Magenta+" VERSION     : "+Green + version)
        sleep(2)
        input(Magenta+"\n Push Enter To Continue "+Cyan+">>")
        sleep(2)
        print(Magenta+"\t  INSTALLING PACKAGES"+Green+"...")
        sleep(0.5)
        sys('pkg install -y '+PKG)
        sleep(1)
        print(Magenta+"\t    GETTING ICON FILE "+Green+"...")
        sleep(1)
        sys('rm -rf $HOME/.vnc')
        sys('wget '+url+" -O $HOME/data.tar.xz")
        print(Magenta+"\n\t   EXTRACTING FILE "+Green+"...")
        sleep(3)
        sys('tar -xvf $HOME/data.tar.xz --directory $HOME')
        sleep(2)
        print(Magenta+"\t  REMOVING CACHED DATA "+Green+"...")
        sys('rm $HOME/data.tar.xz')
        #sys('wget https://github.com/Yisus7u7/termux-desktop-lxqt/releases/downlo -O $')
        sys('wget https://github.com/Yisus7u7/termux-desktop-xfce/releases/download/kde/breeze-cursor-theme_5.20.5-4_all.deb -O $HOME/theme.deb')
        sys('dpkg -i $HOME/theme.deb')
        sys('rm $HOME/theme.deb')
        sys('wget https://github.com/Yisus7u7/termux-desktop-xfce/releases/download/arc/termux-arc-gtk-theme_20210412_all.deb -O $HOME/atheme.deb')
        sys('dpkg -i $HOME/atheme.deb')
        sys('rm $HOME/atheme.deb')

        print(Magenta+"\n\n To Start The Vnc Server, Type :"+Green+" e-tnv"+" start")
        print(Magenta+" To Stop it, Type              :"+Green+" e-tnv"+" stop")
        print(Magenta+" Or                             "+Green+" e-tnv"+" stopall")


    def lxqt(version,url):
        PKG = "xcompmgr audacious wget xpdf qt5-qtbase-gtk-platformtheme qt5-qttools qt5-qtx11extras lxqt lxqt-build-tools otter-browser qgit featherpad gtk2 gtk3 python-tkinter tigervnc xorg-xhost openbox geany qt5-qtwebsockets qt5-qtxmlpatterns qt5-qtdeclarative termux-api geany-plugins xorg-xprop neofetch galculator qt5-qttools glade feathernotes xorg-xprop mtpaint xorg-xhost"
        DIR = "$HOME/Desktop $HOME/Documents $HOME/Downloads $HOME/Public $HOME/Videos $HOME/Templates $HOME/Pictures"
        print(Magenta+"\t   TERMUX - DESKTOP \n")
        sleep(1)
        print(Magenta+" ENVIRONMENT : "+Cyan  + "LXQT")
        sleep(0.3)
        print(Magenta+" VERSION     : "+Green + version)
        sleep(2)
        input(Magenta+"\n Push Enter To Continue "+Cyan+">> ")
        sleep(2)
        print(Magenta+"\t  INSTALLING PACKAGES"+Green+"...")
        sleep(0.5)
        sys('pkg install -y '+PKG)
        sleep(1)
        print(Magenta+"\t    GETTING ICON FILE "+Green+"...")
        sleep(1)
        sys('rm -rf $HOME/.vnc')
        sys('wget '+url+" -O $HOME/data.tar.xz")
        print(Magenta+"\n\t   EXTRACTING FILE "+Green+"...")
        sleep(3)
        sys('tar -xvf $HOME/data.tar.xz --directory $HOME')
        sleep(2)
        print(Magenta+"\t  REMOVING CACHED DATA "+Green+"...")
        sys('wget https://github.com/Yisus7u7/termux-desktop-lxqt/releases/download/data/breeze-cursor-theme_5.20.5-4_all.deb -O $HOME/theme.deb')
        sys('dpkg -i $HOME/theme.deb')
        sys('rm $HOME/theme.deb')
        sys('rm $HOME/data.tar.xz')
        print(Magenta+"\n\n To Start The Vnc Server, Type :"+Green+" e-tnv"+" start")
        print(Magenta+" To Stop it, Type              :"+Green+" e-tnv"+" stop")
        print(Magenta+" Or                             "+Green+" e-tnv"+" stopall")



cmd = '0'
try :
    cmd = argv[1].lower()
except :
    pass

if cmd == 'start':
    sys('vncserver -listen tcp')
    sys('vncserver -list')
    sys('termux-open vnc://127.0.0.1:5901')

elif cmd == 'stop':
    try :
        tn=int(input(Magenta+"Enter DISPLAY ID To Kill"+Green+" : "))
        tmp=str(tn)
        sys('vncserver -kill :'+tmp)
    except ValueError:
        print(Magenta+"ERROR :"+Green+"Input Id be an Integer Only !!!")

elif cmd == 'stopall':
    print(Magenta+"\t   Killing Xvnc")
    sys('killall Xvnc')
    print(Magenta+"\t   Process "+Green+": KILLED")

elif cmd == '-r' or cmd == '--remove':
    print(Magenta+"\n\t REMOVING FILES "+Green+"...")
    sleep(3)
    sys('rm -rf $HOME/.local $HOME/.icons $HOME/.cache $HOME/.config $HOME/.vnc $HOME/.themes')
    print(Magenta+" Process "+Green+" : FINISHED ")

elif cmd == '-unin' or cmd == '--uninstall' or cmd == '-u':
    ui=input(Magenta +"  Do You Want To Uninstall ? \n "+Green+" Other Unsaved Data will be DELETED\n"+Yellow+"  Type yes To Continue "+Green+" : ")
    tmp = ui.lower()
    if tmp == 'yes' :
        print(Magenta +"\t   Uninstalling"+Green+" ...")
        sleep(2)
        sys('pkg uninstall mpv-x xfce4 geany thunar geany-plugins featherpad zenity libnotify xfce4-whiskermenu-plugin xfce4-clipman-plugin xorg-xhost uget ristretto galculator arqiver pinentry-gtk mtpaint lximage-qt lxqt-notificationd xfce4-taskmanager loqui audacious qt5-qtbase-gtk-platformtheme kvantum qt5ct otter-browser tigervnc xcompmgr audacious xpdf qt5-qtbase-gtk-platformtheme qt5-qttools qt5-qtx11extras lxqt lxqt-build-tools otter-browser qgit featherpad gtk2 gtk3 python-tkinter tigervnc xorg-xhost openbox geany qt5-qtwebsockets qt5-qtxmlpatterns qt5-qtdeclarative termux-api geany-plugins xorg-xprop neofetch galculator qt5-qttools glade feathernotes xorg-xprop mtpaint xorg-xhost')
        sys('apt clean')
        sys('apt autoremove -y')
        sys('rm -rf $HOME/.local $HOME/.icons $HOME/.cache $HOME/.config $HOME/.vnc $HOME/.themes')
        print(Magenta+"  Process"+Green+" : FINISHED")
    else :
        print(Magenta+"\n  Process"+Green+" : CANCELLED")
elif cmd == '--help' or cmd == '-h' :
    print("\nUsage :  "+argv[0]+" option [option] \n\noptions : \n\n   -in or --install\t install desktop environment\n   -unin or --uninstall\t uninstall desktop completely\n   start\t         for start vncserver\n   stop\t                 for stop desktop by id\n   stopall\t         for kill all vncservers\n   -r or --remove\t remove themes and icon files\n\n   Example : \n \t e-tnv --install xfce 3.0.9")

elif cmd == '--list' or cmd == '-l':
    print(Magenta+" \n"+Green+" Versions : \n\t"+Magenta+"xfce"+Green+" [ 3.0.1 ] \n\t"+Magenta+"xfce"+Green+" [ 3.0.4 ] \n\t"+Magenta+"xfce"+Green+" [ 3.0.9 ] \n\t"+Magenta+"xfce"+Green+" [ 4.0.2 ] "+Yellow+"[ Default ]\n\n\t"+Magenta+"lxqt"+Green+" [ 1.0.4 ] \n\t"+Magenta+"lxqt"+Green+" [ 2.0.1 ] \n\t"+Magenta+"lxqt"+Green+" [ 2.1.3 ]"+Yellow+"[ Default ] ")

elif cmd == '-i' or cmd =='-in' or cmd == '--install':
    try :
        usr_d = '0'
        usr_d = argv[2].lower()
    except IndexError :
        print(Green+" [1]"+Yellow+" Install"+Magenta+" XFCE ")
        print(Green+" [2]"+Yellow+" Install"+Magenta+" LXQT ")
        try :
            tmp1 = int(input(Magenta+" >> "+Green))
            if tmp1 > 2 or tmp1 < 1 :
                print(Magenta+" ERROR "+Green+":  Undefined Range   ")
            elif tmp1 == 1 :
                usr_d = 'xfce'
            else :
                usr_d = 'lxqt' 
        except ValueError :
            print(Magenta+" ERROR "+Green+":  Input Must Be An Integer  ")
            exit(0)
        if usr_d == 'xfce' :
            print(Yellow+"\t   Select Version ")
            print(Green+" [1]"+Magenta+" 4.0.2 [ Recommended ]")
            print(Green+" [2]"+Magenta+" 3.0.9")
            print(Green+" [3]"+Magenta+" 3.0.4")
            print(Green+" [4]"+Magenta+" 3.0.1")
            try :
                tmp3 = int(input(Magenta+" >> "+Green))
                if tmp3 == 1 :
                    f_v = '4.0.2'
                elif tmp3 == 2 :
                    f_v = '3.0.9'
                elif tmp3 == 3 :
                    f_v = '3.0.4'
                elif tmp3 == 4 :
                    f_v = '3.0.1'
                else :
                    print(Magenta+" ERROR "+Green+": Undefined Range")
                    exit(0)
            except :
                print(Magenta+" ERROR OCCURED "+Green+"...")
            

        elif usr_d == 'lxqt' :
            print(Yellow+"\t   Select Version ")
            print(Green+" [1]"+Magenta+" 2.1.3 [Recommended]")
            print(Green+" [2]"+Magenta+" 2.0.1")
            print(Green+" [3]"+Magenta+" 1.0.4")
            try :
                tmp3 = int(input(Magenta+" >> "+Green))

                if tmp3 == 1 :
                    f_v = '2.1.3'
                elif tmp3 == 2 :
                    f_v = '2.0.1'
                elif tmp3 == 3 :
                    f_v = '1.0.4'
                else :
                    print(Magenta+" ERROR "+Green+"  Undefined Range ")
            except :
                print(Magenta+" Error Occured")
                exit(0)
    usr_v = '0'
    try :
        usr_v = argv[3]
        if usr_d == 'xfce' :
            if usr_v == '4.0.2':
                f_v = '4.0.2'
            elif usr_v == '3.0.9':
                f_v = '3.0.9'
            elif usr_v == '3.0.4':
                f_v = '3.0.4'
            elif usr_v == '3.0.1' :
                f_v = '3.0.1'
            else :
                print(Magenta+"ERROR "+Green+":  Version Not Found")
        elif usr_d == 'lxqt':
            if usr_v == '1.0.4':
                f_v = '1.0.4'
            elif usr_v == '2.0.1':
                f_v = '2.0.1'
            elif usr_v == '2.1.3':
                f_v = '2.1.3'
            
    except:
        if usr_d == 'xfce' :
            if f_v == '0' :
                f_v = '4.0.2'
        elif usr_d == 'lxqt':
            if f_v == '0' :
                f_v =   '2.1.3'
            
            
        
       # if usr_d == 'lxqt':
           # f_v = '2.1.3'
            
    #if usr_d == 'xfce':
        #print(usr_d)
        #print(f_v)
    #elif usr_d == 'lxqt':
        #print(usr_d)
        
    if usr_d == 'xfce' :
        if f_v == '4.0.2' :
            url = 'https://github.com/Yisus7u7/termux-desktop-xfce/releases/download/4.0.2/datar.tar.xz'
        elif f_v == '3.0.9' :
            url = 'https://github.com/er-termux/desktop-files-2/raw/main/xfce/3.0.9/data.tar.xz'
        elif f_v == '3.0.4' :
            url = 'https://github.com/er-termux/desktop-files-2/raw/main/xfce/3.0.4/data.tar.xz'
        elif f_v == '3.0.1' :
            url = 'https://github.com/er-termux/desktop-files/raw/main/xfce/3.0.1/data.tar.xz'

    elif usr_d == 'lxqt' :
        if f_v == '2.1.3' :
            url = 'https://github.com/Yisus7u7/termux-desktop-lxqt/releases/download/data/termux_desktop_lxqt_data.tar.xz'
        elif f_v == '2.0.1' :
            url = 'https://github.com/er-termux/desktop-files/raw/main/lxqt/2.0.1/data.tar.xz'
        elif f_v == '1.0.4' :
            url = 'https://github.com/er-termux/desktop-files/raw/main/lxqt/1.0.4/data.tar.xz'

    if usr_d == 'xfce' :
        sys('rm -rf .cache/ .config/ .icons/ .themes/ .vnc/')
        if f_v == '4.0.2' :
            install.xfce(f_v,url)
        elif f_v == '3.0.9' :
            install.xfce(f_v,url)
        elif f_v == '3.0.4' :
            install.xfce(f_v,url)
        elif f_v == '3.0.1' :
            install.xfce(f_v,url)
    elif usr_d == 'lxqt' :
        sys('rm -rf .cache/ .config/ .icons/ .themes/ .vnc/')
        if f_v == '2.1.3' :
            install.lxqt(f_v,url)
        elif f_v == '2.0.1' :
            install.lxqt(f_v,url)
        elif f_v == '1.0.4' :
            install.lxqt(f_v,url)


else :
    print(Magenta+"e-tnv"+Green+" : "+cmd + " : "+Yellow+"invalid option")
    print("\n Try :\n\t --help \t To See more Information")


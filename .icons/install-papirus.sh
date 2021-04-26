#!/bin/sh
# To Avoid Large files storing onto my repository, this should be installed in a script

wget -qO- https://git.io/papirus-icon-theme-install | DESTDIR="$HOME/.icons" sh

#!/bin/sh
# To Avoid Large files storing onto my repository, this should be installed in a script

TEMP=$(mktemp -d)

git clone https://github.com/daniruiz/flat-remix-gtk $TEMP

mv $TEMP/Flat-Remix-GTK-Blue* ~/.themes
rm -rf $TEMP

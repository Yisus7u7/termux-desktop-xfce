#!/bin/bash
 
echo get shpkg package manager...
sleep 2
rm $PREFIX/bin/shpkg
. <(curl -sL https://git.io/setup-shpkg.sh)
shpkg update
shpkg install qt5ct

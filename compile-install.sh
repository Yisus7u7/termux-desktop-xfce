#Optional tools that will be compiled on-device

pkg install unstable-repo intltool

wget https://archive.xfce.org/src/xfce/xfce4-dev-tools/4.16/xfce4-dev-tools-4.16.0.tar.bz2
tar -xvf xfce4-dev-tools-4.16.0.tar.bz2
cd xfce4-dev-tools-4.16.0/
autoreconf -fi
./configure --prefix=$PREFIX
make
make install
cd ..

exit

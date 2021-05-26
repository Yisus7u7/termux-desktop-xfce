#Optional tools that will be compiled on-device

pkg install perl python libexpat

cpan install XML::Parser
cpan install XML::LibXML

wget https://launchpad.net/intltool/trunk/0.51.0/+download/intltool-0.51.0.tar.gz
tar -xvf intltool-0.51.0.tar.gz
cd intltool-0.51.0/
autoreconf -fi
./configure --prefix=$PREFIX
make
make install
cd ..

wget https://archive.xfce.org/src/xfce/xfce4-dev-tools/4.16/xfce4-dev-tools-4.16.0.tar.bz2
tar -xvf xfce4-dev-tools-4.16.0.tar.bz2
cd xfce4-dev-tools-4.16.0/
autoreconf -fi
./configure --prefix=$PREFIX
make
make install
cd ..

pip install catfish

exit

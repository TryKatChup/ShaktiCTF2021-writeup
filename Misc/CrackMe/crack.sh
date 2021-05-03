#!/bin/sh

tr -d ' '      < dogs.txt     > dogs_tmp.txt
tr 'A-Z' 'a-z' < dogs_tmp.txt > dogs2.txt

tr -d ' '      < colors.txt     > colors_tmp.txt
tr 'A-Z' 'a-z' < colors_tmp.txt > colors2.txt

hashcat -a 1 -j '$_' -k '$_' dogs2.txt colors2.txt --stdout | grep _ > dogscolors.txt
hashcat -a 6 dogscolors.txt '?d?d'       --stdout | grep _ >> dogscolorsnumber.txt
hashcat -a 6 dogscolors.txt '0?d?d'       --stdout | grep _ >> dogscolorsnumber.txt
hashcat -a 6 dogscolors.txt '00?d?d'       --stdout | grep _ >> dogscolorsnumber.txt
hashcat -a 6 dogscolors.txt '+?d?d'       --stdout | grep _ >> dogscolorsnumber.txt
hashcat -a 6 dogscolors.txt '?d?d?d'     --stdout | grep _ >> dogscolorsnumber.txt
hashcat -a 6 dogscolors.txt '0?d?d?d'     --stdout | grep _ >> dogscolorsnumber.txt
hashcat -a 6 dogscolors.txt '00?d?d?d'     --stdout | grep _ >> dogscolorsnumber.txt
hashcat -a 6 dogscolors.txt '+?d?d?d'     --stdout | grep _ >> dogscolorsnumber.txt
#hashcat -a 6 dogscolors.txt '?d?d?d?d'   --stdout | grep _ >> dogscolorsnumber.txt
#hashcat -a 6 dogscolors.txt '?d?d?d?d?d' --stdout | grep _ >> dogscolorsnumber.txt
hashcat -a 0 -m 1400   test dogscolorsnumber.txt
hashcat -a 0 -m 17400   test dogscolorsnumber.txt

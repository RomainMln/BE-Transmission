#!/bin/bash


tail -c +7 fichier-recu.txt  > shift.txt
f=`cat shift.txt`
echo $f
#file=($file>>2)
echo ($f>>2)

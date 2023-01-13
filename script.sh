
#!/bin/bash



echo $f
f=$(($f>>2))
echo $f
tail -c +7 fichier-recu.txt  > shift.txt


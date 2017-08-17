#!/bin/bash

for str in $(cat ./file_list.txt);do var=$(echo $str | sed 's,/g/data3/fj7/Copernicus/,,g' | awk 'BEGIN{FS="/"; strA=""; strB"";}{ for (i=1;i<NF;i++){echo $i; strA=strA" mkdir "strB""$i" && " ; strB=strB""$i"/";}}END{print strA, " cd /projects/WACopernicus/"strB , " && put "}' | xargs -I% echo "cd /projects/WACopernicus && " % $str " && publish " $(echo $str | sed 's,/g/data3/fj7/Copernicus/,/projects/WACopernicus/,g') | xargs -I%  echo \"%\" ); echo "python pshell" $var;done  > bigList.txt

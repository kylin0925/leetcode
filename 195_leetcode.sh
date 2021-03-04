#!/bin/bash
filename='file.txt'
n=1
while read line; do
	# reading each line
	#echo "Line No. $n : $line"
	if [ "$n" -eq 10 ]; then
		echo "$line"
	fi
	n=$((n+1))

done < $filename

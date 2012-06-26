#!/bin/bash
for i in `cat mobile.de.hosts.txt` do
	if [ -n "$i" ] 
	then	
		echo $i > mobile.hosts.txt
	fi
done

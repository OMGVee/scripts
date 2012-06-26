#!/bin/bash
clear
echo "Dju wanna run another term window?"
select yn in "Yes" "No"; do
	case $yn in
		Yes ) open /Applications/Calculator.app;;
		No ) clear; exit;;
	esac
done


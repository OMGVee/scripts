#!/bin/sh
list1="data data2 proc dev sys musem wendy"
list2=""
first=1
for i in $list1
do
if test $first -eq 1
then
first=0
list2="$i"
fi
list2="$echo $list2\|$i"
done
ls / | grep -vw $list2

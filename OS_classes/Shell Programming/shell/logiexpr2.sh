#!/bin/sh
read a
read b
read c

if [ $a -gt $b -a $a -gt $c ]
then
echo "a is greater!"
else
echo "not greater!"
fi



 

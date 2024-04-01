#!/bin/sh
if [ `who | grep amma | wc -l` -ge 1 -a `whoami` != "amma" ]
then
echo "Bill is loading down the machine!"
else
echo "All is well!"
fi



 

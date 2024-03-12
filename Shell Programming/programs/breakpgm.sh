#!/bin/sh
while [ 1 ]
do
echo "Wakeup [yes/no]?"
#resp=yes
read resp
if [ $resp = "yes" ]
then
break
fi
done

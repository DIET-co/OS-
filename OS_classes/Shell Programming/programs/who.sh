#!/bin/sh

user=`whoami`
echo "user name is" $user

numusers=`who | wc -l`
echo "Hi $user! There are $numusers users logged on."

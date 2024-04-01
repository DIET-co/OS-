#!/bin/sh
		#echo "Enter number: "
		#read n
		n=5
		fac=1
		i=1
 		while [ $i -le 5 ]
		do
			fac=`expr $fac \* $i`
			i=`expr $i + 1`
		done
		echo "The factorial of $n is $fac"
		




#!/bin/sh
#testurl.sh
#looks at a list of websites to see if they are up. If they are not up it will
#let the user know

#value= `cat $1`
#echo "File: $value end of file\n"

IFS=''  
if [ $# -eq 0 ]
then
    echo "No arguments supplied"
    exit 1
fi

while read line
do
    if curl --output /dev/null --silent --head --fail "$line";then
	continue
    else 
	echo "Not found: $line"
    fi

done < $1

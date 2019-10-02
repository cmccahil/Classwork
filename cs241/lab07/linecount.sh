#!/bin/sh

#echo "$1"
if [ $# -eq 0 ]
then
    find . | wc -l * 
else
    find . -name "$1" | xargs wc -l
fi 


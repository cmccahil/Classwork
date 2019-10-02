#!/bin/sh 

gcc $1 -o diamonds
echo 5 | ./diamonds > tmp.txt

echo 5 | $2 > tmpone.txt

diff -q tmp.txt tmpone.txt 

rm tmp.txt tmpone.txt

#This script takes the students .c file and compiles it, passes in a value (depending on the file we are testing... rot128 will be any string...diamond will be a number 1-9), and puts it into a temporary file. We then take the graders version of the file (already compiled) and put it into a tempory file. We then compare the files, it will print something if they are different, if will not print anything if they are not. 

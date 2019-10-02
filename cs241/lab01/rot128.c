#include <stdio.h>
#include <limits.h>
//Colin McCahill
//9-10-2017
//Encrypts files by using a rot-128 encryption algorithm.

int main(){ 
    char y=getchar();
    while(y!=EOF){
	y=y+(UCHAR_MAX+1)/2;
	putchar(y);
	y=getchar();
    }

}


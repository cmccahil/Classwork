#include "getnum.h"
#include <stdio.h>

int main(){
    long number=getnum();
    while(number!=EOF){
	if(number>0){
	    printf("0x");
    }
	else if(number<0){
	    printf("-0x");
	    number=number*(-1);
    }
	else{
	    printf("0");
    }
	char hexadecimalnumber[36];
	int i=1;
	int temp=0;
	int quotient=number;
	while(quotient!=0){
	    temp=quotient%16; 
	    if(temp<10){
		temp=temp+48;
	    }
	    else{
		temp=temp+55;
	    }
	    hexadecimalnumber[i]=temp;
	    quotient=quotient/16;
	    i+=1;
	}
	for(int j=i-1;j>0;j--){
	   printf("%c",hexadecimalnumber[j]);
	}
	printf("\n");
	number=getnum();
    }
}


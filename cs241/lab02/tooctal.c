#include "getnum.h"
#include <stdio.h>

int main(){
    long number=getnum();
    while(number!=EOF){
	if(number>0){
	    printf("0");
	}
	else if(number<0){
	    printf("-0");
	    number=number*(-1);
	}
	else{
	    printf("0");
	}
	char octalnumber[36];
	int i=1;
	int temp=0;
	while(number!=0){
	    temp=number%8;
	    temp=temp+48;
	    octalnumber[i]=temp;
	    number=number/8;
	    i+=1;
	}
	for(int j=i-1;j>0;j--){
	    printf("%c",octalnumber[j]);
	}
	printf("\n");
	number=getnum();
    }
}

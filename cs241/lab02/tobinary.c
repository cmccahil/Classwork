#include "getnum.h"
#include <stdio.h>


int main(){
    long number=getnum();
    while(number!=EOF){
	if(number>0){
	    printf("0b");
	}
	else if(number<0){
	    printf("-0b");
	    number=number*(-1);
	}
	else{
	    printf("0");
	}
	long a[32];
	int counter=0;
	for(int i=0;number>0;i++){
	    a[i]=number%2;
	    number=number/2;
	    counter+=1;
	}
	for(counter=counter-1;counter>=0;counter--){
	    printf("%d",a[counter]);
	}
	printf("\n");
	number=getnum();
    }
}

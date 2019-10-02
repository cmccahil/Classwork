#include "getnum.h"
#include <stdio.h>

int main(){
    long number=getnum();

    while(number!=EOF){
	printf("%ld\n",number);

	number=getnum();


    }
}


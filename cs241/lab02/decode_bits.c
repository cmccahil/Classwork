#include <stdio.h>
#include <limits.h>
#include <math.h>
#include <ctype.h>


int main(){
    char y=getchar();
    while(y!=EOF){
	int currentlettervalue=0;
	for(int i=CHAR_BIT-1;i>=0;i--){
	    if(isspace(y)==0){
		if(y=='1'){
		    currentlettervalue=currentlettervalue+pow(2,i);
		    y=getchar();
		}
		else if(y=='0'){
		    y=getchar();
		}
		else{
		    printf("This file contains a non-binary value.\n");
		    exit(1);
		    }
		}
	    if(i==0){
		putchar(currentlettervalue);
	    }
    }
	
 	
}
exit(1);
}

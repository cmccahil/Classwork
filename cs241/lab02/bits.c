#include <stdio.h>
#include <limits.h>
#include <math.h>
#include <ctype.h>

void print_bits(char y){
    for(int i=CHAR_BIT-1;i>=0;i--){
	if((y>=pow(2,i))){
	    printf("%d",1);
	    y=y-pow(2,i);
	}
	else{
	    printf("%d",0);
	}
    }
}
   
void decode_bits(char z){
    static char characters[CHAR_BIT];
    static int counter=0;
    if(isspace(z)!=0){
	counter=0;
    }
    else{
	characters[counter]=z;
	counter+=1;
	if(counter==CHAR_BIT){
	    int currentlettervalue=0;
	    for(int i=0;i<CHAR_BIT-1;i++){
		if(characters[i]=='1'){
		    currentlettervalue=currentlettervalue+pow(2,(CHAR_BIT-i));
		}
		if(characters[i]!='1' && characters[i]!='0'){
		    printf("This file contains a non-binary value.\n");
		}
	    }
	    //printf("%d",currentlettervalue);
	    //putchar(currentlettervalue);
	    counter=0;
	}

    }

}

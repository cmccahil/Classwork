#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
char punct='\0';

void toenglish(char source[]){
    int wordsize=(int)strlen(source);
    if(source[wordsize-3]=='y'){//word starts with a vowel
	for(int i=0;i<(wordsize-3);i++){
	    printf("%c",source[i]);
	}
    }
    else if((source[wordsize-4]=='q') && (source[wordsize-3]=='u')){
	if((64<source[0]) && (source[0]<91)){ //capital letter case
	    source[0]=source[0]+32;
	    source[wordsize-4]=source[wordsize-4]-32;
	}
	printf("%c",source[wordsize-4]);
	printf("%c",source[wordsize-3]);
	for(int k=0;k<(wordsize-4);k++){
	    printf("%c",source[k]);
	}
    }
    else{
	if((64<source[0]) && (source[0]<91)){ //capital letter case
	    source[0]=source[0]+32;
	    source[wordsize-3]=source[wordsize-3]-32;
	}
	printf("%c",source[wordsize-3]);
	for(int i=0;i<(wordsize-3);i++){
	    printf("%c",source[i]);
	}
    }
    }

char * removepunctuation(char source[]){
    char *str=(char *) malloc(sizeof(char) * strlen(source));
    for(int t=0;t<(int)strlen(source);t++){
	if(ispunct(source[t])){
	    punct=source[t];
	    continue;
	}
	else{
	    str[strlen(str)]=source[t];
	}
    }
    return str;
    }


int main(int argc, char *argv[]){
    char flag1[2]="-h";
    char flag2[2]="-?";
    printf("\nPig Latin to English Translator\n");
    for(int i=1;i<argc;i++){
	if(((strncmp(argv[i], flag1, 2))==0) || ((strncmp(argv[i], flag2, 2))==0)){
	    printf("\n\nFlag was detected, program will now end\n");
	    exit(0);
	}
	char *returned_str=removepunctuation(argv[i]);
	toenglish(returned_str);
	printf("%c",punct);
	punct='\0';
	printf(" ");
    }
    printf("\n");
}


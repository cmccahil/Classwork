#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

char punct='\0';
char hyphenstring[100]="";

void topig(char source[]){
    char vowel[12]={'a','e','i','o','u','A','E','I','O','U'};
    char prevowel[100]; //all the letters that come before a vowel(what will be added at end before "yay"
    char newWord[100]; //the word that remains after removing "prevowel
    int prevowellength=0; //keep getting bugs printing the prevowel so this is a variable to keep track 
    for(long i=0;i<(long)strlen(source);i++){
	if(i>0){
	    vowel[10]='y';
	    vowel[11]='Y';
	}
	if((source[i]=='q' || source[i]=='Q') && (source[i+1]=='u' || source[i]=='U')){ //checks for 'qu'
	    for(long k=0;k<(long)strlen(source)-1;k++){
		newWord[k]=source[k+i+2];
	    }
	    prevowel[i]=source[i];
	    prevowel[i+1]=source[i+1];
	    prevowellength=prevowellength+2;
	    i+=1;
	    continue;
	}	    
	for(long j=0;j<12;j++){ //checks to see if char is a vowel and appends prevowel if not
	    if(source[i]==vowel[j]){
		int pigsize=0;
		char returnword[100];
		if(i==0){
		    for(long k=0;k<(long)strlen(source);k++){
			newWord[k]=source[k];
		    }
		    pigsize= strlen(source)+3; //size of the pig latin word 
		    for(long m=0;m<(long)strlen(newWord);m++){ //creates the beginning of the new string 
			returnword[m]=newWord[m];
		    }
		    returnword[pigsize-3]='y';
		    returnword[pigsize-2]='a';
		    returnword[pigsize-1]='y'; 

		}
		
		else{
		    
		    pigsize=strlen(source)+2;
		    returnword[pigsize-2]='a';
		    returnword[pigsize-1]='y';
		    for(long m=0;m<(long)strlen(newWord);m++){ //creates the beginning of the new string 
			returnword[m]=newWord[m]; 
		    }
		    for(long n=strlen(newWord);n<(long)(strlen(newWord)+prevowellength);n++){ //creates middle of the string
			returnword[n]=prevowel[n-strlen(newWord)];
		    }
		}
		int counter=0;
		for(int p=0;p<=pigsize;p++){ //checks for capitalization
		    if((64<returnword[p]) && (returnword[p]<91)){ //character is a capital letter	
			returnword[p]=returnword[p]+32;
			if(counter==0){
			    returnword[0]=returnword[0]-32;
			    counter+=1;
			}
		    }
		}
		for(int o=0;o<pigsize;o++){ //prints out the word
		    printf("%c",returnword[o]);
		}
		returnword[0]='\0';
		prevowel[0]='\0';
		newWord[0]='\0';
		return;
	    }
	}
	for(long k=0;k<(long)strlen(source);k++){
	    newWord[k]=source[k+i+1];
	}
	prevowel[i]=source[i];
	prevowellength+=1;
    }
    for(int q=0;q<(int)strlen(source);q++){
	printf("%c",source[q]);
    }
    return;
}

char * removepunctuation(char source[]){
    char *str=(char *) malloc(sizeof(char) * strlen(source));
    for(int t=0;t<(int)strlen(source);t++){
	if(ispunct(source[t])){
	    punct=source[t];
	    if(punct=='-'){
		punct='\0';
		for(int v=t+1;v<(int)strlen(source);v++){
		    hyphenstring[v-t-1]=source[v];
		}
		return str;
	    }	
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
    printf("\nEnglish to Pig Latin Translator\n");
    for(int i=1;i<argc;i++){
	if(((strncmp( argv[i], flag1, 2))==0) || ((strncmp(argv[i], flag2, 2))==0)){
	    printf("\n\nFlag was detected, program will now end\n");
	    exit(0);
	}
	char *returned_str=removepunctuation(argv[i]);
	topig(returned_str);
	if(strlen(hyphenstring)>0){
	    printf(" ");
	    char *returned_hyphen=removepunctuation(hyphenstring);
	    topig(returned_hyphen);
	    hyphenstring[0]='\0';
	}
	printf("%c",punct);
	punct='\0';
	printf(" ");
    }
    printf("\n");

}

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
typedef int bool;
#define true 1
#define false 0
//Colin McCahill
//10-23-2017
//sorts the lines of text by a specified criteria

//This function makes sure that the strings are compared as if they were capital letters
int foldingcmp(const void* a, const void* b){
    char chA=**(char**)a;
    char chB=**(char**)b;
    if(chA>96){
	chA=chA-32;
    }
    if(chB>96){
	chB=chB-32;
    }
    return strcmp(&chA,&chB);
}

//default string comparator
int cmp(const void* a, const void* b){ 
    return strcmp(*((char**) a),*((char**)b));
}

//my string to long converter (looks at the number at the beginning of each line and returns that number
long mystrtol(char *start, char **rest){
    long number=0;
    int i=0;
    while(isspace(start[i])!=0){ //gets rid of leading white space
	i+=1;
    }
    while(start[i]!=' '){
	if( isdigit(start[i])){
	    number=(number*10)+(((long)start[i])-48);
	    i+=1;
	}
	else{
	    number=0;
	    return number;
	}
    }
    //rest=&start[i];
    return number;
}

//comparator that compares lines based on the leading number 
int numericcmp(const void* a,const void* b){
    char **ia=(char **)a;
    char **ib=(char **)b;
    char *rest;
    long firstline=mystrtol(*ia,&rest);
    long secondline=mystrtol(*ib,&rest);
    return (int)(firstline-secondline); 
}

//default sorter
void sort(char **strings,int length,bool reverse){
    printf("\n");
    size_t strings_len=length;
    qsort(strings,strings_len,sizeof(char *),cmp); //sorts the lines based on comparator
    if(reverse==true){				   //will print out reverse order if given the -r flag
	for(int i=length-1;i>=0;i--){
	    printf("%s\n",strings[i]);
	}
    }
    else{
	for(int i=0;i<length;i++){
	    printf("%s\n",strings[i]);
	}
    }
    printf("\n");
    }

//numeric sorter
void numericsort(char **strings,int length,bool reverse){
    printf("\n");
    size_t strings_len=length;
    qsort(strings,strings_len,sizeof(char *),numericcmp);
    if(reverse==true){
	for(int i=length-1;i>=0;i--){
	    printf("%s\n",strings[i]);
	}
    }
    else{
	for(int i=0;i<length;i++){
	    printf("%s\n",strings[i]);
	}
    }
    printf("\n");
    }

//folding sort sorts lines by alphabetical order regardless of capitalization
void foldingsort(char **strings,int length,bool reverse){
     printf("\n");
    size_t strings_len=length;
    qsort(strings,strings_len,sizeof(char *),foldingcmp);
    if(reverse==true){
	for(int i=length-1;i>=0;i--){
	    printf("%s\n",strings[i]);
	}
    }
    else{
	for(int i=0;i<length;i++){
	    printf("%s\n",strings[i]);
	}
    }
    printf("\n");
    }


int main(int argc, char *argv[]){
    char foldingflag[2]="-f";
    bool foldingboolean=false;
    char numericflag[2]="-n";
    bool numericboolean=false;
    char reverseflag[2]="-r";
    bool reverseboolean=false;
    char usageflag1[2]="-h"; //usage flags stop the program
    char usageflag2[2]="-?"; 
    for(int i=1;i<argc;i++){
	if(((strncmp( argv[i],usageflag1,2))==0) || ((strncmp(argv[i],usageflag2, 2))==0)){
	   printf("\n\n Usage flage detected, program will now end\n");
	  exit(0); 
	}
	if((strncmp( argv[i],foldingflag,2))==0){
	    foldingboolean=true;
	}
	if((strncmp( argv[i],numericflag,2))==0){
	    numericboolean=true;
	}
	if((strncmp( argv[i],reverseflag,2))==0){
	    reverseboolean=true;
	}
	
    }
    char y='\0';
    char ** text; //array of pointers
    text=malloc(1024 * sizeof(char));
    char * string; //buffer
    string=malloc(1024 * sizeof(char));
    int charcounter=0;
    int linecounter=0;
        while((y=getchar()) != EOF ){
	ungetc(y,stdin);
	y=getchar();
	if(y=='\n'){
	    text[linecounter]=malloc(1024 * sizeof(char));
	    strcpy(text[linecounter],string); //copies buffer into the array of pointers 
	    linecounter+=1;
	    string=malloc(1024*sizeof(char));
	    charcounter=0; 
	    continue;
	}
	string[charcounter]=y;
    	charcounter+=1;	
    }
    if(foldingboolean==true){
	foldingsort(text,linecounter,reverseboolean);	
    }
    if(numericboolean==true){
	numericsort(text,linecounter,reverseboolean);
    }
    else{
	sort(text,linecounter,reverseboolean);
    }
    free(text);
    }

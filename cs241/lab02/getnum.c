#include <stdio.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

long readbinary(){
    char binary=getchar();
    char binaryvalues[32];
    long currentnumbervalue=0;
    int counter=0;
    while(isspace(binary)==0){
	if(binary=='1' || binary=='0'){
	    binaryvalues[counter]=binary;
 	    binary=getchar();
	    }
	else{
	    printf("Error in reading binary number");
	    exit(0); 
	    }
	counter+=1;
	}
    for(int i=0;i<counter;i++){
	if(binaryvalues[i]=='1'){
	currentnumbervalue=currentnumbervalue+pow(2,(counter-i-1));
	}
    }

    return currentnumbervalue;
}

long readhexadecimal(){
    char hex=getchar();
    char hexpossibilities[16]={'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};
    char hexvalues[32];
    long currentnumbervalue=0;
    int counter=0;
    while(isspace(hex)==0){
	for(int j=0;j<16;j++){
	    if(hexpossibilities[j]==hex){
		hexvalues[counter]=hex;
		hex=getchar();
		break;
	    }
	    if(j==16){
		printf("Error in reading hexadecimal number");
		exit(0); 
	    }
	}
	counter+=1;
	}
    for(int i=0;i<counter;i++){
	for(int k=0;k<16;k++){
	    if(hexvalues[i]==hexpossibilities[k]){
		currentnumbervalue=currentnumbervalue+(k*pow(16,(counter-i-1)));
	}
    }
    }
    
    return currentnumbervalue;
}

long readoctal(char firstcharacter){
    char oct=firstcharacter;
    char octpossibilities[8]={'0','1','2','3','4','5','6','7'};
    char octvalues[32];
    long currentnumbervalue=0;
    int counter=0;
    while(isspace(oct)==0){
	for(int j=0;j<8;j++){
	    if(octpossibilities[j]==oct){
		octvalues[counter]=oct;
		oct=getchar();
		break;
	    }
	    if(j==8){
		printf("Error in reading hexadecimal number");
		exit(0); 
	    }
	}
	counter+=1;
	}
    for(int i=0;i<counter;i++){
	for(int k=0;k<8;k++){
	    if(octvalues[i]==octpossibilities[k]){
		currentnumbervalue=currentnumbervalue+(k*pow(8,(counter-i-1)));
	}
    }
    }
    return currentnumbervalue;
}

long readdecimal(char firstdigit, char seconddigit){
    char decvalues[32];
    decvalues[0]=firstdigit;
    char dec=seconddigit;
    char decpossibilities[10]={'0','1','2','3','4','5','6','7','8','9'};
    long currentnumbervalue=0;
    int counter=1; 
   /* if(isspace(seconddigit)!=0){	
	currentnumbervalue=(long)firstdigit;
	printf("%ld space ", decvalues[0]);
	return currentnumbervalue;
    }*/
    while(isspace(dec)==0){
	for(int j=0;j<10;j++){
	    if(decpossibilities[j]==dec){
		decvalues[counter]=dec;
		dec=getchar();
		break;
	    }
	    if(j==10){
		printf("Error in reading decimal number");
		exit(0); 
	    }
	}
	counter+=1;
	}
    for(int i=0;i<counter;i++){
	for(int k=0;k<10;k++){
	    if(decvalues[i]==decpossibilities[k]){
		currentnumbervalue=currentnumbervalue+(k*pow(10,(counter-i-1)));
	}
    }
    }
    return currentnumbervalue;

}

long getnum(void){

    char ch=getchar();
    //test if the space is white
    if(isspace(ch)!=0){
	ch=getchar();
    }
    //test if space is negative
    else if(ch=='-'){
	char base[2];
	for(int i=0;i<2;i++){
	    base[i]=getchar();
	}
	if(base[0]=='0' && base[1]=='b'){ //number is binary
	    long binarynumber=readbinary();
	    return (binarynumber*(-1)); 
	}
	else if(base[0]=='0' && base[1]=='x'){ //number is hexadecimal
	    long hexadecimalnumber=readhexadecimal();
	    return (hexadecimalnumber*(-1));
	}
	else if(base[0]=='0' && ('0'<=base[1])&&(base[1]<='7')){ //number is octal 
	    long octalnumber=readoctal(base[1]);
	    return (octalnumber*(-1));
	}
	else{ //number is decimal
	    long decimalnumber=readdecimal(base[0],base[1]);
	    return (decimalnumber*(-1));
	}

    }
    else if(isdigit(ch)!=0){
	char temporaryvalue=ch;
    	ungetc(ch, stdin);
	char base[2];
	for(int i=0;i<2;i++){
	    base[i]=getchar();

	}
	if(base[0]=='0' && base[1]=='b'){ //number is binary

	    long binarynumber=readbinary();
	    return binarynumber; 
	}
	else if(base[0]=='0' && base[1]=='x'){ //number is hexadecimal
	    long hexadecimalnumber=readhexadecimal();
	    return hexadecimalnumber;
	}
	else if(base[0]=='0' && ('0'<=base[1])&&(base[1]<='7')){ //number is octal	    printf("new octal\n");
	    long octalnumber=readoctal(base[1]);
	    return octalnumber;
	}
	else{
	    long decimalnumber=readdecimal(temporaryvalue, base[1]);
	    return decimalnumber;
	}

    }
    else if(ch==EOF){
	exit(0);	
    }
    else{
	printf("There are incorrect number representations in this file");
	exit(0);
}
}




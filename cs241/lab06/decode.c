#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <limits.h>
typedef int bool;
#define true 1
#define false 0
#define NUM_ELEMENTS 257 
FILE *inputfile;
FILE *outputfile;
bool output=false;
bool leaf=false;
bool stopreadingfile=false;
char buffer[8];
char bits[]="";
int counter=0;

struct Node{
 
    char letter;
    bool leaf;
    bool endoffile;
    struct Node *rchild;
    struct Node *lchild;

};

char getbit(){
    static int counter=0;
    static char buf='\0';
    int rv=0; //return value
    if(counter==0){
	buf=fgetc(inputfile);
	counter=8;
    }
    rv=buf & 0x80;
    buf=buf<<1;
    counter--;
    if(rv==0){
	return '0';
    }
    else{
	return '1';
    }
   }

char getbyte(){
    char byte[8]="";
    for (int i=0;i<8;i++){
	byte[i]=getbit();
    }
  //  printf("byte: %s",byte);
    int rchar=0;	//return char
    for(int k=0;k<8;k++){
	if(byte[k]=='1'){
	    rchar=rchar+pow(2,(7-k));
	}
    }
    return (char)rchar;
}


void convert_bits(int y){
    for(int i=CHAR_BIT-1;i>=0;i--){
/*	if((y & (1<<i)) > 0){
	    printf("1");
	}*/
	if((y>=pow(2,i))){
	    strcat(bits,"1");
	    y=y-pow(2,i);
	}
	else{
	    strcat(bits,"0");
	}
}
//strcat(bits," ");
}

void create_tree(struct Node *list){
    char bit=getbit();
    if(bit=='0'){
//	printf("Huffman node\n");
	list->leaf=false;
	list->endoffile=false;
	list->lchild=malloc(sizeof(struct Node));
	if(list->lchild==NULL){
	    printf("Malloc has failed.\n");
	    exit(3);
	}
	create_tree(list->lchild);
	list->rchild=malloc(sizeof(struct Node));
	if(list->rchild==NULL){
	    printf("Malloc has failed.\n");
	    exit(3);
	}
	create_tree(list->rchild);
    	return;
    }
    else if(bit=='1'){
	char byte=getbyte();
	list->leaf=true;
	list->endoffile=false;
	list->letter=byte;
	list->lchild=NULL;
	list->rchild=NULL;
//	printf("leaf node: %c\n",byte);
	return;	    
    }
}

void set_EOF(struct Node *list){
    if(list->leaf==true){
	list->endoffile=true;
	return;
    }
    char y=getbit();    
    if(y=='0'){
	set_EOF(list->lchild);
//	return;
    }
    else if(y=='1'){
	set_EOF(list->rchild);
//	return;
    }
   }

void output_file(struct Node *list){
    if(list->endoffile == true){
	stopreadingfile=true;
//	printf("success");
	return;
    }
    if(list->leaf == true){
	if(output==true){
	    fputc(list->letter,outputfile);
	}
	else{
	    printf("%c",list->letter);
	}
	return;
    }
    char y=getbit();
//    printf("%c",y);
    if(y=='0'){
	output_file(list->lchild);
	return;
    }
    else if(y=='1'){
	output_file(list->rchild);
	return;
    }
    return;
}

void deallocate_memory(struct Node *list){
    if(list->lchild != NULL){
	deallocate_memory(list->lchild);
    }
    if(list->rchild != NULL){
	deallocate_memory(list->rchild);
    }
    free(list);
}

int main(int argc, char *argv[]){
    inputfile=fopen(argv[1],"r");
    if(argv[2]!=NULL){
	output=true;
	outputfile=fopen(argv[2],"w");
    }	
    struct Node *tree = malloc(sizeof(struct Node));
    if(tree==NULL){
	printf("Malloc has failed.\n");
	exit(3);
    }
    create_tree(tree);
    set_EOF(tree);
    
    while(stopreadingfile != true){
	output_file(tree); 
    }
    deallocate_memory(tree);
    fclose(inputfile);
    if(outputfile != NULL){
	fclose(outputfile);
    }
    //free(tree);
}

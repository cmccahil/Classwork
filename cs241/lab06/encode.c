/*
 * Colin McCahill
 * CS241 encode.c
 * 11/20/2017
 */

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
static char *bitstringrep[NUM_ELEMENTS]; //to store the location in the tree of all of the characters in the file 
int bitcounter=0;
FILE *outputfile;
bool output=false;
char buffer[8];


struct Node{
    int frequency;
    int count;
    char letter;
    char path[8];
    bool headnode;
    bool tailnode;
    bool huffmannode;
    struct Node *rchild;
    struct Node *lchild;
    struct Node *next;
    struct Node *prev;
};
/*
struct stackNode{
    struct Node *n;
    struct stackNode *next;
}*/

struct Node *init(){
    struct Node *head;
    struct Node *tail;
    head= malloc(sizeof(struct Node));
    tail=malloc(sizeof(struct Node));
    if (head != NULL) {
    head->count = 0;
    head->headnode=true;
    head->tailnode=false;
    head->rchild=NULL;
    head->lchild=NULL;
    head->next = tail;
    head->prev = NULL;
    head->huffmannode=false;
  }
  if(tail!=NULL){
    tail->count=0;
    tail->tailnode=true;
    tail->headnode=false;
    tail->huffmannode=false;
    tail->rchild=NULL;
    tail->lchild=NULL;
    tail->next=NULL;
    tail->prev=head;
  }
  else{
    printf("Malloc has failed.\n");
    exit(3);
  }
  return(head);
}

void print_bits(char string[]){
  //  printf("\n%s\n",string);
    int i=0;
//    static char buffer[8];
    int outputvalue=0;
    while(string[i]!='\0'){
	if(bitcounter==8){
	    for(int k=0;k<bitcounter;k++){
//		printf("%c",buffer[k]);
		if(buffer[k]=='1')
		    outputvalue=outputvalue+pow(2,(bitcounter-k-1));
		}
	    printf(" ");
	    
	    if(output==true){
		fputc((char)outputvalue,outputfile);
	    }
	    else{
		printf("%c ",(char)outputvalue);
	    }
	    bitcounter=0;
	    
	    memset(buffer,0,strlen(buffer));
//	    buffer[0]='\0';
//	    printf("buffer after empty: %s",buffer);
	    }
//	printf("\n$string[i]= %s\n",&string[i]);
	strncat(buffer,&string[i],1);
//	printf("buffer after one iteration: %s",buffer);
	bitcounter++;
	i++;
    }
 //   if(buffer[0]!='\0'){
//    printf("buffer: %s\n",buffer);
//    }
}

void print_list(struct Node *list){
    struct Node *tmp;
    tmp=list;
    while(tmp->headnode !=true){
	tmp=tmp->prev;
    }
    tmp=tmp->next;
//    printf("printlist first checkpoint");
    while(tmp->tailnode != true){
	printf("%c(%d) -> ",tmp->letter,tmp->count);
	tmp=tmp->next;
    }
    printf("\n");
}


struct Node *HuffmanAdd(struct Node *list){
    struct Node *last=list;
    //finding the start of the list
    while(last->headnode != true){
	last=last->prev;
    }
    last=last->next;
    struct Node *newNode =malloc(sizeof(struct Node));
    
    newNode->lchild=last;
    newNode->rchild=last->next;
    newNode->count= last->count + last->next->count;
    newNode->headnode=false;
    newNode->tailnode=false;
    newNode->huffmannode=true;
	
    //deleting the two nodes from the list
    last->prev->next= last->next->next;
    last->next->next->prev = last->prev;
    //free(last->next);
    //struct Node *tmp1=last;
    //struct Node *tmp2=last->next;
    last=last->prev;

    //finding a spot for the new node
    while((last->tailnode != true) && ((newNode->count) > (last->count))){
	last=last->next;
    }
    newNode->prev = last->prev;
    newNode->next = last;
    last->prev->next = newNode;
    last->prev = newNode;
 //   print_list(last);
    /*if(tmp1 != NULL){
	free(tmp1);
    }
    if(tmp2 != NULL){
	free(tmp2);
    }*/
    return(newNode);
}

struct Node *add(struct Node *list, int frequency, int count, char letter){
    struct Node *newNode = malloc(sizeof(struct Node));
    if(newNode==NULL){
	printf("Malloc has failed.\n");
	exit(3);
    }
    struct Node *last=list;
    while(last->headnode!=true){
	last=last->prev;
    }
    last=last->next;
    while((last->tailnode!=true) && (count> last->count)){
	last=last->next;
    }
    newNode->headnode=false;
    newNode->tailnode=false;
    newNode->huffmannode=false;
    newNode->rchild=NULL;
    newNode->lchild=NULL;
    newNode->frequency = frequency;
    newNode->count = count;
    newNode->letter = letter;
    newNode->next= last;
    newNode->prev = last->prev;
    last->prev->next= newNode;
    last->prev= newNode;
   // printf("Node added!\n");
    return(newNode);
}

void preOrderTraversal(struct Node *list){
   /* if(list->headnode==true){
	printf("headnode");
    }*/
    if(list==NULL){
	return; 
    }	
    if(list->huffmannode==true){
	/*
	if(bitcounter==8){
	    if(output==true){
		fputc(' ',outputfile);
	    }
	    else{
		printf(" ");
	    }
	    bitcounter=0;
	}
	if(output==true){
	    fputc('0',outputfile);
	}*/
//	else{	
	    print_bits("0");
//	}
//	bitcounter++;

    }
    if(list->huffmannode==false){
/*	if(bitcounter==8){
	    if(output==true){
	        fputc(' ',outputfile);
		}
	    else{
		printf(" ");
	    }
	    bitcounter=0;
	}
	if(output==true){
	    fputc('1',outputfile);
	}
	else{	*/
	    print_bits("1");
/*	}
	bitcounter++;*/



//	static char buf=list->letter;
//	static int c;
	for(int i=CHAR_BIT-1;i>=0;i--){
	   /* if(bitcounter==8){
		if(output==true){
		    fputc(' ',outputfile);
		}
		else{
		printf(" ");}
		bitcounter=0;*/
	   // }
	/*    if(output==true){
		fputc((list->letter) & (1 << i) ? '1' : '0',outputfile);
	    }*/
	  //  else{	
		print_bits((list->letter) & (1 << i) ? "1" : "0" );
	   // }
	    //	    bitcounter++;
	   /* if( (list->letter) >= pow(2,i) ){
		printf("%d",1);
		list->letter = (list->letter) - pow(2,i) ;
	    }
	    else{
		printf("%d",0);
	    }*/
	}
	//printf("%u",buf);
//	printf(" ");
    }
    preOrderTraversal(list->lchild);
    preOrderTraversal(list->rchild);
}
/*
void findbitstringV2(struct Node *root){
    struct Node *current=root;
    struct Node 
}*/
void findbitstring(struct Node *list,char path[]){
    if(list==NULL){
	path[strlen(path)-1]='\0';
	return;
    }
    if(list->huffmannode==false){
//	printf("adding bit string\n");
	if(list->letter==EOF){
	    bitstringrep[256]=malloc(sizeof(char)*8);
	    strcpy(bitstringrep[256],path);
	  //  bitstringrep[256]=buffer;
//	     printf("%s ",buffer);
	    path[strlen(path)-1]='\0';
	}
    	else{
//	    printf("%s ",buffer);
	    bitstringrep[(int)list->letter]=malloc(sizeof(char)*8);
	    strcpy(bitstringrep[(int)list->letter],path);
	  //  bitstringrep[list->letter]=buffer;
//	    printf("%s ",bitstringrep[list->letter]);
/*for(int k=0;k<257;k++){
	printf("{%s},",bitstringrep[k]);
   }*/
	    path[strlen(path)-1]='\0';
    	}
    }
 	findbitstring(list->lchild, strcat(path,"0"));
	if(list->lchild!=NULL){
	    if(list->lchild->huffmannode==true){
		path[strlen(path)-1]='\0';
	    }
	}
	findbitstring(list->rchild, strcat(path,"1"));
	if(list->rchild!=NULL){
	    if(list->rchild->huffmannode==true){
		path[strlen(path)-1]='\0';
	    }
	}
//	buffer[strlen(buffer)-1]='\0';
    }

void free_list(struct Node *list){
    if(list->lchild != NULL){
	free_list(list->lchild);
    }
    else if(list->rchild != NULL){
	free_list(list->rchild);
    }
    free(list);
}

int main(int argc, char *argv[]){
    FILE *inputfile;
    inputfile=fopen(argv[1],"r");
    if(argv[2]!=NULL){
	output=true;
	outputfile=fopen(argv[2],"w");
    }	
    struct Node *freqlist;
    int totalnodes=0;
    freqlist=init();
    char y=fgetc(inputfile); //fgetc
    
    int table[NUM_ELEMENTS];
    
    for(int i=0;i<NUM_ELEMENTS;i++){
	table[i]=0;
    }
  //  printf("test1\n");
    while(y!=EOF){
	//freqlist=add(freqlist,y);
	table[(int)y]++;
	y=fgetc(inputfile); //fgetc
    }
   // printf("test2\n");
    add(freqlist,-1,1,y); // hard code adding the EOF
    totalnodes++;
    fclose(inputfile);
    for(int j=0;j<NUM_ELEMENTS;j++){
	if(table[j]>0){
	    add(freqlist, j, table[j], j);
	    totalnodes++;
	}
    }
//   print_list(freqlist);
   while(totalnodes != 1){
	HuffmanAdd(freqlist);
	totalnodes--;
   }
  // print_list(freqlist->next);
   preOrderTraversal(freqlist->next);
   static char path[8]="";
   findbitstring(freqlist->next,path);
   print_bits(bitstringrep[256]);

   freqlist=freqlist->next;
   free(freqlist->prev);
   free(freqlist->next);
   free_list(freqlist);
   inputfile=fopen(argv[1],"r");
   y=fgetc(inputfile);
   while(y!=EOF){
	

	print_bits(bitstringrep[(int)y]);
	y=fgetc(inputfile);
   }

   fclose(inputfile);
   print_bits(bitstringrep[256]);
   for(int m=0;m<257;m++){
	if(bitstringrep[m]!=NULL){
	    free(bitstringrep[m]);
	}
   }
   if(strlen(buffer)>0){

	char pad[]="";
	while(strlen(pad)+strlen(buffer)!=9){
	    strcat(pad,"0");
	}

	print_bits(pad);
   }
   if(outputfile!=NULL){
	fclose(outputfile);
   }
    printf("\n");

}

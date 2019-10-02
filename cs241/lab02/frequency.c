#include <stdio.h>
#define LENGTH 26


int main(){
    int arr[LENGTH];
    for(int i=0;i<26;i++){
	arr[i]=0;
    }
    char y=getchar();

    while(y!=EOF){
	if (y<97){
	    y=y-65;}
	else{
	    y=y-97;
	    
    }
	int x=y;
	arr[x]++;
	y=getchar();
    }
    printf("%s         %s           %s\n","char","Frequencies","Percentage");
    char letters[26]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
    int minimum=arr[0];
    char min=letters[0];
    int maximum=0;
    char max= letters[0];
    int sum=0;
    for(int k=0; k<26; k++){
	if(arr[k]>maximum){
	    max=letters[k];
	    maximum=arr[k];
	}
	if(arr[k]<minimum){
	    min=letters[k];
	    minimum=arr[k];
	}
	sum=sum+arr[k];
    }
    max=max += -32;
    min=min += -32;
    for(int j=0;j<26;j++){
	printf("%c:    %14d                 %4f\n",letters[j], arr[j], ((double)arr[j]/ sum)*100);
    }
    printf("Maximum character(s): %c\n", max);
    printf("Minimum characters(s): %c\n", min);
}

#include <stdio.h>
#include <ctype.h>
//Colin McCahill
//9-10-2017
//generates a simple ASCII art diamond of variable size based on user input
int main(){
    printf("I will print a diamond for you, enter a size between 1-9: ");
    int y= getdigit();
    int i;
    int j;
    int k;
    int m;
    for(i=1;i<(y+1);i++){
	for(j=y;j>i;j--){
	    printf(" ");}
	for(k=(y-i);k<y;k++){
	    printf("*");
	}
	for(m=0;m<(i-1);m++){
	    printf("*");}
	printf("\n");
}
    
    for(i=(y-1);i>0;i--){
	for(j=y;j>i;j--){
	    printf(" ");}
	for(k=(y-i);k<y;k++){
	    printf("*");
	}
	for(m=0;m<(i-1);m++){
	    printf("*");}
	printf("\n");
}
}
//tests that the input is a digit and returns the number value of digit
int getdigit(){
    char number=getchar();
    while(isdigit(number)==0){
         number= getchar();
    }
    int y=number-'0';
    return y;

}



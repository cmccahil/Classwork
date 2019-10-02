#include <stdio.h> 
#include <limits.h>
#include <math.h>
#include "bits.h"



int main(){
    char y=getchar();
    while(y!=EOF){
	print_bits(y);
	y=getchar();
    }
    printf("\n");
}

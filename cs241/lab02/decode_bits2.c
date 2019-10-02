#include <math.h>
#include <ctype.h>
#include "bits.h"
#include <stdio.h>

int main(){
    char ch=getchar();
    while( ch != EOF){
	decode_bits(ch);
	ch=getchar();
    }
    }

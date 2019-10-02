TARGETS=frequency encode_bits decode_bits2 getnum.o todecimal tobinary tohexadecimal tooctal bits.o

all: $(TARGETS)

frequency.o: frequency.c
	gccx -c frequency.c

frequency: frequency.o
	gccx -o frequency frequency.o

encode_bits.o: encode_bits.c
	gccx -c encode_bits.c 

encode_bits: encode_bits.o
	gccx -o encode_bits encode_bits.o bits.o -lm

bits.o: bits.c bits.h
	gccx -c bits.c

decode_bits2.o: decode_bits2.c
	gccx -c decode_bits2.c 

decode_bits2: decode_bits2.o
	gccx -o decode_bits2 decode_bits2.o bits.o -lm

getnum.o: getnum.c getnum.h
	gccx -c getnum.c 

todecimal.o: todecimal.c
	gccx -c todecimal.c

todecimal: todecimal.o getnum.o
	gccx -o todecimal todecimal.o getnum.o -lm

tobinary.o: tobinary.c
	gccx -c tobinary.c

tobinary: tobinary.o getnum.o
	gccx -o tobinary tobinary.o getnum.o -lm

tohexadecimal.o: tohexadecimal.c
	gccx -c tohexadecimal.c

tohexadecimal: tohexadecimal.o getnum.o
	gccx -o tohexadecimal tohexadecimal.o getnum.o -lm

tooctal.o: tooctal.c
	gccx -c tooctal.c

tooctal: tooctal.o getnum.o
	gccx -o tooctal tooctal.o getnum.o -lm

clean:
	rm *.o frequency encode_bits decode_bits2 getnum todecimal tobinary tohexadecimal tooctal bits


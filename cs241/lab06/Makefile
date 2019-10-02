TARGETS = encode decode

all: $(TARGETS)

encode.o: encode.c
	gccx -c encode.c

encode: encode.o
	gccx -o encode encode.o -lm

decode.o: decode.c
	gccx -c decode.c

decode: decode.o
	gccx -o decode decode.o -lm

clean: 
	rm *.o encode decode

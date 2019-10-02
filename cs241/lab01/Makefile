TARGETS = hello rot128 diamond

all: $(TARGETS)

hello.o: hello.c
	gccx -c hello.c

hello: hello.o
	gccx -o hello hello.o

rot128: rot128.c
	gccx -c rot128.c

rot128: rot128.o
	gccx -o rot128 rot128.o

diamond.o: diamond.c
	gccx -c diamond.c

diamond: diamond.o
	gccx -o diamond diamond.o
clean: 
	rm *.o  hello diamond rot128

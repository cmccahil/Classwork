TARGETS= pig unpig

all: $(TARGETS)

pig.o: pig.c
	gccx -c pig.c

pig: pig.o
	gccx -o pig pig.o

unpig.o: unpig.c
	gccx -c unpig.c

unpig: unpig.o
	gccx -o unpig unpig.o

clean:
	rm *.o unpig pig 

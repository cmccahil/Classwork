TARGETS = sort

all: $(TARGETS)

sort.o: sort.c
	gccx -c sort.c

sort: sort.o
	gccx -o sort sort.o

clean: 
	rm *.o sort

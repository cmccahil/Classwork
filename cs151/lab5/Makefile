JFLAGS=
JAVA=java
JAVAC=javac

SRCS = \
    BinaryTree.java\
    EmptyTree.java\
    ConsTree.java\
    TreeMethods.java \
    TreeLoader.java\
    TreeMethodFrame.java\
    TreeMethodApplication.java

all: $(SRCS:.java=.class)

%.class : %.java
	@(echo "Compiling $^" ; $(JAVAC) $(JFLAGS) $^)

clean:
	rm -f *.class

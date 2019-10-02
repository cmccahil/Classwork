import java.util.AbstractList;

/**
 * This is the My arraylist and the different methods
 * @author cmccahil
 *
 * @param <AnyType>
 */
//AnyType[] someArray=(AnyType [])new Object[numElements];

public class MyArrayList<AnyType> extends AbstractList<AnyType> {
    
    private int size;
	//number of items in list
    private AnyType[] data;
    //storage 
    private void resize() {
	AnyType[] differentArray=(AnyType [])new Object[size*2];
	//make diff array
	int counter1=0;
	for(AnyType i:data) {
	    differentArray[counter1]=i;
	    counter1++;
	}
	this.data=differentArray;
	
	
    }
    //resizes the array into a different array
    
    @SuppressWarnings("unchecked")
    
    //creates the initial array
    MyArrayList(int startSize){
	size=0;
	int initialmaxcapacity=2;
	while (initialmaxcapacity<startSize){
	    initialmaxcapacity=initialmaxcapacity*2;
	    
	}
	data=(AnyType[]) new Object[initialmaxcapacity];
    }
    
    //creates the initial array size 
    MyArrayList(){
	this(2);
    }
    //initial capacity
    public int size() {
	return size;
    }
    
    public void add(int index, AnyType element) {
	if (index>data.length) {
	    throw new IndexOutOfBoundsException("Index Out of Bounds! You tried to get "+index+"but the size is "+size);
	}
	if (size==data.length) {
	    resize();
	}
	for(int shiftingover=index;shiftingover<size+1;shiftingover++) {
	    AnyType saveVariable=data[shiftingover];
	    data[shiftingover]=element;
	    element=saveVariable;
	}
	size++;
	
    }
    public boolean add(AnyType element) {
	add(size, element);
	return true;
	//returns true if item is added
	
    }
    public AnyType get(int index) {
	if (index>=size) {
	    throw new IndexOutOfBoundsException("Index Out of Bounds! You tried to get "+index+"but the size is "+size);
	}
	return data[index];
	//returns value stored at the given index
    }
    public AnyType set(int index,AnyType element) {
	if (index>size) {
	    throw new IndexOutOfBoundsException("Index Out of Bounds! You tried to get "+index+"but the size is "+size);
	}
	AnyType savingvalue=data[index];
	data[index]=element;
	return savingvalue;
    }
    public AnyType remove(int index) {
	AnyType savingvalue1=data[index];
	if (index>=size) {
	    throw new IndexOutOfBoundsException("Index Out of Bounds! You tried to get "+index+"but the size is "+size);
	}
	for(int i=index;i<size;i++) {
	    data[i]=data[i+1];
	}
	size--;
	return savingvalue1;
    }
    public boolean isEmpty() {
	if (size==0) {
	    return true;
	}
	else {
	    return false;
	}
    }
    public void clear() {
	for(int index1=0;index1<size;index1++) {
	    data[index1]=null;
	}
    }
 
    
}

import java.util.Iterator;
import java.util.LinkedList;
import java.util.NoSuchElementException;
/**
 * 
 * @author cmccahil
 * hash map with separate chaining with a hash table on top of an array. The array
 * consists of LinkedLists, one per bucket. 
 * @param <K>
 * @param <V>
 */
public class MyHashMap<K, V> {
    
    //set of buckets used in hashtable
    LinkedList<MyEntry>[] table;
    
    //current number of items in table
    int size;
    
    //maximum permitted load factor
    float loadFactor=(float) 0.75;
    //amount of spaces in array
    private int capacity=11;

    //constructor
    MyHashMap(int capacity,float loadFactor){
	table=new LinkedList[capacity];
	this.loadFactor=loadFactor;
	for(int i=0;i<capacity;i++) {
	    table[i]=new LinkedList<MyEntry>();
	}
	this.size=0;

	this.capacity=capacity;
    }
    
    MyHashMap() {
	this(11,(float)0.75);
    }
    
    //dynamically resizes the array and rehashes items
    private MyHashMap<K,V> resize() {
	//resize hashmap
	
	int biggercapacity=(2*capacity)+1;

	MyHashMap<K,V> biggermap= new MyHashMap(biggercapacity,loadFactor);
	
	//rehash items
	
	
	for(int i=0;i<this.capacity;i++) {
	    for(MyEntry k:table[i]) {
		biggermap.put(k.key, k.value);
	    }
	}
	this.capacity=biggercapacity;
	this.table=biggermap.table;
	return biggermap;
    }
    
    //returns amount of items in hashmap
    public int size() {
	return size;
    }
    
    //return true if size==0, false otherwise
    public boolean isEmpty() {
	if (size==0) {
	    return true;
	}
	return false;
    }
    
    //clears hashmap
    public void clear() {
	for(int i=0;i<capacity;i++) {
	    table[i].clear();
	}
    }
    
    //returns string representation of hash table
    public String toString() {
	String HashTable="";
	for(int i=0;i<this.capacity;i++) {
	    for(MyEntry k:table[i]) {
		HashTable=HashTable+k.value+" "+k.key+"\n";
	    }
	}
	return HashTable;
    }
    
    //puts key and value into hashmap
    public V put(K key,V value) {
	if(key==null||value==null) {
	    throw new NullPointerException();
	}
	else {
	MyEntry addvalue=new MyEntry();
	addvalue.key=key;
	addvalue.value=value;
	
	int bucket=Math.abs(key.hashCode()%capacity);
	
	
	//what happens if the same key already exists
	for(MyEntry i:table[bucket]) { 
	    if(i.key==key) {
		V previousvalue=i.value;
		table[bucket].add(addvalue);
		size++;
		if(((float)size/(float)capacity)>loadFactor) {
		    resize();
		}
		return previousvalue;
	    }
	}
	
	//what happens if the key does not exist
	table[bucket].add(addvalue);
	size++;
	if(((float)size/(float)capacity)>loadFactor) {
	    resize();
	}
	return null;
	}
    }
    
    //returns value associated with key
    public V get(K key) {
	int bucket=Math.abs(key.hashCode()%capacity);
	for(MyEntry i:table[bucket]) {
	    if(i.key.equals(key)) {
		return i.value;
	    }
	}
	return null;
    }
    
    //deletes mapping from hashtable
    public V remove(K key) {
	int bucket=Math.abs(key.hashCode()%capacity);
	//for(int i=0;i<table[bucket].size()-1;i++){
	for(MyEntry i:table[bucket]) { 
	    if(i.key==key) {
		//location.remove(key
		V previousvalue=i.value;
		table[bucket].remove(i);
		size--;
		/*if(table[bucket].size()==0) {
		    utilizedbuckets.remove(bucket);
		}*/
		return previousvalue;
	    }	
	}
	return null;
    }
    
    //returns true if key is in table
    public boolean containsKey(K key) {
	int bucket=Math.abs(key.hashCode()%capacity);
	for(MyEntry i:table[bucket]) {
	    if(i.key.equals(key)) {
		return true;
	    }
	}
	return false;
    }
    
    //returns true if value is in table
    public boolean containsValue(V value) {
	for(int i=0;i<this.capacity;i++) {
	    for(MyEntry k:table[i]) {
		if(k.value.equals(value)) {
		    return true;
		}
	    }
	}
	return false;
    }
    
    //iterator of keys in hashtable
    public Iterator<K> keys(){
	return new Iterator<K>() {
	        int iteratorbucket = 0;
	        Iterator<MyEntry> itr = table[iteratorbucket].iterator();
	        int nextCount = 0;

	        public boolean hasNext() {
	            // can just check nextCount and size
	            if(nextCount>=size) {
	        	return false;
	            }
	            return true;
	        }

	        public K next() {
	            // if my hasNext() is false, I should throw a NoSuchElementException
	            if(hasNext()==false) {
	        	throw new NoSuchElementException();
	            }
	            // while itr.hasNext() is false, increment bucket and get the next iterator
	            while(itr.hasNext()==false) {
	        	iteratorbucket++;
	        	itr=table[iteratorbucket].iterator();
	            }
	            // now increment nextCount and return the key from the item itr.next() returns
	        	nextCount++;
	        	return itr.next().key;
	            
	        }

	        public void remove() {
	            // just ask itr to remove, but I need to update my size and nextCount
	            itr.remove();
	            size--;
	            nextCount--;
	        }
	    };
    }
    
    //iterator of values in hashtable
    public Iterator<V> Values(){
	return new Iterator<V>() {
	        int iteratorbucket = 0;
	        Iterator<MyEntry> itr = table[iteratorbucket].iterator();
	        int nextCount = 0;

	        public boolean hasNext() {
	            // can just check nextCount and size
	            if(nextCount>=size) {
	        	return false;
	            }
	            return true;
	        }

	        public V next() {
	            // if my hasNext() is false, I should throw a NoSuchElementException
	            if(hasNext()==false) {
	        	throw new NoSuchElementException();
	            }
	            // while itr.hasNext() is false, increment bucket and get the next iterator
	            while(itr.hasNext()==false) {
	        	iteratorbucket++;
	        	itr=table[iteratorbucket].iterator();
	            }
	            // now increment nextCount and return the key from the item itr.next() returns
	        	nextCount++;
	        	return itr.next().value;
	            
	        }

	        public void remove() {
	            // just ask itr to remove, but I need to update my size and nextCount
	            itr.remove();
	            size--;
	            nextCount--;
	        }
	    };
    }
    
    public class MyEntry{
	private K key;
	public V value;
	
	/*public MyEntry(K key,V value) {
	    this.key=key;
	    this.value=value;
	}
  */  }
}

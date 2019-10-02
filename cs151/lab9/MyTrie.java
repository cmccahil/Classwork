import java.util.AbstractSet;
import java.util.ArrayList;
import java.util.Iterator;
/**
 * 
 * @author cmccahil
 *
 */
public class MyTrie extends AbstractSet<String> {
    boolean isWord; //whether this trie node is the end of a word
    int size; //the number of words represented by this trie
    MyTrie[] children; //the children tries of this node
    
    //constructor
    public MyTrie() {
	this.children=new MyTrie[26];
	this.size=0;
	this.isWord=false;
    }
    
    //returns number of words in Trie
    public int size() {
	return size;
    }
    
    //returns true if trie contains empty string
    public boolean containsEmptyString() {
	return isWord;
    }
    
    //returns true if trie contains the string
    public boolean contains(String string) {
	string=string.toLowerCase();
	if(string.length()==0) {
	    return containsEmptyString();
	}
	
	else {
	    char val=string.charAt(0);
	    int x=val-'a';
	    if(children[x]!=null) {
		return children[x].contains(string.substring(1));
	    }
	    else {
		return false;
	    }
	}
    }
    
    //returns true if trie contains edges represented by prefix
    public boolean containsPrefix(String prefix) {
	if(prefix.length()==0) {
	    return containsEmptyString();
	}
	if(prefix.length()==1) {
	    char val=prefix.charAt(0);
	    int x=val-'a';
	    if(children[x]!=null) {
		return true;
	    }
	    else {
		return false;
	    }
	}
	else {
	    char val=prefix.charAt(0);
	    int x=val-'a';
	    if(children[x]!=null) {
		return children[x].containsPrefix(prefix.substring(1));
	    }
	    else {
		return false;
	    }
	}
    }
    //inserts string into trie, if not already present
    //returns true if it is modified by the operation
    public boolean add(String string) {
	
	if(string.length()==0) {
	    if(this.isWord==true) {
		return false;
	    }
	    else {
	    this.isWord=true;
	    size++;
	    return true;
	    }
	}
	
	else {
	    char val=string.charAt(0);
	    int x=val-'a';
	    if(children[x]!=null) {
		this.size++;
		return children[x].add(string.substring(1));
	    }
	    else {
		children[x]=new MyTrie();
		this.size++;
		return children[x].add(string.substring(1));
	    }
	}
    }
    
    //return true if the trie contains no strings, false otherwise
    public boolean isEmpty() {
	if(size==0) {
	    return true;
	}
	else {
	    return false;
	}
    }
    
    //generates an iterator over all the strings in the trie
    public Iterator<String> iterator(){
	ArrayList<String> iter=this.toList();
	return iter.iterator();
    }
    
    //returns a string representation of the set of strings
    //in the trie
    public String toString() {
	ArrayList<String> listOfStrings=this.toList();
	String returnString="";
	for(String i:listOfStrings) {
	    returnString=returnString+i+"\n";
	}
	return returnString;
    }
    
    //returns a list of strings contained in the trie in alphabetical order
    public ArrayList<String> helperMethod(String prefix,ArrayList<String> storage) {
	if(this.isWord) {
	    storage.add(prefix);
	    
	}
	if(this.isEmpty()) {
	    return storage;
	}
	else {
	    String alphabet="abcdefghijklmnopqrstuvwxyz";   
	    for(int i=0;i<26;i++) {
		char c=alphabet.charAt(i);
		if (children[i]!=null) {
		    children[i].helperMethod(prefix+c, storage);
		}	
	}
	    return storage;
	
    }
    }
   
    private ArrayList<String> toList(){
	if(isEmpty()) {
	    return null;
	}
	return helperMethod("", new ArrayList<String>());
    }
}


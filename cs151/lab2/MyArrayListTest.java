
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

import org.junit.Test;

import jdk.nashorn.internal.ir.annotations.Ignore;
/**
 * tests to test my Array List
 * @author cmccahil
 *
 */
public class MyArrayListTest {

    @Ignore
    public void testSize() {
	MyArrayList<Integer> test = new MyArrayList<Integer>(); 
	ArrayList<Integer>   real = new ArrayList<Integer>();
	assertEquals( "Size after construction", real.size(), test.size());
	test.add(0,5);
	real.add(0,5);
	assertEquals( "Size after add", real.size(), test.size());
    }
    /**
    @Test (expected=IndexOutOfBoundsException.class)
    public void testForAddLeftException() throws Exception {
        MyArrayList<Integer> test = new MyArrayList<Integer>();
        test.add(-1, 5);
    }
    
    @Test
    (expected=IndexOutOfBoundsException.class)
    public void testForAddRightException() throws Exception {
        MyArrayList<Integer> test = new MyArrayList<Integer>();
        test.add(test.size()+1, 5);
    }
**/
    @Ignore
    public void testMyArrayListInt() {
	fail("Not yet implemented");
    }

    @Ignore
    public void testMyArrayList() {
	MyArrayList<Integer> test = new MyArrayList<Integer>();
	ArrayList<Integer>   real = new ArrayList<Integer>();
	assertEquals("Size after construction", real.size(), test.size());
    }

    @Ignore
    public void testAddIntAnyTypeFront() {
	Scanner input=null;
	try {
	    input=new Scanner(new File("test1.txt"));
	}
	catch(FileNotFoundException e) {
	    System.out.println("Problem opening file: " + e.getMessage());
	    System.exit(1);
	}
	MyArrayList<String> test = new MyArrayList<String>();
	ArrayList<String>   real = new ArrayList<String>();
	while(input.hasNextLine()) {
	    String a=null;
	    a=input.nextLine();
	    test.add(0,a);
	    real.add(0,a);
	}
	for(int index=0;index<test.size();index++) {
	    assertEquals("text files",test.get(index).equals(real.get(index)),true);
	}
    }

    @Ignore
    public void testAddAnyType() {
	Scanner input=null;
	try {
	    input=new Scanner(new File("test1.txt"));
	}
	catch(FileNotFoundException e) {
	    System.out.println("Problem opening file: " + e.getMessage());
	    System.exit(1);
	}
	MyArrayList<String> test = new MyArrayList<String>();
	ArrayList<String>   real = new ArrayList<String>();
	while(input.hasNextLine()) {
	    String a=null;
	    a=input.nextLine();
	    test.add(a);
	    real.add(a);
	}
	
	for(int index=0;index<test.size();index++) {
	    System.out.println(test.get(index));
	    assertEquals("Testing that these equal each other",test.get(index).equals(real.get(index)),true);
	}
    }
    
    //test.get(index).equals(real.get(index)),true
    @Ignore
    public void testAddIntAnyTypeBack() {
	Scanner input=null;
	try {
	    input=new Scanner(new File("test1.txt"));
	}
	catch(FileNotFoundException e) {
	    System.out.println("Problem opening file: " + e.getMessage());
	    System.exit(1);
	}
	MyArrayList<String> test = new MyArrayList<String>();
	ArrayList<String>   real = new ArrayList<String>();
	while(input.hasNextLine()) {
	    String a=null;
	    a=input.nextLine();
	    test.add(test.size()/2,a);
	    real.add(real.size()/2,a);
	}
	for(int index=0;index<test.size();index++) {
	    assertEquals("text files",test.get(index).equals(real.get(index)),true);
	}
    }

    @Ignore
    public void testGetInt() {
	fail("Not yet implemented");
    }
    
    @Ignore
    public void testAddEfficiency() {
	MyArrayList<Integer> test=new MyArrayList<Integer>();
	Random rnd=new Random();
	for(int numbers=0;numbers<1000000;numbers++) {
	    int target=rnd.nextInt(1000);
	    test.add(target);
	    if (numbers%10000==0){
		System.out.println(target);
	    }
	}
    }
    @Ignore
    public void testRemoveEfficiency() {
	MyArrayList<Integer> test=new MyArrayList<Integer>();
	Random rnd=new Random();
	for(int numbers=0;numbers<1000000;numbers++) {
	    int target=rnd.nextInt(1000);
	    test.add(numbers);
    }
	System.out.println(test.size());
	for (int i=test.size()-1;i>=0;i--) {
	    if(i%10000==0) {
		System.out.println(test.remove(i));
	    }
	    else {
		test.remove(i);
	    }
	}
	System.out.println(test.size());
    }
    @Test
    public void testMemory() {
	MyArrayList<Integer> test=new MyArrayList<Integer>();
	int i=1;
	while(i>0) {
	    test.add(i);
	    if (i%10000==0) {
		System.out.println(i);
	    }
	    i++;
	}
	//last number in the first test is 134,210,000. 81.304seconds
	//last number in the second test is 18,170,000. It did not terminate(ran it for about a half hour and then gave up)
}
    
}

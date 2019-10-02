import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

import java.util.Iterator;

import org.junit.Test;

public class MyTreeSetTest {

    @Test
    public void testSize() {
	//tests constructor, add, size
	MyTreeSet test=new MyTreeSet();
	test.add("Hello,");
	test.add("my");
	test.add("name");
	test.add("is");
	test.add("Colin!");
	assertEquals("tests size",5,test.size());
	
    }

    @Test
    public void testClear() {
	//tests clear
	MyTreeSet test=new MyTreeSet();
	test.add("Hello,");
	test.add("my");
	test.add("name");
	test.add("is");
	test.add("Colin!");
	test.clear();
	System.out.println(test);
    }

    @Test
    public void testMyTreeSet() {
	fail("Not yet implemented");
    }

    @Test
    public void testAddT() {
	fail("Not yet implemented");
    }

    @Test
    public void testIterator() {
	MyTreeSet test=new MyTreeSet();
	test.add(5);
	test.add(3);
	test.add(9);
	test.add(4);
	test.add(7);
	//System.out.println(test.iterator());
	Iterator<Integer> testIterator=test.iterator();
		while(testIterator.hasNext()) {
		    System.out.println(testIterator.next());
		}
    }

}

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import java.util.Iterator;

import org.junit.Ignore;
import org.junit.Test;

public class MyHashMapTest {

    @Test
    public void testSize() {
	MyHashMap<Integer,Integer> test=new MyHashMap();
	assertEquals(test.size,0);
    }

    @Test
    public void testIsEmpty() {
	MyHashMap<Integer,Integer> test=new MyHashMap();
	assertTrue(test.isEmpty());
    }

    @Test
    public void testClear() {
	fail("Not yet implemented");
    }

    @Test
    public void testToString() {
	MyHashMap<Integer,Integer> test=new MyHashMap();
	System.out.println(test.toString());
    }
    
    @Test
    public void testPut() {
	MyHashMap<Integer,String> test=new MyHashMap();
	test.put(40, "hello");
	test.put(47, "my");
	test.put(47, "name");
	test.put(48, "is");
	test.put(51, "colin");
	test.put(6, "mccahill");
	test.put(2, "!");
	
	
	System.out.println(test.toString());
    }
    
    @Test
    public void testGet() {
	MyHashMap<Integer,String> test=new MyHashMap();
	test.put(40, "hello");
	test.put(47, "my");
	test.put(47, "name");
	test.put(48, "is");
	test.put(51, "colin");
	test.put(6, "mccahill");
	test.put(2, "!");
	
	System.out.println(test.get(40));
    }
    
    @Test
    public void testRemove() {
	MyHashMap<Integer,String> test=new MyHashMap();
	test.put(40, "hello");
	test.put(47, "my");
	test.put(47, "name");
	test.put(48, "is");
	test.put(51, "colin");
	test.put(6, "mccahill");
	test.put(2, "!");
	test.remove(48);
	
	System.out.println(test.toString());
	assertTrue(test.containsKey(40));
	assertTrue(test.containsValue("mccahill"));
    }
    
    @Ignore
    public void testIterator() {
	MyHashMap<Integer,String> test=new MyHashMap();
	test.put(40, "hello");
	test.put(47, "my");
	test.put(47, "name");
	test.put(48, "is");
	test.put(51, "colin");
	test.put(6, "mccahill");
	test.put(2, "!");
	Iterator<Integer> testIterator=test.keys();
	while(testIterator.hasNext()) {
	    System.out.println(testIterator.next());
	}
    }
    
    @Test
    public void testResize() {
	MyHashMap<Integer,String> test=new MyHashMap();
	for(int i=0;i<20;i++) {
	    test.put(i, "test");
    }
	test.put(40, "hello");
	test.put(47, "my");
	test.put(47, "name");
	test.put(48, "is");
	test.put(51, "colin");
	System.out.println(test.size());
	System.out.println(test.toString());
    }
    
    @Test
    public void testContainsKey() {
	
    }
}

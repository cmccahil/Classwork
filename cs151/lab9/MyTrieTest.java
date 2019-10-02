import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import org.junit.Test;

public class MyTrieTest {

    @Test
    public void testIsEmpty() {
	MyTrie test=new MyTrie();
	assertEquals(0,test.size);
	assertTrue(test.isEmpty());
    }

    @Test
    public void testContainsEmptyString() {
	MyTrie test=new MyTrie();
	assertFalse(test.containsEmptyString());
	test.add("");
	assertTrue(test.containsEmptyString());
    }

    @Test
    public void testContains() {
	MyTrie test=new MyTrie();
	test.add("hello");
	test.add("hellos");
	test.add("hella");
	test.add("apples");
	test.add("bolivia");
	test.add("bologna");
	assertTrue(test.contains("hello"));
	assertFalse(test.contains("h"));
	assertTrue(test.contains("hellos"));
	assertEquals(test.size,6);
    }

    

    @Test
    public void testContainsPrefix() {
	MyTrie test=new MyTrie();
	test.add("hello");
	test.add("hellos");
	test.add("hella");
	test.add("apples");
	test.add("bolivia");
	test.add("bologna");
	assertTrue(test.containsPrefix("hell"));
	assertFalse(test.containsPrefix("da"));
	assertTrue(test.containsPrefix("bol"));
    }

    @Test
    public void testContainsString() {
	fail("Not yet implemented");
    }

    @Test
    public void testAddString() {
	fail("Not yet implemented");
    }

    @Test
    public void testToString() {
	MyTrie test=new MyTrie();
	test.add("hello");
	test.add("hellos");
	test.add("hella");
	test.add("apples");
	test.add("bolivia");
	test.add("bologna");
	System.out.println(test.toString());
    }

    @Test
    public void testHelperMethod() {
	fail("Not yet implemented");
    }

}

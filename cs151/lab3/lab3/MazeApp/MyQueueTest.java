package MazeApp;

import static org.junit.Assert.*;

import org.junit.Ignore;
import org.junit.Test;

public class MyQueueTest {

    @Ignore
    public void testPush() {
	fail("Not yet implemented");
    }

    @Ignore
    public void testPeek() {
	fail("Not yet implemented");
    }

    @Ignore
    public void testPull() {
	fail("Not yet implemented");
    }

    @Test
    public void testMyQueue() {
	MyQueue test = new MyQueue();
	System.out.println(test.pop());
	System.out.println(test.peek());
	Square thing = new Square(0,0,1);
	Square temp1 = new Square(2,2,3);
	test.push(thing);
	test.push(temp1);
	System.out.println(test.pop());
	//test.push(thing);
	System.out.println(test.peek());
	
	//fail("Not yet implemented");
    }

}

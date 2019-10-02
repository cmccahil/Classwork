package MazeApp;

import static org.junit.Assert.*;

import org.junit.Ignore;
import org.junit.Test;

public class MyStackTest {

    @Ignore
    public void testPush() {
	fail("Not yet implemented");
    }

    @Ignore
    public void testPop() {
	fail("Not yet implemented");
    }

    @Ignore
    public void testPeek() {
	fail("Not yet implemented");
    }

    @Test
    public void testMyStack() {
	MyStack hello = new MyStack();
	Square fun = new Square(0,0,0);
	hello.push(fun);
	hello.push(fun);
	Square x = new Square (2,2,2);
	hello.push(x);
	hello.push(fun);
	System.out.println(hello.peek());
	System.out.println(hello.pop());
	System.out.println(hello.peek());
	hello.pop();
	System.out.println(hello.pop());
	hello.pop();
	System.out.println(hello.pop());
	//fail("Not yet implemented");
    }

}

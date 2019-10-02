package MazeApp;

import java.util.ArrayList;
/**
 * This is a queue built on an ArrayList, so it causes a stackoverflow on the larger mazes
 * we are unsure how to make this more efficient, so we are leaving it with this issue
 * @author schapin
 *
 */
public class MyQueue {
    ArrayList<Square> myQueue;
    
    public void push(Square x) {
	myQueue.add(x);
    }
    public Square peek() {
	if (myQueue.size()>0) {
	    return myQueue.get(0);
	}
	return null;
    }
    public int length() {
	return myQueue.size();
    }
    public Square pop() {
	if (myQueue.size()>0) {
	    Square temp = peek();
	    ArrayList<Square> temp1 = new ArrayList<Square>();
	    for (int i=1;i<myQueue.size();i++) {
		temp1.add(myQueue.get(i));
	    }
	    myQueue=temp1;
	    return temp;
	}
	return null;
    }
    public MyQueue() {
	myQueue=new ArrayList<Square>();
    }
}

package MazeApp;

import java.util.ArrayList;

public class MyStack {
    public ArrayList<Square> myStack;
    public void push(Square x) {
	myStack.add(x);
    }
    public int length() {
	return myStack.size();
    }
    public Square pop() {
	if (myStack.size()>0) {
	    Square temp = myStack.get(myStack.size()-1);
	    myStack.remove(myStack.size()-1);
	    return temp;
	}
	return null;
    }
    public Square peek() {
	if(myStack.size()>0) {
	    return myStack.get(myStack.size()-1);
	}
	return null;
    }
    public MyStack() {
	myStack = new ArrayList<Square>();
    }
}

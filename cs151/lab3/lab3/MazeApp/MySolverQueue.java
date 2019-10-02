package MazeApp;

import java.util.ArrayList;

public class MySolverQueue {

    private MyQueue worklist;
    private Maze maze;
    private ArrayList<Square> solution;
    public void MakeEmpty() {
	for (int i=0;i<worklist.length();i++) {
	    worklist.pop();
	}
    }
    public boolean isEmpty() {
	if (worklist.length()==0) {
	    return true;
	}
	return false;
    }
    public void add(Square sq) {
	worklist.push(sq);
    }
    public Square next() {
	if (worklist.length()>0) {
	    return worklist.pop();
	}
	return null;
    }
    public boolean isSolved() {
	if (worklist.length()==0||worklist.peek().toString()=="E") {
	    return true;
	}
	return false;
    }
    public String getPath() {
	if (solution.size()>0) {
	    String sol = "";
	    for (int i=0;i<solution.size();i++) {
		sol=sol+ ", ["+ solution.get(i).getCol()+", "+ solution.get(i).getRow()+"]";
	    }
	    return sol;
	}
	return "There are no valid solutions";
    }
    public Square step() {
	if (isEmpty()==true) {
	    return null;
	}
	Square steptest =worklist.pop();
	if (steptest.toString().equals("E")) { //end found:
	    //solution.add(steptest);
	    return steptest;
	}
	//test all cases (N,E,S,W) and add the non-explored ones to the Queue:
	ArrayList<Square> NESW=new ArrayList<Square>();
	NESW= maze.getNeighbors(steptest);
	for (int i=0;i<NESW.size();i++) {
	    //add everything explored to the explored list:
	    if (NESW.get(i).checked()==true) {}
	    else {
		worklist.push(NESW.get(i));//not usable for Queue code:
	    }
	}
	steptest.change();
	Square newspace = step();
	if (newspace!=null) {
	    return newspace;
	}
	return null;
    }
    public void solve() {
	Square x = step();
	if(x!=null) {
	    System.out.println(" ["+x.getRow()+", "+x.getCol()+"]");
	}
	else {
	    System.out.println("no solution");
	}
    }
    public MySolverQueue(Maze maze1) {
	worklist=new MyQueue();
	maze=new Maze();
	maze=maze1;
	worklist.push(maze.getStart());
    }
}



package MazeApp;

import java.util.ArrayList;

public class MazeSolverStack {
    private MyStack worklist;
    private Maze maze;
    private ArrayList<Square> solutionsquares;
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
    /**
     * this code writes the solution path from finish to start.
     * @return String
     */
    public String getPath() {
	if (solutionsquares.size()>0) {
	    String sol = "";
	    for (int i=0;i<solutionsquares.size();i++) {
		sol=sol+ "["+ solutionsquares.get(i).getCol()+", "+ solutionsquares.get(i).getRow()+"],";
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
	//System.out.println("hi");
	if (steptest.toString().equals("E")) { //end found:
	    solutionsquares.add(steptest);
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
	    solutionsquares.add(steptest);
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
	System.out.println("here is the path from the solution to the start:");
	System.out.println(getPath());
    }
    public MazeSolverStack(Maze maze1) {
	worklist=new MyStack();
	solutionsquares = new ArrayList<Square>();
	maze=new Maze();
	maze=maze1;
	maze.loadMaze(maze.saving);
	add(maze.getStart());
    }
}

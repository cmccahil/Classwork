package MazeApp;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

/***
 * This is the initialization of the Maze class
 * it will create and find information about the maze
 * @author schapin&cmccahil
 *
 */
public class Maze {
    private Square[][] maze;
    private String strungMaze;
    private int row;
    private int col;
    public String saving;
    public boolean loadMaze(String fname) {
	try {
	    saving=fname;
	    Scanner input=null;
	    input = new Scanner(new File(fname));
	    //System.out.println(fname);
	    String[] data = input.nextLine().split(" ");
	    row = Integer.parseInt(data[0]);
	    col = Integer.parseInt(data[1]);
	    this.maze=new Square[row][col];
	    int i=0;
	    while (input.hasNextLine()==true&&i<row) {
		data = input.nextLine().split(" ");
		for (int x=0;x<col;x++) {
		    int butts=Integer.parseInt(data[x]);
		    maze[i][x] = new Square(i,x,butts);
		    //System.out.println(maze[i][x].toString());
		}
		i++;
	    }
	    return true;
	}
	catch (FileNotFoundException e) {
	    System.out.println("try running it again with a real input. ");
	    return false;
	}
    }
    public ArrayList<Square> getNeighbors(Square sq){
	int thisrow = sq.getRow();
	int thiscol = sq.getCol();
	ArrayList<Square> friends = new ArrayList<Square>();
	//System.out.println("hi");
	if (thisrow>0) { //north
	    //System.out.println(maze[thisrow][thiscol]);
	    friends.add(maze[thisrow-1][thiscol]);
	}
	if (thiscol<col-1) { //east
	    friends.add(maze[thisrow][thiscol+1]);
	}
	if (thisrow<row-1) { //south
	    friends.add(maze[thisrow+1][thiscol]);
	    //System.out.println(maze[thisrow+1][thiscol]);
	}
	if (thiscol>0) { //west
	    friends.add(maze[thisrow][thiscol-1]);
	}
	return friends;
    }
    public Square getStart() {
	for (int i=0;i<row;i++) {
	    for (int x=0;x<col;x++) {
		if (maze[i][x].toString()=="S") {
		    return maze[i][x];
		}
	    }
	}
	return null;
    }
    public Square getFinish() {
	for (int i=0;i<row;i++) {
	    for (int x=0;x<col;x++) {
		if (maze[i][x].toString()=="E") {
		    return maze[i][x];
		}
	    }
	}
	return null;
    }
    public void reset() {
	loadMaze(saving);
    }
    public String toString() {
	for (int i=0;i<row;i++) {
	    for (int x=0;x<col;x++) {
		if (i==0&&x==0) {
		    strungMaze=maze[i][x].toString();
		}
		if (x==col-1) {
		    strungMaze=strungMaze+maze[i][x]+"\n";
		}
		else {
		    strungMaze=strungMaze+maze[i][x];
		}
	    }
	}
	//System.out.print(strungMaze);
	return strungMaze;
    }
    //public String toString() {
	
    //}
    public Maze() {
	//Scanner input = new Scanner(System.in);
	//System.out.println("please input the file you would like to be used.");
	//saving = input.nextLine();
	//saving= "/usr/users/quota/students/2015/schapin/cs151/lab3/MazeApp/maze-1";
	//if (loadMaze(saving)==true) {
	    //System.out.println("hi");
	//print();
	
    }
    
}

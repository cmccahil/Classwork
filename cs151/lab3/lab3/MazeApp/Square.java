package MazeApp;
/***
 * a class for the squares that will be used in Maze the class
 * initializing takes three integers
 * @author schapin&cmccahil
 *
 */
public class Square {
    private int type;
    private boolean checked;
    public static final int WALL = 1;
    public static final int SPACE = 0;
    public static final int START = 2;
    public static final int EXIT = 3;
    private int row;
    private int col;
    public String toString() {
	if (type==SPACE) {
	    return "_";
	}
	else if (type==WALL) {
	    return "#";
	}
	else if (type==START) {
	    return "S";
	}
	else if (type==EXIT) {
	    //System.out.println("hi");
	    return "E";
	}
	return null;
    }
    public int getRow() {	
	return row;
    }
    public int getCol() {
	return col;
    }
    public int getType() {
	return type;
    }
    public boolean checked() {
	return checked;
    }
    public void change() {
	checked=true;
    }
    public Square(int row1, int col1, int type1){
	type=type1;
	col=col1;
	row=row1;
	checked =false;
    }
}








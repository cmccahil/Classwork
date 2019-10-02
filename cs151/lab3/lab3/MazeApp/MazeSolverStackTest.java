package MazeApp;

import static org.junit.Assert.*;

import java.util.Scanner;

import org.junit.Test;

public class MazeSolverStackTest {

    @Test
    public void test() {
	Maze maze = new Maze();
	Scanner scan = new Scanner(System.in);
	System.out.println("please input the file that you would like to use.");
	maze.saving=scan.nextLine();
	MazeSolverStack tester = new MazeSolverStack(maze);
	tester.solve();
	//fail("Not yet implemented");
    }

}

package MazeApp;

import static org.junit.Assert.*;

import org.junit.Test;

public class MySolverQueueTest {

    @Test
    public void test() {
	Maze maze = new Maze();
	MySolverQueue tester = new MySolverQueue(maze);
	tester.solve();
	//fail("Not yet implemented");
    }

}

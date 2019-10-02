import static org.junit.Assert.assertSame;

import org.junit.Test;

public class MyTreeMapTest {

    @Test
    public void testPutKV() {
	//tests put and restructure (when I tested restructure
	//I had MyTreeMap print the key that it was restructuring (80)
	MyTreeMap mytreemap=new MyTreeMap();
	mytreemap.put(100,"hello");
	mytreemap.put(125,"my");
	mytreemap.put(75,"name");
	mytreemap.put(50,"is");
	mytreemap.put(90,"colin");
	mytreemap.put(80,"mccahill");
	mytreemap.put(95,"!");
	System.out.println(mytreemap);
    }

    @Test
    public void testGetObject() {
	MyTreeMap mytreemap=new MyTreeMap();
	mytreemap.put(50,"hello");
	mytreemap.put(25,"my");
	mytreemap.put(75,"name");
	mytreemap.put(30,"is");
	mytreemap.put(50,"colin");
	mytreemap.put(60,"mccahill");
	assertSame("tests get","name",mytreemap.get(75));
    }
}
    


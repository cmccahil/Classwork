import java.util.AbstractSet;
import java.util.Iterator;
/**
 * 
 * @author cmccahil
 *@author ffeirrera
 * @param <T>
 */

public class MyTreeSet<T extends Comparable<? super T>> extends AbstractSet<T> {

    
    /** Backing storage for the set */
    private MyTreeMap<T, Boolean> set;
    
    // TODO - STUDENTS SHOULD DO THE FOLLOWING
    //
    // 1. Create a 0-argument constructor
    public MyTreeSet() {
	set = new MyTreeMap<T,Boolean>();
    }
    
    // 2. Override the add method
    public boolean add(T item) {
	int i;
	if (set.get(item)==null) {
	    set.put(item,true);
	    return true;
	    }
	   
	
	return false;
    }
    // 3. Override iterator()
    public Iterator<T> iterator(){
	return set.keys();
    }
    // 4. Override size()
    public int size() {
	return set.size;
    }
    
    // 5. Override clear()
    public void clear() {
	set=new MyTreeMap<T, Boolean>();
    }
}

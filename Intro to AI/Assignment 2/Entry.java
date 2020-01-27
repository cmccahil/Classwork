
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Entry {
	String [] attributes;
	String classVariable;
	Double distance;
	
	//transforms input string into an Entry object
	public Entry (String input) {
		attributes = input.split(",");
		//if has class defined (training data)
		if (attributes [attributes.length-1].equals("yes") ||attributes [attributes.length-1].equals("no")) {
			classVariable = attributes [attributes.length-1];
		}
	}
	
	
	public void printEntry () {
		for (int i = 0; i < attributes.length; i++) {
			System.out.print(attributes[i]+" ");
		}
		System.out.println();
	}
}

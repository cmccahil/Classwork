/**
 * This takes out certain words in text files and replaces them with Xs 
 * @author cmccahil
 * @date 09/18/16
 */
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Redactor {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	
	
	
	//Making the first arraylist
	Scanner input=null;
	try {
	    input=new Scanner(new File(args[0]));
	}
	catch(FileNotFoundException e) {
	    System.out.println("Problem opening file: " + e.getMessage());
	    System.exit(1);
	}
	ArrayList<String> words=new ArrayList();
	while(input.hasNextLine()) {
	    String a=null;
	    a=input.nextLine();
	    words.add(a);
	}
	
	
	
	//making the second array list (everything is labeled 1 now)
	Scanner input1=null;
	try {
	    input1=new Scanner(new File(args[1]));
	}
	catch(FileNotFoundException e) {
	    System.out.println("Problem opening file: " + e.getMessage());
	    System.exit(1);
	}
	ArrayList<String> words1=new ArrayList();
	while(input1.hasNext()) {
	    String b=null;
	    b=input1.next();
	    words1.add(b);
	}
	
	
	
	
	//loop to go through the array list and replace the words with X's
	
	int counter=0;
	for (String c: words1) {
	    for (String d:words) {
		if (c.equals(d)){
		    words1.set(counter, "XXXXX");
		}
	    }
	    counter++;
	}
	
	//now I am printing the words regularly 
	
	for (String e:words1) {
	    System.out.print(e+" ");
	}
	
    }

}

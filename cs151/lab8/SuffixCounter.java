import java.util.Iterator;
import java.util.Scanner;

public class SuffixCounter {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	Scanner scannerK=new Scanner(args[0]);
	String stringK=scannerK.next();
	int k=Integer.parseInt(stringK);
	
	System.out.print("Input string: ");
	
	Scanner input=new Scanner(System.in);
	String inputString;
	inputString=input.next();
	
	int counter=0;
	MyHashMap<String,Markov> frequencyCounter=new MyHashMap();
	while(counter<=inputString.length()-k) {
	    String substring=inputString.substring(counter, counter+k);
	    char character=inputString.charAt(counter+k);  
	    //Markov value=new Markov(substring);
	    if(frequencyCounter.containsKey(substring)) {
		frequencyCounter.get(substring).add();
		frequencyCounter.get(substring).add(character);
		counter++;
	    }
	    else {
		Markov value=new Markov(substring);
		value.add();
		frequencyCounter.put(substring, value);
		Markov charactervalue=new Markov(character);
		charactervalue.listOfSuffix.put(character, charactervalue);
		counter++;
	    }
    }
	System.out.println(frequencyCounter.size()+" distinct keys");

	Iterator<Markov> frequencyValues=frequencyCounter.Values();
	while(frequencyValues.hasNext()) {
	    System.out.println(frequencyValues.next());
	    
	}
    }

}

import java.util.TreeMap;

/**
 * 
 * @author cmccahil
 *This is a class that represents a k-character substring and returns a markov model.
 */

public class Markov {
    int counter=0;
    int charactercounter=0;
    String markov;
    Character markov1;
    TreeMap<Character,Markov> listOfSuffix;
    
    public Markov(String substring) {
	markov=substring;
    }
    public Markov(Character suffix) {
	markov1=suffix;
    }
    public void add(){
	counter++;
    }
   public String toString() {
       String markovString=counter+" "+markov;
       return markovString;
    }
    public void add(char c) {
	charactercounter++;
    }

}

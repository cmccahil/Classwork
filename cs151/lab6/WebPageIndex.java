
// TODO - implement this and all JavaDoc comments!
/**
 * @author cmccahil
 * @author fferreira
 * 
 * This is a data structure that that contains the index representation of a web
 * page.
 * 
 * 11/7/16
 */

import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

public class WebPageIndex {
    private MyTreeMap<String, LinkedList<Integer>> indexes;
    private MyTreeSet links;
    private String Url;
    private int wordcount;
    String[] S;

    int addwords = 1;
    int phrasecount = 0;
    int phraselocationsvariable;
    ArrayList<Integer> phraselocations = new ArrayList<Integer>();

    public WebPageIndex(String baseUrl) {
	indexes = new MyTreeMap<String, LinkedList<Integer>>();
	links = new MyTreeSet();
	Url = baseUrl;
	try {
	    HTMLScanner scanner = new HTMLScanner(baseUrl);

	    int count = 0;
	    while (scanner.hasNext()) {
		String token = scanner.next().toLowerCase();
		if (indexes.get(token) == null) {
		    LinkedList<Integer> currentindex = new LinkedList<Integer>();
		    currentindex.add(count);
		    indexes.put(token, currentindex);
		} else if (indexes.get(token) != null) {
		    indexes.get(token).add(count);
		    // left off on here last night
		}
		count++;
	    }
	    wordcount = count;
	    while (scanner.hasNextLink()) {
		links.add(scanner.nextLink());
	    }
	} catch (FileNotFoundException e) {
	    System.out.println(e);
	} catch (IOException e) {
	    System.out.println(e);
	}
    }

    public int getWordCount() {
	// returns total number words on page
	return wordcount;
    }

    public String getUrl() {

	return Url;
    }

    public boolean contains(String s) {
	//return true if word s appears anywhere on page
	if (indexes.containsKey(s)) {
	    return true;
	} else {
	    return false;
	}
    }

    public int getCount(String s) {
	//returns number of time s appears
	int count = indexes.get(s).size();// ask colin about implementation
					  // linked list
	return count;
    }

    public double getFrequency(String s) {
	// returns frequency word s appears on page
	return ((double) getCount(s) / (double) getWordCount());
    }

    public List<Integer> getLocations(String s) {
	// return list representing locations where the word s appears on page
	if (indexes.get(s) == null) {
	    return new LinkedList<Integer>();
	} else {
	    return indexes.get(s);
	}
    }

    public Iterator<String> words() {
	// iterator over words on page in alphabetical order
	return indexes.keys("inorder");
    }

    public String toString() {
	// returns maps tostring value
	return indexes.toString();
    }


    public boolean containsPhrase(String s) {
	S = s.toLowerCase().split("\\s+");
	ArrayList<Integer> foundList = new ArrayList<Integer>();
	for (int z = 0; z < indexes.get(S[0]).size(); z++) {
	    foundList.add(indexes.get(S[0]).get(z));
	}
	for (int wIndex =1;wIndex<S.length;wIndex++) {
	    String word = S[wIndex];
	    for (int f = 0; f < foundList.size(); f++) {
		if(foundList.get(f)!=-10) {
		    //LinkedList<Integer> iList = indexes.get(word);
		for (int i = 0; i < indexes.get(word).size(); i++) {
		    
		    if (foundList.get(f) == indexes.get(word).get(i) - 1) {
			foundList.set(f, indexes.get(word).get(i));
			break;
		    }else if((i+1)==indexes.get(word).size()) {
			//If we don't find a corresponding index link
			foundList.set(f, -10);
		    }
		    
		}
		
	    }
	}
	}
	for(int e = 0; e<foundList.size();e++) {// to find the location and add it to arraylist
	    // and add +1 to phrase count
	    if(foundList.get(e) != -10) {
		phraselocations.add(foundList.get(e));
		phrasecount++;
	    }
	}
	for(int e = 0; e<foundList.size();e++) {
	    if(foundList.get(e) != -10) {
		return true;
	    }
	}
	return false;
    }

    public int getPhraseCount(String s) {
	if (containsPhrase(s)) {
	    return phrasecount;
	} else {
	    return 0;
	}
    }

    public double getPhraseFrequency(String s) {
	// returns number of times phrase s appears on page divided by total words
	return ((double) getPhraseCount(s) / (double) getWordCount());
    }

    public List<Integer> getPhraseLocations(String s) {
	containsPhrase(s);
	List<Integer> listlocations = new ArrayList<Integer>();
	while (phraselocations.size() != 0) {
	    listlocations.add(phraselocations.remove(0));
	}
	return listlocations;
    }
}

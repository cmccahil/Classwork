import static org.junit.Assert.assertSame;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class WebPageIndexTest {

    @Test
    public void testWebPageIndex() {
	WebPageIndex googleIndex = new WebPageIndex("https://www.google.com/");
	
    }
    
    @Test
    public void testGetUrl() {
	WebPageIndex googleIndex = new WebPageIndex("https://www.google.com/");
	System.out.println(googleIndex.getUrl());
    }
    
    @Test
    public void testGetWordCount() {
	WebPageIndex googleIndex = new WebPageIndex("https://www.google.com/");
	System.out.println(googleIndex.getWordCount());
    }

    @Test
    public void testContains() {
	WebPageIndex googleIndex = new WebPageIndex("https://www.google.com/");
	assertTrue(googleIndex.contains("google"));
    }

    @Test
    public void testGetCount() {
	WebPageIndex googleIndex = new WebPageIndex("https://www.google.com/");
	assertSame(1,googleIndex.getCount("google"));
    }

    @Test
    public void testGetFrequency() {
	WebPageIndex googleIndex = new WebPageIndex("https://www.google.com/");
	System.out.println(googleIndex.getFrequency("google"));
    }

    @Test
    public void testGetLocations() {
	WebPageIndex googleIndex = new WebPageIndex("https://www.google.com/");
	System.out.println(googleIndex.getLocations("google"));
    }

    @Test
    public void testWords() {
	WebPageIndex googleIndex = new WebPageIndex("https://www.google.com/");
	System.out.println(googleIndex.words().next());
    }

    @Test
    public void testToString() {
	WebPageIndex googleIndex = new WebPageIndex("https://www.google.com/");
	System.out.println(googleIndex.toString());
    }

    @Test
    public void testContainsPhrase() {
	WebPageIndex cs151index = new WebPageIndex("https://occs.cs.oberlin.edu/~rhoyle/16f-cs151/lab06/index.html");
	System.out.println("phrase " + cs151index.containsPhrase("you are"));
    //does not work with punctuation
    }

    @Test
    public void testGetPhraseCount() {
	WebPageIndex cs151index = new WebPageIndex("https://occs.cs.oberlin.edu/~rhoyle/16f-cs151/lab06/index.html");
	System.out.println("phrase count " + cs151index.getPhraseCount("you are"));
    }

    @Test
    public void testGetPhraseFrequency() {
	WebPageIndex cs151index = new WebPageIndex("https://occs.cs.oberlin.edu/~rhoyle/16f-cs151/lab06/index.html");
	System.out.println("phrase frequency " + cs151index.getPhraseFrequency("you are"));
    }

    @Test
    public void testGetPhraseLocations() {
	WebPageIndex cs151index = new WebPageIndex("https://occs.cs.oberlin.edu/~rhoyle/16f-cs151/lab06/index.html");
	System.out.println("locations " + cs151index.getPhraseLocations("you are"));
    }

}

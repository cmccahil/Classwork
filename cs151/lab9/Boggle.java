import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;
/**
 * class Boggle that represents the Boggle Board
 * @author cmccahil
 *
 */
public class Boggle {
    MyTrie lex; //the dictionary, stored in a Trie
    Square[][] board; //the 4x4 board
    MyTrie foundWords; //The dictionary words on the current board
    MyTrie guesses; //The valid words made so far by our one player
    String[] dice; //array of dice
   
    //constructor that takes dictionary parameter
    public Boggle(String file) {
	lex=new MyTrie();
	try {
	    Scanner input=new Scanner(new File(file));
	    while(input.hasNext()) {
		lex.add(input.next());
	    }
	}
	catch(FileNotFoundException e) {
	    System.out.println("Problem opening file: " + e.getMessage());
	    System.exit(1);
	}
	fillDice();
    }
    
    //return boggle board
    public Square[][] getBoard(){
	return board;
    }
    
    //return number of guesses in guesses
    public int numGuesses() {
	return guesses.size;
    }
    
    //return the squares of the board, one row per line of the string
    public String toString() {
	String returnString="";
	for(int i=0;i<4;i++) {
	    for(int k=0;k<4;k++) {
		returnString=returnString+board[k][i];
	    }
	    returnString=returnString+"\n";
	}
	return returnString;
    }
    
    //return true if the board contains the word word and false otherwise
    public boolean contains(String word) {
	if(foundWords.contains(word)) {
	    return true;
	}
	else {
	    return false;
	}
    }
    
    //add guess to list of guesses, if it is in foundWords
    //return true if it was a valid guess and false otherwise
    public boolean addGuess(String guess) {
	if(contains(guess)) {
	    return guesses.add(guess);
	}
	
	    return false;
	
    }
    public void newGame() {
	//rolls the dice and fills the board with new squares accordingly
	fillDice();
	fillBoardFromDice();
	//construct a trie for the dictionary words found in the board
	foundWords=new MyTrie();
	fillFoundWords();
	guesses=new MyTrie();
	
    }
    
    //constructs the dice from the file dice.txt
    private void fillDice() {
	dice=new String[16];
	try {
	    Scanner sides=new Scanner(new File("dice.txt"));
	    int counter=0;
	    while(sides.hasNextLine()) {
		dice[counter]=sides.nextLine();
		counter++;
	    }
	}
	catch(FileNotFoundException e) {
	    System.out.println("Problem opening file: " + e.getMessage());
	    System.exit(1);
	}
    }
    public int randomInteger(int bound) {
	Random randomGenerator=new Random();
	int randomInt=randomGenerator.nextInt(bound)+1;
	return randomInt;
    }
    
    //returns a list of valid Squares on the board that form the word w
    public ArrayList<Square> squaresForWord(String w){
	ArrayList<Square> word=new ArrayList<Square>();
	outerLoop:for(int i=0;i<4;i++) {
	    for(int k=0;k<4;k++) {
		board[i][k].mark();
		squaresForWord(board[i][k],w,word);
		board[i][k].unmark();
		if(squaresForWord(board[i][k],w,word).size()<w.length()) {
		    word.clear();
		}
		/*if(squaresForWord(board[i][k],w,word).size()==w.length()) {
		    break outerLoop;
	    }*/
	    
	}
	}/*
	for(int i = 0;i<=word.size()-1;i++) {
	    char c=w.charAt(i);
	    String d=""+c;
	    if(word.get(i).toString()!=d) {
		word.remove(i);
	    }
	}*/
	return word;
    }
    
    //returns any one valid list of Squares on the board starting 
    //with sq that form the word w
    private ArrayList<Square> squaresForWord(Square sq,String w,ArrayList<Square> word){
	if(w.equals("")) {
	    return word;
	}
	
	if(w.substring(0,1).equals(sq.toString())) {
	    
	    
	    word.add(sq);
	    for(int i=-1;i<2;i++) {
		for(int j=-1;j<2;j++) {
		    int newX=sq.getX()+i;
		    int newY=sq.getY()+j;
		    if((sq.getX()+i<=3) && (sq.getX()+i>=0) && (sq.getY()+j<=3) 
			    && (sq.getY()+j>=0)&& (!((i==j))&& 
				    (board[newX][newY].isMarked()==false))) {
			
			board[newX][newY].mark();
			
			String substring=w.substring(1);
			squaresForWord(board[newX][newY],substring,word);
			board[newX][newY].unmark();
			
			}
		    }
		}
	    }
	    
	
	return word;    
    }
    
   
    //constructs a new board randomly out of 16 die
    private void fillBoardFromDice() {
	board=new Square[4][4];
	for(int i=0;i<4;i++) {
	    for(int k=0;k<4;k++) {
		int randomdice=randomInteger(15);
		int randomletter=randomInteger(5);
		String letter= "" + dice[randomInteger(randomdice)].charAt(randomletter);
		if(letter.toLowerCase().equals("q")) {
		    letter="qu";
		}
		board[i][k]=new Square(i,k,letter) ;
	    }
	}
    }
    //add to the foundWords Trie all words in the dictionary
    //that start with prefix and can be completed in a valid
    //way on the board starting at square sq
    private void search(Square sq,String prefix) {
	if(lex.contains(prefix)) {
	    foundWords.add(prefix);
	}
	if(lex.containsPrefix(prefix)) {
	    String l=sq.toString();
	    for(int i=-1;i<2;i++) {
		for(int j=-1;j<2;j++) {
		    int newX=sq.getX()+i;
		    int newY=sq.getY()+j;
		    //if the newX and newY is in bounds 
		    if((sq.getX()+i<=3) && (sq.getX()+i>=0) && (sq.getY()+j<=3) 
			    && (sq.getY()+j>=0)&& (!((i==j))&& 
				    (board[newX][newY].isMarked()==false))) {
			
			board[newX][newY].mark();
			String newPrefix=prefix+board[newX][newY].toString();
			search(board[newX][newY],newPrefix);
			board[newX][newY].unmark();
		    }
		}
	    }
	}
    }
    
    //constructs foundWords to contain all words on the board
    //that are in the dictionary
    private void fillFoundWords() {
	foundWords=new MyTrie();
	for(int i=0;i<4;i++) {
	    for(int k=0;k<4;k++) {
		board[k][i].mark();
		search(board[k][i],board[k][i].toString());
		board[k][i].unmark();
	    }
    }
	
    }
    public static void main(String[] args) {
	// TODO Auto-generated method stub
	Boggle boggle = new Boggle(args[0]);
	BoggleFrame bFrame = new BoggleFrame( boggle );
	bFrame.pack();
	bFrame.setLocationRelativeTo(null);
	bFrame.setVisible(true);
    }

}

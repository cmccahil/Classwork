import java.util.Random;
import java.util.Scanner;
/**
 * The computer will pick a number between 1 and 1000 and then the user will try to guess what it is 
 * @author cmccahil
 * @date 09/14/16
 */
public class HiLo {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	System.out.println("Let's play a game!");
	System.out.println("I'm thinking of a number between 1 and 1000");
	System.out.println("Try to guess what it is!");
	System.out.println();
	System.out.print("Enter a guess: ");
	int Counter=0;
	Random rnd=new Random();
	int target=rnd.nextInt(1000)+1;
	int userGuess=-1;
	Scanner input=new Scanner(System.in);
	while(input.hasNextLine()) {
	    String line=input.nextLine();
	    Scanner s2=new Scanner(line);
	    if (s2.hasNextInt()) {
		userGuess=s2.nextInt();
		if (userGuess<target) {
		    System.out.println("Too low!");
		    System.out.println();
		    System.out.print("Enter a guess: ");
		    Counter++;
		}
		else if(userGuess>target) {
		    System.out.println("Too high!");
		    System.out.println();
		    System.out.print("Enter a guess: ");
		    Counter++;
		}
		else {
		    Counter++;
		    break;
		}
	    }
	    else {
		System.out.println("That's not a number, try again.");
		continue;
	    }
	}
	System.out.println("You guessed my number! It took you " + Counter + " tries.");
    }

}

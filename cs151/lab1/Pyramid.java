/**
 * Program to build a pyramid out of stars
 * @author cmccahil
 * @date 2016-09-14
 */
public class Pyramid {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	int input=-1;
	int initialization=0;
	int spaces=0;
	int stars=0;
	int secondstars=0;
	//these all set up the variables needed for the program
	if (args.length!=1) {
	    System.out.println("That is not a length equal to one.");
	    System.exit(1);
	}
	else {

	    try {
		input= Integer.parseInt(args[0]);
	    }catch(NumberFormatException e) {
		System.out.println("This is not a integer");
		System.exit(1);
	    }
	}
	//statements to catch errors
	for (initialization=0; initialization<input; initialization++ ) {
	    for (spaces=initialization; spaces<(input-1); spaces++ ) {
		System.out.print(" ");}
	    for (stars=0; stars<initialization+1; stars++) {
		System.out.print("*");}
	    if (stars>1){
		for (secondstars=0; secondstars<(stars-1); secondstars++) {
		    System.out.print("*");
		}
	    }
	    System.out.println();
	    }
	    }
    }
//printing the pyramid 


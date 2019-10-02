/**
 * This finds frequencies of digits in text files and makes a histogram
 * @author cmccahil
 * @date 09/18/16
 * "I have adhered to the Honor Code in this assignment."
 */
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Benford {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	Scanner input=null;
	try {
	    input=new Scanner(new File(args[0]));
	}
	catch(FileNotFoundException e) {
	    System.out.println("Problem opening file: " + e.getMessage());
	    System.exit(1);
	}
	
	
	
	//count of all leading digits
	int[] numbers=new int[10];
	while (input.hasNext()) {
	    String a=input.next();
	    if(Character.isDigit(a.charAt(0))) {
		int integervalue=Integer.parseInt(a.substring(0, 1));
		numbers[integervalue]++;
	    }
	}
	
	
	
	
	//frequency chart
	int MAXWIDTH=50;
	int totalamountofdigits=0;
	float maxcount=0;
	for(int k:numbers) {
	    totalamountofdigits=totalamountofdigits+k;
	    if (k>maxcount) {
		maxcount=k;
	    }
	}
	System.out.println(maxcount);
	
	int histogramlinenumber=0;
	for(int digit:numbers) {
	    float freq=((float)digit/(float)totalamountofdigits)*100;
	    int barlength=Math.round(((float)digit/maxcount)*MAXWIDTH);
	    System.out.printf("%d %8d %4.1f%%:",histogramlinenumber,digit,freq);
	    System.out.print(totalamountofdigits+" "+digit);
	    for(int stars=0;stars<barlength;stars++) {
		System.out.print("*");
	    }
	    System.out.println();
	    histogramlinenumber++;
	}
	}
    }



import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class TenFoldStratifiedCrossValidation {
	ArrayList <ArrayList <Entry>> folds;
	public TenFoldStratifiedCrossValidation (File trainingFile) {
		folds = new ArrayList <ArrayList<Entry>>();//TODO check
		// two buckets for stratified cross validation, i.e.
		//more or less equal representation of class variables in a fold
		ArrayList <Entry> yesBucket = new ArrayList <> ();
		ArrayList <Entry> noBucket = new ArrayList <> ();
		try {
			Scanner scan = new Scanner(trainingFile);
			//split training set into 2 buckets by class variable
			int numLines = 0;
			while (scan.hasNextLine()) {
				numLines++;
				Entry entry = new Entry(scan.nextLine());
				if (entry.attributes [entry.attributes.length-1].equals("yes")) yesBucket.add(entry);
				else noBucket.add(entry);
			}
			Random random = new Random();//random number generator
			int foldCounter = 0; //init counter to loop over folds
			//initialize folds 
			for (int i = 0; i < 10; i++) {
				folds.add(new ArrayList <Entry> ());
			}
			while (!yesBucket.isEmpty()) {
				int index = random.nextInt(yesBucket.size());
				folds.get(foldCounter%10).add(yesBucket.remove(index));// add random entry to folds
				foldCounter++;
			}
			while (!noBucket.isEmpty()) {
				int index = random.nextInt(noBucket.size());
				folds.get(foldCounter%10).add(noBucket.remove(index));// add random entry to folds
				foldCounter++;
			}
			//System.out.println(numLines);
			for (int i = 0; i < 10; i++) {
				System.out.println("fold"+(i+1));
			//	System.out.println(folds.get(i).size());
				for (Entry e: folds.get(i)) {
					for (int l = 0; l < e.attributes.length-1; l++) {
						System.out.print(e.attributes[l]+",");
					}
					System.out.println(e.attributes[8]);//print class
				}
				System.out.println();
			}

		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
	}
	
	public ArrayList <ArrayList <Entry>> returnSubsets () {
		return folds;
	}
	
	public void printSubsets() {
		for (int i = 0; i < folds.size(); i++) {
			System.out.println("fold"+(i+1));
			for (Entry e: folds.get(i)) {
				e.printEntry();
			}
			System.out.println();
		}
	}
}

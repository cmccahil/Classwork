import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Scanner;

public class MyClassifier {
	
	public static void main(String[] args) {
		File trainingFile = new File (args[0]);
		File testingFile = new File (args[1]);
		String algType = args[2];	
		int k = 0;
		if (algType.substring(algType.length()-2, algType.length()).equals("NN")) {			 
			String kString = algType.substring(0, algType.indexOf('N'));
			k = Integer.parseInt(kString);
			KNN knn = new KNN(trainingFile, testingFile, k);
			//TenFoldStratifiedCrossValidation validation = new TenFoldStratifiedCrossValidation(trainingFile);
		}
		else if (algType.equals("NB")) {
			BufferedReader training;
			try {
				NaiveBayes nb = new NaiveBayes();
				training = new BufferedReader(new FileReader(args[0]));
				BufferedReader testing = new BufferedReader(new FileReader(args[1]));
				String algorithm = args[2];
				ArrayList<String[]> trainingSet = nb.parseFile(training);
				//System.out.println(trainingSet);
				ArrayList<String[]> testingSet = nb.parseFile(testing);
				if(algorithm.equals("NB")) {
					nb.naiveBayes(trainingSet,testingSet);
				}
			} catch (FileNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}

		} 
	}
}

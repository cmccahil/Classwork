import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class NaiveBayes {
	public static ArrayList<Double> calculateMeans(ArrayList<ArrayList<Double>> training){
		ArrayList<Double> means = new ArrayList<Double>();
		for(int i=0;i<training.get(0).size();i++) {
			double mean = 0;
			for(int j=0;j<training.size();j++) {
				mean = mean + training.get(j).get(i);
			}
			means.add(mean/training.size());
		}
		return means;
	}
	
	//standard deviation
	public static ArrayList<Double> calculateSDs(ArrayList<ArrayList<Double>> dataSet, ArrayList<Double> means) {
		ArrayList<Double> SDs = new ArrayList<Double>();
		for(int i=0;i<dataSet.get(0).size();i++) {
			ArrayList<Double> buffer = new ArrayList<Double>();
			for(int k=0;k<dataSet.size();k++) {
				buffer.add(Math.pow((dataSet.get(k).get(i)-means.get(i)), 2));
			}
			double SD = 0;
			for(int j=0;j<buffer.size();j++) {
				SD = SD + buffer.get(j);
			}
			SD = Math.sqrt(SD/(buffer.size()-1));
			SDs.add(SD);
		}
		return SDs;
	}
	
	//probability distribution function
	public static ArrayList<ArrayList<Double>> calculatePDFs(ArrayList<ArrayList<Double>> dataSet,ArrayList<Double> means,ArrayList<Double> SDs){
		ArrayList<ArrayList<Double>> PDFs = new ArrayList<ArrayList<Double>>();
		for(int i=0;i<dataSet.size();i++) {
			ArrayList<Double> PDFrow = new ArrayList<Double>();
			for(int k=0;k<dataSet.get(0).size();k++) {
				double PDF = (1/(SDs.get(k)*Math.sqrt(2*Math.PI)))*(Math.pow(Math.E, (-((Math.pow((dataSet.get(i).get(k)-means.get(k)),2)/(2*(Math.pow(SDs.get(k), 2))))))));
				PDFrow.add(PDF);
			}
			PDFs.add(PDFrow);
		}
		return PDFs;
	}
	public static void naiveBayes(ArrayList<String[]> training, ArrayList<String[]> testing) {
		ArrayList<ArrayList<Double>> noTraining = new ArrayList<ArrayList<Double>>();
		ArrayList<ArrayList<Double>> yesTraining = new ArrayList<ArrayList<Double>>();
		ArrayList<ArrayList<Double>> testingDouble = new ArrayList<ArrayList<Double>>();
		for(int i=0;i<training.size();i++) {
			if(training.get(i)[training.get(i).length-1].equals("yes")){
				ArrayList<Double> buffer = new ArrayList<Double>();
				for (int j = 0; j < training.get(i).length-1; j++) {
					buffer.add(Double.parseDouble(training.get(i)[j]));
				}
				yesTraining.add(buffer);
				}
		}
		for(int i=0;i<training.size();i++) {
			if(training.get(i)[training.get(i).length-1].equals("no")){
				ArrayList<Double> buffer = new ArrayList<Double>();
				for (int j = 0; j < training.get(i).length-1; j++) {
					buffer.add(Double.parseDouble(training.get(i)[j]));
				}
				noTraining.add(buffer);
			}
		}
		for(int i=0;i<testing.size();i++) {
			ArrayList<Double> buffer = new ArrayList<Double>();
			for(int j=0;j<testing.get(0).length;j++) {
				buffer.add(Double.parseDouble(testing.get(i)[j]));
			}
			testingDouble.add(buffer);
		}
		ArrayList<Double> noMeans = calculateMeans(noTraining);
		//System.out.println(noMeans);
		ArrayList<Double> yesMeans = calculateMeans(yesTraining);
		ArrayList<Double> noSDs = calculateSDs(noTraining,noMeans);
		//System.out.println(noSDs);
		ArrayList<Double> yesSDs = calculateSDs(yesTraining,yesMeans);
		ArrayList<ArrayList<Double>> noPDFs = calculatePDFs(testingDouble,noMeans,noSDs);
		ArrayList<ArrayList<Double>> yesPDFs = calculatePDFs(testingDouble,yesMeans,yesSDs);
		//System.out.println(noPDFs.get(0));
		//System.out.println(yesPDFs.get(0));
		for(int t=0;t<yesPDFs.size();t++) {
			double yesValue = yesPDFs.get(t).get(0)*((double)yesTraining.size()/training.size());
			double noValue = noPDFs.get(t).get(0)*((double)noTraining.size()/training.size());
			//System.out.println((double)yesTraining.size()/training.size());
			//System.out.println((double)noTraining.size()/training.size());
			for(int u=1;u<yesPDFs.get(t).size();u++) {
				yesValue = yesValue * yesPDFs.get(t).get(u);
				noValue = noValue * noPDFs.get(t).get(u);
			}
			if(Double.compare(yesValue,noValue) >= 0 ) {
				//System.out.println(Double.compare(yesValue,noValue));
				System.out.println("yes");
			}
			else {
				System.out.println("no");
			}
		}
	}
	
	public static ArrayList<String[]> parseFile(BufferedReader br) {
		ArrayList<String[]> returnSet= new ArrayList<String[]>();
		try {
			String line;
			//line = br.readLine();
			while((line = br.readLine()) != null) {
				String[] newEntry = line.split(",");
				newEntry[newEntry.length-1] = newEntry[newEntry.length-1].substring(0, newEntry[newEntry.length-1].length());
				returnSet.add(newEntry);
				//System.out.println(newEntry.toString());
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return returnSet;
	}



}

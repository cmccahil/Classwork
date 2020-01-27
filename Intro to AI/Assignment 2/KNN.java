import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Scanner;

public class KNN {
	ArrayList<Entry> trainingEntries;
	

	public KNN(File trainingFile, File testingFile, int k) {
		trainingEntries = new ArrayList<>();
		run(trainingFile, testingFile, k);

	}

	public void run(File trainingFile, File testingFile, int k) {
		try {
			Scanner scanTrain = new Scanner(trainingFile);
			Scanner scanTest = new Scanner(testingFile);
			// add training data to list of entries
			while (scanTrain.hasNextLine()) {
				trainingEntries.add(new Entry(scanTrain.nextLine()));
			}
			while (scanTest.hasNextLine()) {
				Entry test = new Entry(scanTest.nextLine());
			//	System.out.print("test: ");
				//test.printEntry();
				ArrayList <Entry> bestNeighbours = new ArrayList <>();
				for (Entry e: trainingEntries) {
					e.distance = euclidianDistance(e, test);//find euclidian distance between training and testing entry
					//add to best neighbour list, if close to testing entry
					if (!bestNeighbours.isEmpty() && e.distance < bestNeighbours.get(bestNeighbours.size()-1).distance) {
						//Entry worstNearestNeighbour = bestNeighbours.remove(bestNeighbours.size()-1);//remove worst neighbour
						//insert entry e into the list
						for (int i = 0; i < bestNeighbours.size(); i++) {
							if (e.distance < bestNeighbours.get(i).distance) {
								bestNeighbours.remove(bestNeighbours.size()-1);
								bestNeighbours.add(i, e);
								//System.out.println("inside loop " + e.distance);
							//	e.printEntry();
								//System.out.println();
								break;
							}
						}
						
					} else if (bestNeighbours.isEmpty() || bestNeighbours.size() < k) {
					//empty best neighbours list or <k in best neighbours list, then add entry
						bestNeighbours.add(e);
					//	System.out.println("empty "+e.distance);
						//e.printEntry();
					}
				}
			//	System.out.println();
//				for (Entry bn: bestNeighbours) {
//					bn.printEntry();
//					System.out.println(bn.distance);
//				}
				int yes = 0;
				for (Entry bn: bestNeighbours) {
					if (bn.classVariable.equals("yes")) yes+=1;
				}
				if (yes >= (bestNeighbours.size()+1)/2) System.out.println("yes"); 
				else System.out.println("no");
			//	System.out.println();
			//	System.out.println();
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}

	// calculate euclidian distance between two entries
	public double euclidianDistance(Entry e1, Entry e2) {
		// TODO possible that differently sized entries?
		double dist = 0;
		for (int i = 0; i < e1.attributes.length - 1; i++) {
			double a = Double.parseDouble(e1.attributes[i]);
			double b = Double.parseDouble(e2.attributes[i]);
			dist += Math.pow(a - b, 2);
		}
		dist = Math.sqrt(dist);
		return dist;
	}
	
	
}

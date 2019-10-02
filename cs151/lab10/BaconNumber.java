import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.URL;
import java.util.ArrayList;
import java.util.Scanner;
/**
 * 
 * @author cmccahil
 *This class reads a data file and allows you to interactively query the System for the 
 *Bacon Number and path for any actor in the database. 
 */
public class BaconNumber {
    

    public static void main(String[] args) {
		// TODO Auto-generated method stub
	Scanner input;
	try {
	    input= new Scanner(new URL(args[0]).openStream());
	    Graph baconGraph=new Graph();
	    while(input.hasNextLine()) {
		String[] line=input.nextLine().split("\\|");
		String actor=line[0].toLowerCase();
		String movie=line[1].toLowerCase();
		if(baconGraph.vertices.containsKey(movie)) {
		    if(baconGraph.vertices.containsKey(actor)) {
			baconGraph.addEdge(movie, actor);
		    }
		    else {
			Vertex actorVertex=new Vertex(actor);
			actorVertex.markActor();
			baconGraph.addVertex(actorVertex);
			baconGraph.addEdge(movie, actor);
		    }
		}
		else if(baconGraph.vertices.containsKey(actor)) {
		    Vertex movieVertex=new Vertex(movie);
		    baconGraph.addVertex(movieVertex);
		    baconGraph.addEdge(movie, actor);
		}
		else {
		Vertex actorVertex=new Vertex(actor);
		actorVertex.markActor();
		baconGraph.addVertex(actorVertex);
		
		Vertex movieVertex=new Vertex(movie);
		baconGraph.addVertex(movieVertex);
		
		baconGraph.addEdge(movie, actor);
		}
	    }
	   
	   
	   baconGraph.setPath(baconGraph.center);
	   int counter=0;
	   while(counter<1) {
        	   System.out.print("Command (type \"quit\" to quit): ");
        	   Scanner command=new Scanner(System.in);
        	   String commandString=command.nextLine();
        	   if(commandString.length()<4) {
        	       System.out.println("invalid command");
        	   }
        	   else if(commandString.equals("quit")) {
        	       break;
        	   }
        	
        	   /**
        	    * this is the find command that finds the shortest path from the current
        	    * center to <name> 
        	    */
        	   else if(commandString.substring(0,4).equals("find")) {
        	       try {
        	       String parameter=commandString.substring(5, commandString.length()).toLowerCase();
        	       if(baconGraph.getVertex(parameter)==null) {
        		   System.out.println(parameter+" is unreachable or not in the database");
        	       }
        	       else {
        		   int baconNumber=baconGraph.getVertex(parameter).getDistance();
        		   System.out.println(baconNumber);
        		   System.out.println(baconGraph.getPath(parameter, "",baconNumber ));
        	   }
        	       }
        	       catch(StringIndexOutOfBoundsException e) {
        		   System.out.println("You didn't give a string");
        	       
        	       }
        	   }
        	   /**
        	    * prints a table of the counts of bacon numbers from 0 up to the longest
        	    */
        	   else if(commandString.equals("table")) {
        	       System.out.println("Table of distances for "+baconGraph.center);
        	       for(int i=0;i<baconGraph.tableOfDistances.length;i++) {
        		   if(baconGraph.tableOfDistances[i]!=0) {
        		       System.out.println("Number\t"+i+":\t"+baconGraph.tableOfDistances[i]);
        		   }
        		   
        	       }
        	       int unreachable=0;
        	       for(Vertex i:baconGraph.vertices.values()) {
        		   if(i.isActor()&&i.getReachable()==false) {
        		       unreachable++;
        		   }
        	       }
        	       System.out.println("Unreachable:\t"+unreachable);
        	   }
        	   /**
        	    * this calculates the average Bacon Number for the given center among
        	    * all connected nodes. 
        	    */
        	   else if(commandString.equals("avgdist")) {
        	       float average=0;
        	       int reachable=0;
        	       int unreachable=0;
        	       
        	       for(Vertex i:baconGraph.vertices.values()) {
        		   if(i.getReachable()&&i.isActor()) {
        		       reachable++;
        		       average=average+i.getDistance()/2;
        		   }
        		   else {
        		       if(i.isActor()) {
        		       unreachable++;
        		       }
        		   }
        	       }
        	       average=average/(reachable);
        	       baconGraph.getVertex(baconGraph.center).setAverage(average);
        	       
        	       System.out.println(String.format("%.17f",average)+"	"+baconGraph.center+" ("+reachable+","+unreachable+")");
        	   }
        	   
        	   /**
        	    * this is the recenter command that changes the center to the given 
        	    * name if it exists in the database.
        	    */
        	   
        	   else if(commandString.substring(0, 8).equals("recenter")) {
        	       try {
        	       String parameter=commandString.substring(9, commandString.length()).toLowerCase();
        	       if(baconGraph.getVertex(parameter)==null) {
        		   System.out.println(parameter+" is not inthe database");
        	       }
        	       else {
        		   baconGraph.recenter(parameter);
        		   baconGraph.resetPath();
        		   baconGraph.setPath(baconGraph.center);
        	       }
        	       }
        	       catch(StringIndexOutOfBoundsException e) {
        		   System.out.println("You didn't give a string");
        	       
        	       }
        	       
        	   }
        	   /**
        	    * for each actor in the current connected component, this calculates 
        	    * the average bacon distance to all actors in that component and then
        	    * prints a table of the n best centers. Wrote the function at bottom
        	    * because it is so long. 
        	    */
        	   else if(commandString.substring(0, 9).equals("topcenter")) {
        	       topcenter(baconGraph, commandString);
        	       	   
        	   }
        	   else {
        	       System.out.println("invalid command");
        	   }
        	   
	   }
	    
	    
	    
	    
	    
	} catch (FileNotFoundException e) {
	    System.out.println("Problem opening file: " + e.getMessage());
	    System.exit(1);
	} catch (IOException e) {
	    // TODO Auto-generated catch block
	    e.printStackTrace();
		}
	
		
	    }

    private static void topcenter(Graph baconGraph, String commandString) {
	ArrayList<Vertex> topcenterList=new ArrayList<Vertex>();
	   int parameter=Integer.parseInt(commandString.substring(10));
	   float average=0;
	   int reachable=0;
	   
	   for(Vertex i:baconGraph.vertices.values()) {
	   if(i.getReachable()&&i.isActor()) {
	       baconGraph.recenter(i.toString());
	       baconGraph.resetPath();
	       baconGraph.setPath(baconGraph.center);
	       for(Vertex j:baconGraph.vertices.values()) {
		   if(j.getReachable()&&j.isActor()) {
		   
		       reachable++;
		       average=average+j.getDistance()/2;
		   }
	       }
	   average=average/(reachable);
	   baconGraph.getVertex(baconGraph.center).setAverage(average);
	   topcenterList.add(i);
	   }
	   
	   average=0;
	   reachable=0;
	   }
	   for(int i=0;i<parameter;i++) {
	   float min=i;
	   for(int j=i+1;j<topcenterList.size();j++) {
	       if(topcenterList.get(j).getAverage()<topcenterList.get(i).getAverage()) {
		   Vertex temporary=topcenterList.get(i);
		   topcenterList.set(i, topcenterList.get(j));
		   topcenterList.set(j, temporary);
	       }
	       
	   }
	   
	   }
	   for(int i=0;i<parameter;i++) {
	   System.out.println(String.format("%.12f",topcenterList.get(i).getAverage())+" "+topcenterList.get(i).toString());
	   }
    }

	

    }



import java.util.ArrayList;

/**
 * this is the vertex class of the graph. The functions and variables are self explanatory
 * @author cmccahil
 *
 */
public class Vertex {
    private int distance;
    private float average;
    private String name;
    private ArrayList<Vertex> adjacentVertices;
    private ArrayList<Vertex> shortestPath;
    private Vertex previous;
    private String color;
    private boolean reachable;
    private boolean isActor=false;
    
    public void setAverage(float distance) {
	this.average=distance;
    }
    public float getAverage() {
	return average;
    }
    
    public void markActor() {
	isActor=true;
    }
    public boolean isActor() {
	return isActor;
    }
    
    public void markReachable() {
	this.reachable=true;
    }
    
    public void markUnReachable() {
	this.reachable=false;
    }
    
    public boolean getReachable() {
	return reachable;
    }
    
   
    public String getColor() {
	return color;
    }
    public void markGrey() {
	this.color="grey";
    }
  
    public void markYellow() {
	this.color="yellow";
    }
  
    public void markGreen() {
	this.color="green";
    }
    
    public Vertex getPrevious() {
        return previous;
    }

    public void setPrevious(Vertex previous) {
        this.previous = previous;
    }

    public int getDistance() {
        return distance;
    }

    public void setDistance(int distance) {
        this.distance = distance;
    }

    
    
    public Vertex(String name) {
	this.distance=1000;
	this.name=name;
	this.adjacentVertices=new ArrayList<Vertex>();
	this.markGrey();
	this.reachable=false;
	this.average=0;
    }
    
    public String toString() {
	return this.name;
	
    }
    
    public ArrayList<Vertex> adjacentVertices(){
	return this.adjacentVertices;
    }
    
    public void addAdjacentVertex(Vertex v) {
	this.adjacentVertices.add(v);
    }
    
}

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

/**
 * this is the graph class that does a lot of the heavy lifting. The functions are pretty
 * self explanatory. Set Path uses breadth first search. 
 * @author cmccahil
 *
 */

public class Graph {
   
    public HashMap<String,Vertex> vertices;
    public Queue<Vertex> queuePath;
    public String center;
    public int[] tableOfDistances;
    
    public Graph(){
	this.vertices=new HashMap<String,Vertex>();
	this.center="kevin bacon (i)";
    }
    
    public void recenter(String newCenter) {
	this.center=newCenter;
    }
    
    /**
     * 
     * @param v
     */
    public void addVertex(Vertex v) {
	vertices.put(v.toString(), v);
    }
    
    public Vertex getVertex(String name) {
	return vertices.get(name);
    }
    
    
    public void addEdge(String v1,String v2) {
	vertices.get(v1).addAdjacentVertex(vertices.get(v2));
	vertices.get(v2).addAdjacentVertex(vertices.get(v1));
    }
    public void resetPath() {
	for(Vertex k:vertices.values()) {
	    k.markGrey();
	    k.setDistance(1000);
	    k.markUnReachable();
	}
    }
    
    public void setPath(String name) {
	queuePath=new LinkedList<Vertex>();
	tableOfDistances=new int[11];
	Vertex v1=vertices.get(name);
	v1.setDistance(0);
	v1.markReachable();
	v1.markYellow();
	
	queuePath.offer(v1);
	
	
	if(v1.getDistance()/2==0 && v1.isActor()) {
		tableOfDistances[0]++;
	    }
	while(queuePath.isEmpty()==false) {
	    
	    Vertex v=queuePath.poll();
	    v.markGreen();
	    for(Vertex i:v.adjacentVertices()) {
		
		if(i.getColor().equals("grey")) {
		    i.setDistance(v.getDistance()+1);
		    i.markReachable();
		    i.markYellow();
		    queuePath.offer(i);
		    i.setPrevious(v);
		    if(i.isActor()) {
			tableOfDistances[i.getDistance()/2]++;
		    }
		}
	    }
	}
		    
    }
    public String getPath(String name,String output,int baconNumber) {
	if(name.equals(center)) {
	    output=output+center+" ("+baconNumber/2+")";
	    return output;
	}
	else {
	    output=output+name+" -> ";
	    Vertex currentVertex=vertices.get(name);
	    if(currentVertex.getPrevious()==null) {
		return name+" is unreachable";
	    }
	    return getPath(currentVertex.getPrevious().toString(),output,baconNumber);
	}
	
    }
}

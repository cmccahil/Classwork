/**
 * Load a tree from a text file.  Format is line based, with each line

 * consisting of a String for data, followed by two ints indicating if
 * the node has a left child or right child.  (1 is yes, 0 is no).
 * Ordering of nodes is postorder.
 *
 * @author John Donaldson
 * @author Benjamin Kuperman (Spring 2007)
 * @author Alexa Sharp (Fall 2012)
 */
/**
 * edited by Colin McCahill
 */
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;
import java.util.Stack;

public class TreeLoader {

    public BinaryTree<String> loadTreeFromFile(String fname) throws IOException
    {
        Stack<BinaryTree<String>> binarytreestack=new Stack<BinaryTree<String>>();
        Scanner input=null;
	try {
	    input=new Scanner(new File(fname));
	}
	catch(FileNotFoundException e) {
	    System.out.println("Problem opening file: " + e.getMessage());
	    System.exit(1);
	}
        while(input.hasNext()) {
            String data=input.next();
            Integer lefttag=input.nextInt();
            Integer righttag=input.nextInt();
            BinaryTree<String> right=new EmptyTree<String>();
            BinaryTree<String> left=new EmptyTree<String>();
            if (righttag==1) {
        	right=binarytreestack.pop();
            }
            if (lefttag==1) {
        	left=binarytreestack.pop();
            }
            
            BinaryTree<String> newtree=new ConsTree(data,left,right);
            binarytreestack.push(newtree);
        }
        if(binarytreestack.size()==1) {
            
        
        return binarytreestack.pop();
        }
        else {
        return new EmptyTree<String>();
        }
        }

    // So you can test your tree loader
    public static void main(String[] args) throws IOException {
        if(args.length!=1){
            System.out.println("Usage:  java TreeLoader filename");
        }
        else {
            TreeLoader tl = new TreeLoader();
            BinaryTree<String> t = tl.loadTreeFromFile(args[0]);
            System.out.println(t);
        }
    }
}

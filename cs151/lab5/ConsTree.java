/**
 * ConsTree
 * @author cmccahil
 *this file has the methods of the binary tree
 * @param <T>
 */
public class ConsTree<T> extends BinaryTree<T> {
    private T data;
    private BinaryTree<T> left;
    private BinaryTree<T> right;
    private int factor=0;
    private String traversal="";

    public ConsTree(T data, BinaryTree<T> left, BinaryTree<T> right) {
	this.data=data;
	this.left= left;
	this.right= right;
    }

    public ConsTree(T data) {
	this(data, new EmptyTree(), new EmptyTree());
    }
    public String toString( String indent ) {
	return right.toString( indent + "   " ) + "\n" + 
	       indent + "/\n" + 
	       indent + data + "\n" + 
	       indent + "\\" + 
	       left.toString( indent + "   ");
    }
    public String toString() {
	return toString("");
    }
    public boolean isEmpty() {
	return false;
    }
    public int height() {
	return 1+Math.max(left.height(), right.height());
    }
    public int nodeCount() {
	return 1+left.nodeCount()+right.nodeCount();
    }
    public int leafCount() {
	if (left.leafCount()==0 && right.leafCount()==0) {
	    return 1;
	}
	else {
	    return left.leafCount()+right.leafCount();
	}
    }
    public int levelCount(int level) {
	if (level==0) {
	    return 1;
	}
	else {
	    return left.levelCount(level-1)+right.levelCount(level-1);
	}
    }
    public BinaryTree<T> mirrorImage(){
	BinaryTree<T> mirrorTree=new ConsTree<T>(data,right.mirrorImage(),left.mirrorImage());
	return mirrorTree;
	
    }
    public int weightBalanceFactor() {
	factor=Math.abs(left.nodeCount()-right.nodeCount());
	return Math.max(factor,Math.max(left.weightBalanceFactor(), right.weightBalanceFactor()));
	
    }
    public int nodeSum() {
	return Integer.parseInt((String)data)+left.nodeSum()+right.nodeSum();
    }
    public void doubles() {
	data=(T)(Integer.toString(Integer.parseInt((String)data)*2));
	left.doubles();
	right.doubles();
    }
    public int maxPathSum() {
	if (left.isEmpty() && right.isEmpty()) {
	    return Integer.parseInt((String)data);
	}
	else {
	    return Math.max(right.maxPathSum()+Integer.parseInt((String)data), left.maxPathSum()+Integer.parseInt((String)data));
	}
	
	
	
    }
    public String preOrder() {
	traversal=traversal+((String)data);
	traversal=traversal+("\n");
	traversal=traversal+(left.preOrder());
	traversal=traversal+(right.preOrder());
	return traversal;
    }
    public String postOrder() {
	traversal=traversal+(left.postOrder());
	traversal=traversal+(right.postOrder());
	traversal=traversal+((String)data);
	traversal=traversal+("\n");
	return traversal;
    }
    public String inOrder() {
	traversal=traversal+(left.inOrder());
	traversal=traversal+((String)data);
	traversal=traversal+("\n");
	traversal=traversal+(right.inOrder());
	return traversal;
    }
    
}

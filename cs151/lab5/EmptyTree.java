
public class EmptyTree<T> extends BinaryTree<T>{
    public EmptyTree( ) {
	
    }
    public String toString( String indent ) {
	return "";
    }
    public String toString() {
	return toString("");
    }
    public boolean isEmpty() {
	return true;
    }
    public int height() {
	return -1;
    }
    public int nodeCount() {
	return 0;
    }
    public int leafCount() {
	return 0;
    }
    public int levelCount(int level) {
	return 0;
    }
    public BinaryTree<T> mirrorImage(){
	return new EmptyTree<T>();
    }
    public int weightBalanceFactor() {
	return 0;
    }
    public int nodeSum() {
	return 0;
    }
    public void doubles() {
	
    }
    public int maxPathSum() {
	return 0;
    }
    public String preOrder() {
	return "";
    }
    public String postOrder() {
	return "";
    }
    public String inOrder() {
	return "";
    }
}

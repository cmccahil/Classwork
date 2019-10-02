/**
 * TODO - add some comments!
 *
 * @author TODO - Your name here
 * @author John Donaldson
 * @author Benjamin Kuperman (Spring 2007, 2008)
 */

// TODO: See Part 2

public class TreeMethods {

    public TreeMethods() {
    }

    public int nodeCount(BinaryTree<String> tree) {
        return tree.nodeCount();
    }

    public int height(BinaryTree<String> tree) {
        return tree.height();
    }

    public int levelCount(BinaryTree<String> tree, int level) {
        return tree.levelCount(level);
    }

    public int weightBalanceFactor(BinaryTree<String> tree) {
        return tree.weightBalanceFactor();
    }

    public int leafCount(BinaryTree<String> tree) {
        return tree.leafCount();
    }

    public BinaryTree<String> mirrorImage(BinaryTree<String> tree) {
        return tree.mirrorImage();
    }

    public int nodeSum(BinaryTree<String> tree) {
        return tree.nodeSum();
    }

    public int maxPathSum(BinaryTree<String> tree) {
        return tree.maxPathSum();
    }

    public void doubles(BinaryTree<String> tree) {
	tree.doubles();
    }

    // Traversals
    public String preOrder(BinaryTree<String> tree) {
        // TODO
        return tree.preOrder();
    }
    public String postOrder(BinaryTree<String> tree) {
        // TODO
        return tree.postOrder();
    }
    public String inOrder(BinaryTree<String> tree) {
        // TODO
        return tree.inOrder();
    }
}

/**
 * The driver class for our TreeMethodFrame GUI.  Contains initialization
 * functions and the main method for users to run.
 *
 * @author John Donaldson
 * @author Benjamin Kuperman (Spring 2007)
 * @author Alexa Sharp (Fall 2012)
 */

import java.awt.*;
import java.awt.event.*;

public class TreeMethodApplication {
    boolean packFrame = false;
    private TreeLoader treeLoader = new TreeLoader();
    private BinaryTree<String> tree = new EmptyTree<String>();
    private TreeMethods treeMethods = new TreeMethods();

    //Construct the application
    public TreeMethodApplication() {
        final TreeMethodFrame frame = new TreeMethodFrame();
        //Validate frames that have preset sizes
        //Pack frames that have useful preferred size info, e.g. from their layout
        if (packFrame) {
            frame.pack();
        }
        else {
            frame.validate();
        }

        //Center the window
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        Dimension frameSize = frame.getSize();
        if (frameSize.height > screenSize.height) {
            frameSize.height = screenSize.height;
        }
        if (frameSize.width > screenSize.width) {
            frameSize.width = screenSize.width;
        }
        frame.setLocation((screenSize.width - frameSize.width) / 2,
                (screenSize.height - frameSize.height) / 2);
        frame.setVisible(true);

        // -- Initialize the ActionListener for buttons ---------------------

        // Load File
        frame.addButtonListener(0, new ActionListener(){
            public void actionPerformed(ActionEvent e) {
                frame.fd.setVisible(true);
                String filename = frame.fd.getFile();
                String dirname = frame.fd.getDirectory();
                if(filename!=null && dirname!=null){
                    try {
                        tree = treeLoader.loadTreeFromFile(dirname + filename);
                        frame.setOutputArea("");
                    }
                    catch (Exception ex1){
                        frame.setOutputArea(ex1.toString());
                        tree = new EmptyTree<String>();
                    }
                    frame.setTreeDisplayArea(tree.toString());
                }
            }
        });

        // Count Nodes
        frame.addButtonListener(1, new ActionListener(){
            public void actionPerformed(ActionEvent e){
                frame.setOutputArea("Node Count: "+treeMethods.nodeCount(tree));
            }
        });

        // Height
        frame.addButtonListener(2, new ActionListener(){
            public void actionPerformed(ActionEvent e){
                frame.setOutputArea("Height: "+treeMethods.height(tree));
            }
        });

        // Mirror
        frame.addButtonListener(3, new ActionListener(){
            public void actionPerformed(ActionEvent e){
                frame.setOutputArea(""+treeMethods.mirrorImage(tree).toString());
            }
        });

        // Count Leaves
        frame.addButtonListener(4, new ActionListener(){
            public void actionPerformed(ActionEvent e){
                int leafct = treeMethods.leafCount(tree);
                if(leafct==1)
            frame.setOutputArea("The tree has 1 leaf");
                else
            frame.setOutputArea("The tree has "+treeMethods.leafCount(tree)+" leaves");
            }
        });

        // Level Count
        frame.addButtonListener(5, new ActionListener(){
            public void actionPerformed(ActionEvent e){
                int level=0;
                String output="";
                int lcount=treeMethods.levelCount(tree,level);
                if(lcount==0)
            output+="The tree is empty";
                else
            while(lcount>0 && level<=1000){
                if(lcount==1)
            output+=("There is 1 node at level "+level+"\n");
                else
            output+=("There are "+lcount+" nodes at level "+level+"\n");
        ++level;
        lcount=treeMethods.levelCount(tree,level);
            }
        frame.setOutputArea(output);
            }
        });


        // Weight Balance Factor
        frame.addButtonListener(6, new ActionListener(){
            public void actionPerformed(ActionEvent e){
                frame.setOutputArea("Weight balance factor:" 
                                       + treeMethods.weightBalanceFactor(tree));
            }
        });


        // Node Sum
        frame.addButtonListener(7, new ActionListener(){
            public void actionPerformed(ActionEvent e){
                try{
                    frame.setOutputArea("Sum of data values: "+treeMethods.nodeSum(tree));
                }
                catch (ClassCastException ex1){
                    frame.setOutputArea("Tree contains non-integer data");
                }
                catch (NumberFormatException ex2){
                    frame.setOutputArea("Tree contains non-integer data");
                }
                catch (Exception ex){
                    frame.setOutputArea(ex.toString());
                }
            }
        });

        // Double
        frame.addButtonListener(8, new ActionListener(){
            public void actionPerformed(ActionEvent e){
                try{
                    treeMethods.doubles(tree);
                    frame.setTreeDisplayArea(tree.toString());
                    frame.setOutputArea("");
                }
                catch (ClassCastException ex){
                    frame.setOutputArea("Tree contains non-integer data");
                }
                catch (NumberFormatException ex2){
                    frame.setOutputArea("Tree contains non-integer data");
                }
                catch (Exception ex){
                    frame.setOutputArea(ex.toString());
                }
            }
        });

        // Max Path Sum
        frame.addButtonListener(9, new ActionListener(){
            public void actionPerformed(ActionEvent e){
                try{
                    frame.setOutputArea("Maximum path sum: "+treeMethods.maxPathSum(tree));
                }
                catch (ClassCastException ex){
                    frame.setOutputArea("Tree contains non-integer data");
                }
                catch (NumberFormatException ex2){
                    frame.setOutputArea("Tree contains non-integer data");
                }
                catch (Exception ex){
                    frame.setOutputArea(ex.toString());
                }
            }
        });
        
        // Pre-order
        frame.addButtonListener(10, new ActionListener(){
            public void actionPerformed(ActionEvent e){
                frame.setOutputArea(""+treeMethods.preOrder(tree));
            }
        });
        // In-order
        frame.addButtonListener(11, new ActionListener(){
            public void actionPerformed(ActionEvent e){
                frame.setOutputArea(""+treeMethods.inOrder(tree));
            }
        });
        // Post-order
        frame.addButtonListener(12, new ActionListener(){
            public void actionPerformed(ActionEvent e){
                frame.setOutputArea(""+treeMethods.postOrder(tree));
            }
        });
        
        // Quit
        frame.addButtonListener(10+3, new ActionListener() {
            public void actionPerformed(ActionEvent e){
                System.exit(1);
            }
        });

    }

    //Main method
    public static void main(String[] args) {
        new TreeMethodApplication();
    }
}

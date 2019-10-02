/**
 * The main frame for our tree GUI.
 *
 * @author John Donaldson
 * @author Benjamin Kuperman (Spring 2007)
 */

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class TreeMethodFrame extends JFrame {

	private static final long serialVersionUID = 1L;

	final static String[] buttonLabels = {"Load File",
        "Count Nodes","Height", "Mirror", "Count Leaves", "Level Counts",
        "Weight Balance Factor","Node Sum", "Double", "Max Path Sum", 
        "Pre-order", "In-order", "Post-order", "Quit"
	};

    int nbuttons = 14;
    JButton[] button = new JButton[nbuttons];
    JTextArea treeDisplayArea = new JTextArea();
    JTextArea outputArea = new JTextArea();
    FileDialog fd = new FileDialog(this);

    //Construct the frame
    public TreeMethodFrame() {
        try {
            init();
        }
        catch(Exception e) {
            e.printStackTrace();
        }
    }

    //Component initialization
    private void init() throws Exception  {

        // Some temp vars to handle the sub-panels
        JPanel jPanel1 = new JPanel();
        JPanel jPanel2 = new JPanel();

        // Basic properties for the window
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setDefaultLookAndFeelDecorated(true);
        this.setSize(new Dimension(700, 500));
        this.setTitle("Tree Methods");

        // Set up the overall window space
        JPanel contentPane = (JPanel) this.getContentPane();
        contentPane.setLayout(new BorderLayout());
        contentPane.setPreferredSize(new Dimension(1200, 280));
        contentPane.add(jPanel1, BorderLayout.CENTER);
        contentPane.add(jPanel2, BorderLayout.SOUTH);

        // Set up the top window for displaying trees
        GridLayout gridLayout1 = new GridLayout();
        gridLayout1.setColumns(2);
        gridLayout1.setHgap(6);

        jPanel1.setLayout(gridLayout1);
        jPanel1.add(new JScrollPane(treeDisplayArea), null);
        jPanel1.add(new JScrollPane(outputArea), null);

        Font monospace = new Font("Monospaced", Font.PLAIN, 14);
        treeDisplayArea.setBorder(BorderFactory.createLoweredBevelBorder());
        //treeDisplayArea.setPreferredSize(new Dimension(140, 200));
        treeDisplayArea.setEditable(false);
        treeDisplayArea.setFont(monospace);

        outputArea.setBorder(BorderFactory.createLoweredBevelBorder());
        //outputArea.setPreferredSize(new Dimension(140, 200));
        outputArea.setEditable(false);
        outputArea.setLineWrap(true);
        outputArea.setFont(monospace);

        // Set up the button bar
        jPanel2.setLayout(new FlowLayout());
        jPanel2.setPreferredSize(new Dimension(1055, 120));

        for(int i=0; i<nbuttons; i++){
            button[i] = new JButton(buttonLabels[i]);
            jPanel2.add(button[i]);
        }
        button[nbuttons-1].setBackground(Color.RED);
        button[nbuttons-1].setForeground(Color.blue);
    }

    void addButtonListener(int buttonIndex, ActionListener listener){
        button[buttonIndex].addActionListener(listener);
    }

    void setOutputArea(String text){
        outputArea.setText(text);
    }

    void setTreeDisplayArea(String text){
        treeDisplayArea.setText(text);
    }
}

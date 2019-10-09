// MyXfloat.java
// skeleton version of MyXfloat

public class MyXfloat extends Xfloat {

    /* constructors
       All of the constructors defined here call the corresponding
       constructors in the Xfloat superclass.  You don't need to 
       change anything here.
    */
  public MyXfloat(){super();}
  public MyXfloat(float f){super(f);}
  public MyXfloat(byte sign, byte exp, int man){super(sign, exp, man);}

    /* skeleton version of xadd; returns 0 */
  public Xfloat xadd(Xfloat y) {return new MyXfloat((byte)0,(byte)0,0);}

    /* skeleton version of xmult; returns 0 */
  public Xfloat xmult(Xfloat y) {return new MyXfloat((byte)0,(byte)0,0);}

    /* main method */
  public static void main(String arg[]) {
    if (arg.length < 2) return;

    /* get x and y from the command line */
    float x = Float.valueOf(arg[0]).floatValue(),
          y = Float.valueOf(arg[1]).floatValue();
    Xfloat xf, yf, zf, wf;

    /* convert x and y to MyXfloat format */
    xf = new MyXfloat(x);
    yf = new MyXfloat(y);

    /* compute z = x*y and w = x+y */
    zf = xf.xmult(yf);
    wf = xf.xadd(yf);

    /* print x, y, z, and w */
    System.out.println("x:   "+xf+" "+x);
    System.out.println("y:   "+yf+" "+y);
    System.out.println("x*y: "+zf+" "+zf.toFloat());
    System.out.println("x+y: "+wf+" "+wf.toFloat());
  }
}

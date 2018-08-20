package Y12R5P1.bbbb;

import java.io.File;
import java.io.FileWriter;
import java.util.Scanner;


public class Die {
  public static void main(String[]args) throws Exception {
    File f = new File(args[0]);
    File f2 = new File(f.getParentFile(),f.getName()+".out");
    Scanner s = new Scanner(f);
    int T = s.nextInt();
    for (int t = 1; t <= T; t++) {
      int N = s.nextInt();
      int[] len = new int[N];
      int[] prob = new int[N];
      for (int i=0;i<N; i++) {
        len[i] = s.nextInt();
      }
      for (int i=0;i<N; i++) {
        prob[i] = s.nextInt();
      }
      println(f2,"Case #"+t+": "+solve(len,prob));
    }
    s.close();
  }

  private static String solve(int[] len, int[] prob) {
    int sol [] = new int[len.length];
    for (int i=0; i<sol.length; i++) {
      sol[i] = i;
    }

    for (int a=0; a<sol.length; a++)
      for (int b=a+1;b<sol.length; b++) {
        if (prob[b]>prob[a]) {
          swap(len,a,b);
          swap(prob,a,b);
          swap(sol,a,b);
        } else if (prob[b]<prob[a]) {
          continue;
        } else {
          //probs same
          continue;
        }
      }
    boolean swapped;
    do {
      swapped = false;
      for (int a=0;a<sol.length-1;a++) {
        if (prob[a]==prob[a+1]) {
          if (sol[a+1]<sol[a]) {
            swap(sol,a,a+1);
            swapped = true;
          }
        }
      }
    } while (swapped);
    return tostr(sol);
  }

  private static void swap(int[] sol, int a, int b) {
    int t = sol[a];
    sol[a] = sol[b];
    sol[b] = t;
  }

  private static String tostr(int[] sol) {
    String ret = "";
    for (int i=0;i<sol.length;i++) {
      if (i>0)ret+=" ";
      ret+=sol[i];
    }
    return ret;
  }

  static void println(File f, String s) throws Exception {
    FileWriter w = new FileWriter(f,true);
    w.write(s+"\n");
    w.close();
    System.out.println(s);
  }
}

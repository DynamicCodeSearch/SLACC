package Y11R5P1.KOTEHOK;

import java.util.*;
import java.io.*;

public class x {
  public static void main (String args []) throws Exception {
    Scanner in = new Scanner (System.in);
    int t = in.nextInt ();
    for (int tt = 1; tt <= t; tt++) {
      int w = in.nextInt ();
      int l = in.nextInt ();
      int u = in.nextInt ();
      int g = in.nextInt ();

      int [] x1 = new int[l], y1 = new int [l], x2 = new int [u], y2 = new int [u];


      for (int i = 0; i < l; i++) {
        x1[i] = in.nextInt ();
        y1[i] = in.nextInt ();
      }

      for (int i = 0; i < u; i++) {
        x2[i] = in.nextInt ();
        y2[i] = in.nextInt ();
      }

      double area = 0;

      for (int i = 0; i < l - 1; i++) {
        area += x1[i] * y1[i + 1] - x1[i + 1] * y1[i];
      }
      area += x1[l - 1] * y2[u - 1] - x2[u - 1] * y1[l - 1];
      for (int i = u - 1; i >= 1; i--) {
        area += x2[i] * y2[i - 1] - x2[i - 1] * y2[i];
      }
      area += x2[0] * y1[0] - x1[0] * y2[0];

      area = Math.abs (area) / g;

      int p1 = 0, p2 = 0;

      double cx = 0;

      System.out.println ("Case #" + tt + ":");

      for (int i = 0; i < g - 1; i++) {
        double ca = area;

        while (ca > 1e-9) {
          //System.out.println (p1 + " " + p2 + " " + ca);

          double nx = Math.min (x1[p1 + 1], x2[p2 + 1]);

          double a1 = y1[p1 + 1] - y1[p1];
          double b1 = x1[p1] - x1[p1 + 1];
          double c1 = a1 * x1[p1] + b1 * y1[p1];
          
          double a2 = y2[p2 + 1] - y2[p2];
          double b2 = x2[p2] - x2[p2 + 1];
          double c2 = a2 * x2[p2] + b2 * y2[p2];


          //System.out.println (a1 + " " + b1 + " " + c1 + " " + a2 + " " + b2 + " " + c2);


          for (int j = 0; j < 100; j++) {
            double cy1, cy2, my1, my2, mx = (nx + cx) * 0.5;
            cy1 = (c1 - a1 * cx) / b1;
            my1 = (c1 - a1 * mx) / b1;
            cy2 = (c2 - a2 * cx) / b2;
            my2 = (c2 - a2 * mx) / b2;

            double la = (cy2 - cy1 + my2 - my1) * (mx - cx);
            //System.out.println (" --> " + la + " " + cx + " " + mx  + " " + cy1 + " " + cy2 + " " + my1 + " " + my2);
            if (la < ca) {
              cx = mx;
              ca -= la;
            } else {
              nx = mx;
            }
          }

          if (ca > 1e-9) {
            if (x1[p1 + 1] < x2[p2 + 1]) ++p1;
            else
            if (x1[p1 + 1] > x2[p2 + 1]) ++p2;
            else {
              ++p1;
              ++p2;
            }
          }
        }
        System.out.println (cx);
      }
    }
  }
}
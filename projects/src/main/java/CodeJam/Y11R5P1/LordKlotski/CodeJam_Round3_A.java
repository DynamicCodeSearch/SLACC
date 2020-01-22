package CodeJam.Y11R5P1.LordKlotski;

import java.util.ArrayList;
import java.util.Scanner;

/************************
 *                      *
 *    Lord Klotski      *
 *                      *
 ***********************/
public class CodeJam_Round3_A {

    static double[][] lower;

    static double[][] upper;

    public static double area(line a, line b) {
        double X1 = a.x1 - a.x2;
        double Y1 = a.y1 - a.y2;
        double X2 = b.x1 - b.x2;
        double Y2 = b.y1 - b.y2;
        return (X1 * Y2 - X2 * Y1) / 2.0;
    }

    public static double evalArea(double cut) {
        ArrayList poly = new ArrayList();
        // find specials:
        line lsp = new line(0, 0, 0, 0);
        line usp = new line(0, 0, 0, 0);
        int hax1 = -1;
        int hax2 = -1;
        for (int i = 0; i < lower.length - 1; i++) {
            if (lower[i][0] < cut && lower[i + 1][0] > cut) {
                lsp.x1 = lower[i][0];
                lsp.x2 = cut;
                lsp.y1 = lower[i][1];
                double f = (cut - lsp.x1) / (lower[i + 1][0] - lsp.x1);
                lsp.y2 = f * lower[i + 1][1] + (1 - f) * lower[i][1];
                hax1 = i;
            }
        }
        for (int i = 0; i < upper.length - 1; i++) {
            if (upper[i][0] < cut && upper[i + 1][0] > cut) {
                usp.x2 = upper[i][0];
                usp.x1 = cut;
                usp.y2 = upper[i][1];
                double f = (cut - upper[i][0]) / (upper[i + 1][0] - upper[i][0]);
                usp.y1 = f * upper[i + 1][1] + (1 - f) * upper[i][1];
                hax2 = i;
            }
        }
        for (int i = 0; i <= hax1; i++) poly.add(new Pnt(lower[i][0], lower[i][1]));
        poly.add(new Pnt(cut, lsp.y2));
        poly.add(new Pnt(cut, usp.y1));
        for (int i = hax2; i >= 0; i--) poly.add(new Pnt(upper[i][0], upper[i][1]));
        double area = 0;
        for (int i = 1; i < poly.size() - 1; i++) {
            Pnt O = (Pnt) poly.get(0);
            Pnt T = (Pnt) poly.get(i);
            Pnt R = (Pnt) poly.get(i + 1);
            //System.out.println(T.x + " " + T.y + " " + rUtils.x + " " + rUtils.y);
            line a = new line(O.x, T.x, O.y, T.y);
            line b = new line(O.x, R.x, O.y, R.y);
            area += area(a, b);
        }
        return Math.abs(area);
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int T = input.nextInt();
        for (int t = 1; t <= T; t++) {
            int W = input.nextInt();
            int L = input.nextInt();
            int U = input.nextInt();
            int G = input.nextInt();
            lower = new double[L][2];
            for (int i = 0; i < L; i++) {
                lower[i][0] = input.nextDouble();
                lower[i][1] = input.nextDouble();
            }
            upper = new double[U][2];
            for (int i = 0; i < U; i++) {
                upper[i][0] = input.nextDouble();
                upper[i][1] = input.nextDouble();
            }
            double g = G;
            double[] cuts = new double[G - 1];
            double firstArea = evalArea(W - 0.00000001);
            //System.out.println(firstArea);
            for (int i = 0; i < cuts.length; i++) {
                double cutArea = (i + 1) / g * firstArea;
                double min = 0.0;
                double max = W + 0.00000001337;
                double mid = 0;
                while (max - min > 0.000000001) {
                    mid = (min + max) / 2.0;
                    double a = evalArea(mid);
                    //System.out.printf("%.1f %.2f %.5f\n" , mid, cutArea, a);
                    if (a > cutArea)
                        max = mid;
                    else
                        min = mid;
                }
                cuts[i] = mid;
            }
            System.out.println("Case #" + t + ":");
            for (int i = 0; i < cuts.length; i++) System.out.println(cuts[i]);
        }
    }
}

class line {

    double x1, x2, y1, y2;

    public line(double a, double b, double c, double d) {
        x1 = a;
        x2 = b;
        y1 = c;
        y2 = d;
    }
}

class Pnt {

    double x, y;

    public Pnt(double a, double b) {
        x = a;
        y = b;
    }
}

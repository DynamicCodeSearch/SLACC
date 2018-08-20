package Y11R5P1.EricStansifer;

import java.io.*;
import java.math.*;
import java.util.*;
import java.text.*;

public class a {
    public static void main(String[] args) {
        Scanner sc = new Scanner(new BufferedInputStream(System.in));

        int T = sc.nextInt();

        for (int casenumber = 1; casenumber <= T; ++casenumber) {
            int w = sc.nextInt();
            int l = sc.nextInt();
            int u = sc.nextInt();
            int g = sc.nextInt();

            int[] xl = new int[l];
            int[] yl = new int[l];
            int[] xu = new int[u];
            int[] yu = new int[u];

            for (int i = 0; i < l; ++i) {
                xl[i] = sc.nextInt();
                yl[i] = sc.nextInt();
            }

            for (int i = 0; i < u; ++i) {
                xu[i] = sc.nextInt();
                yu[i] = sc.nextInt();
            }

            int[] xs = new int[l + u];
            for (int i = 0; i < l; ++i)
                xs[i] = xl[i];
            for (int i = 0; i < u; ++i)
                xs[l + i] = xu[i];
            Arrays.sort(xs);


            int[] areal = new int[l];
            int[] areau = new int[u];

            for (int i = 1; i < l; ++i) {
                areal[i] = areal[i - 1] + (xl[i] - xl[i - 1]) * (yl[i] + yl[i - 1]);
                // System.out.format("  %d%n", areal[i]);
            }

            for (int i = 1; i < u; ++i) {
                areau[i] = areau[i - 1] + (xu[i] - xu[i - 1]) * (yu[i] + yu[i - 1]);
                // System.out.format("  %d%n", areau[i]);
            }

            double[] ss = new double[l + u];
            double[] widths = new double[l + u];

            double[] areas = new double[l + u];
            for (int i = 0; i < l + u; ++i) {
                int il =0;
                int iu =0;
                while (il < l && xl[il] <= xs[i]) ++il;
                --il;
                while (iu < u && xu[iu] <= xs[i]) ++iu;
                --iu;

                // System.out.format("     %d (%d) %d (%d)%n", il, xl[il], iu, xu[iu]);

                double a = 0;
                if (xu[iu] == xs[i]) {
                    a += areau[iu];
                } else {
                    double lambda = (xs[i] - xu[iu]) / ((double) (xu[iu + 1] - xu[iu]));
                    a += areau[iu] + (xs[i] - xu[iu]) * (2 * yu[iu] + lambda * (yu[iu + 1] - yu[iu]));
                }
                // System.out.format("   %.6f%n", a);
                if (xl[il] == xs[i]) {
                    a -= areal[il];
                } else {
                    double lambda = (xs[i] - xl[il]) / ((double) (xl[il + 1] - xl[il]));
                    a -= areal[il] + (xs[i] - xl[il]) * (2 * yl[il] + lambda * (yl[il + 1] - yl[il]));
                }

                areas[i] = a;
                // System.out.format("      %d: %.6f%n", xs[i], areas[i]);

                if (xl[il] < xl[l - 1]) {
                    ss[i] = (yu[iu + 1] - yu[iu]) / ((double) (xu[iu + 1] - xu[iu]))
                        - (yl[il + 1] - yl[il]) / ((double) (xl[il + 1] - xl[il]));
                    widths[i] = yu[iu] + (yu[iu + 1] - yu[iu]) * (xs[i] - xu[iu]) / ((double) (xu[iu + 1] - xu[iu]));
                    widths[i] -= yl[il] + (yl[il + 1] - yl[il]) * (xs[i] - xl[il]) / ((double) (xl[il + 1] - xl[il]));
                }
            }

            System.out.format("Case #%d:%n", casenumber);

            double area = areau[u - 1] - areal[l - 1];

            for (int i = 1; i < g; ++i) {
                double na = (area * i) / g;
                int j = 0;
                while (j < l + u && areas[j] <= na) ++j;
                --j;

                double ans;
                if (Math.abs(na - areas[j]) < 0.000000001) {
                    ans = xs[j];
                } else if (Math.abs(ss[j]) < 0.000000001) {
                    ans = xs[j] + (na - areas[j]) / (2.0 * widths[j]);
                } else {
                    ans = xs[j] + (-widths[j] + Math.sqrt(widths[j] * widths[j] + (na - areas[j]) * ss[j])) / (ss[j]);
                }
                System.out.format("%.6f%n", ans);
            }
        }
    }
}

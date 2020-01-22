package CodeJam.Y12R5P1.akevi;

import java.io.BufferedReader;
import java.util.Scanner;

import static java.lang.Double.parseDouble;
import static java.lang.System.in;
import static java.lang.System.out;

public class QA {

    public String[] parts(BufferedReader br) throws Exception {
        String line = br.readLine();
        if (line == null)
            return null;
        return line.trim().split("\\s+");
    }

    static boolean nextp(int v[], int n) {
        int i = n - 1;
        while (i > 0 && v[i] <= v[i - 1]) i--;
        boolean succ = i > 0;
        int j = i--;
        if (succ) {
            while (j + 1 < n && v[j + 1] > v[i]) j++;
            int t = v[i];
            v[i] = v[j];
            v[j] = t;
        }
        while (++i < --n) {
            int t = v[i];
            v[i] = v[n];
            v[n] = t;
        }
        return succ;
    }

    public static void main(String args[]) throws Exception {
        //BufferedReader br = new BufferedReader(new InputStreamReader(in));
        Scanner sc = new Scanner(in);
        int z = sc.nextInt();
        double p[] = new double[11111];
        double l[] = new double[11111];
        int v[] = new int[11111];
        double eps = 1e-13;
        for (int cas = 1; cas <= z; cas++) {
            out.print("Case #" + cas + ":");
            //
            int n = sc.nextInt();
            for (int i = 0; i < n; i++) l[i] = parseDouble(sc.next());
            for (int i = 0; i < n; i++) p[i] = parseDouble(sc.next()) * .01;
            //if (n > 11) continue;
            int o = 0;
            for (int c = 0; c < n; c++) {
                int j = 0;
                double best = 1e200;
                double lsum = 0, rsum = 0;
                double psum = 0;
                double m = 0;
                double q = 1;
                for (int i = 0; i < o; i++) {
                    m += l[v[i]];
                    psum += p[v[i]] * q;
                    rsum += p[v[i]] * q * m;
                    q *= 1 - p[v[i]];
                }
                m = 0;
                q = 1;
                for (int k = 0; k <= o; k++) {
                    double ans = lsum + rsum * (1 - p[c]) + psum * (1 - p[c]) * l[c] + p[c] * (m + l[c]) * q;
                    /*for (int u = 0; u < k; u++) {
						out.print(" " + v[u]);
					}
					out.print(" (" + c + ")");
					for (int u = k; u < o; u++) {
						out.print(" " + v[u]);
					}
					out.println(": " + ans);*/
                    if (best >= ans - eps) {
                        best = ans;
                        j = k;
                    }
                    if (k == o)
                        break;
                    m += l[v[k]];
                    psum -= p[v[k]] * q;
                    double s = p[v[k]] * q * m;
                    lsum += s;
                    rsum -= s;
                    q *= 1 - p[v[k]];
                }
                for (int i = o; i >= j; i--) {
                    v[i + 1] = v[i];
                }
                v[j] = c;
                o++;
            //out.println();
            }
            for (int i = 0; i < o; i++) {
                out.print(" " + v[i]);
            }
            out.println();
        }
    }
}

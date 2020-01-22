package CodeJam.Y14R5P1.je;

import java.io.BufferedReader;
import java.io.InputStreamReader;

import static java.lang.Integer.parseInt;
import static java.lang.Math.max;
import static java.lang.System.in;
import static java.lang.System.out;

public class A {

    public static String[] parts(BufferedReader br) throws Exception {
        String line = br.readLine();
        if (line == null)
            return null;
        return line.trim().split("\\s+");
    }

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(in));
        int cas = parseInt(br.readLine());
        for (int z = 1; z <= cas; z++) {
            String[] ss = parts(br);
            int N = parseInt(ss[0]);
            long p = parseInt(ss[1]);
            long q = parseInt(ss[2]);
            long r = parseInt(ss[3]);
            long s = parseInt(ss[4]);
            long[] arr = new long[N];
            Long[] cum = new Long[N];
            long tot = 0;
            for (int i = 0; i < N; i++) {
                arr[i] = ((i * p + q) % r) + s;
                if (i > 0)
                    cum[i] = cum[i - 1] + arr[i];
                else
                    cum[i] = arr[i];
                tot += arr[i];
            }
            long L = 0;
            long R = tot + 1;
            while (L + 1 < R) {
                long M = (L + R) >> 1;
                // out.println(L+" "+rUtils+" "+M+" "+ok(M,cum));
                if (ok(M, cum)) {
                    R = M;
                } else {
                    L = M;
                }
            }
            // out.println(rUtils+" "+tot);
            double ans = (tot - R) * 1.0 / tot;
            out.println("Case #" + z + ": " + ans);
        }
    }

    static long getSum(Long[] cum, int a, int b) {
        if (b < a)
            return 0;
        if (a == 0)
            return cum[b];
        else {
            return cum[b] - cum[a - 1];
        }
    }

    static boolean ok(Long M, Long[] cum) {
        for (int a = 0, b = 0; a < cum.length; a++) {
            while (b < cum.length && getSum(cum, a, b) <= M) b++;
            if (b == a)
                return false;
            b--;
            if (max(getSum(cum, 0, a - 1), getSum(cum, b + 1, cum.length - 1)) <= M)
                return true;
        }
        return false;
    }

    static long INF = 1L << 60;
}

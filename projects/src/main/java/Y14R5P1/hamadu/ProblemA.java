package Y14R5P1.hamadu;

import java.io.PrintWriter;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;


public class ProblemA {
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		PrintWriter out = new PrintWriter(System.out);
		
		int T = in.nextInt();
		for (int cn = 1 ; cn <= T ; cn++) {
			int N = in.nextInt();
			long p = in.nextInt();
			long q = in.nextInt();
			long r = in.nextInt();
			long s = in.nextInt();
			long[] d = new long[N];
			for (int i = 0 ; i < N ; i++) {
				d[i] = (p * i + q) % r + s;
			}
			out.println(String.format("Case #%d: %.11f", cn, solve(d)));
		}
		out.flush();
	}
	
	private static double solve(long[] d) {
		int n = d.length;
		long[] imos = new long[n+1];
		for (int i = 0 ; i < n ; i++) {
			imos[i+1] = imos[i] + d[i];
		}
		long best = 0;
		for (int h = 0 ; h < n ; h++) {
			int min = h;
			int max = n-1;
			for (int cur = 0 ; cur < 40 ; cur++) {
				int med1 = (min * 2 + max) / 3;
				int med2 = (min + max * 2) / 3;
				long v1 = take(imos, h, med1);
				long v2 = take(imos, h, med2);
				if (v1 < v2) {
					min = med1;
				} else {
					max = med2;
				}
			}
			for (int c = min-2 ; c <= max+2 ; c++) {
				if (h <= c && c < n) {
					best = Math.max(best, take(imos, h, c));
				}
			}
		}
		return 1.0d * best / imos[n];
	}


	private static long take(long[] imos, int h, int t) {
		long left = imos[h];
		long med = imos[t+1] - imos[h];
		long right = imos[imos.length-1] - imos[t+1];
		return imos[imos.length-1] - Math.max(left, Math.max(med, right));
	}



	public static void debug(Object... o) {
		System.err.println(Arrays.deepToString(o));
	}
}

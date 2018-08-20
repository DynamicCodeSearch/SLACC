package Y14R5P1.wyj;



import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.util.Scanner;

public class A {

	private static File inputF = new File("A-large.in");
	private static File outputF = new File("A-large.out");

	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(inputF);
		BufferedWriter out = new BufferedWriter(new FileWriter(outputF));
		int tc = sc.nextInt();
		for (int tt = 1; tt <= tc; tt++) {
			out.write("Case #" + tt + ": ");

			int n = sc.nextInt();
			int p = sc.nextInt();
			int q = sc.nextInt();
			int r = sc.nextInt();
			int s = sc.nextInt();

			long[] a = new long[n];
			long sum = 0;
			for (int i = 0; i < n; i++) {
				a[i] = ((long) i * p + q) % r + s;
				sum += a[i];
			}
			int x = 0, y = 0;
			long tmp = 0;
			for (int i = 0; i < n; i++) {
				tmp += a[i];
				if (tmp * 3 <= sum) {
					x = i;
				}
				if (tmp * 3 <= sum * 2) {
					y = i;
				}
			}

			double ans = 0;

			for (int dx = -3; dx <= 3; dx++) {
				for (int dy = -3; dy <= 3; dy++) {
					int rx = x + dx;
					int ry = y + dy;
					if (rx < 0 || rx >= n || ry < 0 || ry >= n) {
						continue;
					}

					long sum1 = 0, sum2 = 0, sum3 = 0;
					for (int i = 0; i < n; i++) {
						if (i < rx) {
							sum1 += a[i];
						} else {
							if (i <= ry) {
								sum2 += a[i];
							} else {
								sum3 += a[i];
							}
						}
					}
					long maxSum = Math.max(sum1, Math.max(sum2, sum3));
					double rate = (sum - maxSum) * 1.0 / sum;
					if (rate > ans) {
						ans = rate;
					}

					// out.write(maxSum + " " + sum + "\n");
				}
			}

			out.write(String.format("%.10f", ans));

			out.newLine();
		}

		sc.close();
		out.flush();
		out.close();
	}
}

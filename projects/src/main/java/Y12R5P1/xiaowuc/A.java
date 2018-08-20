package Y12R5P1.xiaowuc;


import java.awt.*;
import java.awt.event.*;
import java.awt.geom.*;
import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;

public class A {
	static StringTokenizer st;
	static BufferedReader br;
	static PrintWriter pw;

	public static void main(String[] args) throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(
				System.out)));
		final int NUM_CASES = readInt();
		for(int casenum = 1; casenum <= NUM_CASES; casenum++)	{
			int n = readInt();
			for(int i = 0; i < n; i++)
				readInt();
			int[] prob = new int[n];
			for(int i = 0; i < n; i++)
				prob[i] = readInt();
			ArrayList<Integer> go = new ArrayList<Integer>();
			while(go.size() != n)	{
				int max = 0;
				for(int i = 1; i < n; i++)	{
					if(prob[i] > prob[max])
						max = i;
				}
				go.add(max);
				prob[max] = -1;
			} 
			pw.print("Case #" + casenum + ":");
			for(int out: go)
				pw.print(" " + out);
			pw.println();
		}
		pw.close();
	}

	public static long readLong() throws IOException {
		return Long.parseLong(nextToken());
	}

	public static double readDouble() throws IOException {
		return Double.parseDouble(nextToken());
	}

	public static int readInt() throws IOException {
		return Integer.parseInt(nextToken());
	}

	public static String nextToken() throws IOException {
		while (st == null || !st.hasMoreTokens()) {
			if (!br.ready()) {
				pw.close();
				System.exit(0);
			}
			st = new StringTokenizer(br.readLine());
		}
		return st.nextToken();
	}
}

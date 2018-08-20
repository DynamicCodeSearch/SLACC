package Y12R5P1.wata;

import static java.lang.Math.*;
import static java.util.Arrays.*;
import java.io.*;
import java.util.*;

public class A {
	Scanner sc = new Scanner(System.in);
	
	int N;
	int[] L;
	int[] P;
	
	void read() {
		N = sc.nextInt();
		L = new int[N];
		for (int i = 0; i < N; i++) L[i] = sc.nextInt();
		P = new int[N];
		for (int i = 0; i < N; i++) P[i] = sc.nextInt();
	}
	
	void solve() {
		Entry[] es = new Entry[N];
		for (int i = 0; i < N; i++) es[i] = new Entry(P[i], L[i], i);
		sort(es);
		for (int i = 0; i < N; i++) {
			if (i > 0) System.out.print(" ");
			System.out.print(es[i].id);
		}
		System.out.println();
	}
	
	class Entry implements Comparable<Entry> {
		int P, L, id;
		Entry(int P, int L, int id) {
			this.P = P;
			this.L = L;
			this.id = id;
		}
		@Override
		public int compareTo(Entry o) {
			if (P * o.L - o.P * L != 0) return -(P * o.L - o.P * L);
			return id - o.id;
		}
	}
	
	void run() {
		int caseN = sc.nextInt();
		for (int caseID = 1; caseID <= caseN; caseID++) {
			read();
			System.out.printf("Case #%d: ", caseID);
			solve();
			System.out.flush();
		}
	}
	
	void debug(Object...os) {
		System.err.println(deepToString(os));
	}
	
	public static void main(String[] args) {
		try {
			System.setIn(new BufferedInputStream(new FileInputStream(args.length > 0 ? args[0] : (A.class.getName() + ".in"))));
		} catch (Exception e) {
		}
		new A().run();
	}
}

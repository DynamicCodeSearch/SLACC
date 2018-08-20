package Y12R5P1.jpaulson;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class A {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int T = in.nextInt();
		for(int cas=1; cas<=T; cas++) {
			int n = in.nextInt();
			int[] L = new int[n];
			final int[] P = new int[n];
			Integer[] I = new Integer[n];
			for(int i=0; i<n; i++)
				L[i] = in.nextInt();
			for(int i=0; i<n; i++) {
				P[i] = in.nextInt();
				I[i] = i;
			}
			Arrays.sort(I, new Comparator<Integer>() {
				public int compare(Integer A, Integer B) {
					if(P[A] != P[B]) return P[B]-P[A];
					return A-B;
				}
			});
			System.out.printf("Case #%d:", cas);
			for(Integer x:I)
				System.out.print(" "+x);
			System.out.println();
		}
		//BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	}
}

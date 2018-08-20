package Y12R5P1.dai;

import java.util.Arrays;
import java.util.Scanner;


public class R3A {

    public static void main(String[] args) {
        new R3A().solve();
    }

    private void solve() {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 1; i <= t; i++) {
            solve(sc, i);
        }
    }

    private void solve(Scanner sc, int t) {
        int n = sc.nextInt();
        int[] l = new int[n];
        int[] p = new int[n];
        for (int i = 0; i < n; i++) {
            l[i] = sc.nextInt();
        }
        for (int i = 0; i < n; i++) {
            p[i] = sc.nextInt();
        }
        Level[] levels = new Level[n];
        for (int i = 0; i < n; i++) {
            levels[i] = new Level(i, l[i], p[i]);
        }
        Arrays.sort(levels);
        
        
        StringBuilder sb = new StringBuilder().append("Case #").append(t).append(":");
        for (int i = 0; i < n; i++) {
            sb.append(" ").append(levels[i].i);
        }
        System.out.println(sb);
    }
    
    static class Level implements Comparable<Level> {
        final int i;
        final double hi;
        public Level(int i, int l, int p) {
            super();
            this.i = i;
            hi = (double)l / p / 100; 
        }
        @Override
        public int compareTo(Level o) {
            if (hi != o.hi) {
                return (int) Math.signum(hi - o.hi);
            }
            return i - o.i;
        }
        
    }
}

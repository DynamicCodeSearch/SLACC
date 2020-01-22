package CodeJam.Y14R5P1.Ryan;

import java.util.Scanner;

public class A {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        final int cases = scanner.nextInt();
        for (int t = 0; t < cases; t++) {
            System.out.println("Case #" + (t + 1) + ": " + solve(scanner));
        }
    }

    static long choose(Long[] partials, int a, int b, int n) {
        long first = partials[a];
        long second = partials[b] - partials[a];
        long third = partials[n] - partials[b];
        return Math.max(first, Math.max(second, third));
    }

    static long choose(Long[] partials, int i, int n) {
        long first = partials[i];
        long rest = partials[n] - first;
        if (first > rest)
            return first;
        int low = i, high = n;
        while (low + 1 < high) {
            int guess = (low + high) / 2;
            long second = partials[guess] - partials[i];
            if (second * 2 > rest)
                high = guess;
            else
                low = guess;
        }
        return Math.min(choose(partials, i, low, n), choose(partials, i, low + 1, n));
    }

    static double solve(Scanner scanner) {
        int n = scanner.nextInt();
        int p = scanner.nextInt();
        int q = scanner.nextInt();
        int r = scanner.nextInt();
        int s = scanner.nextInt();
        int[] array = new int[n];
        for (int i = 0; i < n; i++) {
            array[i] = (i * p + q) % r + s;
        //System.out.print(" "+array[i]);
        }
        //System.out.println();
        Long[] partials = new Long[n + 1];
        for (int i = 1; i <= n; i++) partials[i] = partials[i - 1] + array[i - 1];
        long best = partials[n];
        for (int i = 0; i < n; i++) {
            long now = choose(partials, i, n);
            //System.out.println("  "+i+": "+now);
            best = Math.min(best, now);
        }
        long total = partials[n];
        return 1 - (double) (best) / total;
    }
}

package Y13R5P1.gilesg;

// @gilesgardam
import java.util.*;
import static java.lang.Math.*;

public class ProblemA {
    int M = 37;

    void run() {
        Scanner sc = new Scanner(System.in);
        int numCases = sc.nextInt();
        for (int caseNum = 1; caseNum <= numCases; caseNum++) {
            long B = sc.nextLong();
            int N = sc.nextInt();
            long[] x = new long[M];
            for (int i = 0; i < N; ++i) {
                x[i] = sc.nextLong();
            }
            Arrays.sort(x);
            d(x);

            long nacho = 0;
            double answer = 0.0;
            for (int i = 0; i < M; ++i) {
                if (i < M-1 && x[i] == x[i+1]) {
                    continue;
                }
                for (int j = i; j < M; ++j) {
                    if (j < M-1 && x[j] == x[j+1]) {
                        continue;
                    }
                    answer = max(answer, solve(x, i+1, j+1, B));
                }
            }

            p("Case #%d: %.9f\n", caseNum, answer);
        }
    }

    boolean can_bet(long[] x, long bet, int keep, int burn, long B) {
        return total_bet(x, bet, keep, burn) <= B;
    }

    long winning_bet(long[] x, long bet, int keep, int burn) {
        long ret = 0;
        for (int i = 0; i < keep; ++i) {
            ret += max(0, bet - x[i]);
        }
        return ret;
    }

    long losing_bet(long[] x, long bet, int keep, int burn) {
        long ret = 0;
        for (int i = keep; i < burn; ++i) {
            ret += max(0, bet + 1 - x[i]);
        }
        return ret;
    }

    long total_bet(long[] x, long bet, int keep, int burn) {
        return winning_bet(x, bet, keep, burn) + losing_bet(x, bet, keep, burn);
    }

    double solve(long[] x, int keep, int burn, long B) {
        // best we can do keep,
        // burning burn
        int b = burn - keep;

        // binary search for smallest possible bet we cannot make
        long lo = 1;
        long hi = burn < M ? x[burn] : B + 1;
        while (lo < hi) {
            long mid = (lo + hi) / 2;
            if (can_bet(x, mid, keep, burn, B)) {
                lo = mid + 1;
            }
            else {
                hi = mid;
            }
        }

        long bet = lo - 1;

        long win = winning_bet(x, bet, keep, burn);
        long total = total_bet(x, bet, keep, burn);

        double payoff = 36.0 * win / keep;
        double ret = payoff - total;
        d(keep, burn, bet);
        d("ret", ret);
        return ret;

    }

    boolean debug = false;
    void p(String f, Object...params) {
        System.out.printf(f, params);
    }
    void d(Object...params) {
        if (debug) {
            p("DEBUG: %s\n", Arrays.deepToString(params));
        }
    }
    void die() {
        throw new RuntimeException();
    }
    public ProblemA(String[] args) {
        if (args.length > 0 && args[0].equals("debug")) {
            debug = true;
        }
    }
    public static void main(String[] args) {
        new ProblemA(args).run();
    }
}

package CodeJam.Y11R5P1.rf;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Locale;
import java.util.StringTokenizer;

public class A {

    BufferedReader br;

    PrintWriter out;

    StringTokenizer st;

    boolean eof;

    static class Point {

        double x, y;

        public Point(double x, double y) {
            super();
            this.x = x;
            this.y = y;
        }
    }

    double getY(double x, Point st, Point en) {
        double coef = (x - st.x) / (en.x - st.x);
        return st.y + coef * (en.y - st.y);
    }

    void solve() throws IOException {
        out.println();
        int width = nextInt();
        int down = nextInt();
        int up = nextInt();
        int g = nextInt();
        Point[] downB = new Point[down];
        for (int i = 0; i < down; i++) downB[i] = new Point(nextInt(), nextInt());
        Point[] upB = new Point[up];
        for (int i = 0; i < up; i++) upB[i] = new Point(nextInt(), nextInt());
        ArrayList<Point> res = new ArrayList<Point>();
        res.add(new Point(0, upB[0].y - downB[0].y));
        int ukUp = 1;
        int ukDown = 1;
        while (ukUp < up - 1 || ukDown < down - 1) {
            if (upB[ukUp].x < downB[ukDown].x) {
                double newX = upB[ukUp].x;
                double newY = upB[ukUp].y - getY(newX, downB[ukDown - 1], downB[ukDown]);
                ukUp++;
                res.add(new Point(newX, newY));
            } else if (upB[ukUp].x > downB[ukDown].x) {
                double newX = downB[ukDown].x;
                double newY = getY(newX, upB[ukUp - 1], upB[ukUp]) - downB[ukDown].y;
                ukDown++;
                res.add(new Point(newX, newY));
            } else {
                res.add(new Point(upB[ukUp].x, upB[ukUp].y - downB[ukDown].y));
                ukUp++;
                ukDown++;
            }
        }
        res.add(new Point(width, upB[up - 1].y - downB[down - 1].y));
        //		for (Point p : res) {
        //			System.out.println(p.x + " " + p.y);
        //		}
        double piece = 0;
        for (int i = 0; i < res.size() - 1; i++) piece += 0.5 * (res.get(i + 1).y + res.get(i).y) * (res.get(i + 1).x - res.get(i).x);
        piece /= g;
        int uk = 0;
        double curX = 0;
        double curLeft = piece;
        for (int i = 0; i < g - 1; i++) {
            double curY;
            while (true) {
                curY = getY(curX, res.get(uk), res.get(uk + 1));
                double remArea = (res.get(uk + 1).y + curY) * 0.5 * (res.get(uk + 1).x - curX);
                if (remArea > curLeft)
                    break;
                curLeft -= remArea;
                uk++;
                curX = res.get(uk).x;
            }
            double left = curX;
            double right = res.get(uk + 1).x;
            for (int j = 0; j < 70; j++) {
                double midX = (left + right) * 0.5;
                double midY = getY(midX, res.get(uk), res.get(uk + 1));
                if ((curY + midY) * (midX - curX) * 0.5 > curLeft)
                    right = midX;
                else
                    left = midX;
            }
            out.printf("%.9f\n", left);
            curX = left;
            curLeft = piece;
        }
    }

    void preCalc() throws IOException {
    }

    void gcjSolve() throws IOException {
        Locale.setDefault(Locale.US);
        preCalc();
        int tests = nextInt();
        for (int i = 1; i <= tests; i++) {
            out.print("Case #" + i + ": ");
            System.out.println("Test " + i + " started");
            solve();
        }
        System.out.println("Finished!");
    }

    void inp() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        out = new PrintWriter(System.out);
        gcjSolve();
        out.close();
    }

    public static void main(String[] args) throws IOException {
        new A().inp();
    }

    String nextToken() {
        while (st == null || !st.hasMoreTokens()) {
            try {
                st = new StringTokenizer(br.readLine());
            } catch (Exception e) {
                eof = true;
                return "0";
            }
        }
        return st.nextToken();
    }

    String nextString() {
        while (st == null || !st.hasMoreTokens()) {
            try {
                st = new StringTokenizer(br.readLine());
            } catch (Exception e) {
                eof = true;
                return "0";
            }
        }
        return st.nextToken("\n");
    }

    int nextInt() throws IOException {
        return Integer.parseInt(nextToken());
    }

    long nextLong() throws IOException {
        return Long.parseLong(nextToken());
    }

    double nextDouble() throws IOException {
        return Double.parseDouble(nextToken());
    }
}

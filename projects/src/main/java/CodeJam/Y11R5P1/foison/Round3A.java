package CodeJam.Y11R5P1.foison;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Round3A {

    public static String problemName = "A";

    public static String inputName = "large";

    public static class Cross implements Comparable<Cross> {

        Cross(double x, double low, double high) {
            this.x = x;
            this.low = low;
            this.high = high;
        }

        public double x;

        public double low;

        public double high;

        public boolean equals(Object o) {
            Cross c = (Cross) o;
            return x == c.x && low == c.low && high == c.high;
        }

        @Override
        public int compareTo(Cross arg0) {
            return ((Double) x).compareTo(arg0.x);
        }
    }

    public static class Point {

        Point(double x, double y) {
            this.x = x;
            this.y = y;
        }

        public double x;

        public double y;
    }

    public static String handleCase() {
        int w = in.nextInt();
        int lNum = in.nextInt();
        int uNum = in.nextInt();
        int g = in.nextInt();
        ArrayList<Point> lower = new ArrayList<Point>();
        ArrayList<Point> upper = new ArrayList<Point>();
        for (int i = 0; i < lNum; i++) {
            lower.add(new Point(in.nextInt(), in.nextInt()));
        }
        for (int i = 0; i < uNum; i++) {
            upper.add(new Point(in.nextInt(), in.nextInt()));
        }
        ArrayList<Point> allPoints = new ArrayList<Point>();
        for (Point p : upper) {
            allPoints.add(p);
        }
        for (int i = lower.size() - 1; i >= 0; i--) {
            allPoints.add(lower.get(i));
        }
        double area = 0;
        for (int i = 0; i < allPoints.size(); i++) {
            area += allPoints.get(i).x * allPoints.get((i + 1) % allPoints.size()).y;
            area -= allPoints.get(i).y * allPoints.get((i + 1) % allPoints.size()).x;
        }
        area = Math.abs(area / 2.0);
        ArrayList<Cross> crosses = new ArrayList<Cross>();
        for (Point p : lower) {
            int upperInd = 0;
            for (; upperInd + 2 < upper.size(); upperInd++) {
                if (upper.get(upperInd + 1).x > p.x) {
                    break;
                }
            }
            double xfrac = (p.x - upper.get(upperInd).x) / (upper.get(upperInd + 1).x - upper.get(upperInd).x);
            double interpolatedY = upper.get(upperInd).y + xfrac * (upper.get(upperInd + 1).y - upper.get(upperInd).y);
            crosses.add(new Cross(p.x, p.y, interpolatedY));
        }
        for (Point p : upper) {
            int lowerInd = 0;
            for (; lowerInd + 2 < lower.size(); lowerInd++) {
                if (lower.get(lowerInd + 1).x > p.x) {
                    break;
                }
            }
            double xfrac = (p.x - lower.get(lowerInd).x) / (lower.get(lowerInd + 1).x - lower.get(lowerInd).x);
            double interpolatedY = lower.get(lowerInd).y + xfrac * (lower.get(lowerInd + 1).y - lower.get(lowerInd).y);
            crosses.add(new Cross(p.x, interpolatedY, p.y));
        }
        Collections.sort(crosses);
        double chunkSize = area / g;
        double currentX = 0;
        double currentLow = crosses.get(0).low;
        double currentHigh = crosses.get(0).high;
        int crossInd = 1;
        for (int i = 0; i < g - 1; i++) {
            double chunkLeft = chunkSize;
            while (chunkLeft > 0.0000000001) {
                double crossArea = (crosses.get(crossInd).x - currentX) * (((currentHigh - currentLow) + (crosses.get(crossInd).high - crosses.get(crossInd).low)) / 2.0);
                if (chunkLeft > crossArea) {
                    chunkLeft -= crossArea;
                    currentX = crosses.get(crossInd).x;
                    currentLow = crosses.get(crossInd).low;
                    currentHigh = crosses.get(crossInd).high;
                    crossInd++;
                } else {
                    double lo = currentX;
                    double hi = crosses.get(crossInd).x;
                    double thisX = 0, thisHigh = 0, thisLow = 0;
                    for (int j = 0; j < 100; j++) {
                        thisX = (lo + hi) / 2.0;
                        double xfrac = (thisX - currentX) / (crosses.get(crossInd).x - currentX);
                        thisHigh = currentHigh + xfrac * (crosses.get(crossInd).high - currentHigh);
                        thisLow = currentLow + xfrac * (crosses.get(crossInd).low - currentLow);
                        double thisArea = (thisX - currentX) * (((currentHigh - currentLow) + (thisHigh - thisLow)) / 2.0);
                        if (thisArea > chunkLeft) {
                            hi = thisX;
                        } else {
                            lo = thisX;
                        }
                    }
                    currentX = thisX;
                    currentHigh = thisHigh;
                    currentLow = thisLow;
                    chunkLeft = 0;
                }
            }
            out.printf("%.010f%n", currentX);
        }
        return "";
    }

    public static int[] readIntArr() {
        int n = in.nextInt();
        int[] res = new int[n];
        for (int i = 0; i < n; i++) res[i] = in.nextInt();
        return res;
    }

    public static interface Parser<T> {

        public T next();
    }

    public static <T> ArrayList<T> readList(Parser<T> p) {
        int n = in.nextInt();
        ArrayList<T> res = new ArrayList<T>();
        for (int i = 0; i < n; i++) res.add(p.next());
        return res;
    }

    public static Parser<Integer> intParser = new Parser<Integer>() {

        public Integer next() {
            return in.nextInt();
        }
    };

    public static void main(String[] args) throws FileNotFoundException {
        String inFilename = problemName + "-" + inputName + ".in";
        String outFilename = problemName + "-" + inputName + ".out";
        System.out.println("Reading from " + inFilename);
        System.out.println("Writing to " + outFilename);
        in = new Scanner(new File(inFilename));
        out = new PrintStream(new File(outFilename));
        int ncases = in.nextInt();
        for (int i = 0; i < ncases; i++) {
            System.out.println("Running case " + (i + 1) + "...");
            out.println("Case #" + (i + 1) + ":");
            handleCase();
        }
        System.out.println("Done!");
    }

    static Scanner in;

    static PrintStream out;
}

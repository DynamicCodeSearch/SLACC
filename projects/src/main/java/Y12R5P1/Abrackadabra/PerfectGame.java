package Y12R5P1.Abrackadabra;

import java.io.*;
import java.util.*;
import java.math.*;

// 6/9/12 6:00 PM
// by Abrackadabra

public class PerfectGame {
    public static void main(String[] args) throws IOException {
        if (args.length > 0 && args[0].equals("Abra")) debugMode = true;
        new PerfectGame().run();
        /*new Thread(null, new Runnable() {
            public void run() {
                try {
                    new PerfectGame().run();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }, "1", 1 << 24).start();*/
    }

    int IOMode = 0; //0 - consoleIO, 1 - <taskName>.in/out, 2 - input.txt/output.txt, 3 - test case generator
    String taskName = "";
    boolean testBasedProblem = true;

    class Level implements Comparable<Level> {
        int length;
        double probabilityToDie;
        double estimatedTime;
        int index;

        Level(int length, double probabilityToDie, int index) {
            this.length = length;
            this.probabilityToDie = probabilityToDie;
            estimatedTime = length / probabilityToDie;
            this.index = index;
        }

        @Override
        public int compareTo(Level o) {
            if (estimatedTime != o.estimatedTime) return Double.compare(estimatedTime, o.estimatedTime);
            return Integer.compare(index, o.index);
        }
    }

    void solve() throws IOException {
        int n = nextInt();
        int[] l = new int[n];
        double[] p = new double[n];
        for (int i = 0; i < n; i++) l[i] = nextInt();
        for (int i = 0; i < n; i++) p[i] = nextInt() / 100.0;
        Level[] levels = new Level[n];
        for (int i = 0; i < n; i++) {
            levels[i] = new Level(l[i], p[i], i);
        }
        Arrays.sort(levels);
        out.print("Case #" + testIndex + ": ");
        for (Level level : levels) out.print(level.index + " ");
        out.println();
    }

    long startTime = System.nanoTime(), tempTime = startTime, finishTime = startTime;
    long startMem = Runtime.getRuntime().totalMemory(), finishMem = startMem;
    int testIndex;

    void run() throws IOException {
        init();
        if (debugMode) {
            con.println("Start");
            con.println("Console:");
        }

        int tests = testBasedProblem ? nextInt() : 1;
        for (testIndex = 1; testIndex <= tests; testIndex++)
            solve();

        finishTime = System.nanoTime();
        finishMem = Runtime.getRuntime().totalMemory();
        out.flush();
        if (debugMode) {
            int maxSymbols = 1000;
            BufferedReader tbr = new BufferedReader(new FileReader("input.txt"));
            char[] a = new char[maxSymbols];
            tbr.read(a);
            if (a[0] != 0) {
                con.println("File input:");
                con.println(a);
                if (a[maxSymbols - 1] != 0) con.println("...");
            }
            tbr = new BufferedReader(new FileReader("output.txt"));
            a = new char[maxSymbols];
            tbr.read(a);
            if (a[0] != 0) {
                con.println("File output:");
                con.println(a);
                if (a[maxSymbols - 1] != 0) con.println("...");
            }
            con.println("Execution time: " + (finishTime - startTime) / 1000000000.0 + " sec");
            con.println("Used memory:    " + (finishMem - startMem) + " bytes");
            con.println("Total memory:   " + Runtime.getRuntime().totalMemory() + " bytes");
        }
    }

    boolean tick(double x) {
        if (System.nanoTime() - tempTime > x * 1e9) {
            tempTime = System.nanoTime();
            con.println("Tick at " + (tempTime - startTime) / 1000000000 + " sec");
            con.print("   ");
            return true;
        }
        return false;
    }

    static boolean debugMode = false;
    PrintStream con = System.out;

    void init() throws IOException {
        if (debugMode && IOMode != 3) {
            br = new BufferedReader(new FileReader("input.txt"));
            out = new PrintWriter(new FileWriter("output.txt"));
        } else
            switch (IOMode) {
                case 0:
                    br = new BufferedReader(new InputStreamReader(System.in));
                    out = new PrintWriter(System.out);
                    break;
                case 1:
                    br = new BufferedReader(new FileReader(taskName + ".in"));
                    out = new PrintWriter(new FileWriter(taskName + ".out"));
                    break;
                case 2:
                    br = new BufferedReader(new FileReader("input.txt"));
                    out = new PrintWriter(new FileWriter("output.txt"));
                    break;
                case 3:
                    out = new PrintWriter(new FileWriter("input.txt"));
                    break;
            }
        if (!debugMode)
            con = new PrintStream(new OutputStream() {
                public void write(int b) throws IOException {
                } // to /dev/null
            });
        if ((IOMode == 1 && taskName.length() == 0) || (IOMode != 1 && taskName.length() != 0)) {
            System.err.println("Leha, check IO settings");
            System.err.flush();
            System.exit(0);
        }
    }

    BufferedReader br;
    PrintWriter out;
    StringTokenizer in;

    boolean hasMoreTokens() throws IOException {
        while (in == null || !in.hasMoreTokens()) {
            String line = br.readLine();
            if (line == null) return false;
            in = new StringTokenizer(line);
        }
        return true;
    }

    String nextString() throws IOException {
        return hasMoreTokens() ? in.nextToken() : null;
    }

    int nextInt() throws IOException {
        return Integer.parseInt(nextString());
    }

    long nextLong() throws IOException {
        return Long.parseLong(nextString());
    }

    double nextDouble() throws IOException {
        return Double.parseDouble(nextString());
    }
}
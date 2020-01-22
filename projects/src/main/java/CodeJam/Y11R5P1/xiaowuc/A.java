package CodeJam.Y11R5P1.xiaowuc;

import java.awt.*;
import java.awt.geom.Area;
import java.awt.geom.Path2D;
import java.awt.geom.PathIterator;
import java.awt.geom.Point2D;
import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class A {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("aOut.txt")));
        int qq = Integer.parseInt(br.readLine());
        outer: for (int caseNum = 1; caseNum <= qq; caseNum++) {
            pw.println("Case #" + caseNum + ": ");
            StringTokenizer st = new StringTokenizer(br.readLine());
            int lastX = Integer.parseInt(st.nextToken());
            int bottom = Integer.parseInt(st.nextToken());
            int top = Integer.parseInt(st.nextToken());
            int cut = Integer.parseInt(st.nextToken());
            Point[] down = new Point[bottom];
            for (int i = 0; i < down.length; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                down[i] = new Point(a, b);
            }
            Point[] up = new Point[top];
            for (int i = 0; i < up.length; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                up[i] = new Point(a, b);
            }
            double[] points = new double[2 * (top + bottom)];
            int c = 0;
            for (int i = 0; i < down.length; i++) {
                points[c++] = down[i].x;
                points[c++] = down[i].y;
            }
            for (int i = up.length - 1; i >= 0; i--) {
                points[c++] = up[i].x;
                points[c++] = up[i].y;
            }
            double lastKnown = 0;
            double min = 0;
            double max = lastX;
            Area orig = makeArea(points);
            double origArea = computeArea(orig);
            for (int i = 1; i < cut; i++) {
                max = lastX;
                for (int j = 0; j < 50; j++) {
                    double mid = (min + max) / 2;
                    double[] poly = new double[8];
                    poly[0] = mid;
                    poly[1] = 1001;
                    poly[2] = mid;
                    poly[3] = -1001;
                    poly[4] = lastKnown;
                    poly[5] = -1001;
                    poly[6] = lastKnown;
                    poly[7] = 1001;
                    Area rect = makeArea(poly);
                    rect.intersect(orig);
                    double area = computeArea(rect);
                    if (area < origArea / cut) {
                        min = mid;
                    } else {
                        max = mid;
                    }
                }
                lastKnown = min;
                pw.println(min);
            }
        }
        pw.close();
    }

    public static Area makeArea(double[] pts) {
        Path2D.Double p = new Path2D.Double();
        p.moveTo(pts[0], pts[1]);
        for (int i = 2; i < pts.length; i += 2) p.lineTo(pts[i], pts[i + 1]);
        p.closePath();
        return new Area(p);
    }

    public static double computeArea(Area area) {
        double totArea = 0;
        PathIterator iter = area.getPathIterator(null);
        ArrayList<Point2D.Double> points = new ArrayList<Point2D.Double>();
        while (!iter.isDone()) {
            double[] buffer = new double[6];
            switch(iter.currentSegment(buffer)) {
                case PathIterator.SEG_MOVETO:
                case PathIterator.SEG_LINETO:
                    points.add(new Point2D.Double(buffer[0], buffer[1]));
                    break;
                case PathIterator.SEG_CLOSE:
                    totArea += computePolygonArea(points);
                    points.clear();
                    break;
            }
            iter.next();
        }
        return totArea;
    }

    public static double computePolygonArea(ArrayList<Point2D.Double> points) {
        Point2D.Double[] pts = points.toArray(new Point2D.Double[points.size()]);
        double area = 0;
        for (int i = 0; i < pts.length; i++) {
            int j = (i + 1) % pts.length;
            area += pts[i].x * pts[j].y - pts[j].x * pts[i].y;
        }
        return Math.abs(area) / 2;
    }
}

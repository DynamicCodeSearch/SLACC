package Y11R5P1.huameng;

import java.util.*;

public class A {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int cases = in.nextInt();
		for(int cc=1;cc<=cases;++cc) {
			System.out.println("Case #" + cc + ": ");
			int w = in.nextInt(); //width
			int l = in.nextInt(); //lower points
			int u = in.nextInt(); //upper points
			int g = in.nextInt(); //guests
			Point[] lower = new Point[l];
			for(int i=0;i<l;++i) {
				lower[i] = new Point(in.nextInt(), in.nextInt());
			}
			Point[] upper = new Point[u];
			for(int i=0;i<u;++i) {
				upper[i] = new Point(in.nextInt(), in.nextInt());
			}
			
			
			double totalArea = 0.0;
			int curL = 1;
			int curU = 1;
			int lastX = 0;
			double curHeight = 1.0*upper[0].y-lower[0].y;
			while(curL < l && curU < u) {
				int lowX = lower[curL].x;
				int upX = upper[curU].x;
				int curX = Math.min(lowX, upX);
				if (curX == lowX && curX == upX) {
					double thisHeight = upper[curU].y-lower[curL].y;
					totalArea += (1.0*curHeight + thisHeight) / 2 * (curX-lastX);
					
					//System.err.println("dist: " + (curX-lastX));
					//System.err.println("newHeight: " + thisHeight);
					//System.err.println("oldHeight: " + curHeight);
					curHeight = thisHeight;
					lastX = curX;
					++curL;
					++curU;
				}
				else if (curX == lowX) {
					double upHeight = upper[curU-1].y + (upper[curU].y-upper[curU-1].y) * (1.0*(curX-upper[curU-1].x)/(upper[curU].x-upper[curU-1].x));
					upHeight -= lower[curL].y;
					totalArea += ((1.0*curHeight)+upHeight)/2 * (curX-lastX);
					
					//System.err.println("dist: " + (curX-lastX));
					//System.err.println("newHeight: " + upHeight);
					//System.err.println("oldHeight: " + curHeight);
					curHeight = upHeight;
					lastX = curX;
					++curL;
				}
				else {
					double lowHeight = lower[curL-1].y + (lower[curL].y-lower[curL-1].y) * (1.0*(curX-lower[curL-1].x)/(lower[curL].x-lower[curL-1].x));
					//System.err.println("prevLowHeight: " + lowHeight);
					lowHeight = upper[curU].y-lowHeight;
					totalArea += ((1.0*curHeight)+lowHeight)/2 * (curX-lastX);
					
					//System.err.println("dist: " + (curX-lastX));
					//System.err.println("newHeight: " + lowHeight);
					//System.err.println("oldHeight: " + curHeight);
					curHeight = lowHeight;
					lastX = curX;
					++curU;
				}
				//System.err.println(totalArea);
			}
			//System.err.println(totalArea);
			ArrayList<Point> upperPoints = new ArrayList<Point>();
			for(Point p : upper) {
				upperPoints.add(p);
			}
			ArrayList<Point> lowerPoints = new ArrayList<Point>();
			for(Point p : lower) {
				lowerPoints.add(p);
			}
			double prevX = 0.0;
			double goal = totalArea/g;
			double target = 0.0;
			double ERR = 0.000001;
			List<Double> answers = new LinkedList<Double>();
			A: for(int i=0;i<g-1;++i) {
				target += goal;
				double minX = prevX;
				double maxX = 1.0*w;
				while(minX < maxX) {
					double curX = (minX+maxX)/2;
					double area = findArea(curX, prevX, lowerPoints, upperPoints);
					//System.err.println(curX + ": " + area);
					if (Math.abs(area-target) < ERR) {
						prevX = curX;
						answers.add(curX);
						continue A;
					}
					else if (area-target < 0) {
						minX = curX;
					}
					else {
						maxX = curX;
					}
					//find area between prevX and curX
				}
			}
			for(Double d : answers) {
				System.out.printf("%.6f\n", d);
			}
		}
	}
	
	public static double findArea(double stopX, double prevX, ArrayList<Point> lower, ArrayList<Point> upper) {
		double curHeight = 1.0*upper.get(0).y-lower.get(0).y;
		int curU = 1;
		int curL = 1;
		int u = upper.size();
		int l = lower.size();
		double lastX = 0;
		double totalArea = 0.0;
		while(curL < l && curU < u && (lower.get(curL).x < stopX || upper.get(curU).x < stopX)) {
			Point curUp = upper.get(curU);
			Point curLow = lower.get(curL);
			Point prevUp = upper.get(curU-1);
			Point prevLow = lower.get(curL-1);
			int lowX = curLow.x;
			int upX = curUp.x;
			int curX = Math.min(lowX, upX);
			if (curX == lowX && curX == upX) {
				double thisHeight = curUp.y-curLow.y;
				totalArea += (1.0*curHeight + thisHeight) / 2 * (curX-lastX);
				
				////System.err.println("dist: " + (curX-lastX));
				////System.err.println("newHeight: " + thisHeight);
				////System.err.println("oldHeight: " + curHeight);
				curHeight = thisHeight;
				lastX = curX;
				++curL;
				++curU;
			}
			else if (curX == lowX) {
				double upHeight = prevUp.y + (curUp.y-prevUp.y) * (1.0*(curX-prevUp.x)/(curUp.x-prevUp.x));
				upHeight -= curLow.y;
				totalArea += ((1.0*curHeight)+upHeight)/2 * (curX-lastX);
				
				////System.err.println("dist: " + (curX-lastX));
				////System.err.println("newHeight: " + upHeight);
				////System.err.println("oldHeight: " + curHeight);
				curHeight = upHeight;
				lastX = curX;
				++curL;
			}
			else {
				double lowHeight = prevLow.y + (curLow.y-prevLow.y) * (1.0*(curX-prevLow.x)/(curLow.x-prevLow.x));
				lowHeight = curUp.y-lowHeight;
				totalArea += ((1.0*curHeight)+lowHeight)/2 * (curX-lastX);
				
				////System.err.println("dist: " + (curX-lastX));
				////System.err.println("newHeight: " + lowHeight);
				////System.err.println("oldHeight: " + curHeight);
				curHeight = lowHeight;
				lastX = curX;
				++curU;
			}
			////System.err.println(totalArea);
		}
		////System.err.println("before last part: " + totalArea);
		//find area between last used x value and the end x value
		double curX = stopX;
		Point prevU = upper.get(curU-1);
		Point nextU = upper.get(curU);
		Point prevL = lower.get(curL-1);
		Point nextL = lower.get(curL);
		double upperHeight = prevU.y + (nextU.y-prevU.y) * 1.0*(curX-prevU.x)/(nextU.x-prevU.x);
		double lowerHeight = prevL.y + (nextL.y-prevL.y) * 1.0*(curX-prevL.x)/(nextL.x-prevL.x);
		double newHeight = upperHeight-lowerHeight;
		totalArea += (upperHeight - lowerHeight + curHeight) / 2 * (curX-lastX);
		////System.err.println("dist: " + (curX-lastX));
		////System.err.println("newHeight: " + newHeight);
		////System.err.println("oldHeight: " + curHeight);
		return totalArea;
	}
}

class Point {
	int x;
	double y;
	public Point(int x, int y) {
		this.x = x;
		this.y = 1.0*y;
	}

}
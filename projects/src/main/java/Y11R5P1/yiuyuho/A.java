package Y11R5P1.yiuyuho;

/*

Author: Yiu Yu Ho
Creation: <Creation Date>
Last Updated: <Last Updated Date>
*/

import java.io.*;
import java.util.*;
import java.text.*;

public class A
{
	public PrintStream out = System.out;
	public PrintStream err = System.err;
	public Scanner in = new Scanner(System.in);
	public DecimalFormat fmt = new DecimalFormat("0.000000000");

	public int An, Bn, cut;
	public Pair[] A, B;
	public double W;
	
	public void main() throws Exception
	{
//		err = new PrintStream(new FileOutputStream("error.log"), true);

		int TCase = in.nextInt();
		for(int cc = 1; cc <= TCase; ++cc)
		{
			W = in.nextDouble();
			Bn = in.nextInt();
			An = in.nextInt();
			
			cut = in.nextInt();
			
			B = new Pair[Bn];
			for(int i = 0; i < Bn; ++i)
			{
				B[i] = new Pair(in.nextDouble(), in.nextDouble());
			}
			
			A = new Pair[An];
			for(int i = 0; i < An; ++i)
			{
				A[i] = new Pair(in.nextDouble(), in.nextDouble());
			}
			
			Pair[] P = merge(A, B);
			double area = pArea(P);
			double target = area / cut; 
			
			out.println("Case #" + cc + ":");
			err.println("Case #" + cc + ":");
			
			double Lx = 0.0;
			for(int i = 0; i < cut-1; ++i)
			{
				//Hx : area(Lx, Hx) = target
				double low = Lx, high = W;
				double Hx, T;
				
				for(int cnt = 0; cnt < 1000; ++cnt)
				{
					Hx = (low + high)/2.0;
					
					if(cake(Lx, Hx) < target) low = Hx;
					else high = Hx;
				}
				
				Hx = (low + high) / 2.0;
				out.println(Hx);
				
				Lx = Hx;
			}
			
		}//end for cc = 1 ... TCase

	}//end public void main()

	public Pair[] merge(Pair[] u, Pair[] v)
	{
		ArrayList<Pair> R = new ArrayList<Pair>();
		
		for(int i = 0; i < u.length; ++i) R.add(u[i]);
		for(int i = v.length - 1; i >= 0; --i) R.add(v[i]);
		
		return R.toArray(new Pair[0]);
	}
	
	public double cake(double Lx, double Hx)
	{
		Pair[] u = cut(A, Lx, Hx);
		Pair[] v = cut(B, Lx, Hx);
		
		Pair[] P = merge(u, v);
		return pArea(P);
	}
	
	public Pair[] cut(Pair[] p, double Lx, double Hx)
	{
		ArrayList<Pair> R = new ArrayList<Pair>();
		
		//Lx <= Hx < W
		int i = 0;
		while(p[i].x <= Lx) ++i;
		
		R.add(inter(p[i-1], p[i], Lx));
		
		while(p[i].x < Hx)
		{
			R.add(p[i]);
			++i;
		}
		
		R.add(inter(p[i-1],p[i],Hx));
		
		return R.toArray(new Pair[0]);
	}
	
	public Pair inter(Pair P0, Pair P1, double x)
	{
		double t = (x - P0.x) / (P1.x - P0.x);
		double y = P0.y + t * (P1.y - P0.y);
		
		return new Pair(x, y);
	}
	
	public double tol = 1e-12;
	public boolean eq(double x, double y) { return Math.abs(x - y) < tol; }	
	
	//---------------------- Pair (double) ----------------------------------------
	//double point
	//Use eq(double, double)
	private class Pair implements Comparable<Pair>
	{
		public final double x, y;
		public Pair(double xx, double yy) { x = xx; y = yy; }
		
		public int compareTo(Pair u)
		{
			if(!eq(x, u.x)) return (x < u.x ? -1 : 1);
			if(!eq(y, u.y)) return (y < u.y ? -1 : 1);
			return 0;
		}

		public Pair midpoint(Pair u) { return new Pair((x + u.x)/2, (y + u.y)/2); }
		public Pair add(Pair u) { return new Pair(x + u.x, y + u.y); }
		public Pair subtract(Pair u) { return new Pair(x - u.x, y - u.y); }
		public Pair multiply(double s) { return new Pair(x*s, y*s); }

		public double length() { return Math.sqrt(x*x + y*y); }
		public double dist(Pair u) { return subtract(u).length(); }

		public Pair rotate(double t) 
		{
			double xx, yy;
			xx = x*Math.cos(t) - y*Math.sin(t);
			yy = x*Math.sin(t) + y*Math.cos(t);
			return new Pair(xx, yy); 
		}

		public double[] ret() { return new double[]{x, y}; }
		public String toString() { return "("+x+","+y+")"; }
	}
//---------------------- End Pair (double) ------------------------------------	
	
	//Find area of polygon p
	public double pArea(Pair[] p)
	{
		int a, b;
		double sum = 0.0;

		a = p.length - 1;
		for(b = 0; b < p.length; b++)
		{
			sum += p[a].x*p[b].y - p[a].y*p[b].x;
			a = b;
		}
		return Math.abs(sum)/2.0;
	}	
	
	public static void main(String[] args)
	{
		long startTime = System.currentTimeMillis();

		try
		{
			(new A()).main();
		}
		catch(Exception e) { e.printStackTrace(); }

		long endTime = System.currentTimeMillis();

		long ms = endTime - startTime;
		long sec = ms/1000; ms = ms%1000;
		long min = sec/60; sec = sec%60;

		System.err.println("Time Spent: " + min + " minute(s) " + sec + " second(s) " + ms + " (ms)");
	}
}//ends public class A

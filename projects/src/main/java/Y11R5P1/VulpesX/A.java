package Y11R5P1.VulpesX;

import java.util.*;
import java.awt.*;

public class A
{
	static Point[] a, l, u;
	static int W, L, U, G;

	public static void main(String args[])
	{
		Scanner scan = new Scanner(System.in);

		int T = scan.nextInt();

		for(int ca=1;ca <= T;ca++)
		{
			W = scan.nextInt();
			L = scan.nextInt();
			U = scan.nextInt();
			G = scan.nextInt();

			a = new Point[L+U];
			l = new Point[L];
			u = new Point[U];

			for(int i=0;i < L;i++)
			{
				l[i] = a[i] = new Point(scan.nextInt(), scan.nextInt(), false);
			}

			for(int i=0;i < U;i++)
			{
				u[i] = a[i+L] = new Point(scan.nextInt(), scan.nextInt(), true);
			}

			Arrays.sort(a);

			System.out.println("Case #" + ca + ":");


			//Find total area
			double area = area(0, W);
			double lastx = 0;
			double target = area / G;

			//make cuts
			for(int i=0;i < G-1;i++)
			{
				//Binary search
				double lo = lastx;
				double hi = W;
				double mid = 0;

				while(hi - lo > 0.00000000001)
				{
					mid = (hi+lo)/2;

					double ar = area(lastx, mid);

					if(ar > target)
						hi = mid;
					else
						lo = mid;
				}

				System.out.println(mid);
				lastx = mid;
			}
		}
	}


	public static double area(double x1, double x2)
	{
		int ulidx = 0;
		int llidx = 0;

		for(int i=0;i < U;i++)
		{
			if(u[i].x <= x1)
				ulidx = i;
		}

		for(int i=0;i < L;i++)
		{
			if(l[i].x <= x1)
				llidx = i;
		}

		double rtn = 0;

		while(true)
		{
			//System.out.println(x1 + " " + ulidx + " " + llidx);
			double xe = Math.min(Math.min(u[ulidx+1].x, l[llidx+1].x), x2);

			double d1 = x1 - u[ulidx].x; //distance in x
			double d3 = xe - u[ulidx].x;
			double d2 = u[ulidx+1].x - u[ulidx].x;
			double ysu = u[ulidx].y + (d1/d2)*(u[ulidx+1].y - u[ulidx].y);
			double yeu = u[ulidx].y + (d3/d2)*(u[ulidx+1].y - u[ulidx].y);

			d1 = x1 - l[llidx].x;
			d2 = l[llidx+1].x - l[llidx].x;
			d3 = xe - l[llidx].x;
			double ysl = l[llidx].y + (d1/d2)*(l[llidx+1].y - l[llidx].y);
			double yel = l[llidx].y + (d3/d2)*(l[llidx+1].y - l[llidx].y);

			rtn += (xe-x1) * ((ysu-ysl)+(yeu-yel))/2;
			/*
			System.out.println(xe + " " + x1);
			System.out.println(ysu + " " + ysl);
			System.out.println(yeu + " " + yel);
			System.out.println("ADDING: " + ((xe-x1) * ((ysu-ysl)+(yeu-yel))/2));*/

			if(u[ulidx+1].x < l[llidx+1].x)
			{
				x1 = u[ulidx+1].x;
				ulidx++;
			}
			else
			{
				x1 = l[llidx+1].x;
				llidx++;
			}
			
			//System.out.println(x1 + ", " + xe);

			if(x1 >= x2)
				break;
		}

		return rtn;
			
	}
}


class Point implements Comparable
{
	int x, y;
	boolean up;

	public Point(int ix, int iy, boolean u)
	{
		x = ix;
		y = iy;
		up = u;
	}

	public int compareTo(Object o)
	{
		Point that = (Point)o;

		return this.x - that.x;
	}
}
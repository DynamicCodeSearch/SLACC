package Y11R5P1.humblefool;

import java.util.*;

public class IrregularCakes
{
	static Scanner sc = new Scanner(System.in);
	public static void main(String[] args)
	{
		int T = sc.nextInt();
		for(int i=1;i<=T;i++)
		{
			System.out.println("Case #"+i+": ");
			solveCase();
		}
	}
	static final int BASE = -1000;
	static double solve(int[] x, int[] y, double X)
	{
		double res = 0.0;
		for(int i=0;i+1<x.length;i++)
		{
			if(x[i+1]+1e-9 >= X)
			{
				double ratio = (X-x[i])/(x[i+1]-x[i]);
				res += ((2*y[i]+(y[i+1]-y[i])*ratio)/2.0 - BASE)*(X-x[i]);
				break;
			}
			else
			{
				res += ((y[i+1]+y[i])/2.0-BASE)*(x[i+1]-x[i]);
			}
		}
		return res;
	}
	static void solveCase()
	{
		int W = sc.nextInt(), L = sc.nextInt(), U = sc.nextInt(), G = sc.nextInt();
		int[] lowerX = new int[L], lowerY = new int[L];
		for(int i=0;i<L;i++)
		{
			lowerX[i] = sc.nextInt();
			lowerY[i] = sc.nextInt();
		}
		int[] upperX = new int[U], upperY = new int[U];
		for(int i=0;i<U;i++)
		{
			upperX[i] = sc.nextInt();
			upperY[i] = sc.nextInt();
		}
		
		double area = solve(upperX, upperY, W) - solve(lowerX, lowerY, W);
		double prevX = 0;
		for(int i=1;i<G;i++)
		{
			double lower = prevX, upper = W, req = area*i/G;
			for(int times=0;times<=100;times++)
			{
				double middle = (lower+upper)/2.0;
				double cutArea = solve(upperX, upperY, middle) - solve(lowerX, lowerY, middle);
				if(cutArea < req)
					lower = middle;
				else
					upper = middle;
			}
			System.out.println(lower);
			prevX = lower;
		}
	}
}

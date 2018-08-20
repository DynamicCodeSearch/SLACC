package Y14R5P1.iSuneast;

import java.util.Scanner;

public class Main {
	Scanner scan=new Scanner(System.in);
	
	long[] arr;
	long[] sum;
	int N;
	long p,q,r,s;
	
	void input()
	{
		N=scan.nextInt();
		p=scan.nextLong();
		q=scan.nextLong();
		r=scan.nextLong();
		s=scan.nextLong();
		arr=new long[N];
		sum=new long[N+1];
		for (int i=0;i<N;i++)
		{
			arr[i]=(i*p+q)%r+s;
		}
		for (int i=1;i<=N;i++)
		{
			sum[i]=sum[i-1]+arr[i-1];
		}
	}
	
	long getRes(long a,long b,long c)
	{
		long s=Math.max(a, b);
		s=Math.max(s, c);
		return sum[N]-s;
	}
	
	double solve()
	{
		long res=-1;
		for (int a=1,b=1;b<=N;b++)
		{
			long third=sum[N]-sum[b];
			for (;a<=b;a++)
			{
				long first=sum[a-1];
				long second=sum[b]-sum[a-1];
				res=Math.max(res, getRes(first,second,third));
				if (first<=second)
					continue;
				else
				{
					break;
				}
			}
			a-=2;
			if (a<1) a=1;
		}
		return (res+0.0)/sum[N];
	}
	
	void run()
	{
		int t=scan.nextInt();
		for (int i=1;i<=t;i++)
		{
			input();
			System.out.printf("Case #%d: %.10f\n",i,solve());
		}
	}
	
	public static void main(String[] args)
	{
		new Main().run();
	}
}

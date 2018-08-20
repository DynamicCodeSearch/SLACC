package Y11R5P1.dooglius;

import java.io.*;
import java.util.*;
public class A{
	private static Scanner sc;
	public static void main(String[] args) throws Exception{
		sc = new Scanner(System.in);
		int t = sc.nextInt();
		for(int i = 1; i <= t; i++){
			System.out.println("Case #"+i+":");
			go();
		}
	}
	private static void go(){
		int w = sc.nextInt();
		int l = sc.nextInt();
		int u = sc.nextInt();
		int g = sc.nextInt();
		int[] lax = new int[l];
		int[] lay = new int[l];
		for(int i=0; i<l; i++){
			lax[i]=sc.nextInt();
			lay[i]=sc.nextInt();
		}
		int[] uax = new int[u];
		int[] uay = new int[u];
		for(int i=0; i<u; i++){
			uax[i]=sc.nextInt();
			uay[i]=sc.nextInt();
		}
		Trap[] arr=new Trap[w];
		double ly=lay[0],uy=uay[0];
		int nextl=1,nextu=1;
		double total=0;
		for(int x = 0; x < w; x++){
			if(x==lax[nextl])nextl++;
			if(x==uax[nextu])nextu++;
			double nly=ly+(lay[nextl]-ly)/(lax[nextl]-x);
			double nuy=uy+(uay[nextu]-uy)/(uax[nextu]-x);
			//System.out.println(ly+" "+uy+" "+nly+" "+nuy);
			arr[x]=new Trap(uy,ly,nuy,nly);
			total+=arr[x].area;
			ly=nly;
			uy=nuy;
		}
		for(int i=1; i<g; i++){
			System.out.println(findPoint(arr,i*total/g));
		}
	}
	private static double findPoint(Trap[] arr, double area){
		//System.out.println("Finding "+area);
		int i = 0;
		double buf=0;
		while(arr[i].area<area-buf && i<arr.length-1){
			buf+=arr[i++].area;
		}
		//System.out.println((area-buf)+" as part of #"+i+": "+arr[i].part(area-buf)+"+"+i);
		return arr[i].part(area-buf)+i;
	}
	private static class Trap{
		double left,right;
		double area;
		public Trap(double highy1, double lowy1, double highy2, double lowy2){
			left=highy1-lowy1;
			right=highy2-lowy2;
			area=(left+right)/2;
			//System.out.println("area: "+area);
		}
		public double part(double needed){
			if(Math.abs(right-left)<.000001) return needed/area;
			else return (Math.sqrt(left*left+2*needed*(right-left))-left)/(right-left);
		}
	}
}
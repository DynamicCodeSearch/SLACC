package Y14R5P1.sroyal;

import java.util.*;
public class a {
    public static void main(String[] args){
        Scanner br = new Scanner(System.in);
        int t = br.nextInt();
        for(int c = 1;c<=t;c++){
            int n = br.nextInt();
            long p = br.nextInt();
            long q = br.nextInt();
            long r = br.nextInt();
            long s = br.nextInt();
            long[] nums = new long[n];
            for(int i = 0;i<n;i++){
                nums[i] = (i*p +q)%r+s;
            }
            long[] rsum = new long[n];
            for(int i = 0;i<n;i++){
                if(i != 0){
                    rsum[i]+=(rsum[i-1]);
                }
                rsum[i]+=nums[i];
            }
            long best = 0;
            for(int i = 0;i<n;i++){
                int low = i;
                int high = n-1;
                long prefixSum = (i == 0 ? 0 : rsum[i-1]);
                while(high-low>1){
                    int mid = (high+low)/2;
                    long sum = (rsum[mid]-prefixSum);
                    long suffSum = rsum[n-1]-sum-prefixSum;
                    if(sum <= suffSum){
                        low = mid;
                    }
                    else{
                        high = mid;
                    }
                }
               
                for(int j = low;j<=high;j++){
                    long sum = (rsum[j]-prefixSum);
                    long suffSum = rsum[n-1]-sum-prefixSum;
                    long max = Math.max(sum, suffSum);
                    max = Math.max(max, prefixSum);
                    best = Math.max(best, rsum[n-1]-max);
                }
            }
            System.out.printf("Case #%d: %.10f\n", c, (best*1.0)/rsum[n-1]);
        }
    }
}

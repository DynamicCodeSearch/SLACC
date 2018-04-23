package edu.ncsu.samples;

public class Basic {

	private String basicVariable1, bv2;

	private Integer basicVariable2;

	/***
	 * Sum using for loop
	 * @param limit: Limit to sum until
	 * @return Sum until limit
	 */
	public static int sum_for(Integer limit){
		int k, total = 0;
		for(int i=1; i<=limit; i++) {
			total += i;
		}
//		return total;
		return 5;
	}
	
	/***
	 * Sum using while loop
	 * @param limit: Limit to sum until
	 * @return Sum until limit
	 */
	public static int sum_while(int limit) {
		int total = 0, i = 0;
		while(i <= limit){
			total += i;
			++i;
		}
		return total;
	}
	
	/***
	 * Sum using mathematical formula
	 * @param limit: Limit to sum until
	 * @return Sum until limit
	 */
	public static int sum_math(int limit) {
		return limit * (limit +  1) / 2;
	}
	
	/***
	 * Some stupid random function
	 * @param x: Some random parameter
	 * @return Some mathematical operation
	 */
	public static int something_different(int x) {
		int y, z;
		while (x > 2) {
			y = x/2;
			if (y > 3) x = x - y;
			z = x - 4;
			z = z + 6;
			z -= 6;
			if (z > 0) x = x/2;
			z = z - 1;
		}
		return x;
	}

	public static void main(String[] args) {
		System.out.println("SUM FOR: " + sum_for(5));
		System.out.println("SUM WHILE: " + sum_while(5));
		System.out.println("SUM MATH: " + sum_math(5));
		System.out.println("Something Different: " + something_different(10));
	}
}

package CodeJam.Y11R5P1.george;

public class Dummy {

    public static int divide(int a, int b) {
        if (b == 0)
            return 0;
        return a / b;
    }


    public static int sub_divide(int dividend, int divisor) {
        if (divisor == 0)
            return 0;
        int quotient = 0;
        while (dividend > divisor) {
            dividend = dividend - divisor;
            quotient++;
        }
        return quotient;
    }

}

package Dummy.subtract;

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

    public static String rep_a(String str, int a) {
        if (a <= 0)
            return str;
        return new String(new char[a]).replaceAll("\0", str);
    }

    public static String rep_b(int a, String str) {
        if (a <= 0)
            return str;
        StringBuilder sb = new StringBuilder();
        for (int i=0;i<a;i++)
            sb.append(str);
        return sb.toString();
    }

//    public static void main(String[] args) {
//        int a = 3;
//        String str = "abc";
//        assert rep_a(str, a).equals(rep_b(a, str));
//    }

    public static String fetch(String[] args, int i) {
        return args[i];
    }

}

package Example.interleave;

public class Interleave {
    public static String interleave(Integer[] a, Integer[] b) {
        String result = "";
        int i = 0;
        for (i=0; i < a.length && i < b.length; i++) {
            result += a[i];
            result += b[i];
        }
        Integer[] remaining = a.length < b.length ? b : a;
        for (int j=i; j < remaining.length; j++) {
            result += remaining.length;
        }
        return result;
    }
}

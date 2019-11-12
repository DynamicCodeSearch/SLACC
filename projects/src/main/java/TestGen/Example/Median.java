package TestGen.Example;

import java.util.Arrays;

class IntObj {

    public int value;

    public IntObj() {
    }

    public IntObj(int i) {
        value = i;
    }
}

class FloatObj {

    public float value;

    public FloatObj() {
    }

    public FloatObj(float i) {
        value = i;
    }
}

class LongObj {

    public long value;

    public LongObj() {
    }

    public LongObj(long i) {
        value = i;
    }
}

class DoubleObj {

    public double value;

    public DoubleObj() {
    }

    public DoubleObj(double i) {
        value = i;
    }
}

class CharObj {

    public char value;

    public CharObj() {
    }

    public CharObj(char i) {
        value = i;
    }
}


public class Median {

    public IntObj getMedian(IntObj a, IntObj b, IntObj c) {

        IntObj median = new IntObj();
        if ((a.value >= b.value && a.value <= c.value) || (a.value >= c.value && a.value <= b.value)) {
            median.value = a.value;
        }
        if ((b.value >= a.value && b.value <= c.value) || (b.value >= c.value && b.value <= a.value)) {
            median.value = b.value;
        } else {
            median.value = c.value;
        }
        return median;
    }

    public int median(int a, int b, int c) {
        if ((a > b && a <=c) || (a >= c && a <= b))
            return a;
        if ((b > a && b <= c) || (b >= c && b <= a))
            return b;
        return c;
    }
    static long func_4ab1 (Long[] arr) {
        Arrays.sort(arr);
        return arr[0];
    }
}



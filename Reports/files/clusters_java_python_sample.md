### Array Length

```
public static Integer func_27e3170c022a451692603ffed47fbcf0(Integer[] xxx) {
    int n = xxx.length;
    return n;
}
def func_40f170b11c494c5ca05133eda4cee7de(seq):
    rsum = 0
    rbegin = len(seq)
    return rbegin
```

### Average Area

```
public static Double func_56a4af83dadc4270b11914b2c73ce8c6(Long s, Integer g) {
    double gs = 1.0 * (double) s.longValue() / (double) g.intValue();
    return gs;
}
def func_7aa108c55a064628afbb367e9e7a206e(area, G):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    return part
```

### Subtraction

```
public static Integer func_231ab8904358494c8a37df8b7e9eaac9(Integer t) {
    int h = t - 1;
    return h;
}
def func_f63cca139311488eb5f4bbdc9c087b9d(N):
    a_lo = 0
    a_hi = N - 1
    return a_hi
```


### Array Sum
```
public static Long func_c5ad96721f624071bf9720a66fafbe7b(Long sl, Long[] a2) {
    long sm = a2[0];
    long sr = 0L;
    for (int i = 1; i < a2.length; ++i) {
        sr += a2[i].longValue();
    }
    long sum = sm + sr;
    long ans = Math.max(sm, sr);
    int l = 0;
    for (int r = 1; r < a2.length; ++r) {
        sm += a2[r].longValue();
        sr -= a2[r].longValue();
        while (l < r && Math.max(sl + a2[l], sm - a2[l]) < Math.max(sl, sm)) {
            sl = sl + a2[l];
            sm -= a2[l].longValue();
            ++l;
        }
        ans = Math.min(ans, Math.max(sr, Math.max(sm, sl)));
    }
    return sum;
}
def func_06f8a9ef4fb844ef82161d2847cdb925(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return allv
```

### Minimum in Array
```
public static long func_3b0e83fe0a194e82a1ab62d5cbaf086d(Long[] x2) {
    long res = Long.MAX_VALUE;
    Long[] arr$ = x2;
    int len$ = arr$.length;
    for (int i$ = 0; i$ < len$; ++i$) {
        long xx = arr$[i$];
        if (xx >= res)
            continue;
        res = xx;
    }
    return res;
}
def func_64370f211be94eb09baf3bf3468e6614(y):
    ymin = min(y)
    count = 0
    return ymin
```

### Maximum in Array
```
public static Long func_2f2aba615b114279bb22a9ee61a113f7(Long[] values) {
    long max = values[0];
    for (int i = 1; i < values.length; ++i) {
        if (max >= values[i])
            continue;
        max = values[i];
    }
    return max;
}
def func_fc1df07e5f3644499d33685ea449984b(x):
    lo = min(x)
    hi = max(x)
    return hi
```



## Stats
### Cluster sizes
* Number of clusters: 1185
* Number of functions clustered: 4180
* Number of functions not clustered: 2248

### REPORT
```
       Min : 2
      Mean : 3.5
    Median : 2
       Max : 94
       std : 4.04
       iqr : 2
```
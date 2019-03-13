

WRONG = False

def comp(c, m):
    b = 0
    for i in range(c):
        b += m - Xs[i]


    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]

    if b > B:
        return WRONG

    return 36 * gain / c - b



def solve(infile):
    global B, N, Xs
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))

    ans = 0

    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m

    return ans

def _main():
    infile = open("test_files/Y13R5P1/A.in")
    T = int(infile.readline())
    for tn in range(T):
        print("Case #{0}: {1:.10f}".format(tn + 1, solve(infile)))
    infile.close()


if __name__ == "__main__":
    _main()

def nums(infile, t=int):
    return map(t, infile.readline().strip().split())


def _main():
    infile = open("codejam/test_files/Y14R5P1/A.in")
    z = int(infile.readline())
    for cas in xrange(1,z+1):
        n, p, q, r, s = nums(infile)
        v = [(i*p+q)%r+s for i in xrange(n)]
        sums = [0]*(n+1)
        for i in xrange(n):
            sums[i+1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1,n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i]-sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L],sums[i]-sums[L],sums[n]-sums[i]), max(sums[R],sums[i]-sums[R],sums[n]-sums[i]))

        print "Case #%s: %.10f" % (cas, 1 - float(ans)/sums[n])
    infile.close()


if __name__ == "__main__":
    _main()

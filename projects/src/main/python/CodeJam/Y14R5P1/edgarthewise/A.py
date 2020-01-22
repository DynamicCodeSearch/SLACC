#!/home/edgar/pypy/bin/pypy
from numpy import *


def _main():
    infile = open("codejam/test_files/Y14R5P1/A.in")
    T = int(infile.readline())
    for t in range(1,T+1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]

        NT = (arange(N, dtype=int64)*p+q)%r+s
        PS = array([0] + list(cumsum(NT)), dtype=int64 )
        S = PS[-1]

        minmax = S

        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1+(S-s1)/2.0)
            assert b0 >= a
            for b in (b0-1,b0):
                if 0<b and b<=N:
                    mx = max(s1, PS[b]-PS[a], S-PS[b])
                    if mx < minmax:
                        minmax = mx

        print "Case #"+str(t)+":",float(S-minmax)/S
    infile.close()


if __name__ == "__main__":
    _main()

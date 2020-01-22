

import sys


def computeEtries(p):
    pr = p / 100.0
    re = 1
    running = pr
    multiplier = 2
    while multiplier < 10000 or multiplier*running > 1e-9:
        re += multiplier*running
        running *= pr
        multiplier += 1
    return (1-pr)*re



def _main():
    ets = [computeEtries(p) for p in range(100)]
    infile = open("codejam/test_files/Y12R5P1/A.in")
    T = int(infile.readline())

    for tcase in range(T):
        N = int(infile.readline())
        Ls = map(int, infile.readline().split())
        Ps = map(int, infile.readline().split())

        etries = [ets[p] for p in Ps]
        seq = [(index, Ls[index], etries[index]) for index in range(N)]
        for k in range(N):
            best = k
            for s in range(k+1, N):
                in1 = seq[best][0]
                L1 = seq[best][1]
                E1 = seq[best][2]

                in2 = seq[s][0]
                L2 = seq[s][1]
                E2 = seq[s][2]

                extra_if_1_goes_first = (E2-1)*E1*L1
                extra_if_2_goes       = (E1-1)*E2*L2
                if abs(extra_if_1_goes_first - extra_if_2_goes) < 1e-9:
                    if in2 < in1:
                        best = s
                elif extra_if_2_goes < extra_if_1_goes_first:
                    best = s

            swap = seq[best]
            seq[best] = seq[k]
            seq[k] = swap

        print "Case #%d:" % (tcase+1),
        print ' '.join(map(str, [seq[i][0] for i in range(N)]))
    infile.close()

if __name__ == "__main__":
    _main()

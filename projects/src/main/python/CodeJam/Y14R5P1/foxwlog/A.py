
from __future__ import division

def in_range(a, b, S):
    return S[b+1] - S[a]

def compute(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    # store partial sums in S[]
    S = [0] * (N+1)
    S[0] = 0
    for i in range (0, N):
        S[i+1] = (p*i+q)%r + s + S[i]
    # binary search a
    a_lo = 0
    a_hi = N-1
    min_solveig_score = S[N] + 1 # not set yet
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        # binary search b
        b_lo = a_try
        b_hi = N-1
        min_max_mid_hi = S[N] + 1 # not set yet
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try+1] - S[a_try]
            hi_range = S[N] - S[b_try+1]
            # update minimum:
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        # update the minimum
        min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break

    return ("%1.10f" % (1 - min_solveig_score / S[N]))

def _main():
    infile = open("codejam/test_files/Y14R5P1/A.in")
    num_trials = int(infile.readline())
    for i in range (0, num_trials):
        print("Case #" + str(i+1) + ": " + str(compute(infile)))
    infile.close()


if __name__ == "__main__":
    _main()

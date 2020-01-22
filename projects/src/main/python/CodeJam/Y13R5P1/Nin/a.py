#!/usr/bin/edu.ncsu.python3




def profit(my, X, loss):
    ans = -loss
    outcome = min([my[i] + X[i] for i in range(37)])
    pos = [i for i in range(37) if my[i] + X[i] == outcome]
    N = len(pos)
    for p in pos:
        ans += my[p]*36 / N
    return ans

def solve(B, N, X):
    while len(X) < 37:
        X.append(0)
    X.sort()
    my = [0 for i in range(37)]
    #print(X)
    #print(my)
    max_profit = profit(my, X, 0)
    for i in range(1, B+1):
        m = 0
        for j in range(1, 37):
            if my[j] + X[j] < my[m] + X[m]:
                m = j
            elif my[j] + X[j] == my[m] + X[m]:
                if my[j] < my[m]:
                    m = j
        # place coin on m
        my[m] += 1
        p = profit(my, X, i)
        if p > max_profit:
            max_profit = p
    return max_profit

def _main():
    infile = open("codejam/test_files/Y13R5P1/A.in")
    T = int(infile.readline())
    for test_case in range(1, T+1):
        B, N = map(int, infile.readline().strip().split(' '))
        X = list(map(int, infile.readline().strip().split(' ')))
        print("Case #{0}: {1}".format(test_case, solve(B, N, X)))
    infile.close()

if __name__ == "__main__":
    _main()

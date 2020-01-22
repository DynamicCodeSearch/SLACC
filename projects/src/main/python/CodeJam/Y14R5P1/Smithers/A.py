from __future__ import division

def _main():
    infile = open("codejam/test_files/Y14R5P1/A.in")
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]

        dev = [(i * p + q) % r + s for i in range(n)]
        #print(dev)

        tot = sum(dev)
        i = 0
        j = n-1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0

        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))

        print('Case #' + str(ti) + ':', best / tot)
    infile.close()

if __name__ == "__main__":
    _main()

#!/usr/bin/env python

def _main():
    infile = open("codejam/test_files/Y12R5P1/A.in")
    T = int(infile.readline())
    for t in range(1, T + 1):
        n = int(infile.readline())
        l = map(int, infile.readline().split())
        p = map(int, infile.readline().split())
        a = zip(l, p, range(n))
        a.sort(lambda x, y: x[0] * y[1] - x[1] * y[0])
        print 'Case #%d:' % t,
        for x in a:
            print x[2],
        print
    infile.close()


if __name__ == '__main__':
    _main()

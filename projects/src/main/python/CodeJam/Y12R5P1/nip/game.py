#! /usr/bin/env python

import numpy as np


def _main():
    infile = open("codejam/test_files/Y12R5P1/A.in")
    ntest = int(infile.readline())
    for test in range(ntest):
        n = int(infile.readline())
        l = np.array([int(i) for i in infile.readline().strip().split()])
        p = np.array([int(i) for i in infile.readline().strip().split()])
        res = ['%d' % i for i in np.argsort(-p, kind='mergesort')]
        print "Case #%d: %s" % (test+1, ' '.join(res))
    infile.close()

if __name__ == "__main__":
    _main()

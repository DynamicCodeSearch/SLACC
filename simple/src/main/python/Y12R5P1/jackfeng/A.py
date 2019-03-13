#!/usr/bin/python
#coding: utf-8

import os, sys
import math
from operator import itemgetter

def solve(input):
    def split(func, sep=' '):
        return map(func, input.readline().strip().split(sep))

    def cmp_fun(i1, i2):
        if i1[2] != i2[2]:
            return -1 if i1[2] > i2[2] else 1
        elif i1[1] != i2[1]:
            return -1 if i1[1] > i2[1] else 1

        return -1 if i1[0] < i2[0] else 1

    split(int)
    L = split(int)
    P = split(int)

    #items = sorted(zip(range(len(L)), L, P), cmp=lambda i1, i2: i1[2] > i2[2] or (i1[2] == i2[2] and i1[1] > i2[1]) or (i1[2] == i2[2] and i1[1] == i2[1] and i1[0] < i2[0]))
    items = sorted(zip(range(len(L)), L, P), cmp=cmp_fun)
    return ' '.join(map(lambda i: str(i[0]), items))

def _main():
    with open("test_files/Y12R5P1/A.in", 'r') as input:
        T = int(input.readline().strip())
        for t in range(1, T+1):
            print 'Case #%d: %s' % (t, solve(input))

if __name__ == '__main__':
    _main()

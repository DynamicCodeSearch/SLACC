#!/usr/bin/python

from sys import stdin, stderr

def line(infile):
	return map( int, infile.readline().strip().split() )

def getsum(a,b, total, totalsum):
	kA = totalsum[a-1] if a > 0 else 0
	kB = totalsum[b] - kA
	kC = total - totalsum[b]
	return max(kA, kB, kC)

def _main():
	infile = open("codejam/test_files/Y14R5P1/A.in")
	T, = line(infile)
	for T in xrange(1,T+1):
		N, p, q, r, s = line(infile)
		A = [ (i*p+q) % r + s for i in xrange(N) ]

		total = sum(A)
		totalsum = [ a for a in A ]
		for i in xrange(1,N):
			totalsum[i] += totalsum[i-1]


		best = total
		b = 0
		for a in xrange(N):
			if b < a:
				b += 1
			while b < N-1 and getsum(a,b, total, totalsum) >= getsum(a,b+1, total, totalsum):
				b += 1

			best = min( best, getsum(a,b, total, totalsum) )

		best = total - best

		print >>stderr, 'Case #%d' % T
		print 'Case #%d: %.10f' % (T, 1.0*best/total)
	infile.close()

if __name__ == "__main__":
	_main()

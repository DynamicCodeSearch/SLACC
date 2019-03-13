#!/usr/bin/python

def get(infile, f=int):
	return map(f, infile.readline().split())


def _main():
	infile = open("test_files/Y14R5P1/A.in")
	T, = get(infile)

	for testCase in range(1, T+1):

		N, p, q, r, s = get(infile)
		t = [(i * p + q) % r + s for i in range(N)]
		total = sum(t)
		c = [0]
		for x in t:
			c.append(c[-1] + x)

		a = b = 0
		best = 0

		while b <= N:
			if a == b or c[b] - c[a] <= total / 3:
				b += 1
				if b > N:
					break
			else:
				a += 1

			best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))

		print "Case #%d: %.10f" % (testCase, float(best) / float(total))
	infile.close()

if __name__ == "__main__":
	_main()

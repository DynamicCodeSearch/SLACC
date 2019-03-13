from sys import stdin

def getans(a, b):
  tmp = a.index(min(a))
  a[tmp] += 1
  b[tmp] += 1
  m = min(a)
  res = 0.0
  k = 0
  for i in xrange(37):
    if a[i] == m:
      res += 36.0*b[i]
      k += 1
  res /= k
  return res


def _main():
  infile = open("test_files/Y13R5P1/A.in")
  T = int(infile.readline())
  for _ in xrange(1, T+1):
    B, N = map(int, infile.readline().split())
    a = map(int, infile.readline().split())
    a.extend([0] * (37-N))
    b = [0]*37
    ans = 0.0
    for i in xrange(B): ans = max(ans,getans(a, b) - (i+1))
    print 'Case #%d: %f' % (_, ans)
  infile.close()

if __name__ == "__main__":
  _main()

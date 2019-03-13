
def _main():

  infile = open("test_files/Y12R5P1/A.in")
  T = int(infile.readline())

  for t in range(1, T+1):
    n = int(infile.readline())
    L = map(int, infile.readline().strip().split())
    P = map(int, infile.readline().strip().split())

    l = []
    for i, p in enumerate(P):
      if p != 0:
        l.append((float(L[i]) / p, i));
      else:
        l.append((1E30, i));
    l.sort()

    print 'Case #%d: ' % t,
    for p, i in l:
      print i,
    print ''
  infile.close()

if __name__ == "__main__":
  _main()
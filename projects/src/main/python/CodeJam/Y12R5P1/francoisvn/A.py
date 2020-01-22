#!/usr/bin/python

def _main():
  infile = open("codejam/test_files/Y12R5P1/A.in")

  T = int(infile.readline())
  for t in range(T):
    N = int(infile.readline())

    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
      L.append(float(tok))

    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
      P.append(float(tok)/100)

    #print
    #print N,L,P

    E = []
    for i in range(N):
      e = 1.0/(1-P[i])
      E.append(e)
    #print "E:",E

    X = []
    for i in range(N):
      x=L[i]*E[i]
      if E[i]==1:
        x=0
      X.append([x,-i])

    #print "X:",X
    X.sort(reverse=True)
    #print "X:",X

    print "Case #%d:" % (t+1),
    for x in X:
      print (-x[1]),
    print
  infile.close()

if __name__ == "__main__":
  _main()

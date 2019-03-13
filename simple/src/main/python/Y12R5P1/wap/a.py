def alphabet(n, l, p):
    v = []
    for i in xrange(n):
        v.append((-p[i], i))
    v.sort()
    return " ".join([str(j[1]) for j in v])

def _main():
    fn = open("test_files/Y12R5P1/A.in","r")
    tcase = int(fn.readline())
    for x in range(tcase):
        ab = int(fn.readline())
        kk = fn.readline()
        zl = [int(k) for k in kk.split()]
        kk = fn.readline()
        zp = [int(k) for k in kk.split()]
        print "Case #%d: %s" % (x+1, alphabet(ab,zl,zp))
    fn.close()

if __name__ == "__main__":
    _main()

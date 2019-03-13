
def _main():
	infile = open("test_files/Y12R5P1/A.in")
	testCount = int(infile.readline())
	for testIndex in range(testCount):
		ans = "Case #" + str(testIndex+1) + ": "
		n = int(infile.readline())
		l = [int (x) for x in infile.readline().split(" ")]
		p = [int (x) for x in infile.readline().split(" ")]
		a = []
		for i in range(n):
			a += [[i, 1.0 * p[i] / l[i], l[i]]]
		a.sort(key = lambda x:-x[1])
		for i in a:
			ans += str(i[0]) + " "
		print (ans )
	infile.close()

if __name__ == "__main__":
	_main()

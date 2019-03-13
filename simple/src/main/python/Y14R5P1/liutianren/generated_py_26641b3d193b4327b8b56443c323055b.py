import sys
sys.path.append('/home/george2/Raise/ProgramRepair/CodeSeer/projects/src/main/python')
from Y14R5P1.liutianren.pa import *

def func_b7ac5fe003534a369b5aec00bcdd371b(A, q, p, r, i, s):
    a = s + (i * p + q) % r
    A.append(a)
    return a


def func_4f647da57d784845a69b2374612069c0(a, A):
    A.append(a)
    psum = psum + a
    return psum


def func_805366c712b34cf3a55833bd94fec175(a, S):
    psum = psum + a
    S.append(psum)
    return psum


def func_0fe8cbfa557948b39902d154be091bcf(A, q, p, r, i, s):
    a = s + (i * p + q) % r
    A.append(a)
    psum = psum + a
    return a


def func_7795ba23206e4560bafd9f913baf3c8a(A, q, p, r, i, s):
    a = s + (i * p + q) % r
    A.append(a)
    psum = psum + a
    return psum


def func_32c92e553af945d3a2fbfd4259b5c95b(a, S, A):
    A.append(a)
    psum = psum + a
    S.append(psum)
    return psum


def func_731daa6475a7445f9c6f5e8c3133e4d4(S, A, q, p, r, i, s):
    a = s + (i * p + q) % r
    A.append(a)
    psum = psum + a
    S.append(psum)
    return a


def func_aaab17d8f8834d589b74673642ef8123(S, A, q, p, r, i, s):
    a = s + (i * p + q) % r
    A.append(a)
    psum = psum + a
    S.append(psum)
    return psum


def func_9c5c57414433474fb461d57fbba6e671(S, i, j, psum):
    pgain = max(S[j], S[i] - S[j])
    gain = max(S[j], S[i] - S[j], psum - S[i])
    return pgain


def func_5abf7ed201f04c6f9ab63dfd863a3624(S, i, j, psum):
    pgain = max(S[j], S[i] - S[j])
    gain = max(S[j], S[i] - S[j], psum - S[i])
    return gain


def func_cc55eea84363492abd4d457ef335dfe4(S, i, j, psum):
    gain = max(S[j], S[i] - S[j], psum - S[i])
    mingain = min(mingain, gain)
    return gain


def func_5583bc2bfbdb436db8006cebb69b11c4(S, i, j, psum):
    gain = max(S[j], S[i] - S[j], psum - S[i])
    mingain = min(mingain, gain)
    return mingain


def func_0a4392010bd24f578a84b2444754ce88(pgain, minpgain):
    if pgain <= minpgain:
        hpi = j
    j = j + 1
    return j


def func_506a234433784793b52c21382bdec6ac(pgain, minpgain):
    if pgain <= minpgain:
        hpi = j
    j = j + 1
    return hpi


def func_347a606abae24f739b8a7473ba73b1a7(S, i, j, psum):
    pgain = max(S[j], S[i] - S[j])
    gain = max(S[j], S[i] - S[j], psum - S[i])
    mingain = min(mingain, gain)
    return pgain


def func_6cffab610bd843b7b0494046bcfac49b(S, i, j, psum):
    pgain = max(S[j], S[i] - S[j])
    gain = max(S[j], S[i] - S[j], psum - S[i])
    mingain = min(mingain, gain)
    return gain


def func_7189b258ca134403aa7d3bf71740e5eb(S, i, j, psum):
    pgain = max(S[j], S[i] - S[j])
    gain = max(S[j], S[i] - S[j], psum - S[i])
    mingain = min(mingain, gain)
    return mingain


def func_e2e18e56ee1644a68e352ce4c48a225a(S, i, minpgain, psum):
    j = hpi
    while j <= i:
        pgain = max(S[j], S[i] - S[j])
        gain = max(S[j], S[i] - S[j], psum - S[i])
        mingain = min(mingain, gain)
        if 2 * S[j] > S[i]:
            break
        if pgain <= minpgain:
            hpi = j
        j = j + 1
    return mingain


def func_3b6d7b1706644a4e8cd02b41d3501401(S, i, minpgain, psum):
    j = hpi
    while j <= i:
        pgain = max(S[j], S[i] - S[j])
        gain = max(S[j], S[i] - S[j], psum - S[i])
        mingain = min(mingain, gain)
        if 2 * S[j] > S[i]:
            break
        if pgain <= minpgain:
            hpi = j
        j = j + 1
    return pgain


def func_6a6100622f5e46bba745b1e199d314a2(S, i, minpgain, psum):
    j = hpi
    while j <= i:
        pgain = max(S[j], S[i] - S[j])
        gain = max(S[j], S[i] - S[j], psum - S[i])
        mingain = min(mingain, gain)
        if 2 * S[j] > S[i]:
            break
        if pgain <= minpgain:
            hpi = j
        j = j + 1
    return hpi


def func_41cc33d58cce46d7971c77c39b92db74(S, i, minpgain, psum):
    j = hpi
    while j <= i:
        pgain = max(S[j], S[i] - S[j])
        gain = max(S[j], S[i] - S[j], psum - S[i])
        mingain = min(mingain, gain)
        if 2 * S[j] > S[i]:
            break
        if pgain <= minpgain:
            hpi = j
        j = j + 1
    return j


def func_080f0976862642d28c2044a7e5976039(S, i, minpgain, psum):
    j = hpi
    while j <= i:
        pgain = max(S[j], S[i] - S[j])
        gain = max(S[j], S[i] - S[j], psum - S[i])
        mingain = min(mingain, gain)
        if 2 * S[j] > S[i]:
            break
        if pgain <= minpgain:
            hpi = j
        j = j + 1
    return gain


def func_fc05b86451c349c7ae796b718afaff94():
    A = []
    S = []
    return S


def func_4b5407d3d9044c3896063344877f24b4():
    A = []
    S = []
    return A


def func_f6857b2da9c04116b182776d5013a697():
    S = []
    psum = 0
    return S


def func_2a11215d766d419e9661804ade01216d():
    S = []
    psum = 0
    return psum


def func_f7ecc06fdbc64a7592ff48fbf217c363(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    return i


def func_719669b4b6bd47ca87a107ad08579a7b(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    return psum


def func_a497461c9b7c4268bd5ff98afa1a682d(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    return a


def func_749938a23d494c0f860ed0f702a99efa(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    return a


def func_f26a3f234ba84f8d82c074dea317ffed(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    return i


def func_4e075b6e59cc415daca8eb5eb2bc2837(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    return psum


def func_1cea03d2442c41798726dd74d8d9a32f(psum):
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    return mingain


def func_0790d9e81a734e8d9aa03f63607f8e2b(psum):
    mingain = psum
    minpgain = psum
    return mingain


def func_c73315b5aa644f0eb7454e6a004a25b7(psum):
    mingain = psum
    minpgain = psum
    return minpgain


def func_efa98545c3854f92960d5c1a6fdbba81(psum):
    minpgain = psum
    hpi = 0
    return hpi


def func_8024920ec57044969cc1e0f764d7dd39(psum):
    minpgain = psum
    hpi = 0
    return minpgain


def func_e6d029c2fb5a421b8bc02f71d9910742(N, S, minpgain, psum):
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return mingain


def func_42184e20e80e435199203dd2d8bafbbb(N, S, minpgain, psum):
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return gain


def func_2ddde746d5d647029870f1e7d940f646(N, S, minpgain, psum):
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return hpi


def func_da72f6bed5904a43927491e518026c74(N, S, minpgain, psum):
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return pgain


def func_01d58ea91fb649898ea070248347a561(N, S, minpgain, psum):
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return j


def func_60a9cbb9e203427e8fbf6d2e02204fea(N, S, minpgain, psum):
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return i


def func_43c19d6aafa24da589108f895b791812(N, S, minpgain, psum):
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return float(psum - mingain) / psum


def func_a66c2b6a5ae544a9a10c5717d5147b44():
    A = []
    S = []
    psum = 0
    return S


def func_d711fb2c4bb5408f964a716fd2760123():
    A = []
    S = []
    psum = 0
    return A


def func_bab063a390034a3e907260a91ddb0ba0():
    A = []
    S = []
    psum = 0
    return psum


def func_89520863509241c6938cc799077e71ed(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    return S


def func_2eafe3a7702d46ee88136df8edf45be5(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    return psum


def func_a233020961ec4e3eae425a094fe17764(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    return a


def func_ac51824063474411834cf9cbce6da70c(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    return i


def func_b4990af39135459d96c62595ee20b9ab(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    return i


def func_c449ec15464342e791ff3eacdb9abe1c(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    return psum


def func_3f712eb9fb00484188a1911dd770f454(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    return a


def func_81480aa91a6f42e282dffc0689cc6bbd(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    return a


def func_27824dc4cda1459eaf436c38092b006e(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    return mingain


def func_d2d49cb5c9aa4dd3b4ad0f2c3f17a3e1(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    return i


def func_fdf9d2a17a5d4f4fa86afd0084854b96(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    return psum


def func_b9cdaf3512f0487aa615150415b3eca9(psum):
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    return mingain


def func_dc400d407d514c66a0f00e41e8c416cc(psum):
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    return minpgain


def func_30abd218827d43d7ae7a1ba1f3b77afa(psum):
    mingain = psum
    minpgain = psum
    hpi = 0
    return minpgain


def func_57491aff8a7840fea20c04eb0465b1f4(psum):
    mingain = psum
    minpgain = psum
    hpi = 0
    return mingain


def func_057827decc524a3aa78b85e46c591133(psum):
    mingain = psum
    minpgain = psum
    hpi = 0
    return hpi


def func_e175c84bbb9e46a285c606fc1873e674(N, S, psum):
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return i


def func_7f4d45d037504a43952508ff400301ce(N, S, psum):
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return hpi


def func_d13c64122028415fa348138c5337f1a2(N, S, psum):
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return minpgain


def func_2c8d66b8e8494d7da50b3d0e55d7ed02(N, S, psum):
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return mingain


def func_36f780ec8fff4214a3d0d7e62811a8d6(N, S, psum):
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return gain


def func_56066b587d3542c79fbb1596310a0786(N, S, psum):
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return j


def func_c06ca9718d47411abe8e36bf61c063a2(N, S, psum):
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return pgain


def func_70a13f5600474ac199539dba7b92e4a7(N, S, minpgain, psum):
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return float(psum - mingain) / psum


def func_b47615c3c44b4e7b8e8b79bf9b340fe7(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    return i


def func_f25ec8382d17431a933c4425dbad69a6(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    return A


def func_92a7c17153554f5a8b888f0c99ccc908(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    return S


def func_c08cef70440541c4b5d7325f9778ff67(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    return psum


def func_8f3714cfe25f4fdf991d5f2e8c5b24d4(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    return a


def func_e1eb75ae65ec4a39af2292add3aa0f16(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    return i


def func_0eb884871b7246b5b153eae1c91876e0(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    return psum


def func_89ea100f3f1d4d37bdcc86501d628aa5(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    return S


def func_52f1bb55fd0a4989b6ae8428f0bfd465(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    return a


def func_b5e47067f352460981a68e75ac3b488a(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    return psum


def func_a23f31349fff479da49c4318b8638a1e(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    return mingain


def func_9b97e855cb174e73aee12347d68e4f27(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    return a


def func_2217146b87934627b2d3ed27e7420c84(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    return i


def func_5029b157c9f84c9898c818c24fc84347(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    return a


def func_a0339e408849463c800a71a954f796ea(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    return mingain


def func_83059db1c85e426eb8b59f8808e915bb(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    return i


def func_614ea52b7064488a8de8a98ca6994015(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    return psum


def func_28690fd1eb864bd094f2d2bc5b3ec402(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    return minpgain


def func_dd24e6726a204177870c5e212346dfc4(psum):
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return minpgain


def func_7960889ab9c74e799253a4e83fed7fbb(psum):
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return mingain


def func_cf48a6db17b744bfbb8c939da541da93(psum):
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return hpi


def func_a7a0219037b94fe0b320520dcd8e4466(N, S, psum):
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return pgain


def func_69794909e1c34da5972885ad766e0c8c(N, S, psum):
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return gain


def func_4efbaf10483540bc969bfa12fc937ea4(N, S, psum):
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return hpi


def func_aa2da8ae23014a5a9eb08730f0af5440(N, S, psum):
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return mingain


def func_2cc3e049fe7a4969a68a4b3008c96377(N, S, psum):
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return j


def func_8231678d745d4f19b9761387a05eebce(N, S, psum):
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return i


def func_03d3eac3541d4b5690de20bf0848fcc2(N, S, psum):
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return minpgain


def func_9460447054f641a6bc1cce0105fd27cf(N, S, psum):
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return float(psum - mingain) / psum


def func_d0a08a9821a64712bb2ced4e603e702f(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    return S


def func_b709b84b68824f22ba16b7ec98ff8702(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    return psum


def func_2c4be757d97e49a59bfaa1fc43c50a27(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    return A


def func_02d871b3726d4e88b940c88e61b44ff7(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    return i


def func_46b38e1011024e409327e7f6b5ff25a9(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    return a


def func_04266cae184b41ba86d02095dd29f6a2(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    return S


def func_7152470275014f658fa59b4cdaeaea92(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    return psum


def func_b48c882d8e85448c958300c276cfa67e(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    return a


def func_4ffd2cd609444843856cca8538fac343(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    return mingain


def func_1439a4d9e7c64cdd9bd7077ac3a59089(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    return i


def func_5daf051d00124fd0a639fc7f54b08a09(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    return minpgain


def func_1354288ccba84eed8ae92c512dac9a21(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    return a


def func_0cfb74f92a4e4baf8f392b0dd53a8708(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    return psum


def func_c028c7ad92004fe2b2372c862cb6ab5d(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    return mingain


def func_ef7c8b79e2c845a18f0fee457574ebd2(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    return i


def func_a1551ae7b9114cb08a9b6a3ea97b8abb(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return mingain


def func_07f3c89b0c584115a6680d70d82b2926(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return a


def func_c0538a6420194a83b0b383c39d2da05f(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return psum


def func_9de1b83b1eca42b7b6bebe67ed3903e4(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return hpi


def func_e0f0f052e14146c29ca1590a758acfa3(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return minpgain


def func_fd26edd4faf84deab13e8c40cb29e74f(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return i


def func_b3241811d60546289bdf7ee6fc9e20c7(N, S, psum):
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return j


def func_f937227ddfbc44dfa4dfe19838e3412c(N, S, psum):
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return pgain


def func_383d4bcf3d164e2797ac6d9e6de1741e(N, S, psum):
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return mingain


def func_238f1c452ea24086bd8c32190fffacf9(N, S, psum):
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return i


def func_9d91769de67448d2906e79d06cb05b55(N, S, psum):
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return minpgain


def func_d78fe9e4de30454cb8414e541a287f97(N, S, psum):
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return gain


def func_75109454bd8a45a283aca541cd94e2ba(N, S, psum):
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return hpi


def func_68bead40c66f48fdb5a670a3f2750593(N, S, psum):
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return float(psum - mingain) / psum


def func_f5962c052a794db48324e97566dfb89c(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    return a


def func_1830a3211fcf43318b039339a80d9ac0(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    return A


def func_5002d93c3ef046ffb9a973244d8c3e32(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    return i


def func_22ad3aae2a344fa497050d0a3edd8b84(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    return mingain


def func_f1a3569dd8924799be146a79bee1a0d5(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    return psum


def func_7f91a1185a474a76bfdb5d8a16e3b9ae(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    return S


def func_d91c9a4c0a9a496989efba0bda01db50(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    return S


def func_0db2f7f158824d4696913c2298349c87(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    return minpgain


def func_edec0b6f897941cabcea81d590e0c42d(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    return a


def func_2693877005bc425bb5d10d50ba184b66(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    return mingain


def func_1ce5638f9bdd4f8aba7b70dc06e5b47f(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    return i


def func_66e6367549a14b1ea1af5a9fdf4a18f2(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    return psum


def func_fbc8600b5e19405494a9e67aff3e958c(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return hpi


def func_87d5f065e44c43d5a92d0865ce67b846(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return a


def func_4e43a58b6a98411a9807218eef1737ea(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return mingain


def func_d6685b452db2449f808a44b0134871c2(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return minpgain


def func_38244230e4e1401b95efbb92e53bda2e(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return psum


def func_31c61452d8d042e5987f7c997a9e82fd(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return i


def func_615debe1e52c4d5e9c45b79969794e81(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return j


def func_80c1841ab60c4ca1aff6524d5392324b(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return psum


def func_e714ff5f98e04d81b84a009f24311324(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return mingain


def func_f9fcba341f564c719cee8c10a032a601(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return pgain


def func_4936dd9d4f07490e8cc9cc49604d3768(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return a


def func_9d6a3f375ce746cbbca5831b3322a123(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return i


def func_25823d7a17fe4a0d9d7274801a34c785(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return gain


def func_11f18fe4e49544389c0b1b0080a9bbc3(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return minpgain


def func_77b0dd0f5ece42d8bdb602d57aa8d0d9(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return hpi


def func_bfca667e3c6c48a0856c692d8a707e80(N, S, psum):
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return float(psum - mingain) / psum


def func_a1219e3a67b64b6c84d15b38f19bdc0f(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    return psum


def func_5fb2311d68394da088bbb77042ae3f39(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    return a


def func_5baf0148fdbc41c5a0884af3c8b9488b(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    return A


def func_6f530fbee79943b1941bd8d51128f7ad(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    return mingain


def func_14b40d2d5796402bb55efe34c514758d(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    return i


def func_969a285cfd9042ab88335e7ed7b4df66(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    return S


def func_59a299a5ebcf4967a956d9d122584dba(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    return minpgain


def func_e304ea182c4b42999a07238ef4fc8a44(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return a


def func_0b5a8e2f2eee466d8ae95c6f156cae38(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return hpi


def func_03347800e1b44621be7ac99d75e51117(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return minpgain


def func_10bb7af27bbd4273ac65078cfb075a37(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return S


def func_f44bff9274064b568f97c4d9cb7c22a2(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return mingain


def func_163d112482f546ac8b79335b3e42388d(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return i


def func_802d188bb9dd4f0fa2e896e30ac6940f(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return psum


def func_36afc1157b3a4d98973283c89e551c95(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return a


def func_34db1e8092a14fa8bb6106c1aead6c2d(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return i


def func_22b6c464349b459198d3f0a1c2878bb4(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return pgain


def func_7b4840b9ffdc410eacaea1af315eba1c(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return gain


def func_ec4a1bd36c564bdab45625216eddba75(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return psum


def func_5d2c937a2b9f4e78b187542550dc2517(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return mingain


def func_88933903641a4219bfcd3fe481eccb77(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return minpgain


def func_3b0afafda89a43e2bb3a9980d5bb8f82(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return hpi


def func_a37cc5227aa7488a9be87102c356b008(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return j


def func_2eb67baef7324be29129845893004761(N, S, A, q, p, r, s):
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return float(psum - mingain) / psum


def func_f266123b0c4846998dd359ed4bdb5b84(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return psum


def func_925a3ebc9fd440a482fdf727841ae576(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return A


def func_adbbf3b510fd40d4b4e6214ec6b2e658(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return S


def func_714d2f270e304256a669a737f70b05ec(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return mingain


def func_023b1282d89b4658a884376e64c37278(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return minpgain


def func_2af9cbec022e44c89e114a5ce4b48ef0(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return i


def func_2f109fa61b7546c6856d48d9e2769ffc(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return a


def func_71142994bb33474398dea0fc8f2a326e(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    return hpi


def func_7058c4e1ed1d44e89960c28f84290b4f(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return gain


def func_6579940ed29f481794db86541902a629(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return minpgain


def func_c3fe3ca4797c4f7885494ad61968c3c6(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return hpi


def func_7d23a97a960e4b70ab90c416cb5dc552(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return psum


def func_ca17dd55efb041c7a2849793e25916ab(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return a


def func_f9d0fe1c076f46f193c2517448dac04a(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return pgain


def func_016dfbfebd444e53b2f148aff80505dc(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return i


def func_34ad324c059547b5b04b4756f95ca337(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return j


def func_426213315ea7410a94fb09ec4513b86e(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return S


def func_7931e2dc00de4fc3ae7fb5b2a530f251(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return mingain


def func_5f1c8567a4ca4b47b0ce58629de7df8e(N, S, A, q, p, r, s):
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return float(psum - mingain) / psum


def func_f175bba566a549b8ab301ca384863ec3(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return a


def func_0035aba98d68485abf7b6f3a94431c81(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return mingain


def func_e1a3b33b2d3f42e8b8ff9694a796ae7b(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return S


def func_03cecdc8dae04e27bb969d108b458f97(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return hpi


def func_082af1d6e6534c459e4d3fd0f6c453f1(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return pgain


def func_9ef3de985828496ea61225cb3a168cab(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return psum


def func_14c9a5f472f94ebe8b6e49475439dcd6(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return j


def func_dd84a6414ece4f57bdff9140824c530e(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return gain


def func_b6e4ba192f3348439b1b3727df1968a1(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return minpgain


def func_6f5ad5fb2e174f73bb4c951cc96c585d(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return i


def func_e3780b0a05cc4fb8b8ffdc236f22954f(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return A


def func_abfc3aebb400425799aff89bf84f7781(N, A, q, p, r, s):
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return float(psum - mingain) / psum


def func_25cf29aa45eb4953933671bb51a0d73a(N, q, p, r, s):
    A = []
    S = []
    psum = 0
    for i in range(N):
        a = s + (i * p + q) % r
        A.append(a)
        psum = psum + a
        S.append(psum)
    """mingain = psum
	for i in range(N):
		for j in range(i+1):
			gain = max(S[j],S[i]-S[j],psum-S[i])
			mingain = min(mingain,gain)
	return float(psum-mingain)/psum"""
    mingain = psum
    minpgain = psum
    hpi = 0
    for i in range(N):
        j = hpi
        while j <= i:
            pgain = max(S[j], S[i] - S[j])
            gain = max(S[j], S[i] - S[j], psum - S[i])
            mingain = min(mingain, gain)
            if 2 * S[j] > S[i]:
                break
            if pgain <= minpgain:
                hpi = j
            j = j + 1
    return float(psum - mingain) / psum


def func_e386ba13b5e6444d857791be90564075():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    return T


def func_3ad2304ed4c845ac9a89aa5f56d752ea():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    return infile


def func_8505bca3c5a94d64a05c79143850f6e7(infile):
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    return r


def func_b76665a33a3a4cc4b62f81e11949867b(infile):
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    return q


def func_b7a2172a208b425992a390d579f4816a(infile):
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    return s


def func_07ebb54ae41a439f97ef84edabe07d3b(infile):
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    return T


def func_304baf99a0574262b7f0caf7d4eff9f3(infile):
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    return t


def func_d44f2afc173d4cb28f35c9e4b0bdc7f0(infile):
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    return N


def func_34d4f8497c234262a9d2ef200655977e(infile):
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    return p


def func_b168879d54db44f8b434bde7a17a762b(T, infile):
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    infile.close()
    return N


def func_24f7c1edc9e24007a1ece13da11bc5ba(T, infile):
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    infile.close()
    return t


def func_dfa4e25f70364c17bdbb73b6703a79e3(T, infile):
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    infile.close()
    return r


def func_4916594f3be0497db895604237ee47a3(T, infile):
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    infile.close()
    return p


def func_4f871ae77902499bb0f9c5a6af8ca118(T, infile):
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    infile.close()
    return q


def func_511d5ed4b0da47b7a7261330883e77db(T, infile):
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    infile.close()
    return s


def func_492b7b2ff8b84d8d817c2414184bea3f():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    return r


def func_78829a7e763d4429a2ee474821c369a5():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    return t


def func_3c768c58687a45f080dfb73d6cc7b833():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    return infile


def func_220a5723e0e7427a90183154b850c688():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    return T


def func_b8fa2e4effa8495d916ce456f54f5736():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    return q


def func_51c9c93f290947e1b368c81f64dc4095():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    return s


def func_a32461e0c1654763b1f0be6030e2c52b():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    return N


def func_5292248012c74ccebc933ea35b58a0e9():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    return p


def func_d74ac30fac404082b82c8b16a56f7483(infile):
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    infile.close()
    return t


def func_05c94f28678248aeafe70985e3327dd0(infile):
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    infile.close()
    return s


def func_d9cec4d5b73842d98865e44cab92630c(infile):
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    infile.close()
    return r


def func_8cfcf581fa694333b13159edb9a2d857(infile):
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    infile.close()
    return p


def func_c5fcb53f14fb4b8d869502a0de9bf295(infile):
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    infile.close()
    return T


def func_7b8a7f5d05744fe79c987722ca11c464(infile):
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    infile.close()
    return N


def func_6b61f21bde9f4a6a93cfcac94ab6c9ae(infile):
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    infile.close()
    return q


def func_a018108d85c6493abb158d11c80ba5ab():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    infile.close()
    return N


def func_f624f0afe0ad4530b03774e621d5d86a():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    infile.close()
    return p


def func_d536ffe452c94b92b1b232032359a975():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    infile.close()
    return infile


def func_1203201756974e1dbb0318ee53c8cdaf():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    infile.close()
    return r


def func_9bcce734072047fea47192e11fab0dc3():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    infile.close()
    return t


def func_8f07af81f01e457ca3cbcba0182d612f():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    infile.close()
    return q


def func_3b0fc402dab640b09a2c5a54b0167d0b():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    infile.close()
    return s


def func_35a3f4a8084f4dfeab38d2273935e6fa():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N, p, q, r, s = map(int, infile.readline().split())
        print 'Case #{}: {}'.format(t + 1, solve(N, p, q, r, s))
    infile.close()
    return T

import sys
sys.path.append('/home/george2/Raise/ProgramRepair/CodeSeer/projects/src/main/python')
from Y14R5P1.protos.codejam import *

def func_98697841739a42efa27a1233ac93c776(s, d, m):
    v = s + t + 1 >> 1
    if d[v] <= m:
        s = v
    else:
        t = v - 1
    return t


def func_c4df38cf061e490ab3066b836508f3d6(s, d, m):
    v = s + t + 1 >> 1
    if d[v] <= m:
        s = v
    else:
        t = v - 1
    return s


def func_c595b9b3efed49f6ad1c136278394027(s, d, m):
    v = s + t + 1 >> 1
    if d[v] <= m:
        s = v
    else:
        t = v - 1
    return v


def func_27f0cb399fc9400ab85da8506d923547(s, d, m):
    s, t = s, len(d) - 1
    while s != t:
        v = s + t + 1 >> 1
        if d[v] <= m:
            s = v
        else:
            t = v - 1
    return s


def func_7f4c598e2edb4b0591146cec5e1bf5d7(s, d, m):
    s, t = s, len(d) - 1
    while s != t:
        v = s + t + 1 >> 1
        if d[v] <= m:
            s = v
        else:
            t = v - 1
    return t


def func_9cd42b18aa7f424c8b8be52eac573ad3(s, d, m):
    s, t = s, len(d) - 1
    while s != t:
        v = s + t + 1 >> 1
        if d[v] <= m:
            s = v
        else:
            t = v - 1
    return v


def func_cfe82e3de08f4b44a162dd16af052d78(s, d, m):
    while s != t:
        v = s + t + 1 >> 1
        if d[v] <= m:
            s = v
        else:
            t = v - 1
    return s, d[s]


def func_77164ba2a5fd40d68b6cc19c24a5530c(s, d, m):
    s, t = s, len(d) - 1
    while s != t:
        v = s + t + 1 >> 1
        if d[v] <= m:
            s = v
        else:
            t = v - 1
    return s, d[s]


def func_0b9266c1019a4ef1990c54b8513f3bef(snm, s, t):
    m = s + t >> 1
    i, j = getpt(snm, 0, m)
    return i


def func_896cd5d6badf417996e5eb4bec1df821(snm, s, t):
    m = s + t >> 1
    i, j = getpt(snm, 0, m)
    return m


def func_60631e941b16404f988d7023c51824ef(snm, s, t):
    m = s + t >> 1
    i, j = getpt(snm, 0, m)
    return j


def func_dfb4c678e27442b78c38c20d18803797(snm, m):
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    return j


def func_240a3585e4bc4be9a481417b6964d1dc(snm, m):
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    return k


def func_919e08662a4843c0a324679005a2eae8(snm, m):
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    return l


def func_0ffe932d741c4d3da92e10c7bcf2dec5(snm, m):
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    return i


def func_409627bb4a7d49e9adcc7cca6748dbb8(i, snm, j, m):
    k, l = getpt(snm, i, m + j)
    l -= j
    return l


def func_d07aaccb553143c7834437698bf6d3d5(i, snm, j, m):
    k, l = getpt(snm, i, m + j)
    l -= j
    return k


def func_571a179ac8584296abded2cc4bafd641(snm, j, n, m):
    l -= j
    if snm[n] - l - j <= m:
        t = m
    else:
        s = m + 1
    return t


def func_20fccad3f7ef435b90596a7eeea2ef80(snm, j, n, m):
    l -= j
    if snm[n] - l - j <= m:
        t = m
    else:
        s = m + 1
    return s


def func_2a06b24ef23a4c769ca40ad16842b016(snm, j, n, m):
    l -= j
    if snm[n] - l - j <= m:
        t = m
    else:
        s = m + 1
    return l


def func_8bc3750158e04d33bedb2781e0b9fe92(snm, s, t):
    m = s + t >> 1
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    return l


def func_338968fb5e5c40a0a600b46167113722(snm, s, t):
    m = s + t >> 1
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    return j


def func_3500fc892cdf4b6a863de49de049d1e0(snm, s, t):
    m = s + t >> 1
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    return i


def func_e959c45417db4b339f8fc8229e2b26b0(snm, s, t):
    m = s + t >> 1
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    return k


def func_b7e2b1d8aa304d32a89d9fa8d2dd6bf8(snm, s, t):
    m = s + t >> 1
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    return m


def func_7ac0c62f509a4a9490a8b2219a1ae89d(snm, m):
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    l -= j
    return i


def func_b37ff46d428e4df385b23eb6ab0c18c1(snm, m):
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    l -= j
    return l


def func_17f56b74191641d0a9e6cdee9a28c804(snm, m):
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    l -= j
    return j


def func_c45864eccfa1458ca1c4986307304ad8(snm, m):
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    l -= j
    return k


def func_259cf3e2da3144be8ce2621fdde341a4(i, snm, j, n, m):
    k, l = getpt(snm, i, m + j)
    l -= j
    if snm[n] - l - j <= m:
        t = m
    else:
        s = m + 1
    return s


def func_e397c16bc0914151936f14c6bd7e2092(i, snm, j, n, m):
    k, l = getpt(snm, i, m + j)
    l -= j
    if snm[n] - l - j <= m:
        t = m
    else:
        s = m + 1
    return k


def func_e92cd43263ca4bf3b0c437083cec4265(i, snm, j, n, m):
    k, l = getpt(snm, i, m + j)
    l -= j
    if snm[n] - l - j <= m:
        t = m
    else:
        s = m + 1
    return t


def func_90f1793c79cb4b59aaccc29478dfd76d(i, snm, j, n, m):
    k, l = getpt(snm, i, m + j)
    l -= j
    if snm[n] - l - j <= m:
        t = m
    else:
        s = m + 1
    return l


def func_944c839025b94fc38fd49b99413d0ac8(snm, s, t):
    m = s + t >> 1
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    l -= j
    return j


def func_beda2559937845ecb28552c7d7aac990(snm, s, t):
    m = s + t >> 1
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    l -= j
    return k


def func_ee793f32cda44570b12b703969f61819(snm, s, t):
    m = s + t >> 1
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    l -= j
    return l


def func_5d57166f1426447781ca88495798d809(snm, s, t):
    m = s + t >> 1
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    l -= j
    return i


def func_479e40073c224d5cb8e06d75ade8b81d(snm, s, t):
    m = s + t >> 1
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    l -= j
    return m


def func_c387cb8a0c5a418db2595fc92de88cc0(snm, n, m):
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    l -= j
    if snm[n] - l - j <= m:
        t = m
    else:
        s = m + 1
    return s


def func_0b452795a61146cda5c55425cb3aa9e0(snm, n, m):
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    l -= j
    if snm[n] - l - j <= m:
        t = m
    else:
        s = m + 1
    return j


def func_3e195d59025d4997a348bb4a59acb395(snm, n, m):
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    l -= j
    if snm[n] - l - j <= m:
        t = m
    else:
        s = m + 1
    return l


def func_f17c19bd1c534940a342713c93ea7780(snm, n, m):
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    l -= j
    if snm[n] - l - j <= m:
        t = m
    else:
        s = m + 1
    return i


def func_5947f8ce4aae4603836c0c4840926559(snm, n, m):
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    l -= j
    if snm[n] - l - j <= m:
        t = m
    else:
        s = m + 1
    return k


def func_7eb6d74ed33c4c539729abf16c4c2c8f(snm, n, m):
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    l -= j
    if snm[n] - l - j <= m:
        t = m
    else:
        s = m + 1
    return t


def func_0fd13d5900aa4f14b77bd9077e19063f(snm, n):
    m = s + t >> 1
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    l -= j
    if snm[n] - l - j <= m:
        t = m
    else:
        s = m + 1
    return l


def func_59fc859c0d6a484986512ca3255b992a(snm, n):
    m = s + t >> 1
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    l -= j
    if snm[n] - l - j <= m:
        t = m
    else:
        s = m + 1
    return i


def func_af1c311404b64f18975c7da4573221e5(snm, n):
    m = s + t >> 1
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    l -= j
    if snm[n] - l - j <= m:
        t = m
    else:
        s = m + 1
    return m


def func_43ca54adf9334ac68be96de7653813b6(snm, n):
    m = s + t >> 1
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    l -= j
    if snm[n] - l - j <= m:
        t = m
    else:
        s = m + 1
    return t


def func_95408b0437d04acea7991acfb553f9c5(snm, n):
    m = s + t >> 1
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    l -= j
    if snm[n] - l - j <= m:
        t = m
    else:
        s = m + 1
    return k


def func_c9f9c85519ca4edfb77fc768a83b9ebd(snm, n):
    m = s + t >> 1
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    l -= j
    if snm[n] - l - j <= m:
        t = m
    else:
        s = m + 1
    return j


def func_5d66d29882714c72bc7211a32761ba63(snm, n):
    m = s + t >> 1
    i, j = getpt(snm, 0, m)
    k, l = getpt(snm, i, m + j)
    l -= j
    if snm[n] - l - j <= m:
        t = m
    else:
        s = m + 1
    return s


def func_fe99419ee1fc4ae0b67e9a49d96f8e36(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    return n


def func_9ba7ad4d2889428fb6ef35b2385d7e18(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    return num


def func_c759c114d3314c3bbd343187aa977629(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    return i


def func_d69ed04bc11144eb9b62bf31fa021d32(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    return r


def func_11a4b33573e14696a2406a677a0cf99c(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    return s


def func_03fc3647144b4095a93b5d2ee10af684(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    return p


def func_1c740b237b3446869da77694127e49c6(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    return q


def func_0e0168831e5849e2aaba0a9bc2ca3ed4():
    num = []
    snm = [0]
    return snm


def func_3b5cc1331d2f4503b33e4c94e14307ec():
    num = []
    snm = [0]
    return num


def func_1884737bc1034d20b2883e586b7967d9(q, s, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    return i


def func_aba96a0bd5404972b58355e0ab674c36(q, s, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    return snm


def func_312ac75541bd487691fa877c58ff39d2(q, snm, p, num, n, r):
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    return t


def func_8b71e0043b1e44729ec9e8f628c441f0(q, snm, p, num, n, r):
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    return s


def func_704137af15a149f890bc376fbf835eaa(q, snm, p, num, n, r):
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    return i


def func_5f73b947f5f54009a253a6c55a1ec97a(snm, n):
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return l


def func_5070313317f845b387d3fc90781c39ba(snm, n):
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return i


def func_9caf0c5885164560aa876a1e3f0be488(snm, n):
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return t


def func_26046892dcc74f5e971411bb271582a3(snm, n):
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return s


def func_88cbd437dc7849faa81a10cefb42712a(snm, n):
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return j


def func_154d7a37a37145d99f9c292395adb00d(snm, n):
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return m


def func_e14147de9fd14145b217949ac0191eba(snm, n):
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return k


def func_a32bfdd44113421d9c0ba0a2ba36f442(snm, n):
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return s


def func_e6a98e4fa3a342b39d8d7142fccd18b7(snm, n):
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return j


def func_a4342112feb44a38ae8637d2076a4d2d(snm, n):
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return m


def func_d0e167a200ed44a39403e661c4928f4a(snm, n):
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return res


def func_f7f94ccf6cd24b9cbc444cbf164deebf(snm, n):
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return l


def func_8bbdabd3b55b41e2a9d947c426f84eec(snm, n):
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return k


def func_d8a0b304b05e43e894c987c67dcc9e38(snm, n):
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return t


def func_bfd3a0ac1dae43c7bb3e5eb36339a48f(snm, n):
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return i


def func_d31cd8ce27b7418d8fe2ad75f1b00b7c(case, snm, s, n):
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return res


def func_b056bf19b1f3401a844617bf1c671c50(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    return p


def func_e23a10a7e9f64f409b32ff9a93138fba(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    return snm


def func_47dac2ef11ad486096bca41702952a67(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    return q


def func_d45c4caa69324c078e69ccf189a8ca88(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    return r


def func_eccf46852e154b9f8c7aca40e6236a87(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    return num


def func_dad658b3a41147109085cea7bb70a583(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    return n


def func_49738190a92e4861ac8e22e90c8497b3(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    return s


def func_55734a3177c847d9ad81848fd1c389a7(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    return i


def func_0fce97ba52d8494091a43c3679cfe570(q, s, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    return num


def func_c3639c67c6d1435883219b243497718e(q, s, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    return i


def func_67cf15e1ee9344e19b20b4e5f0076fd7(q, s, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    return snm


def func_eac24e0baeaf42ff9fb5faa1a9b8420a(q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    return t


def func_0b4cc93bf2934f3684822634f79af993(q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    return i


def func_532c2604d58641e68ab9d174f68d7ad5(q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    return s


def func_9836946e28474ecaa389fdc30b6a292b(q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    return snm


def func_08d9ebc1f6344809be2569343e918db8(q, snm, p, num, n, r):
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return s


def func_f8a91a119a684c2989827561ac1b9b9c(q, snm, p, num, n, r):
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return t


def func_08890f0f720c4b388ea2c6686b51dc22(q, snm, p, num, n, r):
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return i


def func_f64745e2565c4ff1b248a45a0336767b(q, snm, p, num, n, r):
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return j


def func_81d0db00a8d14de6a76ed973c98a950a(q, snm, p, num, n, r):
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return l


def func_133b7862b339475ebc8e2955b4dc276f(q, snm, p, num, n, r):
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return m


def func_702b83d9d9ba4e8e821a35fff07d1377(q, snm, p, num, n, r):
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return k


def func_7975c742337f4228b7b2b5a519e37257(snm, n):
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return l


def func_bea5d8362336445cb5d526e0d11f49eb(snm, n):
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return m


def func_b650e8a958274076bfe53e5f7666f3b7(snm, n):
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return k


def func_98c525cabba041cd926f16a93a7ac91b(snm, n):
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return i


def func_2721823961284feb848559f525cb3aca(snm, n):
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return t


def func_d5876e3d49a34216be71af0fb683a205(snm, n):
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return res


def func_9e9a0d49d06d46e8beec067f7e423b5b(snm, n):
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return s


def func_47a51a311d8a4ed0929085b7d129ca29(snm, n):
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return j


def func_ecdf56d62ddd490d901dab753ba8d1b0(case, snm, n):
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return s


def func_93c60cf81f7248c6aad99db3d903b017(case, snm, n):
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return m


def func_a70353aad98f4fb980650590d0dcec18(case, snm, n):
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return t


def func_90d4723f07cb41e0965b6166ad7b3dda(case, snm, n):
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return res


def func_5b99e385ecf14e0e81b7e28749b76d93(case, snm, n):
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return k


def func_288625eaa0144cb09d532f38e5cb3cfe(case, snm, n):
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return i


def func_5ea41a03459946128638c57b6e89651a(case, snm, n):
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return j


def func_b257f68ee1704cdbb1ee838b6a910d4d(case, snm, n):
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return l


def func_dadd7c93ce4f433fbd496aeb849524ab(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    return r


def func_d4944e489ee14b518ec7bcd0d1c93a2e(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    return n


def func_d7fa3524a8f74b2aac5d726bcd7cf674(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    return q


def func_84a066494b7247e39be796d31b213ea5(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    return num


def func_2127c62b5a554638a8b0e9c93fbea8df(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    return s


def func_4da7c5382e8f42578148a221d11fffbd(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    return p


def func_eb6125f700d646d7b217035450c4a541(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    return snm


def func_e05fc1a6f67847879ed67c05da2843ff(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    return i


def func_3c6b7bcce66a488d9fd7e582367cdc3a(q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    return i


def func_a3d6178f798c4ad8a5681fa94ffbb6b6(q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    return t


def func_ea1634f53b9e4109a5dc080258070637(q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    return snm


def func_af98d702fed846b084ed653177bb92ed(q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    return num


def func_3750913ca4774aedaebff9d288759229(q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    return s


def func_f3ce23d9f8c946fcb6085c3f62dbb6ce(q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return t


def func_cfbf4fea560a4e3b8d69c7255db3f3f4(q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return j


def func_279f977da38a439891632f3744648627(q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return k


def func_8a8b14bc79ec4dc6a052fb953795294b(q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return i


def func_fecf72c436f44bebb49a0685015b42b9(q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return s


def func_ad576e8b9efa46b9ad3b659f7b5d0818(q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return m


def func_55b2668a6f644e73a531bb17e0880e34(q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return l


def func_357d7b21cf344f2a979d67af0cfc8a4e(q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return snm


def func_d265312b3e1843e8a568f8be2461f9af(q, snm, p, num, n, r):
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return k


def func_fc1bd8693a1c4e8c81df3223e2ae077c(q, snm, p, num, n, r):
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return res


def func_011af378452d4f3d9e6b504d00a37015(q, snm, p, num, n, r):
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return i


def func_4d8fcac203994ec5a6563eb3bbf43626(q, snm, p, num, n, r):
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return m


def func_c56cd2a106c84af09609cf0b5a6c3654(q, snm, p, num, n, r):
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return s


def func_588742a76bfd4c5e854fbef05170415b(q, snm, p, num, n, r):
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return t


def func_2c17791e090b44159ee82f348abea40d(q, snm, p, num, n, r):
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return l


def func_2b30ffbab63947e1b0e93f5fe2b778da(q, snm, p, num, n, r):
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return j


def func_c410b0c3a1bf42d1ad659e3fe2cc3a2d(case, snm, n):
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return t


def func_00a7b77eb38c438b8f6aeaf22dbbadde(case, snm, n):
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return k


def func_025152f9b0a945398564125cb0ae2d83(case, snm, n):
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return l


def func_cd711d620a1d4f808608e9c08e2b76b9(case, snm, n):
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return m


def func_b91af1e4715841b6879f38ac56431dda(case, snm, n):
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return res


def func_1d4e97e17ecf4b93939937d52251881a(case, snm, n):
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return j


def func_fd7e5313fab34b839dd65cb4acedc6dc(case, snm, n):
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return i


def func_b1f3b29e7d774f26b6cd09a001d8b35f(case, snm, n):
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return s


def func_92ff00f3f98d47b6b19703bb6c5c9a60(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    return t


def func_883a774d022d4519af78a964765ea34b(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    return i


def func_672e17e47ad646549bc123c4149d6246(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    return p


def func_10fe62d03c72418b9b15b17ca97f0d48(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    return num


def func_b8aa6dc6e3c4494ab9a72dc355775d7c(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    return r


def func_e231baf019d444e580aae879f6a11ea6(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    return n


def func_510c3b88c0fc43b4ab50080db7182001(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    return s


def func_74d4a80ad569479b968867bbc657972e(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    return q


def func_2e774981d6464f518775fb51fa8a6b16(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    return snm


def func_e9d6746e494f4955a34ffb0563e94f07(q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return s


def func_cd852f07db70447bb7a2a6aaf0b04b31(q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return snm


def func_4d04b23aefa94b18b1a649c94296c765(q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return i


def func_f9a7c7ca120f41bb8e83c43fcdc41bbd(q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return m


def func_75ed92a4968344c3b565770a96106120(q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return num


def func_00242e6e3a6b4bf19afb5d7b70afbfce(q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return k


def func_19d26817b04443b68b79880f09187e22(q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return t


def func_75f6b4987fb54bb8b20efb6cb2902a01(q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return l


def func_8a9b0367d3a8415fb622c321d3cc3622(q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return j


def func_22d34b988c1f41ab8e1e272391faeceb(q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return l


def func_d42f1d47848a41ae84a701c38d35fae6(q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return snm


def func_55db9808d6ff491bac1bff741a2b274e(q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return i


def func_7f10010fb1b44b0e805cca4a39ec81e7(q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return s


def func_919dca45229f441ebbae7173b271db57(q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return t


def func_e1a7a64de8cb4266a78f297ccb20f972(q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return j


def func_490239183d804b45aa8643c285bb8b1f(q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return res


def func_fa49cb6a8632452ba2550a737d4f1971(q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return m


def func_802a99c3d3fa411bb67a900b16c7fed0(q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return k


def func_5500f3b2602d47fab1f6002240e8706b(case, q, snm, p, num, n, r):
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return res


def func_7b941e851f3e4970952aaf8b603e03b4(case, q, snm, p, num, n, r):
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return m


def func_4ab7071e3ae74484830c1d6dc38191ce(case, q, snm, p, num, n, r):
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return l


def func_4f3fa168472e4efb975556fb86801275(case, q, snm, p, num, n, r):
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return i


def func_8623c98475f14f83a42b4eb63c7f1c22(case, q, snm, p, num, n, r):
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return k


def func_cd8179473aee47ab90f3af25cef3a327(case, q, snm, p, num, n, r):
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return s


def func_85f21a94d2be4f2aabb3b9ebb778e250(case, q, snm, p, num, n, r):
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return j


def func_a1ed4ed4089e41dabca223727e28ece0(case, q, snm, p, num, n, r):
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return t


def func_7136a2513ca04cf393ba2e01654cc060(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return q


def func_cd6ee2fd8ce14a84add7ee46b39196de(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return l


def func_abd5a81d1e674900b1452056c22a1a3c(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return k


def func_e3cb32dd60bf4fb09e87907b5e0e88fc(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return n


def func_d1ec693e207f469f9aa0ee1cef2ba46d(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return j


def func_2ea64fca4f084b718313ab86b8bf0b29(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return p


def func_c9c390be677f4b129db589b52d8753b6(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return snm


def func_a50ee10aef904b5abebcc53028624c30(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return num


def func_20ff22b00e124e959bd1171b4aa043a7(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return r


def func_31bc9078ad65417da14f7af7c41a7135(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return i


def func_67393e15d8d947119d5ea09f45bce57d(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return m


def func_eb108384d2c5493fbf8acf1b0502cd48(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return t


def func_230d08cb58aa48c986a3e773d25d8b10(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    return s


def func_620680be6a0d4cfc84d443c0ff87aacf(q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return snm


def func_3735bcd3a93749f69ff1b470209e0579(q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return s


def func_505f5d4b42b94c6599f50a0aee7ff1f5(q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return i


def func_545cb534a1684afc82035f51cf2c4084(q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return l


def func_d1e1f6064d884d2685faf80170f3f49d(q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return j


def func_3f4e50c108784bb0a2e750d1da46b232(q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return m


def func_5927ca2d0064430d96dfe35ba93e468e(q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return num


def func_df4ecd2cea5b40088da738fb06489e5b(q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return k


def func_68cb6f8c6f2c470196fe1cda4f3ea183(q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return res


def func_9a486c60cbba44e9b3116bcf4231d936(q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return t


def func_f75142ccd0ca45a59cb13361a3575ab2(case, q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return m


def func_1b557970a719415a8d3df855f49677ac(case, q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return snm


def func_a6b9627890794490bf41c4d693313224(case, q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return s


def func_1e68b1b248454319abd1774f7ace9bd7(case, q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return j


def func_d05320e21bba44eb9194118f8a4a4197(case, q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return l


def func_a0ed6ab297eb41e89d2477d04eb35432(case, q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return res


def func_2f799ee529da429cb178e334c8e9cd48(case, q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return i


def func_2df4fa668f7a4857b58ebc7234bf10e0(case, q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return t


def func_0298ce16bfb54aea8d97e3413e864e83(case, q, p, num, n, r):
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return k


def func_5af70a81773f41e98507d82ff819c52c(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return m


def func_9034761789364581a3ff0560ab174d9e(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return t


def func_6f3e877659a34db5ab1af1e21970b9da(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return num


def func_a858c55a0f3247b792d31c7217589240(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return i


def func_3240518f888f40e3b96abb26d74ac1a9(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return s


def func_7631e54126534c5593c60098638510e3(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return q


def func_b67e7b8612684474b73464319ab19783(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return snm


def func_77fc12d0d69f481aa6f3a22bf9d4eecd(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return n


def func_7354419ee94d4fe79bb71954bbdbcda8(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return res


def func_dc8c70ea16e84ee296d942836a90e7e2(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return l


def func_831d957088fc49ee9972f51e66f71b3a(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return p


def func_1c1fadd768284415ba2c284be18e619d(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return r


def func_b805b5420dc547e89017f2ee22711e86(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return k


def func_66ba3a7641934b4a92540897e244525f(infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])
    return j


def func_e7af90dd29bb4120a4a8914ca73faab1(case, q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return j


def func_0bf3b5e5d8ae44ce999366a38aeecadc(case, q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return res


def func_78d700e40e7747d3b11874bd90ac52ea(case, q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return m


def func_6f4f7c9a92614b5fb64f52af006dae46(case, q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return num


def func_df524e93334345339896ca5f0bf4a2c4(case, q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return k


def func_bfd1b4ac9b624d67a384e7d6f8059e29(case, q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return s


def func_6649ca926c274f1da07319e0cfd16249(case, q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return t


def func_4f5afe16e8164e6b9ce12a0e4afad4c5(case, q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return l


def func_15a240a63e2746b5ae2904f54097996d(case, q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return snm


def func_c3d9998425d74d3489d7c1ce8e7dc0e7(case, q, p, n, r):
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return i


def func_45bfb87338074ebc8e98bdd9afdff4fd(case, infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return t


def func_8d6b2aeeac39460da5a1adc5d05dc3a4(case, infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return m


def func_9384e1148e0447b4b6913da1793ad7d0(case, infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return k


def func_d4b2df15093a43a4adc3f97148dceaa0(case, infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return p


def func_cfdf678e69dc49a4937af7abf4ffecd0(case, infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return i


def func_a66c7809c39541b197127a67ee549f6f(case, infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return l


def func_0ea7731d73bf45aa81ebd0984e80231a(case, infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return j


def func_e6a09dc189e1437c8254e616d7a2d93e(case, infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return s


def func_a62abc49609d495b8a6a3c6e7d65c6f0(case, infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return num


def func_69147ca59fd04512b1a451262880979f(case, infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return q


def func_6c79f811a858477c970bb05054e4bdf6(case, infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return r


def func_f8d912640cfa4bd092b33110ea153de9(case, infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return snm


def func_1524faacf48845d7b7e24961cec98fe2(case, infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return n


def func_460382c2d30e4baba1d6b3464c2ece87(case, infile):
    n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
    num = []
    snm = [0]
    for i in xrange(n):
        num.append((i * p + q) % r + s)
        snm.append(snm[-1] + num[-1])
    s, t = 0, snm[n]
    while s != t:
        m = s + t >> 1
        i, j = getpt(snm, 0, m)
        k, l = getpt(snm, i, m + j)
        l -= j
        if snm[n] - l - j <= m:
            t = m
        else:
            s = m + 1
    res = (snm[n] - s) / float(snm[n])('Case #%d: %.10f' % (case, res))
    return res


def func_04b9a1453c0c465c82ee6e63c29e103b():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    return infile


def func_6cac6acf50f94966940f6697342435fa():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    return cases


def func_be1a6f9f30f14e0c88448c8dc4d3adf5(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return p


def func_1409c1dbbc51474a8c310d6134ee8c5d(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return snm


def func_7228ea1a7a8a444caafaf857717b41f4(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return m


def func_0375faa7d6c04cf7941ebb88260d1510(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return case


def func_93fa20b3049549c79124d92f99eda325(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return cases


def func_cf9a322e171a43c3b0cea4fd3ec78ffc(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return num


def func_5ce904bb64da48bd99f06b8c7cb610b6(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return r


def func_4c38978e39e24c339355ca53b8bb31d5(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return s


def func_c58503942e9445f59333288ea33ba5b3(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return j


def func_a63d8a90424d40c4bd60b55334d23a0a(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return n


def func_f9c5d25275a546b68789dcc3bf4eddc5(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return k


def func_5023116fb62c469ebfe6df9c97b2452d(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return t


def func_1bb29a7c82b841d181c63e940556a88f(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return res


def func_5fa0553af6364e97a0064135bd0eb8c0(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return q


def func_b28b5b3543c94166940d8640828e4f7a(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return l


def func_878b3f25f3794b9f88bc30133086479b(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return i


def func_d93bf4eb84ef4a508625db8009e441f5(cases, infile):
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return s


def func_b2729fb9ae16432da129a203d650117a(cases, infile):
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return m


def func_468772c0a1f64829a52d5620228facb6(cases, infile):
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return r


def func_2436756b40be44649b625ef7e7ba5c80(cases, infile):
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return q


def func_b0b313be660c43bdb17e7a96bb8e5137(cases, infile):
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return i


def func_d8da4fd02c4a409bb035c953fa0178eb(cases, infile):
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return snm


def func_18e5eb8ad5264a7e81d12aade7bfa434(cases, infile):
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return p


def func_7f7e37b9a9cc46fe9b537f00a716e223(cases, infile):
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return num


def func_53f0309f14f9440495b70ada2b3a97e1(cases, infile):
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return l


def func_15c8ce6785984a889a3eb26e41a9a127(cases, infile):
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return k


def func_f90cb2848bf942448403568dc6f82b23(cases, infile):
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return res


def func_4c9c9ad422df41668cee3c9978b23184(cases, infile):
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return t


def func_57670b76c1a54c90a77d1916d28b9c94(cases, infile):
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return j


def func_26e097cdf6ba42fe81f89f0205c2e42f(cases, infile):
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return n


def func_073ff8dba6b4438998c59e62d3df01c7(cases, infile):
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return case


def func_05a031d24dde47589d6b284de1ddaf69():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return n


def func_175b64f1014c43bd8628cb617cc48d26():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return r


def func_a8e24f0ffec84ccebde5b1264ac9d944():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return p


def func_faf67dcb19334a58818fd6080b13df10():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return t


def func_6b557aa60859447a9aceff450f4625a1():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return i


def func_135b498c68d74463a738f6d2338f4a97():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return cases


def func_e5ee93ac7db34d9f815472f79fd2beed():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return j


def func_c780494930e44f519e1e45bd2f336404():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return num


def func_9013e944cd0f4c4cbfe388b11ccd8ca6():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return snm


def func_005a4cb28855463fb271781c0a9da322():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return case


def func_d04ec49442954077a7782534892842ac():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return l


def func_971024b88cf94a7990e94a3857fba02b():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return s


def func_67ea865be6fe40f49a00dc4eea2364a6():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return res


def func_95ba1584895947be97f74dc8bad126ac():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return m


def func_98d46e022bfb4594be55b5e2b5a8f833():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return k


def func_3155cf9e86d74299a3eedda20891bed4():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return infile


def func_3a276d8b944e4bfc9079d715b8485d06():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    return q


def func_6561c031c45b41618d89cc9f15e836e8(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return i


def func_44d83fd5dbf44582b53e2ef534767116(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return res


def func_8c59ecfcd7c243eb88bc4f760fddabe4(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return q


def func_504215390e494670ac2410dd12f5a724(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return k


def func_3b57a5dae0e14eca9f6f01768a98b2c8(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return r


def func_5af52a96280b47538de083d2fbf3f377(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return snm


def func_2fd9a0ee84c14c4dab232cbf3d99a301(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return l


def func_81bedd34e70a4cd9877de15d0e972fb3(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return num


def func_69c8a56655e442a7b7ebba43fc935fb5(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return t


def func_72b4886975ae429e9113031e4377e475(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return p


def func_81d3bfa3ab544c72b41cdb47bac01f64(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return m


def func_c0b8e71f027f45a6b65a602956f1bafb(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return cases


def func_f775be2f64bf4de7a47882dc9dfa1986(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return case


def func_704c0167c557488f928807a605641f9f(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return s


def func_9f633556b5134103ad18f370fb44fa8b(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return j


def func_821c013f9897494ab99aea4ccbf25064(infile):
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return n


def func_ef10ce436d394ed68fbb3e3b10898b2e():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return t


def func_2a55a246e86d4886906a7d5dadd5aea6():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return n


def func_164db1f1f40e49f09be2df62a25be94d():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return p


def func_91b9128b594f47559d62f6ff6f4669c4():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return snm


def func_6793b625329b4306a987e5881bb48de7():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return i


def func_b246509ab7344556b1fd8cc9d5dc6bd1():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return q


def func_10027c72fd5e4688ad4afdf5894c7df5():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return infile


def func_ac38659e140045b5b3d623f9e8dc146d():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return case


def func_4a63603fc14e464c8fe55d2833f8c6dc():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return l


def func_a46762d2141a4000a050c221692922a7():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return res


def func_8405720d490d4a548cb4f8550dccabb7():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return cases


def func_1017da6b52ae4902a76cccc44006d39f():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return m


def func_508cef76985e4b7a832a7d32eae8f6c2():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return r


def func_de4edbcea7b44b458c6b10a9713f6ac8():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return s


def func_24251ebc5a6c41dd8cfc31b8f259a332():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return k


def func_93e20fcd79b6489284de865877194c64():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return j


def func_550b931572cd4108868222eafb74d074():
    infile = open('test_files/Y14R5P1/A.in')
    cases = int(infile.readline())
    for case in range(1, cases + 1):
        n, p, q, r, s = tuple([int(i) for i in infile.readline().split()])
        num = []
        snm = [0]
        for i in xrange(n):
            num.append((i * p + q) % r + s)
            snm.append(snm[-1] + num[-1])
        s, t = 0, snm[n]
        while s != t:
            m = s + t >> 1
            i, j = getpt(snm, 0, m)
            k, l = getpt(snm, i, m + j)
            l -= j
            if snm[n] - l - j <= m:
                t = m
            else:
                s = m + 1
        res = (snm[n] - s) / float(snm[n])
        print 'Case #%d: %.10f' % (case, res)
    infile.close()
    return num

import sys
sys.path.append('/home/george2/Raise/ProgramRepair/CodeSeer/projects/src/main/python')
from CodeJam.Y14R5P1.kevinsogo.a import *

def func_1fab62cc50144cb7a5d466fdc892ce0c(L, sums, R):
    M = L + R >> 1
    ta = sums[M]
    return ta


def func_20b0dbf59b2146cfa514f7b09df439f5(L, sums, R):
    M = L + R >> 1
    ta = sums[M]
    return M


def func_1b8d6bc3d9b24458bbe6d496755ddc0f(sums, M, i):
    ta = sums[M]
    tb = sums[i] - sums[M]
    return ta


def func_75ac5fe5924442e397738b65a94f4394(sums, M, i):
    ta = sums[M]
    tb = sums[i] - sums[M]
    return tb


def func_5b859fa9af3740b9bbf15fea098b6757(ta, sums, M, i):
    tb = sums[i] - sums[M]
    if ta < tb:
        L = M
    else:
        R = M
    return R


def func_5b71b14897b041729f60b8b1e796510a(ta, sums, M, i):
    tb = sums[i] - sums[M]
    if ta < tb:
        L = M
    else:
        R = M
    return L


def func_caed6a8e8ca04787a5253e1f3263b8ce(ta, sums, M, i):
    tb = sums[i] - sums[M]
    if ta < tb:
        L = M
    else:
        R = M
    return tb


def func_88352c1f79c9479b8c3b8c242540df72(L, sums, R, i):
    M = L + R >> 1
    ta = sums[M]
    tb = sums[i] - sums[M]
    return tb


def func_8357d42eeeb9463b93e064880addb639(L, sums, R, i):
    M = L + R >> 1
    ta = sums[M]
    tb = sums[i] - sums[M]
    return M


def func_0f4ac2d510654bc68eb8203bb246a7d8(L, sums, R, i):
    M = L + R >> 1
    ta = sums[M]
    tb = sums[i] - sums[M]
    return ta


def func_cba17a23ae2b479484d90f715992139a(sums, M, i):
    ta = sums[M]
    tb = sums[i] - sums[M]
    if ta < tb:
        L = M
    else:
        R = M
    return tb


def func_f0a46599871c40caa485ff52fc6ea379(sums, M, i):
    ta = sums[M]
    tb = sums[i] - sums[M]
    if ta < tb:
        L = M
    else:
        R = M
    return ta


def func_fa4385aa7f6b4dad888fea59fade840a(sums, M, i):
    ta = sums[M]
    tb = sums[i] - sums[M]
    if ta < tb:
        L = M
    else:
        R = M
    return L


def func_fd839f2d9f8a444dbdd520168cc06e13(sums, M, i):
    ta = sums[M]
    tb = sums[i] - sums[M]
    if ta < tb:
        L = M
    else:
        R = M
    return R


def func_263f0e1666894a738d57a95e56570c83(sums, i):
    M = L + R >> 1
    ta = sums[M]
    tb = sums[i] - sums[M]
    if ta < tb:
        L = M
    else:
        R = M
    return L


def func_c3f945345a0a4b80972cf98637a5d747(sums, i):
    M = L + R >> 1
    ta = sums[M]
    tb = sums[i] - sums[M]
    if ta < tb:
        L = M
    else:
        R = M
    return M


def func_3383764b2234431e80140ce0d31768c7(sums, i):
    M = L + R >> 1
    ta = sums[M]
    tb = sums[i] - sums[M]
    if ta < tb:
        L = M
    else:
        R = M
    return tb


def func_d22821e7c4d5438f9ac11049b3e8319f(sums, i):
    M = L + R >> 1
    ta = sums[M]
    tb = sums[i] - sums[M]
    if ta < tb:
        L = M
    else:
        R = M
    return R


def func_d5f0f95553024b278e3c23f39d047562(sums, i):
    M = L + R >> 1
    ta = sums[M]
    tb = sums[i] - sums[M]
    if ta < tb:
        L = M
    else:
        R = M
    return ta


def func_a90140e21794417783245f5ce8fd640e(i):
    L = 0
    R = i
    return L


def func_cde943ba0c684ce1bc6984978f123e62(i):
    L = 0
    R = i
    return R


def func_4d426df33ed14691ba2b378057f2bf1c(sums, i):
    R = i
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    return tb


def func_c53fe97bc4c74e17b38c3b4e2dc44655(sums, i):
    R = i
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    return R


def func_b0b0fbfb598248b6b6ed0b5b0cdd206b(sums, i):
    R = i
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    return L


def func_c28a92f39b5544579b1e322e6000cfff(sums, i):
    R = i
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    return M


def func_80a7c3ff17b149199a241df30f373024(sums, i):
    R = i
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    return ta


def func_5b173cdd92dd4538bd16f64bd0bbf572(n, sums, i):
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]), max(
        sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return ans


def func_7d0f327fb5bf40d097074487cb121fa5(n, sums, i):
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]), max(
        sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return M


def func_7039e49efac846309af74370a1326b93(n, sums, i):
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]), max(
        sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return ta


def func_f55de79138194be2915da8bebfcea6f4(n, sums, i):
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]), max(
        sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return R


def func_ad932daac6104262a9d1fc1842c01e86(n, sums, i):
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]), max(
        sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return tb


def func_bc9e4cae4940469a83a2a7ac25fa1875(n, sums, i):
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]), max(
        sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return L


def func_95273be675bf4d8e9cdc2ed1d7ef3e83(sums, i):
    L = 0
    R = i
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    return R


def func_d524d54ead914f3e9da72dc56e1c24f4(sums, i):
    L = 0
    R = i
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    return ta


def func_f9fad7adc2224c2c87bd557a8993fc50(sums, i):
    L = 0
    R = i
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    return tb


def func_9690aff9db284bc9b0ce33ee1640a9a6(sums, i):
    L = 0
    R = i
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    return L


def func_78f06a7e150a482ca97f6301670882d5(sums, i):
    L = 0
    R = i
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    return M


def func_eedbff19446941ff84aef6679321d17d(n, sums, i):
    R = i
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]), max(
        sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return tb


def func_0b547cc3398f48c884ea0a5ff1c57546(n, sums, i):
    R = i
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]), max(
        sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return L


def func_a4e4ad6c0256433abd81824c505ac63b(n, sums, i):
    R = i
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]), max(
        sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return ta


def func_026b5c645fed4dddbb9ac060629b8e7c(n, sums, i):
    R = i
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]), max(
        sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return R


def func_b2b6ad10a386492dab50b6512f513f78(n, sums, i):
    R = i
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]), max(
        sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return M


def func_f037e7a880b14fb7a7bc4e62b4f9ad2a(n, sums, i):
    R = i
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]), max(
        sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return ans


def func_0fd0f2203221417e80c315ba1a669827(n, sums, i):
    L = 0
    R = i
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]), max(
        sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return ans


def func_219fa31a2b6f4244b599c448adfadfca(n, sums, i):
    L = 0
    R = i
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]), max(
        sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return L


def func_a06cb7cc9587467584631bd3c4bf901e(n, sums, i):
    L = 0
    R = i
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]), max(
        sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return tb


def func_4c7262ba6cba4f5bab3a49dd8e05050c(n, sums, i):
    L = 0
    R = i
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]), max(
        sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return ta


def func_fad263e0e4cf4a0383bdbe2123450034(n, sums, i):
    L = 0
    R = i
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]), max(
        sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return R


def func_8cce52d7c32e4230b7cbcf5b33b8a56a(n, sums, i):
    L = 0
    R = i
    while R - L > 1:
        M = L + R >> 1
        ta = sums[M]
        tb = sums[i] - sums[M]
        if ta < tb:
            L = M
        else:
            R = M
    ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]), max(
        sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return M


def func_646d94532f5b49268111b04065060a1a(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    return q


def func_24f6c77174b747e593f0b687a5c27565(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    return s


def func_668c0dd4c9c64c19bb5f148ed246cc81(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    return p


def func_88511536bff447e38f57cf54b66f4cdd(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    return i


def func_f82e472deb384e9cb5a5eba5b89c9291(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    return n


def func_ce808dbcab8d41438591917549e1eef4(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    return r


def func_65fa3e5c8b9c4dc0b0275cb67981b153(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    return v


def func_2372420de96347fea3bea2f480eb1261(p, r, s, n, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    return i


def func_7607c8edb3944cc5ae52162bfbe1abd6(p, r, s, n, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    return sums


def func_75b282ee54ba4cbfb0084aa77185c3ba(p, r, s, n, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    return v


def func_b0e88099aff44fd99801beddace8f8d1(v, n):
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    return sums


def func_f8b212bf25b4488e816e17bd28bdc9a6(v, n):
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    return i


def func_b0e8371208aa44418da4b2e692e5b5ba(v, n, sums):
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    return ans


def func_61ae8df8d2754869be621b980c83e11c(v, n, sums):
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    return i


def func_fc3aa1b4f67b445f831aefcc76f0f968(n, sums):
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return i


def func_86aa924b6abc4c55af76fb07083101fd(n, sums):
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return L


def func_3d0453e529a14bd09c2802514aa97d9c(n, sums):
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return R


def func_0f7464490cf547afacf86c0736e1ca85(n, sums):
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return tb


def func_7e9aca69ba4b46029ac32c59efbdedfe(n, sums):
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return M


def func_a12326c5267a43d0a923427eda2b8373(n, sums):
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return ans


def func_6b19a23dbe1747b382738a10efbb8b97(n, sums):
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return ta


def func_d9bdda2d41ba488db8ad8c50c9c7fae0(n, cas, sums):
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return L


def func_943ee61f3ea4428699e748dc74f726bb(n, cas, sums):
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return ans


def func_5beb5757040a46d0b2c186ce6097f3f2(n, cas, sums):
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return tb


def func_7e57649d1dd34d30bfae8ef909a5bb4b(n, cas, sums):
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return M


def func_da45c46a246f43aa81fab4f75d330ca5(n, cas, sums):
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return ta


def func_91723935908a446f84a2cdaf8538d8e2(n, cas, sums):
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return R


def func_07d96cd2f257412dac943b9e2f381774(n, cas, sums):
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return i


def func_a860c4946ea340a5a17c5942bc4905e8(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    return s


def func_c2f6e1b3d1d241f1a6f1fe122a088076(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    return q


def func_1c42bc0d8ee3408f9a73b3b33b801521(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    return p


def func_e102d7c78a9f48208a08fff65feceaaf(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    return n


def func_2e9947f4a8f447e397ba78ddfe26324a(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    return v


def func_d7ab372d06234b31b61ba93adae4ed17(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    return i


def func_00a3eb98c652443c8d761947515b6595(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    return r


def func_56cf673023e443eaa0f3a5cf7ab7e193(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    return sums


def func_c9d82092b9c54e91824cb697c6cd4f8c(p, r, s, n, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    return sums


def func_7632e75c12784964b5426a90ae0e558a(p, r, s, n, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    return v


def func_2ea9849bb3bb495989e2d88e2e6613fc(p, r, s, n, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    return i


def func_868775c1f9474d42b5a115f3b30e5e5c(v, n):
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    return sums


def func_c0decd3effff409a8766df590212ab19(v, n):
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    return i


def func_03a111b9b67b44d0ad98d843ba0dcbb1(v, n):
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    return ans


def func_382204dac5d3456c872243d9333bad2f(v, n, sums):
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return ta


def func_39106dda214a40febd1084d0a0c3943b(v, n, sums):
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return i


def func_8a1912d105f040799f759d41fb78b260(v, n, sums):
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return M


def func_05de1477743d4e21959422d0071a6dc1(v, n, sums):
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return ans


def func_2e169977eb0d448cb171824bc1ff4965(v, n, sums):
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return tb


def func_bfc4f688b45546879098458ac006c42f(v, n, sums):
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return L


def func_f07506738a58423abfddbd65761f4918(v, n, sums):
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return R


def func_a8587a784d034981be8c9eaef31aa749(n, cas, sums):
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return M


def func_2e7d1f848bf248efb922754abf7bb52f(n, cas, sums):
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return ta


def func_2cd95bf1b7f14554a01a07540b177223(n, cas, sums):
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return tb


def func_6717dd9a85f64fbf849d996c62ecf5ce(n, cas, sums):
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return i


def func_88294acefe664bcca6b13cb02d406414(n, cas, sums):
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return ans


def func_bb99c8ad87c94820bee741ff0accbff1(n, cas, sums):
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return R


def func_5405cf3696fa421d96bec869d9f48553(n, cas, sums):
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return L


def func_8c54e81fb06d482a865d65076abed404(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    return p


def func_28e4f5fee6cf41a6ba4623881eded737(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    return v


def func_74f1917498a94eb0a7cb108f35a13c74(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    return n


def func_58c13b4e5dc9494b887d39d9b2ce0a8e(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    return sums


def func_68b5e0d30be242c28861e91d8419da25(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    return s


def func_1aa8487631c446539fd3013c837014c9(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    return q


def func_c5fa2dd3d4b04ebf82cf064f76f477e7(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    return i


def func_0d29d5b8bbb2408f9d4334ee7c4e244b(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    return r


def func_d5448f701eba4a87b25646a66d500c8e(p, r, s, n, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    return i


def func_5b5aa7ab1eb24ee48e4b6b96ac96ee01(p, r, s, n, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    return v


def func_c60ce2fd3ef04529a0f1cee330f0990a(p, r, s, n, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    return ans


def func_85000b9f03f3483dab4663f6b7e20a19(p, r, s, n, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    return sums


def func_c5a74235b7954d46a598512699ae0b0c(v, n):
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return i


def func_be812ed82fec4989bfeed751ff83ceb5(v, n):
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return ans


def func_60e95f66abfa415382e647be1d3f7409(v, n):
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return tb


def func_973c7527417147bb873acc7f665d1e11(v, n):
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return M


def func_0939ef454b804940bafd2113a1d23f70(v, n):
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return R


def func_dc38e51c6edf4aff99ad18128d4d67af(v, n):
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return sums


def func_cada8271271342c982165aea4fc9e897(v, n):
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return ta


def func_116de1d6de0c47928eafa8e0b57d1e90(v, n):
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return L


def func_e5082c595ca049da8a95b9eaf53dcaf7(v, n, cas, sums):
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return R


def func_b70b5731a8a04e699c7eb8100cdcd474(v, n, cas, sums):
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return i


def func_bc61fbccae1e43bdb18c3c2f9ac87358(v, n, cas, sums):
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return M


def func_aae7c4bff4ab4c98804013434906aecb(v, n, cas, sums):
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return ans


def func_4773eeb0b0c04aab8f5e6b165f0b54c1(v, n, cas, sums):
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return L


def func_adf40514d76940c8b188b014bd4d1bc7(v, n, cas, sums):
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return tb


def func_74fb115ffd984aca90d3985a8c4b1b8e(v, n, cas, sums):
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return ta


def func_39a02aec7b62414fa7a204582af8c419(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    return i


def func_985cfe6ec7a246a0830b67450469bea9(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    return ans


def func_617d575f1e5a44a09c54169bdca61f1e(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    return q


def func_4a3d2d8e74e94742b94c37a87e292b39(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    return v


def func_b752d0e190c94e83a12a0cde0cd02e22(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    return n


def func_a0760a56327e4c5fb0fc21e6d8d79b0c(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    return p


def func_c83c8fd270154b3fa9a6c8666a73bb79(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    return r


def func_29ab20642cfb4b2da680c402ef64d909(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    return sums


def func_5a640bfbbe894aa48e11e61f6251ecef(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    return s


def func_3b931df8257d475e93098ee60d855ba7(p, r, s, n, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return tb


def func_0a559bb8b840483c9feda75632667cb7(p, r, s, n, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return i


def func_f3ddf63b31534d6bb4d1964ada5f0c43(p, r, s, n, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return sums


def func_d337720fc28b4e7eade492638551257d(p, r, s, n, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return R


def func_53c5c02fc819427bacce70761e524d53(p, r, s, n, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return L


def func_643ec1ba9fe949bfbd474b4a22d582fa(p, r, s, n, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return ans


def func_b35cd9b1c8504070ba06645e163a71eb(p, r, s, n, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return ta


def func_7d9cbd7fb67e49b7a2f7f203d1dc7876(p, r, s, n, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return v


def func_4795f616c5cc49fba342140bc284bc60(p, r, s, n, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return M


def func_b08706539fb54d9e8b649ad72606e038(v, n, cas):
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return sums


def func_0f17a2a585244fee8785672ad3239c5c(v, n, cas):
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return M


def func_c143a8f10839426484b5b940ec70caa8(v, n, cas):
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return R


def func_88aaf79625704c2ca2371637514c4502(v, n, cas):
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return ta


def func_a968e1a7e1a34ca6ac274206333bb1f9(v, n, cas):
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return tb


def func_e6dfbf6fd35c479e97855b59d556d3c1(v, n, cas):
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return L


def func_04fecfcfaeba4d5db6b541715ef58ee4(v, n, cas):
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return i


def func_973ffdb247724d96ad91ad11e3b0a52d(v, n, cas):
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return ans


def func_d0195296e94b4e1faeeb9d2c09b99928(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return tb


def func_f5804e9c13c6405a91e7d60e72500754(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return v


def func_75703dd7b0f3451eb155cc1aa564c72e(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return p


def func_d57529b78982452da20b3c309269a0cc(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return M


def func_c6a2f74d003240d4860f64fa12b921f7(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return q


def func_c35988e71aa04a6888391b0fd0dcf61d(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return sums


def func_6718cf681a6448be9dd03abf985316ec(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return ans


def func_0f735c6e7a89433da60322b39dc1a57a(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return ta


def func_3b1821367d144f6c82bbfd6f024bd671(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return s


def func_68047a2d4d9044cfa3702680d305ac4c(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return i


def func_f0315941ba4d47d885a14340650f57d9(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return L


def func_a1e5bb539c2c4a59a9b72add2d653d66(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return r


def func_50e6f565d9e74badbd410f6c5b1753df(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return R


def func_e98ffa2b88864f418078ebf17f35b72b(infile):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
    return n


def func_9790defe19824e8bbacf8a46d41a2b91(p, r, s, n, cas, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return sums


def func_90eb93458648436cbfbe4843f4dd93c3(p, r, s, n, cas, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return ans


def func_348e913aac64475e95e46df782094207(p, r, s, n, cas, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return ta


def func_ba398b7eb37845eab625255530cccb33(p, r, s, n, cas, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return i


def func_5c8b9174adda404aad750914e8a6fd29(p, r, s, n, cas, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return L


def func_ab9258028c62466ca86a790f8f281597(p, r, s, n, cas, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return M


def func_40cde3d6e41946cfb6ca83b65d95c5b6(p, r, s, n, cas, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return tb


def func_b20a27368d184a74b0a9ce7374d480c5(p, r, s, n, cas, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return v


def func_a3e124e790764143bb2af6e78048c4ea(p, r, s, n, cas, q):
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return R


def func_4b44449a8010442b9a7638a17f9fea7f(infile, cas):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return i


def func_bafc4ced5c55441c97b29216411f177a(infile, cas):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return sums


def func_24273f0466514ec08167e937e9779620(infile, cas):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return s


def func_96c5b0ff9e5940e0b7484313f6f24188(infile, cas):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return v


def func_2628dc7e2fa3468c84212dc0c00fd4c5(infile, cas):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return ta


def func_2951fd8853df41eb94743b76f1b769da(infile, cas):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return r


def func_15b7c970ac2b4f3088edc60959302801(infile, cas):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return tb


def func_45f72b3739a04954931656c07fa438a2(infile, cas):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return q


def func_b90b8bbef0a945cdb37000d462adaced(infile, cas):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return M


def func_f45686d5342b471191d19a1abc35844d(infile, cas):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return p


def func_cce9c59a074e45b5af70680cdbf34ec6(infile, cas):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return R


def func_dc51b1ef74d541c681c71322a2b19703(infile, cas):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return n


def func_3a2f5ae114a94b6aa5b2d0855cdfc554(infile, cas):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return ans


def func_ef2fd5a7634f447789b0746b63f5fcae(infile, cas):
    n, p, q, r, s = nums(infile)
    v = [((i * p + q) % r + s) for i in xrange(n)]
    sums = [0] * (n + 1)
    for i in xrange(n):
        sums[i + 1] = sums[i] + v[i]
    ans = sums[n]
    for i in xrange(1, n):
        L = 0
        R = i
        while R - L > 1:
            M = L + R >> 1
            ta = sums[M]
            tb = sums[i] - sums[M]
            if ta < tb:
                L = M
            else:
                R = M
        ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i]),
            max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))(
            'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n]))
    return L


def func_7069a034bbad48069dc01a104fc2ba76():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    return infile


def func_297241f8e7f9421482f79933e8526cbd():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    return z


def func_ef77ff506eda4b92bac71ebba758301a(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return q


def func_8c7fa4368c584c6984c4d38403c74501(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return cas


def func_40576f12d7924adaac424b1d0636ef78(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return ta


def func_d64ea2854ef848f49dbd8e8a74823c05(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return s


def func_9bf4f9deadf04942878869f21ad03d80(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return v


def func_01564c1a8fca4607a293d179e7cded1b(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return n


def func_43942fdd30ac41ad9c73cdfd0e0bb96c(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return R


def func_146ca2360d3b446996fcd8f59e81a60c(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return tb


def func_2700d43e38604af2a186292fdd5763e5(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return L


def func_e8b4a2ad032a4a128b02b16523034e71(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return sums


def func_b57e57c7a5f7486c9fe3afe7e866bc3b(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return p


def func_01e5a191261b4213bcc3fa269f1f44b9(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return M


def func_eaf32c1385674082817d016bd9a8a152(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return i


def func_1628d3a8c5fa4ee58e306b124a65852e(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return ans


def func_26317cbfecbe41b0943e05061f031152(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return z


def func_5f660237c88f460586a46872a3db6b19(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return r


def func_d29735db5df3480e926b884da21ab5b0(z, infile):
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return n


def func_ee3ffc24a80b4488b50e420c9c0d1fcf(z, infile):
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return p


def func_6e4adc2d970f413ea7761211a8f2f730(z, infile):
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return tb


def func_c972b838dab54c1a9cc980d386546c53(z, infile):
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return R


def func_6e273e75b49e465fa3cf422a6061e184(z, infile):
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return s


def func_4571a0abfece48b7aa31130c2a336bd0(z, infile):
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return ans


def func_c060f496b73b49509ba6ec8679522aae(z, infile):
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return v


def func_fa2e8d19ad1146af8db24db4f5b0cd5d(z, infile):
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return r


def func_b267a85dfb334e71b28cb3ae1a5ca672(z, infile):
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return ta


def func_293635334347407cb771d32dba54d0c6(z, infile):
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return cas


def func_93419f027abb4d7da0e12210cf9b0186(z, infile):
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return q


def func_911ac771ef3342d397a5a1e68347344d(z, infile):
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return sums


def func_74b9f5e829c04b688a1621fdd619bd31(z, infile):
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return M


def func_90ed01294c8542d6af876237acbfb4aa(z, infile):
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return L


def func_63bfa8c5d5cf45198b421a5700a4a0e9(z, infile):
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return i


def func_9ef91f28b67340998359369b521e0400():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return v


def func_3dc2b59139b44451b0950ba376bf1eca():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return s


def func_4dd4076d10a44972badbacef3cbffeb4():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return M


def func_2a4def029f194a238e9ca49badb8a8ca():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return infile


def func_5da5e18071a0407683dc3707b2c7668c():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return n


def func_26a7a347498b457a8121ff75865e484b():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return z


def func_3116e18c6436416e8f592b6cfa09109a():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return cas


def func_b6f640d65f114f27a091333a28fb26a2():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return q


def func_06369c050fdf4f4ab32bef2b60b13cbf():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return R


def func_0c0d03327f22493db2b2e98b9f485948():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return tb


def func_482dac3a747c49beae1791f88f666993():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return L


def func_47fd288bf38040be839383a26cf8e56f():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return r


def func_a6b858e4eb6f40f8af2d980506712041():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return ans


def func_c3e235bce1de4929832fb9ba7e0b6f0b():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return ta


def func_b9c3fc9ffb6243f9b09a27691187110f():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return sums


def func_3a50b0f0123245149304f737e46bfbbb():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return i


def func_db8f1934f08e4b6fafb05ee0f862cb99():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    return p


def func_1994dfc4394c4ae0abb41737bb91ae9d(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return cas


def func_eb2102ca2df545e9a38b3e66cbc4dee3(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return R


def func_e008827f27754c01ba014bac0879dcf9(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return M


def func_b19c34ee5d6746fda8a935f18968b9ef(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return tb


def func_734404cddb754ff8a148fded300e80f3(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return sums


def func_bcb90b59a16e492280f8ed9004855c45(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return p


def func_653c43fb95744526bd83ea8b9bd8ca32(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return q


def func_f8ff6653a1584eefab72cb3e70b3e363(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return n


def func_145057ac38f64b999c16d5bb65e205a4(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return s


def func_6be719fde85d4ee1aa6e4e945420aa6c(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return i


def func_6cbe63af973040438fe490aad2062997(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return v


def func_a5b90e1f5b314db387a3415e98afb0eb(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return ans


def func_73f166bdcda24fd5bdd4aad8dd926d2c(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return L


def func_1800a859d80242909e8969f8cf141ca5(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return r


def func_669dbc5de6de41afa2f2835e4776c3ae(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return ta


def func_3fa8ccbc1b0648539491b5a10139cc0f(infile):
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return z


def func_99d79836f0af45c9b5c00df07655c2eb():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return M


def func_76c04478e2d64a0494a28cbffd66b835():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return L


def func_8afc752b389546cc9bcdf2924d6dd4bd():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return v


def func_fa766f8205ac4c7caa58ca1d647dcec4():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return z


def func_592eb7243435474cabd335f7fbe78089():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return n


def func_a90b4b123b0b4a799df267e63ccb9ef0():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return R


def func_258296fb1419437699fe93b7e7031b98():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return tb


def func_aa8f40f1b5234824bf96d659cc7c11f3():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return i


def func_be3e9fca1f0e4336b6d3f9e3dc2322bb():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return sums


def func_7c27388f461e4096bc841a2817a95bb4():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return infile


def func_56019eb5db284380a05cb689b91cb36e():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return s


def func_c28a102298bc40e791b82c0561da370e():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return ta


def func_5948f63d8cfa4d7698349f3577b00036():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return q


def func_8369e1937a8b4ab1bae30af0605ce649():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return cas


def func_47f0fbad0f5a48a8b682401fda142c05():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return ans


def func_11140975f6be4e76b0aa23affad0875c():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return r


def func_124ac8900e954597893de7e6cf78d0cd():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    z = int(infile.readline())
    for cas in xrange(1, z + 1):
        n, p, q, r, s = nums(infile)
        v = [((i * p + q) % r + s) for i in xrange(n)]
        sums = [0] * (n + 1)
        for i in xrange(n):
            sums[i + 1] = sums[i] + v[i]
        ans = sums[n]
        for i in xrange(1, n):
            L = 0
            R = i
            while R - L > 1:
                M = L + R >> 1
                ta = sums[M]
                tb = sums[i] - sums[M]
                if ta < tb:
                    L = M
                else:
                    R = M
            ans = min(ans, max(sums[L], sums[i] - sums[L], sums[n] - sums[i
                ]), max(sums[R], sums[i] - sums[R], sums[n] - sums[i]))
        print 'Case #%s: %.10f' % (cas, 1 - float(ans) / sums[n])
    infile.close()
    return p

import sys
sys.path.append('/home/george2/Raise/ProgramRepair/CodeSeer/projects/src/main/python')
from Y14R5P1.Grzesiu.A import *

def func_0c1046dd31d944ea823eab991f0e63dc(totalsum, b, a):
    kA = totalsum[a - 1] if a > 0 else 0
    kB = totalsum[b] - kA
    return kA


def func_422fc4f073a5491ca907af456989307d(totalsum, b, a):
    kA = totalsum[a - 1] if a > 0 else 0
    kB = totalsum[b] - kA
    return kB


def func_cb25b39d091a4ed0be971403e40545e8(kA, totalsum, total, b):
    kB = totalsum[b] - kA
    kC = total - totalsum[b]
    return kC


def func_48ddb4d7198042df9124af4330d4a9de(kA, totalsum, total, b):
    kB = totalsum[b] - kA
    kC = total - totalsum[b]
    return kB


def func_bba41d648d0441dca54c56d48145d9af(kB, kA, totalsum, total, b):
    kC = total - totalsum[b]
    return max(kA, kB, kC)


def func_130b9eec4f0f4f0491610e9a630f05df(totalsum, total, b, a):
    kA = totalsum[a - 1] if a > 0 else 0
    kB = totalsum[b] - kA
    kC = total - totalsum[b]
    return kB


def func_c418382fb0eb4534952deae538bb9d95(totalsum, total, b, a):
    kA = totalsum[a - 1] if a > 0 else 0
    kB = totalsum[b] - kA
    kC = total - totalsum[b]
    return kA


def func_dfb1511a80fe42d0920b4b71b233a7ac(totalsum, total, b, a):
    kA = totalsum[a - 1] if a > 0 else 0
    kB = totalsum[b] - kA
    kC = total - totalsum[b]
    return kC


def func_b007cdf7074f4d2382215cd9b63f23b6(kA, totalsum, total, b):
    kB = totalsum[b] - kA
    kC = total - totalsum[b]
    return max(kA, kB, kC)


def func_e65f348d9f5c470e812bbdfd0bb9769b(totalsum, total, b, a):
    kA = totalsum[a - 1] if a > 0 else 0
    kB = totalsum[b] - kA
    kC = total - totalsum[b]
    return max(kA, kB, kC)


def func_8e4850ce4f84418ebfc04ad182d62d33(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    return p


def func_7116f7f249d84c3e8c2e9376e5e146f0(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    return s


def func_416f54a060fd409d8a38cf6f7339f537(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    return A


def func_da0f02fa2fab4bfd90e55bb5c1f3897a(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    return q


def func_f1cafdeac7924855905a43e0e50f8c85(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    return i


def func_af94cd7291db4d8392637e0964190c75(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    return r


def func_dd4ee7dff058465e8f9093c72bf44be5(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    return N


def func_6dd4a037ee1c41ed8bdf11451d7e1266(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    return total


def func_954d03bde7054130aab706fa6da97018(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    return A


def func_82ac2147bb5d453ca2588da6a7904c95(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    return i


def func_9391841ca22f4e45864b78ca7501bd3b(A):
    total = sum(A)
    totalsum = [a for a in A]
    return total


def func_5fa8c3c70c6b4c4d824ad7d14417620a(A):
    total = sum(A)
    totalsum = [a for a in A]
    return totalsum


def func_94aff88d4b4848d3bd7c9da2849f2741(A):
    total = sum(A)
    totalsum = [a for a in A]
    return a


def func_deacbfabc9ed40e0a33ec1637bf3430d(N, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    return i


def func_9d5cfc4a34764e4f867da51ac2811b37(N, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    return a


def func_03d2f890a2c949a89793ecdc37f01f8f(N, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    return totalsum


def func_bc6e0ffb677a4a67b1ba826848706e9a(N, total, totalsum):
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return best


def func_6193114b510e409fbb3ed2fb52bd8b7d(N, total, totalsum):
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return i


def func_78f971ff88584c14ad46ac76e6fc8032(total):
    best = total
    b = 0
    return b


def func_f3a042db45ca47a0880954620f7b5783(total):
    best = total
    b = 0
    return best


def func_d26fbe01c90148db82aaa7350d85683b(N, total, totalsum):
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return b


def func_b2b1a0159b424f4a8e5e2b5bac201d3d(N, total, totalsum):
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return best


def func_00ae7a5021ec492d8850a5f8530f152f(N, total, totalsum):
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return a


def func_eba418b4202c415fb7e3f41e9688876c(N, total, totalsum):
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return a


def func_a55d54ba506b4cd2ad93472f66412496(N, total, totalsum):
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return best


def func_5c90fc2fd4474d2f8fe63538661a736b(N, total, totalsum):
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return b


def func_cb9fa78f3b444f86ad7698e0c085d7c8(T, total):
    best = total - best('Case #%d' % T)
    return best


def func_93deb75380134701984007a407855566(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    return q


def func_d92a13d828a942c28298b66ca886930d(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    return p


def func_5a6d25f1446a46529d652fb6c2ae134f(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    return r


def func_150486a3999145ec89520933b8f88e70(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    return i


def func_0d712110dc7c47779dd70c540d1aa50d(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    return A


def func_7937b50a609540bdb874c3ad9fcda873(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    return s


def func_3073a97d9ecd4a1c92b7db471d088adb(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    return total


def func_b43a45da96df4bc199eada33015296a5(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    return N


def func_6a89344f1c3c4b8da1b282d31691fa98(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    return totalsum


def func_8fb52450fc054702b35b62053f47b93d(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    return A


def func_a5faeb40726d4e7287b8837bc707874f(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    return i


def func_bb60e94bb9a14c1bae93b1a33d441eef(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    return a


def func_b47f7a892dd2437bbb253b9fb787f688(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    return total


def func_0287b13dbc004259bde8be86e46d338a(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    return i


def func_721f8e105ea84f1eac5263bbeb281074(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    return total


def func_8007080568044eaaa1129ad105693aaf(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    return a


def func_8c742d967969486fb7cf47965a68ccad(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    return totalsum


def func_cba549662da849b58feff5076242d903(N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return a


def func_5427bae4642e4fdeb8cc62f7b3113952(N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return i


def func_099d62d420a14be2af61d0eef35882cc(N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return totalsum


def func_412aa6909aca4e2f958cf37202da9dd7(N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return best


def func_e35f043e8aa84ecc8b3e0393dfd707bc(N, total, totalsum):
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return best


def func_8beeb2ec54f54b3391cac4ec0668b67d(N, total, totalsum):
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return b


def func_652d5bbc2211491288de6c3066a45dce(N, total, totalsum):
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return i


def func_d184302c4fe64cde800c5118ad0b7f31(N, total, totalsum):
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return a


def func_d016d8debeab484193fc6070b396464f(N, total, totalsum):
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return b


def func_c668763de076457cafe3d525f03b9aed(N, total, totalsum):
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return best


def func_ce9c680390fa4a739bcb2f216f41cc08(N, total, totalsum):
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return best


def func_8cefb7563b65491f840bd963a4e06e28(N, total, totalsum):
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return a


def func_9205e1b6d15c47ae95da73e32aa7d2c2(N, total, totalsum):
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return b


def func_7d3bdd4aaa334ab79331397a4270a372(T, N, total, totalsum):
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return best


def func_8819fef0fc5148e4a0470dcfa8346b13(T, N, total, totalsum):
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return b


def func_83b5413719db4c81ba4a54550c7a474e(T, N, total, totalsum):
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return a


def func_4628dff9ecb34bc9b8665814ed14c2d3(T, total):
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return best


def func_f6c3835ea4824cbf80d96583a94cb3d0(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    return A


def func_a2a7841663d749e0b6a1538c684e1b57(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    return N


def func_a433cc19c124454a97c8a4cf27bcd898(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    return total


def func_f24006dc23f846e185568867764af2ee(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    return totalsum


def func_c3c09e290323417ba11580f0e7713ce4(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    return s


def func_0945d65e8a434ee9a719cfdfaf94fcd4(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    return r


def func_f149df5fefb448f49ed7ffaf58d287e6(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    return p


def func_d7b19a4983f64e608c3a2995ec0ffc2d(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    return a


def func_5aaf89c6004f40429b036ef3d20be59f(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    return i


def func_b33308ebf4ba4c2f86b38d6d146ad9cc(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    return q


def func_ed829d76cfdd4b59a9adc102aa0fbaa5(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    return total


def func_95540fe1d5db495a96297feb9ab821b2(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    return A


def func_8ab2527b70af452baf1cf9779d1cbcaf(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    return i


def func_a8cd2d6b156e44b2ad0e6504ac6bbed1(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    return totalsum


def func_d06f6698c2a846998ba7071fd9458b55(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    return a


def func_3644d4881d65454a8b0e9d0510e38422(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return totalsum


def func_b3feac9ec0694c90b19b8e431568b51d(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return best


def func_f9479ff289a948be8c2d7a7b0f2dfa83(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return i


def func_ac8b92c83ce248479046b3d1191f9935(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return total


def func_4875af921b0c4977ba51da4e664ab59b(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return a


def func_31a999361e184b9b8d1f149a051ddcc1(N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return best


def func_df07ccb748a54e528df29cc926af1ee4(N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return i


def func_d398a0b3c1c94fae9678823ece240fea(N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return totalsum


def func_faff262f409e4f248fa54d003c00fefb(N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return a


def func_114e4fe8358a4f32a697fd438e39773e(N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return b


def func_668cfa2fae264d36867d27ffd2ae1e2b(N, total, totalsum):
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return best


def func_cdd19a5dbfc643abaeaec08464a05c9d(N, total, totalsum):
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return a


def func_2174296acb144810a55351d88c5dcce7(N, total, totalsum):
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return b


def func_1f03d84bfae0482f9aa5f9d61a1da0c7(N, total, totalsum):
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return i


def func_5833337ca69a40a181bf8c1cc7d68ff7(N, total, totalsum):
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return b


def func_fe7110a853a64080b6fbd23084718eaa(N, total, totalsum):
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return a


def func_b1f3ff45a4c94846843ba29db93fe331(N, total, totalsum):
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return best


def func_81ea9263f3e842a9ae01a7433382d4c8(T, N, total, totalsum):
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return best


def func_bf9d5058feb84aee80c5ca00a2cb54b2(T, N, total, totalsum):
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return a


def func_030442168f234726b610e6a0c02e47a9(T, N, total, totalsum):
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return b


def func_ec1d02104ff94365a146555cb0225777(T, N, total, totalsum):
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return best


def func_68b2410982af4f4a96700459610ac3f8(T, N, total, totalsum):
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return b


def func_ea040bbde3f44a7cb65e7b1f853f83e2(T, N, total, totalsum):
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return a


def func_0e8c513fb442411f97db0855e99c9cfc(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    return N


def func_c7aac4232ceb4332bb6765fe230eb8cb(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    return r


def func_c64ef9dd33e540a1933b88193be1c149(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    return s


def func_b70140caa4824149831541bdc759ac7b(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    return total


def func_d8e62241fbe24924a08ed3df065f67da(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    return totalsum


def func_3c475224df74450ebbbebd68db957a8b(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    return q


def func_43f87e93b79b46e9b36f5ec1ac85c946(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    return a


def func_241fa146277d48f2b99447ee62343980(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    return i


def func_190c482f8d024b3599d388e753beb073(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    return A


def func_8c8a3306df2b4e8c8535f5c1df820f9e(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    return p


def func_cd51604d70bb4ef5933fa927221116fa(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return totalsum


def func_bb3e4b971f22470da676c5b725207f07(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return best


def func_a019d6d9f147401e9081f89d7dbe4bba(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return i


def func_e05db95d4c7a47b89133877c29283d4e(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return A


def func_771e4fdad22c419e80e2672653ef8ad7(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return total


def func_6e414cd37558425f9ae245e0f4b7c937(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return a


def func_785e8ebf3c9146ce952803401103dabe(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return a


def func_9d95579b9fda4f26b88e39b79c5059d5(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return best


def func_1b7921098626402992761f63a58479ce(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return b


def func_68e5b2a66f5a4bddae385b8336308872(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return total


def func_9dc316eb090e414098169c7abcf13cb7(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return i


def func_80d4864700ce4dd0ad11216a8af20a43(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return totalsum


def func_b64703189512463e9ee70d7dc83fc375(N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return best


def func_bd4c2269f3a444c580534180fd56666c(N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return b


def func_0eb21573e19d44e0904f29a1a176a7b4(N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return a


def func_6e165c549d7349069dcad42585d4381a(N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return i


def func_f5e3925197d94712bb243ebda63886d0(N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return totalsum


def func_0932f865260643f1a109fb1ae90c5edf(N, total, totalsum):
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return i


def func_1390dd1047e146e1b1a6cf7838cfb5c2(N, total, totalsum):
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return best


def func_75b310ced29e4f85b6ffa5be84905f4e(N, total, totalsum):
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return b


def func_e19d5aceda4d42708e3d55d1748c2237(N, total, totalsum):
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return a


def func_a4c25e095ba743018293dafb1fadc8fb(T, N, total, totalsum):
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return best


def func_fc482b6c95e542c4b070b3f2c6e75c4c(T, N, total, totalsum):
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return a


def func_68482c37c95e43219306daddda33308c(T, N, total, totalsum):
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return b


def func_689e87938d01400d89fcdbd0a1657e42(T, N, total, totalsum):
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return b


def func_a33e235cc6ce497db3a71f850c881560(T, N, total, totalsum):
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return best


def func_73eacd2b66e2428facf6fe9dcd7caa33(T, N, total, totalsum):
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return a


def func_fcb42c7f0c6141958b4c4eb757cf8ced(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return best


def func_1b522bba99d244768f92ca0d66907596(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return r


def func_f7b9697a0bbe437eaca9e33bb5952488(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return totalsum


def func_fe527a3ce0b3419aae5f158d3651b562(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return a


def func_63de86573b224aae9f1f9e8474443dcb(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return s


def func_6462f1db1fbf46449e1f9f9c17b4ca86(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return A


def func_15a8181c64ab4692a82de8ea05f134df(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return total


def func_8b434e63e32147d2bc32c6d882bf50f6(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return q


def func_06849a63535c47c5a28626d1066aa50c(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return p


def func_993fcca1c0e649cc8d64de87bd4242ee(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return i


def func_e2f8594e9ca64dcd8654f23efbcc83ad(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    return N


def func_a8bb40fc65134737ba360f8f3cd4b5ba(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return b


def func_5c936034506c47c5bd14033a6b953f6a(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return a


def func_ed345658196c43768f6c38d1cd4015d4(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return best


def func_3e88384849a9496ba926be882060713b(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return total


def func_6d4fff6f763647ea8f0e9dd103679f30(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return totalsum


def func_a5c7bc28811e4fd1ac02c08c235801d5(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return A


def func_7248f802060a4e7794c8959d6107aced(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return i


def func_bed0aeae57e14a26a98754c47d037921(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return b


def func_1031ea5561494143b4f27b3c582366d1(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return total


def func_53561c5d176f45759894a733267b6035(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return a


def func_88aabe94e6764b318ca15090dd04797b(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return totalsum


def func_aeff768c0ff849b28f22b3666805f417(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return i


def func_7f27c39d96914c7ca3021ab236623286(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return best


def func_9bd6ec8d36d940eeb9c65f5f0fee09bd(N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return i


def func_fff41eaa356b426abbec77e0ae7cc499(N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return best


def func_76d4ce7de8cd4ebdaea20dfb1d396722(N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return b


def func_533c9fcc8ae8408a928cf5db36ca6bab(N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return totalsum


def func_c6ebc6f32ada46b89d186717cd7f078e(N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return a


def func_f781a8c9fa3547e0bbec9cee8cd9dc58(T, N, total, totalsum):
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return b


def func_71f4942496a64bf18d521cf89329fc4c(T, N, total, totalsum):
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return best


def func_c3f89268148b4e67be97d9e5a2e5914e(T, N, total, totalsum):
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return i


def func_1e34644ed714453fa16f2cadc0130a53(T, N, total, totalsum):
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return a


def func_01e307c903734bd9aefbc95a706f28b8(T, N, total, totalsum):
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return best


def func_61e5332a00f8429382f5e19b86b0d934(T, N, total, totalsum):
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return a


def func_5eb9c9bbd97d4c67928fcd40c9ac09e6(T, N, total, totalsum):
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return b


def func_3eca48fdc68a451eb952d89dadf9c55d(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return p


def func_7d3910e9f0b74b938c3dd982d0e5d964(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return q


def func_d917dff6872b4f9088039baa3af2221d(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return N


def func_01a1ccf646a24ddb8981de1e709514b2(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return r


def func_6cc54bb0375142feb13cf04e82a65936(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return A


def func_0be6caff8ed74f02b53e6aa04d43bf93(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return i


def func_3d82270a03184d0e85302a0befa29e7d(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return best


def func_2199d683b992451d9c735d69c8380c8c(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return a


def func_13c29f009dca43cea9c187660f33a6db(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return b


def func_49b4495284ab46febcbc82c7168483c0(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return total


def func_7a087966ced24570a7629b2dc30f9a29(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return s


def func_479c4c122a8b4679b2faaa9b5d48f378(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    return totalsum


def func_f4ad26e4e8b4430daaf801ac9274191c(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return totalsum


def func_d9e3392f603c479ca85259bc0c7b34b2(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return b


def func_1d7d2382410e4afbad6e132229e3df25(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return A


def func_893929db04274d1f82a7d73563096ef6(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return a


def func_50795ee331ee43258656611679f9b6d6(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return best


def func_818782be43824fbabb7740c3f72462ce(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return total


def func_1b4eba326d7447e585ef56ee6461ac8f(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return i


def func_d28aa504c42b4e95a31d5ecc209cc372(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return totalsum


def func_a0601ae8aa534f048cb6098f9f85db51(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return total


def func_c952a48a25e247f8be18eabaf023cdfd(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return i


def func_835332840fcf4d8e917feeca658aec77(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return a


def func_1a6aa03d8fed4735b6c35cda31b064e8(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return best


def func_41a16dbe9ef949c3a0325a4933038f16(N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return b


def func_297acb7c309b46209e1a96b19a82e91a(T, N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return a


def func_8c735db321ef4188a222ecdcd7b2efe8(T, N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return b


def func_dd31827642ae4575831fe6cda5a39b91(T, N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return best


def func_1d7e4a5716a44b22a2305573c28676a1(T, N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return totalsum


def func_c4ac65d1931343bb9b6e996ad4152ef3(T, N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return i


def func_f27c58c7cc4d4147a89c1096958515f5(T, N, total, totalsum):
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return best


def func_e62fe36dc80e44a0a41bea416e4f92f1(T, N, total, totalsum):
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return a


def func_e11294462e2445489b52e6b0eed435ee(T, N, total, totalsum):
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return i


def func_49924ab686004a759bf4948f2bb194d6(T, N, total, totalsum):
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return b


def func_75b0e58d5c2046e0bb5b1406882523c4(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return r


def func_4e2e5c8fcc194f20993cddfdc052c55a(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return b


def func_7403b011372b40a3a65d9ad4ebe400ba(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return N


def func_27cd90810fbf4495ae543bd7962d072b(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return A


def func_00ffe956dfba46ddbc805bd41de24ddf(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return p


def func_9bbacec9b3af419cb486abe3fb656408(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return totalsum


def func_93308f57be724854adc102abcc118d34(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return i


def func_b0aa3e8451194389961221e9c416616a(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return a


def func_f56482a2429e4e148f120717c06e84b8(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return q


def func_8055994d0065464d93ef85cd8c21131e(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return s


def func_3bcd690eec1940128543fccbf5c22bfb(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return total


def func_0221858737204fa389e982dac0799bbd(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    return best


def func_5139fada504242c281e3dfaf4c5444b6(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return totalsum


def func_4df52d7b70ad4a37810abf46330a3aa3(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return i


def func_c5d31a6eb622455b9f7c863026b5eada(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return total


def func_6d0a581ab9084400bc2ad4509dd962e0(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return b


def func_47d3b72343c94709985a4ec5a9754219(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return a


def func_10c189a3fd28494689725a3fdc8f9891(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return A


def func_d43643d34ebd49c591a6a144a9caf44f(p, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return best


def func_c6d2018833c143c2bd608c67feb3227d(T, N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return best


def func_526fa2fc984f4447b08763398b048a81(T, N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return total


def func_3366a28a998f41dc933c3362dceb1430(T, N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return totalsum


def func_e61ed751ed6c464ea3c72675a48a505b(T, N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return i


def func_698f2fced81d49a7b92b09b9cc787229(T, N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return a


def func_2e985ed82f844b43a73426f35f0d4513(T, N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return b


def func_326a084b251c474aba3bf5157e019e23(T, N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return i


def func_83f866438efe4c8f894f8b44ba707abe(T, N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return b


def func_192877dd3f8542e0a895f6b9f318d9a9(T, N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return a


def func_6be1570d9df14bdeabe0c780d71063f1(T, N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return totalsum


def func_ea53fec8af8b41f69313c3e927e451d9(T, N, total, A):
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return best


def func_172a73f5168749b1ac20de58ee22ef30(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return N


def func_76570db24c144caa91967ac9ac1e9e4c(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return r


def func_adbf640f1e9e4cc0a7fd3eaee07b38a9(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return totalsum


def func_2aaa3e8ae0c640c793a528fc63a5e41c(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return total


def func_957089c5fc5545cb9ce942b5d4ef80e8(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return q


def func_366f89dec9974b10990f0331536c05c8(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return p


def func_7d49a5cd82954d9bb8f4557a9e1764de(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return s


def func_59a339997e42418688238fc08183ea56(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return best


def func_9411e23d1c104f8b81d7ae15d9cd790d(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return a


def func_38ef4e85f58242eb890ce11e30ee544b(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return A


def func_0a3d9c5358794d96a07a86e88bd11f43(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return i


def func_a89677cd5d8b407aaf99ada694aa9eac(infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best
    return b


def func_7fbab4a6a241418781b5a2d12d1a7f03(p, T, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return b


def func_9aa3be1304334d078816c173dc2f37d7(p, T, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return best


def func_6187c62abd5d4f4ea088f53fc2d4a8cf(p, T, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return total


def func_ff3b2d5022b841e495bea0c9eb53a45a(p, T, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return totalsum


def func_1f93aa92e947411b91e6f2783d55222a(p, T, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return A


def func_597204c0cb404c9983974cf8f235e6ca(p, T, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return i


def func_8605c097769648f3819629d43916b606(p, T, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return a


def func_ef7dba35d5834656a73cd78555f023b1(T, N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return best


def func_45b5aec34b7548d7b1f5f9d42de99bd8(T, N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return totalsum


def func_d6b516d8e9234a5dad5dc8802b0504ab(T, N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return b


def func_611534ecf9b2487c9cdcd23bf333395c(T, N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return total


def func_7934f1a86e094e1d864da8df5603aa7c(T, N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return a


def func_e5b4633dc62346eba6d8ace8f7f5b9e6(T, N, A):
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return i


def func_c8ac40984b3c4144871b8690b2828687(T, infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return N


def func_809b9e1e6c3a496f9caa599728bbb901(T, infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return i


def func_1ceb53a530e1435bb681a95a0d241be1(T, infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return s


def func_97d13fa555774b9e84f227df329b52f2(T, infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return total


def func_bb6de3759b69441ea78b54431633b006(T, infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return A


def func_05499c2e780348f98504bf8f7b9c7d9d(T, infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return p


def func_00d72e88b8404654b956708f231daadc(T, infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return q


def func_af9e65eec45c451b8eb830b4b95345aa(T, infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return totalsum


def func_b0ff1c498786447195d14db4860ca57f(T, infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return r


def func_411779ddb1ec4ade957f1d8871308397(T, infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return a


def func_81c3b38dac0c48fca84e80de2cad5358(T, infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return best


def func_72dc98d4f7504e5387cd75838acb038e(T, infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)
    return b


def func_8ce62155b9734233b417516d60100590(p, T, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return totalsum


def func_70be2c23b409422c9fdf414d68939ccb(p, T, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return b


def func_e3a7d5c635e54faa89dea71f048d02ab(p, T, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return i


def func_0f4fb040495b4139925341acd807c78c(p, T, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return a


def func_f539a9e24bac4f8796e02e51c3d12476(p, T, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return total


def func_ec4ef50f73ed4cae94034202d150039b(p, T, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return best


def func_5288b32e62e7470fab938555be76d716(p, T, N, q, s, r):
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return A


def func_efaa44fe3f2b4b2c9855bfd133bd99b0(T, infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return b


def func_56c37c59c8934f7aa515817dbe7140a2(T, infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return a


def func_7495008816464a76bb91d2ffc4988345(T, infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return i


def func_beef533c5bd543f695c4e264d1cd8fe0(T, infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return A


def func_e3493e1ae4b94c3b88b0cacdc6ceb441(T, infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return totalsum


def func_48e70dfd9719447583b13b505e41e402(T, infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return best


def func_002b1a05bdcd4e15a8af5576d9b91ca5(T, infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return p


def func_1e9868541192432497f7afddf6598f40(T, infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return r


def func_15358d1d753f4af0b5abf587f122981a(T, infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return s


def func_525021bbfb694e2d81ea77e6dfdfb893(T, infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return q


def func_3085b093b0094ae3babe3700b49f3241(T, infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return N


def func_529d5d0ce6d24c7b89be80d23f00dc9d(T, infile):
    N, p, q, r, s = line(infile)
    A = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(A)
    totalsum = [a for a in A]
    for i in xrange(1, N):
        totalsum[i] += totalsum[i - 1]
    best = total
    b = 0
    for a in xrange(N):
        if b < a:
            b += 1
        while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 
            1, total, totalsum):
            b += 1
        best = min(best, getsum(a, b, total, totalsum))
    best = total - best('Case #%d' % T)('Case #%d: %.10f' % (T, 1.0 * best /
        total))
    return total


def func_d3f7b486a618491a9a2c5ce79bc867c9():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    return T


def func_0784b0652171461a8249f952f2b48000():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    return infile


def func_379b3ac414f3412d82a2a3d21559845e(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return i


def func_a15be2b4249741d2a57c8a1a96e038dd(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return p


def func_ddaa4aa4e21a46f1a02effc47cf59045(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return r


def func_f2ee59dcc42c4d53b8a37093f7e40f19(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return A


def func_4e6cc241c7314974b4d28fd300c27ef7(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return totalsum


def func_dc36827cd4164af3965269e69805f105(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return N


def func_311acdaf55a14825b30544b6f62de751(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return best


def func_2b849feb727142e989b398248e69c4b0(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return total


def func_84004c157eb24824a7dd45092acff705(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return a


def func_ed9f2e9046bd48a6bc7b1f2cbd4b3307(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return s


def func_06ac1429d0dd4b6786a480a62be93d63(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return q


def func_358f85f329ad449f915a3878e2b03ee6(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return b


def func_d96a764c862148198fc928d5c4aea2ef(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return T


def func_392b3c81c3aa40eda55980e1c2344b73(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return A


def func_d17b7e8cddaf4ab9b9cec7ed00676ccb(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return best


def func_160b060d21ff4a44a65dff46a628505c(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return totalsum


def func_d52463c4007c4b1298b2c5b933e78cab(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return i


def func_03d836aa566443159aaee96fbb4e9967(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return b


def func_7e38d9e98b1049158c869d531753c12f(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return N


def func_10894e4371e1435d9b05f716a68add7b(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return a


def func_0a11821b1137476e88c18298384deb8b(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return q


def func_15bad475ff63420baa3ece9f13f35a04(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return s


def func_caf0cedfefe54103993a5aaffc3a5f5b(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return r


def func_73f6530a43ca4df1af33294cc65337cc(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return total


def func_5ad67b425b01433da824f5b458409971(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return p


def func_2a6eb9490f3b4fa89c4c00fe246f8bcf(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return T


def func_39b5ff4411a3446aa7aa21c266357ed7(N, a, total, totalsum):
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return b


def func_8abb784db8474fe48574d1cf6e65cedc(N, a, total, totalsum, infile):
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return b


def func_c10f7260f9ae4d4db9084aa2e4364cda():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return A


def func_1e62ef3080d34852a8994b744dd7cf8b():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return totalsum


def func_2fe7817bb9454ac4a7f42c36b06e5656():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return N


def func_41b7bcd3d9054f88afd5d7481ab082db():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return s


def func_2c40fb27367d4bb09fd59d10002217fe():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return best


def func_879c0a5a046d402197301a1dd262a502():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return T


def func_5700b7f5ad5445a2ae57b59931d8218f():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return q


def func_3fb83ef4cbac4845919264234344ea5b():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return total


def func_ed1ca0fdfe934213a9689a109a05a323():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return a


def func_14b182e6c4d442a2a6333c20f33098af():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return b


def func_74cdc7c4ea58410b9e9e3d4153b8528f():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return infile


def func_52fd8244225c47539b667eff5ac1c506():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return r


def func_1e280bac5e4f4881b06a6ffb6c3bcd27():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return p


def func_97bfc163c6f94530a61ae008f98138c5():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    return i


def func_7f420ba7f38040f9bdf680eed5f6ca30(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return s


def func_f1905696e0384d21b40588505d7d96a4(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return best


def func_10ccb346b51f4c6bbbd2924a66031d26(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return a


def func_dd77ecfb51634b54906d9828787b665a(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return p


def func_2df92723130a4dbb9e3bd917045f1364(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return totalsum


def func_a4f0e5f3379042e6868bfda705691e5a(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return A


def func_eeffb7d067d94cf895a14810273b3adb(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return b


def func_5b593d280d894227886d9820e2620ed7(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return i


def func_8fc587178b0f425893cfb8b8d0bf3ab0(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return T


def func_eb5f88e2fd7749f08864f8f47842b573(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return q


def func_1ca496655a6749638375900047039b79(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return r


def func_d398731c95e149a2a588991bfb6cc19c(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return total


def func_10873cb0fc834b2e8aae8c536c30e9ff(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return N


def func_b564fdc0138845c596ef79cd1a15d0bc(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return s


def func_b42646bf57b04e1ba5eb398e69ab566a(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return total


def func_f13a21b1f8294c6ea4692285e7257508(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return N


def func_e6c89cbce82b4fe59072ac31bd8cccfc(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return b


def func_7b973b66bfe248a1b083a7b65d8747cb(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return i


def func_06a170a9d28944df9bd77ac6dbfc9bb9(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return a


def func_e56980d85c51442fa98eaac3e42761f6(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return totalsum


def func_ff24164b9e5c498eb583322af419353c(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return q


def func_d22a16a174d74323bcdfc0748c900fb7(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return A


def func_3198becba046425b9f7701a079086953(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return r


def func_42bb0ea960504637ac6203bee7e46b30(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return best


def func_510efd6a1bef4ea4915b38410ec44f95(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return T


def func_d4db808b5c5f4ad19f746d92b5eceea1(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return p


def func_0fe0cb5387d84c33a820ce7538128287(N, a, total, totalsum, infile):
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return b


def func_a4c9e7f7ac2d41169d555389b022f1b2():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return totalsum


def func_df00b7d4111b4b17ae5338bc5d859307():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return A


def func_e3759d7baf854516acd05dd65f58e267():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return p


def func_001061ffe51349cbb94a04ecda918986():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return N


def func_b5cf5d42ed4d46ce9647adf74afadbdf():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return best


def func_c8c31fa793ec4baf9ebe919e60d10e63():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return r


def func_81d7ec305fd14deea9aae3abfb35ea46():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return T


def func_b78708fc55d5493dbd5bf9e59d12fffc():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return a


def func_dc22601ca4164c319547ec8092cd1ca0():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return total


def func_c41e70b8b5b145f3b436438803d19f3e():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return i


def func_7649988e353d42b4b610723f812d4f3e():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return q


def func_60b98beb7ef74a05829454996e6baf05():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return infile


def func_3fd2df326bee456eba012bbca72a6827():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return s


def func_8b92c7641e484c3185ac21b876e1c6a3():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    return b


def func_a058fb23c70c4f83b621ff8b996ca757(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return s


def func_79cd49364c704b2481ae80b0d388570e(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return r


def func_6beb80e3001a481a84058c4d33a9c8ce(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return best


def func_1691ea258a804e008ed80b0b27bfe0b0(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return q


def func_684fcc825d8c47bcad7082f202f2183f(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return i


def func_c1bd00b0cf194523b77e76a0ff6c7b63(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return b


def func_cedb8992c5f34bb4a21e2acfb535ab9a(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return T


def func_f25afc94d1bf4c3cb31d44c394340e06(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return N


def func_754e6e270ffc43aea9841c9db716860a(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return total


def func_ad489c77b0394a6d991496c4c1d96e9a(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return totalsum


def func_d2f5cfd435914ff79a6b5ec165eb991c(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return a


def func_a834e99521a342968ed049cd9018765f(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return A


def func_368aa2f7d8f843508c1434ee4c9483aa(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return p


def func_a8cf91de524d4990853190090965d2ff(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return i


def func_5a1da4b690934fcfa28be57548550a80(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return N


def func_c24477c0275f4141bc5892c5976f4776(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return total


def func_347910efdefd4af6a57bfb08473be165(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return s


def func_fb81a2754a094fd5a2d0d9692c491195(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return A


def func_4ef8b31e24144bee942d35ba1d2774b8(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return totalsum


def func_c39bfa9851fc481fae8afe335afe55fd(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return best


def func_8f7d9b18b0f14b1e8ab440a10887730d(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return T


def func_70a941215b834f7eac54b7c1636adfb4(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return p


def func_b4cd67a31efc4ead91b67fbc22e24dac(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return q


def func_a22c619581fb44ae9f584033f0899eb8(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return r


def func_693ed1bad29e4b8a95d978208b7d6f86(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return a


def func_07cf1ae667834722a41368a3a3a52f0c(infile):
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return b


def func_c172c6329ac8403aae7f07e75e313b64():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return a


def func_6c62f09ceaea47129e83e1b939749cb9():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return T


def func_01dc285a49b245bb9b0949a7ec01a023():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return r


def func_f1811e15e03843e49fea3ba532ea8abe():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return A


def func_dd8add574ccb4aae9485ee4faad801bf():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return b


def func_afac472c35384280869ae404198805bc():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return best


def func_ebc4290fb5fb4b4299252ce7da042619():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return i


def func_7f3b9e7f1be74cb8a0529d04b3de64d8():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return totalsum


def func_735b12cfd01b4a4c81f3ece45e4a28c2():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return N


def func_cf36e98c4f894327bcf08c3194ae7721():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return infile


def func_cb643894a3014ef1b37f5c0d1b54a565():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return p


def func_a107482df78246eb8d81ca5011347c4c():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return q


def func_918853ad2ecf47eaba61a6f1fc6d92df():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return s


def func_8f053287fe174bdf8ad67b55f778290f():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    return total


def func_4e14ae8b08734803a9a1388cc930810a(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return p


def func_dbd53d84aa8b47279f057ebe3203305e(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return T


def func_0bd728dcd1ac4427bbd2f8f5b9caf23d(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return s


def func_745b0911081e4c1096ca52012199c83c(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return r


def func_779e7f4767144f6e8016401603b095b1(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return i


def func_68558b99861c4206a49c8c7e776ad176(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return q


def func_9317c45f78c1496bb6b2d72ec0df9393(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return N


def func_f74e74844ed94f00bade2c9e428e8d12(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return a


def func_8b1d8cfc9aa14b8e86397102da61361d(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return A


def func_5a3ff70a1bc943febae09e1fabf395d2(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return best


def func_512bd04277844ab09213194c90f64f0f(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return total


def func_de5c06ddd14d4f9a800fe3568514c055(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return b


def func_3dabdf4bb9bd4b19862c5bafe2e6a31d(infile):
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return totalsum


def func_905f4c30854f45e6a2a1e429dcc65ffa():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return infile


def func_c4b455e670464f0abb57a45a200956ec():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return r


def func_424728ccf8bf444ebac61c68c76f4d3f():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return b


def func_b2fbcb34b7bc404195a6d2b707095403():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return A


def func_9c2399ce63344af09045aa205c8e5ec3():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return T


def func_0baf7a2224154215ad97b22e7a041b21():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return best


def func_d1a5f32b7cd240c0b383329cd5fc9faa():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return N


def func_7a1ced1d999d45729628f9914c8dc9a8():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return a


def func_5c85d4feecc64c9cbbafcefb97477778():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return i


def func_a0bf93db7a5e4eff9bf8c8b9f3acefae():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return s


def func_acfda2965eb343009d6f0e762bc726f0():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return p


def func_4898b02e04f14731b38090bd045f16b8():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return total


def func_48cfc21f8f454641b8ba772c3aae73e7():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return totalsum


def func_109fbb71de58446b8ad0e46b3e8f694f():
    infile = open('test_files/Y14R5P1/A.in')
    T, = line(infile)
    for T in xrange(1, T + 1):
        N, p, q, r, s = line(infile)
        A = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(A)
        totalsum = [a for a in A]
        for i in xrange(1, N):
            totalsum[i] += totalsum[i - 1]
        best = total
        b = 0
        for a in xrange(N):
            if b < a:
                b += 1
            while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, 
                b + 1, total, totalsum):
                b += 1
            best = min(best, getsum(a, b, total, totalsum))
        best = total - best
        print  >> stderr, 'Case #%d' % T
        print 'Case #%d: %.10f' % (T, 1.0 * best / total)
    if b < a:
        b += 1
    while b < N - 1 and getsum(a, b, total, totalsum) >= getsum(a, b + 1,
        total, totalsum):
        b += 1
    infile.close()
    return q

import sys
sys.path.append('/home/george2/Raise/ProgramRepair/CodeSeer/projects/src/main/python')
from Y14R5P1.frank.p1 import *

def func_9366e54e3ba44f0393fb0a116c8c29d2(sum0, ps, j, i, sum1):
    v1 = sum1[j]
    tmp = max(sum0[i], v1, ps - v1)
    return tmp


def func_c7028f344ca34ff7823f76348131104a(sum0, ps, j, i, sum1):
    v1 = sum1[j]
    tmp = max(sum0[i], v1, ps - v1)
    return v1


def func_6fb1b25097c1447097115949e403748c(sum0, ps, v1, i):
    tmp = max(sum0[i], v1, ps - v1)
    if tmp < bestAnswer:
        bestAnswer = tmp
    return tmp


def func_a1f0562f557a423f9baa7ae207f9c00e(sum0, ps, v1, i):
    tmp = max(sum0[i], v1, ps - v1)
    if tmp < bestAnswer:
        bestAnswer = tmp
    return bestAnswer


def func_000b844355f544599d61958ae02db300(sum0, ps, j, i, sum1):
    v1 = sum1[j]
    tmp = max(sum0[i], v1, ps - v1)
    if tmp < bestAnswer:
        bestAnswer = tmp
    return bestAnswer


def func_90f3b1598335463eb3c9e77efda8c207(sum0, ps, j, i, sum1):
    v1 = sum1[j]
    tmp = max(sum0[i], v1, ps - v1)
    if tmp < bestAnswer:
        bestAnswer = tmp
    return v1


def func_a3df69fb6acb4556a7fcb8139937e97b(sum0, ps, j, i, sum1):
    v1 = sum1[j]
    tmp = max(sum0[i], v1, ps - v1)
    if tmp < bestAnswer:
        bestAnswer = tmp
    return tmp


def func_28053e18ffdd45fbada547c100bda374(sum0, allv, i):
    ps = allv - sum0[i]
    j = max(j - 1, i)
    return ps


def func_2d9300dabf6648b2a53a3a6a59cd1460(sum0, allv, i):
    ps = allv - sum0[i]
    j = max(j - 1, i)
    return j


def func_4357ebc7d506405e917818171e645837(n, sum0, ps, i, sum1):
    j = max(j - 1, i)
    while j <= n:
        v1 = sum1[j]
        tmp = max(sum0[i], v1, ps - v1)
        if tmp < bestAnswer:
            bestAnswer = tmp
        if float(v1) > ps / 2.0:
            j += 1
        else:
            break
    return j


def func_a6b6bd2e835a485e927b63c579748ad9(n, sum0, ps, i, sum1):
    j = max(j - 1, i)
    while j <= n:
        v1 = sum1[j]
        tmp = max(sum0[i], v1, ps - v1)
        if tmp < bestAnswer:
            bestAnswer = tmp
        if float(v1) > ps / 2.0:
            j += 1
        else:
            break
    return bestAnswer


def func_4ddd6652084c47b4bbb371b0eb0f1345(n, sum0, ps, i, sum1):
    j = max(j - 1, i)
    while j <= n:
        v1 = sum1[j]
        tmp = max(sum0[i], v1, ps - v1)
        if tmp < bestAnswer:
            bestAnswer = tmp
        if float(v1) > ps / 2.0:
            j += 1
        else:
            break
    return tmp


def func_8ab0277671904ec784ebbab6587b2582(n, sum0, ps, i, sum1):
    j = max(j - 1, i)
    while j <= n:
        v1 = sum1[j]
        tmp = max(sum0[i], v1, ps - v1)
        if tmp < bestAnswer:
            bestAnswer = tmp
        if float(v1) > ps / 2.0:
            j += 1
        else:
            break
    return v1


def func_96fd3b22035544d8b9a161d0a5be0fda(n, sum0, allv, i, sum1):
    ps = allv - sum0[i]
    j = max(j - 1, i)
    while j <= n:
        v1 = sum1[j]
        tmp = max(sum0[i], v1, ps - v1)
        if tmp < bestAnswer:
            bestAnswer = tmp
        if float(v1) > ps / 2.0:
            j += 1
        else:
            break
    return ps


def func_6bcb6d939f8b4a32864d75b4d7d54625(n, sum0, allv, i, sum1):
    ps = allv - sum0[i]
    j = max(j - 1, i)
    while j <= n:
        v1 = sum1[j]
        tmp = max(sum0[i], v1, ps - v1)
        if tmp < bestAnswer:
            bestAnswer = tmp
        if float(v1) > ps / 2.0:
            j += 1
        else:
            break
    return bestAnswer


def func_11f053f1602649ceb8dc97d861e8b45c(n, sum0, allv, i, sum1):
    ps = allv - sum0[i]
    j = max(j - 1, i)
    while j <= n:
        v1 = sum1[j]
        tmp = max(sum0[i], v1, ps - v1)
        if tmp < bestAnswer:
            bestAnswer = tmp
        if float(v1) > ps / 2.0:
            j += 1
        else:
            break
    return tmp


def func_e0204441c1974461ae9612b51f5b41f4(n, sum0, allv, i, sum1):
    ps = allv - sum0[i]
    j = max(j - 1, i)
    while j <= n:
        v1 = sum1[j]
        tmp = max(sum0[i], v1, ps - v1)
        if tmp < bestAnswer:
            bestAnswer = tmp
        if float(v1) > ps / 2.0:
            j += 1
        else:
            break
    return j


def func_8189841da26c4077a6f3d85b33752ef2(n, sum0, allv, i, sum1):
    ps = allv - sum0[i]
    j = max(j - 1, i)
    while j <= n:
        v1 = sum1[j]
        tmp = max(sum0[i], v1, ps - v1)
        if tmp < bestAnswer:
            bestAnswer = tmp
        if float(v1) > ps / 2.0:
            j += 1
        else:
            break
    return v1


def func_d2ae85cecdad40bda843cb643c18f46d(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    return r


def func_95a4b37503bc4dd28ff7b94e86991cf7(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    return aa


def func_bf52ff28569642d7a60944dc42487465(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    return x


def func_c838b7d4d91f430bad06a5829f8ace37(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    return s


def func_c3b8811def444f94af103e486f01056e(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    return n


def func_3afbf729b7554596b73e3ae94cdb2571(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    return p


def func_6dfee5bd0c7043bc8a755aaa28c76414(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    return q


def func_638dca06c2944f44ba74880dda5b98e7(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    return a


def func_1de59b260157477c8776ffd6b0a0d4f8(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    return x


def func_453c06e558524dc6991540ac625b2528(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    return aa


def func_7ab1d639acef4b07974c969ebcd909ea(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    return x


def func_998466b60d1f41f196fa9dc32979c281(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    return a


def func_014482df6c29481195f5bbbbb9c1d9d8(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    return sum0


def func_e62ab93c74314298b8702a1bd38b34ea(n):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return sum0


def func_e2621c96e3ea4bae8b733b028513cdad(n):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return sum1


def func_dd492eea452b4799b05134a80845410f(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return i


def func_92bcd071b3aa43f3af60d6bb7a2f8232(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return sum1


def func_71bccde17763488c9c69a0efe20e75e7(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return i


def func_dbfd505a9530452eaa3b732b179894f8(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return allv


def func_2b9d2bcb8d5142118a41d59f31f44de5(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return i


def func_72932eac3f1c4bfd9ea8f7acfa887a21(sum0):
    allv = sum0[-1]
    bestAnswer = allv
    return allv


def func_efbd1ded4bf34b89929bd98ef823c5d1(sum0):
    allv = sum0[-1]
    bestAnswer = allv
    return bestAnswer


def func_414765bad9154294a1d4a942c2340d97(allv):
    bestAnswer = allv
    j = 0
    return bestAnswer


def func_6ce0225cd2cf468db596e5a81c311b79(allv):
    bestAnswer = allv
    j = 0
    return j


def func_3259c31fcd554d5f8bf7cd5062f47194(n, sum0, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return bestAnswer


def func_1552e7d99a2548a0bb2366c8b8c8c7d7(n, sum0, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return i


def func_512bede6d608413b851420d8a1e6619a(n, sum0, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return j


def func_83d5764b9ce7425aa7eeb6841466ce5f(n, sum0, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return ps


def func_079c336c0fb743ab80d0e5358f24ac66(n, sum0, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return v1


def func_f35c6c556c7e44deac8d8fe39094145c(n, sum0, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return tmp


def func_31b1e7ce378947d690e184702ce9a4c6(n, sum0, allv, sum1):
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return ps


def func_8d7704bc1f15494f94be3d0d7c63b0ca(n, sum0, allv, sum1):
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return bestAnswer


def func_3b0cd0af0d294b60ae959e753dfc0878(n, sum0, allv, sum1):
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return v1


def func_3eb440061bac4dccb14f1ed15979d85b(n, sum0, allv, sum1):
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return j


def func_33f04e8eca56431f98ced7b68b411cf0(n, sum0, allv, sum1):
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return answer


def func_ceca3bdd3617471d96ce313e84c971e5(n, sum0, allv, sum1):
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return tmp


def func_bd16243e583841a5bc45e680be630fe7(n, sum0, allv, sum1):
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return i


def func_a5c37f862b9e4c1685e9c2ede20b690f(bestAnswer, allv):
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return answer


def func_cc5fcbd48eb448efbf7bbc28208cf9cd(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    return q


def func_4cc01fdb4b834893ba2f427fe21a4c01(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    return r


def func_6a50d26c0ced4c94b1c8f8055905d10a(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    return p


def func_77485f11c9de447c82c92750bdeebdcc(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    return n


def func_1af364b19df24075b40b631e30035d19(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    return s


def func_e2ff5ae4b3574caf9d0dbdcf3ade4ba6(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    return s


def func_f9e7bee6d13d402b837bf72c4bf4a1ae(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    return q


def func_bb44573e15f145bc8d6e415398ce2039(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    return p


def func_f1962e336e424c89bae912ca60bec0e7(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    return n


def func_78938fe8f87c450ea82c9824da854907(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    return a


def func_5389c79c47cf45d4a1a68050a09081a7(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    return aa


def func_e638a20cbac440fb99f0427485a3d0b4(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    return x


def func_edfda58c65394184be19ce8e259df1a7(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    return r


def func_908f5a7d8e5047d5854fafa65ca0a26d(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    return aa


def func_f76a76d8b6894727a4e0591cf6d2b212(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    return a


def func_67e5dbddce5e494ba7f908f02c6085c7(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    return x


def func_c475271088f946249752df96d4132d70(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    return x


def func_04e4866f5a014a4992194383a5a4a798(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    return a


def func_b6d27529cad543fe9e3df1075512c8d9(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    return sum0


def func_1af8307fc55b4069a3fb283fefacfa1b(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return sum0


def func_3fd410544c004fdf9d14686072a77063(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return sum1


def func_5e53ce5c3c074d23ae3fdee5ad1a589d(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return i


def func_338cc8f285504b16936e571b124e4c95(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return sum0


def func_2537eab5812e468790a5900265fbc8c3(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return sum1


def func_0df95f05bed345f39b4b8b22f5dc33fc(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return sum1


def func_204a5c5a85b841fcb3085a167e2f3158(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return i


def func_2a8e2dae4af14ba7a03389fef9bd81fd(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return allv


def func_24053d1b00f04eadb00d50d5a0cf1463(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return i


def func_bc110244fa5d4914b27895a902bd530f(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return allv


def func_3bbf4736189c414db210dd131d594631(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return bestAnswer


def func_c6a6296d922a4752b39d7e8c55160575(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return i


def func_32ff8cf9e1cc490d86f83d63f67111ce(sum0):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return bestAnswer


def func_a3c6c434b64c41c7a7a17ac20c46f1b3(sum0):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return j


def func_7b752419f2cb467bb14bb825f5a1cc94(sum0):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return allv


def func_f05bf0f3d2c7491bba3bc925aa1f56a2(n, sum0, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return i


def func_2f7cfe73b6d348adb302db87a4ed9c8c(n, sum0, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return tmp


def func_f4033cc4a44e4350aca39d176897b08d(n, sum0, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return j


def func_b8172efc11794fe094cc748108a40a5e(n, sum0, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return ps


def func_d8a8a3141920491b8fc4b32d2b36f001(n, sum0, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return v1


def func_260cd9abcca3450088165e9dd506b2c0(n, sum0, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return bestAnswer


def func_50224be90ad74626a36171110642688c(n, sum0, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return v1


def func_3325da13594c4e3dba568793a5aa7375(n, sum0, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return answer


def func_199f5c3ec4ff42dbb88a0a061eb5402e(n, sum0, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return i


def func_749721faff99486fbd096fa09bfcbfe6(n, sum0, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return ps


def func_2efc700e0792468a8eae8d7264fde12d(n, sum0, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return tmp


def func_8b4096fcaa394f25a7d797818dbae5a9(n, sum0, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return j


def func_ed5dd6c915334a65b4fc0ca7047f6884(n, sum0, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return bestAnswer


def func_f184a5a2c86d4114ac08739473dcbdd3(n, sum0, allv, sum1):
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return ps


def func_f8e996e05920479fac682fb0fd2725a9(n, sum0, allv, sum1):
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return tmp


def func_a7c78ddcdba9499c80913be7c9f2be29(n, sum0, allv, sum1):
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return v1


def func_e6548378c1a545a79ec88542b98ca76c(n, sum0, allv, sum1):
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return bestAnswer


def func_9b6b482884a44dc9b3efd3081378e665(n, sum0, allv, sum1):
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return j


def func_5a5111338c674897963c03ce3a72ebe2(n, sum0, allv, sum1):
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return answer


def func_5f4e2857e5f24824bbaa60e67abcf0ee(n, sum0, allv, sum1):
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return i


def func_fa93ab2c26d8477c8034344e5a4d7f0a(bestAnswer, ouf, allv):
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return answer


def func_b4f99bc73db3471dbe656bdd212d304d(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    return q


def func_3356d3b386854322aaadbc1050a76f68(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    return r


def func_9ee8e89202dd4a37800631498ad4af87(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    return p


def func_bc9d2e53737b4be385ac1f1bdbc3f134(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    return aa


def func_a17bf177abba400697fd7ce77f665ce8(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    return s


def func_7e4f1ac407fa4791a80748d2eb48ca10(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    return x


def func_fb1108169d5c4a7ca31abd3e9220831b(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    return n


def func_32524c3a673e4348b93b53397a604bf5(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    return r


def func_d94d7bc0e3474f0e92f614167912bb31(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    return q


def func_457125fea4204106b37c5db31830963b(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    return x


def func_694b3d3dab9c487498678fd2eb13a706(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    return a


def func_47877ecab0ec4e9c9e81071ad13a732d(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    return aa


def func_567f5f3a09df47b3a03e30ca1a257edb(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    return n


def func_50bc96709fd54bcf8ecab99293b3f7e7(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    return s


def func_c4416153b9a3489ab9afb35b62d069df(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    return p


def func_57b337e18ff647d999f052a3ac37f152(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    return sum0


def func_4bbc4348ff404920a9335c0708a663be(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    return x


def func_1135ef979aa841c2ac82b9d11fe928b7(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    return a


def func_60204e55a15f411b8023172ff955f84c(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    return aa


def func_e578bf3c71d345febb8118f39719f0f1(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return a


def func_cbae4854060f4287aa646d1f0b79c4bc(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return x


def func_f6b150cc883b4b2aa09f432d7499988e(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return sum0


def func_b54d84e36fce418a975f5c6bc2da8092(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return sum1


def func_532b3915c3c24186b292f4a127a39a30(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return sum0


def func_75b3531dc019428c8f9517e958335839(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return i


def func_abb6b833b1d3466899698d273d8c289e(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return sum1


def func_f0f1234c13c74452bb00a29a78bd0b87(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return sum0


def func_c00e9dd98930400fbbeb48823a588114(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return sum1


def func_616468c0e36348fd89bb65fd6294ab05(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return i


def func_35a073ba7be1422e80990fbb6c531328(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return sum1


def func_643527c7e2ae43bd8397fe0d54430250(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return allv


def func_f4f8ee439896485298a55c6ee4201793(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return i


def func_fde07364bb19440487abfb477484096e(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return i


def func_bde494b89d1946708ec5fcddfde71ef6(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return bestAnswer


def func_be97963aa43d47639f9887911d249bbe(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return allv


def func_73189a254b7e459d8eec0f2c1f4287a5(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return i


def func_858808ba74f944e49ff9274e1776e349(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return allv


def func_c423ac1bb8d5464da48b11aa23efa38f(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return j


def func_7c993343c57a47ebaecd3fb0dd9b624c(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return bestAnswer


def func_1f90e19c19d14a709f44cdba95a2cc88(n, sum0, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return tmp


def func_c05796c9725246359567cbf207f5c6d8(n, sum0, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return bestAnswer


def func_ac514bcafbd54487a06aa3a735e914aa(n, sum0, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return ps


def func_4a05dcc493c945fc95a601b4188a76f1(n, sum0, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return v1


def func_b9a90d7f400044458060f1caf5d01362(n, sum0, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return j


def func_9a57ce815c504b8dbb0936ca9795656f(n, sum0, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return i


def func_c5f407b164724a6782a7824d4954f95a(n, sum0, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return allv


def func_4806ad49713940fab8202625f02d0852(n, sum0, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return ps


def func_456e8b1186c94a2cb2835cb8867d0e81(n, sum0, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return j


def func_034852ca721447259a67b01813b9878c(n, sum0, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return tmp


def func_65c3eaf8c24549e693970e25c01e6c99(n, sum0, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return i


def func_57149673b3bc4a02865652b94afe8385(n, sum0, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return answer


def func_ae0ae396f0474f43867c0665ecf73389(n, sum0, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return bestAnswer


def func_b31528386ad54ac1a3b0d235bd29cea3(n, sum0, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return v1


def func_b383ba4a9cd64d768777b05414da41f0(n, sum0, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return i


def func_56d0fe10e75748aa85b66b4d22bb9db2(n, sum0, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return bestAnswer


def func_616e642920c8455e9cab41dda484b05c(n, sum0, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return ps


def func_7c539937c06247ddb94244701cc33e8b(n, sum0, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return tmp


def func_7502d58c257b4ec6a2d8bcc5248abbfd(n, sum0, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return j


def func_da610328771549d8bfb4aa048fe2c000(n, sum0, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return v1


def func_65c5ede34f0247ceb3295aef049ee2ad(n, sum0, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return answer


def func_1bcf5111f33c4628885a0acb03566aec(n, sum0, ouf, allv, sum1):
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return i


def func_b3a2336cf64a41c6a732c0aaa1678fa3(n, sum0, ouf, allv, sum1):
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return answer


def func_8d691b7ff59d47bdb97c04b87c938762(n, sum0, ouf, allv, sum1):
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return tmp


def func_f6e6738a7b2e4825bfba3f5f1815b27a(n, sum0, ouf, allv, sum1):
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return v1


def func_427a8456422b4ea68e6760b22da25665(n, sum0, ouf, allv, sum1):
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return bestAnswer


def func_0a0c272428354dc2a7bdaaabef11e104(n, sum0, ouf, allv, sum1):
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return j


def func_1357ab3aa1c642e5ad02067e2b34b222(n, sum0, ouf, allv, sum1):
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return ps


def func_7d52d2d17f204cbcab43c416163c696f(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    return x


def func_61b0e5dbedb84e089b93c25917b04f02(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    return n


def func_c677675b5758479284003eb658630663(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    return q


def func_f8a176f99e7a441b864371ea2dcb2c71(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    return r


def func_0e73a06a4c864fb6b6aa44adc1f189c7(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    return a


def func_4ecc6336b3ca438fb9f9d2f54dd88a80(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    return aa


def func_a7816f1c41794a4db6ced5e90f950000(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    return s


def func_122a3ba8b3d84bd1ba030a38fef106da(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    return p


def func_26f8479c59cc4759950490653e7b4318(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    return s


def func_d1e64d8cc02c4f38b4745cd32319742e(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    return p


def func_99c45e626816421aaf843ca9ba3ba379(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    return x


def func_1c782f7af6204f1cbe686f9b53d1f6a3(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    return a


def func_8460991413b44b63ab3a0d13e1c7f5f6(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    return sum0


def func_a331d8bb5763432ab5a1bdeca2562e85(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    return n


def func_1a7e1fb3c5234889990892cc4e309455(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    return r


def func_9aa5a839da8e48839c6077690c732c7f(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    return q


def func_ba4f9ccbc66746ee9b5e8549f9aaa22f(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    return aa


def func_458ef14df1114a2d83fec0dcf9e1a89b(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return sum0


def func_37c47c2d25ef401dbf67dc73c9832172(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return a


def func_e1baa839d4bb4c74a3ea6c6d7404fff1(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return sum1


def func_0d0e868e5213484c873452944f898844(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return aa


def func_956dfd18b59a449bbffdd245ee3ddcf1(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return x


def func_037abde5d6ab4ad6920080cd32ab8a5f(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return x


def func_0cb7b1c68b3047259012f088e3bc4454(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return sum1


def func_16f14a1beb3d4f36b00c02a409f030c1(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return a


def func_cf2f655806cb4f5bb22358848adc8d83(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return sum0


def func_d9f412c2946e4d7a9aedc56ca174583a(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return i


def func_d858e6d8ea8445bfb8ffed333be952b5(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return sum1


def func_8d0ff236045b47c1a5aeb5a2ef263cd9(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return i


def func_e0ff05158ad94a18bf2a607845c8ac1f(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return sum0


def func_c3c5e90443f24251a2b31aced4fc775a(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return i


def func_b4bfb6954f91466194caeb83a70dd9f6(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return allv


def func_d153e18de50e462f90929bf8375b8d2d(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return sum0


def func_d7070a4041f2468db64fea51f0333ff6(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return sum1


def func_e8020623c50c468c870250a34257a8f2(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return sum1


def func_9c4e6145d8644e88b1ea17a6ad64c261(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return bestAnswer


def func_dc13160f426f448e8d25ac3e455f8a21(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return allv


def func_7fdeea5666fd49ff80bb7baebd8984f5(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return i


def func_6a7bb4733b6342c2bbad6ffd524d6d29(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return j


def func_aa04559655d74cd295033600e66ab7a0(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return bestAnswer


def func_d5fe3b85546a4ec4acfd394b19c25278(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return allv


def func_d36c2152467c45da847a3b5e9b2703b3(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return i


def func_825119e358ee4ed8965f98d5683c314d(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return ps


def func_8fc96404166a48c38cfbb4fe7d30b56a(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return bestAnswer


def func_2820848057234223a564adce760302e0(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return j


def func_5c9d7cceba724c29a6bc2352c4dcd6aa(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return v1


def func_5d4497f5e0b44f2c81ca4572a2705d49(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return tmp


def func_fe569f18e9ed4170a3a4a9ad7d56d64a(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return allv


def func_799744d091994369a1a87fc2ddfb35ba(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return i


def func_a656b82a43b94f349b70f926f1f2e0aa(n, sum0, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return tmp


def func_b221f4d75dc84a8f805ad593f5e3249f(n, sum0, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return bestAnswer


def func_b523f305588d45568c2194e7c2c85c9b(n, sum0, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return i


def func_1d5ffaf09c55420d803ca0046bbcd6a5(n, sum0, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return answer


def func_ff1a8bbd4a174fbd919df4a30e7fc511(n, sum0, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return ps


def func_c1c6e9c70c1a4d9ab36e3e19f71d61ee(n, sum0, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return v1


def func_f96f4dd571ba4a6ab407b553a05b5ff7(n, sum0, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return allv


def func_830b6492f3d949b3b08b9f9a55fc49ab(n, sum0, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return j


def func_e1c36c80b52a40b58137309358a8724e(n, sum0, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return ps


def func_13370d97b34f442e9c42c0081f805fa8(n, sum0, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return v1


def func_2bec56e942ec477fae52e5f139ac3a7e(n, sum0, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return j


def func_dfd33bf259da455a9b10afc5ca00c283(n, sum0, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return i


def func_23e6fcbcd0794e0b9fe1df58cdc9e79c(n, sum0, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return bestAnswer


def func_258899abf628419dba3aa0796e85000a(n, sum0, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return answer


def func_1b4d5cb74f574a9f9cb4f49adeab8406(n, sum0, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return tmp


def func_c3036a9f8ac84803bec6ae110c2f56a9(n, sum0, ouf, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return j


def func_44259e40bb874de1800c160a3727ae34(n, sum0, ouf, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return ps


def func_a6866f91b62146bba355c6c3693ae772(n, sum0, ouf, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return tmp


def func_3848d766335d40298d73c6ff0433be5a(n, sum0, ouf, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return i


def func_6348ddc8ba9f4670b085ee752c631629(n, sum0, ouf, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return bestAnswer


def func_90e1d9a9f4fc4391bee8dbe3dec27785(n, sum0, ouf, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return answer


def func_b68c1906a7524130b55afd22fb6674cb(n, sum0, ouf, allv, sum1):
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return v1


def func_723662e2dce5414d9f650c38a152320d(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    return q


def func_771f2aeca1fb410880bb55c151fba569(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    return aa


def func_ea4577b9ecf540779ef09aef66fcac76(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    return r


def func_cbcf58def12d4e56b2840b6891399c0e(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    return p


def func_377e4f9e8aaa40ef85ecf82219e6c8c6(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    return s


def func_96529c968f2b4bc7a02f1680b376b021(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    return n


def func_4afe3fd042f143cba06b86d1d85bdb05(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    return x


def func_d9431e6d5bb64ff0a5d4f3e421efa86c(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    return a


def func_64882aea1d6e44bda7e70d6b0b249996(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return sum1


def func_3b4f9fc6ad89402ca01c027b2ea88622(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return p


def func_4de5b2a83abd4cfd9d49383292d6e54a(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return sum0


def func_3823b9e0fbfc4f83a62fd7eee86a35be(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return a


def func_ff2cde9df1c34d5eabb1e6a5fa8a5903(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return aa


def func_219bc09a62f24d759e8cd6d20cc10fe6(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return q


def func_8b234d3b987d43d5b4bc13d750e79b3c(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return s


def func_909f02ceee42482489c9c443506a9dd3(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return n


def func_4b9ec07f64794fc798391e61d5b6aff6(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return x


def func_6952c66b52be4976ac8596cae4608b01(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return r


def func_41f29f6ac7354f1b9da3678bfd427a75(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return aa


def func_d1e571d2ff164f9cbf6f1d838165fe9a(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return x


def func_765cfab86755446994cc9f2b7425f354(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return i


def func_1f40a0946d034653a2bb31b98f06d5ab(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return a


def func_2ebbb8e2b47d471d8268e5fb4e5cce7b(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return sum1


def func_2261fefb640b454d960cbd8af49ead5e(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return sum0


def func_57d0b6e2515d4601963338493ceef57b(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return i


def func_75ebf7c44d324ca78f7d6750bc64ec5b(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return x


def func_ef63f48e60ae4900b3aa61d243fba697(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return sum1


def func_05f3005f0bec4d8d894a302b4431142a(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return a


def func_ffd51af1f07e41e5925c6c4e34be29a9(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return sum0


def func_8100462642bd4218b2c4134943318eef(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return sum1


def func_1a8c07c0f2d64f09a779b92d136a1716(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return i


def func_6fb126e903f8455995365c4a6f3c033c(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return allv


def func_8b5bda9a3ff849d1a6871bafa02cf7ed(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return sum0


def func_4d13e5d34a034941ab1c1e6657e2485a(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return sum1


def func_60c69cd0a3a34f3cbf698390f33bdcd2(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return bestAnswer


def func_daa54d907f594e21b3ea2d9bb73e9d82(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return sum0


def func_dc6ab3aacd77451ca8d94fe76c412923(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return i


def func_58bb98d517584b2185dbb527d6764ad1(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return allv


def func_185239ba68c443c6b2582d258c679896(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return i


def func_fe0f0a56ff074cae8ce71c44dedea248(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return sum1


def func_7fc5c0bd480e4b0d92c8dd9a0d7bf67a(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return bestAnswer


def func_31d7e13da9dc47988bc634a900928686(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return j


def func_343b3d98f0d84a938d1c5737613149d0(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return allv


def func_737c807ed2964e2997786e26698e9cbc(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return allv


def func_8041dd5730914ae5926491a3780954b4(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return bestAnswer


def func_a135821bc5e945a0901d79f01b5005d1(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return j


def func_aed38e57b859474d9f58bdb5d44f7448(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return tmp


def func_90efa0a2db61453492fee621628158fd(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return ps


def func_8b7cb1df22a64ae4aa8de3d015bd50fd(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return i


def func_6e6377624c54473c807df277939c47ee(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return v1


def func_eca84524829e432d9c8bf70e0bc4cc6a(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return j


def func_deea78e5f26546e98fdd2890ebce7b44(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return i


def func_465db3ed2194496097cb5c368671b197(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return bestAnswer


def func_684ec74e2621424abcd504be57912390(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return answer


def func_5d01c99cf33a48cdbef6baf2354f89e1(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return v1


def func_0f1dfc5132f24217b2338afcae9b2a35(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return ps


def func_0dbefeb2148f470796384b30f15e50c7(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return tmp


def func_b838c64a94044bf8a1c9ca8813c37df8(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return allv


def func_e9363aa2a69e470f9f80db8f2b6f3804(n, sum0, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return v1


def func_3c6ca4fb914a49b890874aedf711729c(n, sum0, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return bestAnswer


def func_0e68d658717444f993d50d2766792cda(n, sum0, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return tmp


def func_2df44095745d4059b27108621cbce9c6(n, sum0, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return allv


def func_5f5f6bf6cb7e49828fee41020baa1800(n, sum0, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return i


def func_745ec0319c434543b786b4786c5cf85d(n, sum0, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return answer


def func_4ae3f08530cc4faeb3fac95d6ff1babb(n, sum0, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return j


def func_db27576438e34afe8b538454d5a0c80c(n, sum0, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return ps


def func_24e8e368a6534e73a299b0bf8b5008ef(n, sum0, ouf, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return bestAnswer


def func_959e1de9d61241a18cbae0a0c2a78a13(n, sum0, ouf, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return tmp


def func_652590c3592f4d6f8d07d2abafcfcca8(n, sum0, ouf, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return answer


def func_efc31cdaa8d74cbb9725eb4d81f9dc0b(n, sum0, ouf, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return ps


def func_531b2b210618442f90bd00f5231771bc(n, sum0, ouf, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return i


def func_848de88c8e2b45db91bda5534d4bc489(n, sum0, ouf, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return j


def func_11806bec31e644268f615322a3b26026(n, sum0, ouf, allv, sum1):
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return v1


def func_cadb9fd23c95465996ca04672b944ce5(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    return x


def func_7b867dc1f5bc4a53a4b305e27b91da75(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    return q


def func_864df95488844bae88e5979cd2c250c1(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    return sum0


def func_ac13abc595f64ff9a058d8efd9f80018(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    return r


def func_069297d465aa4302a7bc93b8286934dc(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    return s


def func_205a76346f5c40ae8b69d6877d55c9ce(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    return n


def func_508ca651766e4004a10982b21e9db925(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    return p


def func_5fa57a64b66a4c3188445d832b950f68(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    return a


def func_a864334b68264b87bc4af7b59e5ffeac(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    return aa


def func_104d4176c2d6491cac49867e59705cbc(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return n


def func_f74f8689e91348a0b55321f8aee742d2(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return x


def func_b97f282c88914481bfc14d794e5da434(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return p


def func_e1202ba44e16493c93c293e82ac303ba(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return sum0


def func_e221580e04c24049a137f5c0cec28ad5(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return s


def func_a15433e5906a402486e16e68aede9914(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return i


def func_ea6f193ba8854cc89b6953c8e69ca45a(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return r


def func_7dc7201ae9644055ba69693f5d7b3d19(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return sum1


def func_5a01fe2dba2b49e8b451b5079ef4d77f(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return a


def func_7de82f0d4b894a89bab157ab3f10009f(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return q


def func_5d82cb875d2d4177959309d8cab3ef5f(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return aa


def func_1abd30ee8cf747ff96d708756dadd699(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return a


def func_0c5e78a5031846838b3f2cc969a3001e(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return sum1


def func_f693e8320ccb409aac4caa1e8d1c3569(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return aa


def func_2ea5937b70b2402faf78ddff33254844(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return x


def func_7e5f6ddaa1e8403ea19f19a9db8969af(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return sum0


def func_fdaa570c605f4ed2ba48a022db215735(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return i


def func_7925b579f8194a70975fd12335c05238(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return a


def func_7a8a97acb92d437db681b2cd680cfa38(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return allv


def func_8ba867f8b37b47d095a94de8450ea944(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return sum1


def func_5b8b5a3c5af54abbbb3a6cedc5ba1fde(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return sum0


def func_a10218a2d0ed4a76b3d172be732597d9(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return x


def func_4668f27363684d1b94846409ae7180f9(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return i


def func_8a8685b6e67547ec8360d11838c7e704(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return i


def func_3be06b2833734523a4f69cad9221f318(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return bestAnswer


def func_e05caa7e5e994e0bbf59abc8ac95ec92(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return sum1


def func_06f8a9ef4fb844ef82161d2847cdb925(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return allv


def func_33bfdbe3378441119caff060a66c0717(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return sum0


def func_dfb7911d437747f585ce792046c87724(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return allv


def func_7e589c3161df45abab23a96852c187d1(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return j


def func_0c84493135174cf996159a392762dd0c(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return i


def func_b972c5319364414a94769f1dd853a755(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return bestAnswer


def func_26bb55685f354bdbb191b78d6d005017(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return sum1


def func_ba347e533e694057b350ed2621668adc(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return sum0


def func_f2f7d6a6b72448998697d639ebb6c700(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return v1


def func_e557092a724c4db984f028efee165c07(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return sum1


def func_dad65aa306a34ee28db5eb99c9ab3623(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return j


def func_f798fc0bcdde46aba41a6607e6b95d98(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return tmp


def func_e331c32e8752407083a039618e3ef1bd(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return bestAnswer


def func_ea663ab7025345e295ff44b6bc7b9a0e(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return i


def func_8db4f5d2cdd149a5b755b9c43ad859eb(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return allv


def func_c9561e06eed64a4184585bbd924b36ec(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return ps


def func_4e949bb9aea341cf96b5c1ff53f2bd6e(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return allv


def func_598b9d54bca64b4eb8e577a99efe9517(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return j


def func_c24140af23904928976215ef0f0f61ce(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return i


def func_a44bafe1cecb4d28905b0656062dc5f9(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return tmp


def func_44b9fc0999974e13b587bf020399c08d(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return bestAnswer


def func_035ec2e7fe6c444f8c455b9786ffd37b(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return ps


def func_e48262e5a400449ea73e31b6df96b683(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return v1


def func_f0e47d0b71f54714a105f0f35bd09f0f(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return answer


def func_9ae53822c89245cf99d3119fe572f5c3(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return ps


def func_1ec2e0d67e154e1ba1eef351c68fe4b3(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return j


def func_156dc6e0b021442c8ceb47199c2fa43b(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return i


def func_8d37ed50cb5140148eba46c9ed120c72(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return allv


def func_6ce2eb555bcd439495f75f6297527c17(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return tmp


def func_d125da5a0d1745eda315aa1663a6c811(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return bestAnswer


def func_9f485e8f4aa7490abd30ae0aab8311ab(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return v1


def func_8a03fbea3d4b4d0fb5e6d3803d605cd1(n, sum0, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return answer


def func_d38d36f3644a4e53bd906fa6697695c5(n, sum0, ouf, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return tmp


def func_ba2510eafe1745c3b82929a5ea3fd3b1(n, sum0, ouf, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return allv


def func_2d908186544a453883269ffb0d74f1cf(n, sum0, ouf, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return v1


def func_839ed01804ce4fc7ae9d32ddd5fe0c12(n, sum0, ouf, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return j


def func_1a43a3eea9894f8ba5a60408be3e90a9(n, sum0, ouf, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return bestAnswer


def func_6ad658828c184ad8ad74d8785a058a9e(n, sum0, ouf, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return ps


def func_a26dc75801974f73bf34d162a29b469e(n, sum0, ouf, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return i


def func_59d8f02c91ab45d687153ce55f5eabd3(n, sum0, ouf, sum1):
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return answer


def func_9d2c39b52a7a4792bad523ce5d39384e(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return sum1


def func_ed2c8ea0afda43b5bc3619602cb17ab5(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return sum0


def func_cd5a2c82144f45029caf7c9bdd34e528(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return r


def func_d458e61cfc9e4159aac0207e21f08ce8(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return aa


def func_56558222c7644162aa4c8de4769555e5(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return x


def func_c18d59da276e40998c82514444e21cc9(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return s


def func_c23b43acb03d4c068ca08287408de177(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return q


def func_aa6555a622e347aea019c1aa73c0e450(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return p


def func_15a99a9a819f4182bf6c6fbc43d266ae(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return a


def func_201d1838d97945418d14a7b540b647df(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    return n


def func_b7f31ff9630e4827ad27d96674bcd5e2(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return a


def func_6d051aba8a0b41dd9f2dd0180401f57c(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return aa


def func_09ab1f5edb3f450bbb52e6608e36464f(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return sum0


def func_da13985cb4754f00bc402f93ab835831(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return i


def func_70f473c4a93543be9af4cdec53d17a5f(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return sum1


def func_3eae097aef3143d19fe60fc22fffe4d2(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return q


def func_4d485ad4b0d1467aa89ecb0f83522b1f(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return x


def func_e146342f26dd47858eae4a39921deed3(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return n


def func_4a190a99dfbf413cab22f40f4de52813(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return s


def func_37825abe3ee141f088c9b2809ff83c82(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return p


def func_1c57dde10e4b4eab9664f7546190096e(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return r


def func_07447492ba1f4e4b956cbd519c890db6(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return aa


def func_b622567bbe6d4e3c857798425771e61b(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return allv


def func_ab32b4a5d68f4103901ea15a4b56847e(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return x


def func_ee77efdc31da452ea18b3071974ccc01(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return sum1


def func_ca3b84f869a841c1aebcb5fdd750e371(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return sum0


def func_9600ab998dcc4ce291ab02e5800b77fd(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return i


def func_1daa49ee9d4c435db0899d46778f568a(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return a


def func_5c8ec3a665e043668e8cbf4df4eda51b(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return sum0


def func_75e6ca63c5b2412cbe27c0e05d7b0239(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return i


def func_128474a87b4748ec8a04cba6773fae55(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return sum1


def func_57d5e9dde2aa417b90643d3515b1ae0a(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return allv


def func_1ba22366cca74ae7859c4034e196887b(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return bestAnswer


def func_da5544635f094a118387bab5ac773e01(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return a


def func_119b38713d3742f6bde61b022f4919a9(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return x


def func_687a324ae2b1433aac7969742a6df95c(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return j


def func_e659ee444a464641ab92335d95f51603(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return bestAnswer


def func_db8e74af1a7b41ab989683184ef74b97(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return allv


def func_ad381b291cb24183bcf5e56f7ac1d42e(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return sum0


def func_bef4488b23b043609abf289cd9219b6f(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return i


def func_9d20f1b6aca14366bbe2565942d01298(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return sum1


def func_0191659c69a64912a36109f1e1f35e15(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return v1


def func_4113b59a8e9b47beaedccb0489f01822(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return i


def func_531cb4d66adc4d87b3f404f010780a39(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return ps


def func_237614a5f4bb49bbbc86655d6451ec22(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return tmp


def func_df34f8348f0e46e2ab4f296838386a6a(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return sum1


def func_6aee96dc864f412380d7b02a3676718f(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return sum0


def func_de999f26f9a040f6b9aef7243da65864(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return allv


def func_1140af74449f4459b98caf678dc46580(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return j


def func_1e4419e9ff9542499f2dcc7097805e79(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return bestAnswer


def func_c4dad8b97b4a41e392514d40804d81e5(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return allv


def func_703fc1a8ed8346d4a8a17014c1379901(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return bestAnswer


def func_ea3f057f92a24f51a051ff0cc2ee87e5(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return sum1


def func_356244f07b9c466e92a2d0521585da9e(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return tmp


def func_c5c734f4819449a98edd94e4db4c5270(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return i


def func_1432bb8e4fa44c06953b54676301930c(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return ps


def func_054461809c004085b43699427560a522(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return v1


def func_34764f340ecc4bf89b17ee9bcc90eaf6(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return answer


def func_92bc7959211f439993891d3cb7295ca2(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return j


def func_7048776cbfc94ef79083ca3009d4dbe5(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return i


def func_885ec26da7254661882098f7cb3cc52c(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return answer


def func_012e425f0eb24221a78d9b7cc5c8b792(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return j


def func_ab3dca28c7024e7cbbfe6766cb7f1e1f(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return v1


def func_54495ac6b14840d49a76e737e41adebb(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return tmp


def func_139590bec83c41efb34be90c8ce71a20(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return bestAnswer


def func_17c25d6c64984ae7bc7454a6fec278db(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return ps


def func_89a97825dc4845c1b92359bca7c5ee4a(n, sum0, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return allv


def func_6806b601234948c78685fb22ecfbdaf6(n, sum0, ouf, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return ps


def func_b24ec8c8333445a69e870d384c3b25d0(n, sum0, ouf, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return i


def func_a8867a4e1b0a4d4692dde2c8e27ef33e(n, sum0, ouf, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return tmp


def func_c39a7768baee475f91ba1457f891cb06(n, sum0, ouf, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return allv


def func_8f9e2cd7d69340a99c5cda5aeb365051(n, sum0, ouf, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return answer


def func_ba2d7c513475406aa4288af510f40e64(n, sum0, ouf, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return v1


def func_a23c43ae35164cb096948370126fda37(n, sum0, ouf, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return bestAnswer


def func_ede94975a64b49049f6ae1e6bf58fee5(n, sum0, ouf, a, sum1):
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return j


def func_d0a37413d9f54c569478a3595c5cdff0(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return sum0


def func_2b96c4d9620b4b7982b505a6eefb5105(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return i


def func_89e9b85a26c544a086aedb0df8518457(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return a


def func_a739149f7b9c4a66879b5a179e607fc2(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return aa


def func_8950cf6d63e64811bbfc92294e2db368(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return sum1


def func_d330898f48f64641b269448d408a56b9(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return x


def func_fa0bc27282894aaaa51e59d26159f5ab(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return p


def func_a069cac6f4a943368fca29268583c839(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return s


def func_29503c3e6fef4bb9b060ec03846a338f(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return r


def func_5e5c3b47d4604c749abb44d8926cc698(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return q


def func_c1ee4721fa4347988b32a3b253c8edad(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    return n


def func_e46193477f944cc594c7b95ed69ed697(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return allv


def func_962c3925ab91406bb6d35ebb3c9f81e4(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return x


def func_5da007c696994102abec5a5729d2c416(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return a


def func_459a492a92e04a3db6760f5a9909fa83(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return sum1


def func_02dd3451f25444018e56dd418d8c521b(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return s


def func_de8b61b6695c4822a6a63df1eee283fe(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return r


def func_824eb95d103246368c5a039b3ce70ce5(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return aa


def func_5195e8eac9154680a3da42848775242f(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return sum0


def func_7d379303322d4eb99174f51fc6ff1f89(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return i


def func_bc4c27c7b4ca46a0966c347addeb7668(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return q


def func_6cbb3971ccb64144b3103b6c225f718e(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return n


def func_3971f8bd09a94e60badc3d82fa36d6fd(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return p


def func_d86749847b10437f8ae17d16b3410a14(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return x


def func_74832609afb74f7f9bc10147789a305a(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return sum0


def func_e55e8291451b420781fb4438592fb70c(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return a


def func_2700ea89841b4497b2e0b06b69f3d990(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return aa


def func_a06253e8d064446188a18303b66b2d91(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return bestAnswer


def func_86f526a3ae4c486093d6df2f6486aa0b(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return i


def func_676da792b4cd4746a2d058816ff801d4(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return allv


def func_da4699718f684d5bba5affa2a2916f24(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return sum1


def func_79f08c4200e945248dc17aaa714c1cc0(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return allv


def func_c2119b1f3ba64491b149a67c00e59dc6(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return j


def func_aa3c82724c6d4b5ebc559bd2c8d45136(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return i


def func_91386b323f2c4963b3ddd0d116ffa8f3(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return sum1


def func_71ccf1ff26f0495791771fe4cecf61cb(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return x


def func_0aad9ce9d22f41aeaab806889152aac8(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return sum0


def func_b0804a90e2c2462f89ee31f3e87d8f4f(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return bestAnswer


def func_98a1f52f42eb48e98f667634396c1981(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return a


def func_a6fc11be5695452c88915f15db14b097(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return allv


def func_aef63fbb5f14434db1a1c585ca43d90b(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return sum1


def func_ad7cdd02f92945fe9598971924f88e03(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return ps


def func_531561c68bab480598a1e609e85570ce(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return j


def func_5ff401507eec421f87b54baaab690daf(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return bestAnswer


def func_b19fdc4fd3934e0397d4d909ace74cea(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return tmp


def func_45efdb147dda42d6b0cd6cf8e38bd824(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return v1


def func_f2f8ef25248245cca7007e9bf9274ff8(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return sum0


def func_dd5d6276785f4eaf9bad263cca311b66(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return i


def func_bc50ce1c677242faad458af88ab6c834(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return allv


def func_728dc919ca4d430d96c65b6bb254ef10(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return v1


def func_a030538fe98649fb816f3e00e17110a9(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return bestAnswer


def func_7b3b7042ea1942f2baee6b6de77f92a1(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return sum1


def func_a8aab68ca7d44b7b8e71847f83f0545d(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return j


def func_181b200d5ba64ff8b7f01a21bc87a322(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return tmp


def func_be9b7af50d1d4a1b8b76437749e0fecd(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return i


def func_986edb6e383a4e95818b5a40913bb5df(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return ps


def func_4f76281b322c4e6bac1036ad37b50be1(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return answer


def func_d712d2d88b814b70b56eaa49c952ecf1(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return sum0


def func_0ed4e80b375d42ff92d0f22a566b766c(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return allv


def func_96c20820037a42c0a7d60b04a8aeecdf(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return i


def func_a1a6903fcb1f428faf30197ab294fb73(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return tmp


def func_6031dff404e146f7b201b24ae2236ba4(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return bestAnswer


def func_f23e24aa1c8945308f699207e8b6ef15(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return answer


def func_78544090c67d412094363b15de3bf2cf(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return v1


def func_8355a38f30244b338b1b13aed95a9d7a(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return j


def func_420319d315ba40c8a42c58ad39cf70df(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return ps


def func_6c1bbd203eb244e9a32998dccc99809a(n, sum0, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return sum1


def func_f030a30050b04edbafc5274f00f2118f(n, sum0, ouf, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return j


def func_0446f91c69bc47fbb0c850d121143276(n, sum0, ouf, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return answer


def func_214ad7a1a64140bba767df7c7dc83743(n, sum0, ouf, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return ps


def func_4df3eab54c334c06b408f1ac5885e549(n, sum0, ouf, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return tmp


def func_18bf9e054a37431296af8ca032d5ec8f(n, sum0, ouf, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return i


def func_6e3c4cf704e6407f9016552a369ea855(n, sum0, ouf, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return allv


def func_c2ed0ccd72644b80a3d873f02c40ce52(n, sum0, ouf, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return v1


def func_b6ec475d402e46d1bd7c576a7ce7ba38(n, sum0, ouf, a, sum1):
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return bestAnswer


def func_c477e3897e2d4b87bbedc1da367b5c8e(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return s


def func_6ad7bcbfbf0a4138aa43e6b4a376ceda(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return p


def func_866f09c202f64ca08698740fd8cffbc0(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return q


def func_c1e6506118f243c38d9b3c49a7789b09(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return r


def func_ade11e1570d3422d8ebc05dd05fef9af(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return a


def func_7a3723a7f6234ad8b4354019563ba9d5(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return n


def func_7dc8dbaf664e4fc189691bf5aefec7c3(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return aa


def func_b758a6f6138443fdbb9ccabd59e78564(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return sum1


def func_8ec65912c89b400f867257fd7ac5375c(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return sum0


def func_64c56b52c8c242e8b5ee7514ef5fe4da(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return x


def func_5157328dcf1745918b1bb856e664c792(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    return i


def func_4a6ff05343594bb886f41727853f22c9(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return a


def func_9f4a9d91f77745e199eb3a8c74935474(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return s


def func_59a49b4264334389954bef695d1cce0f(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return sum0


def func_ca289c50a83646fdaac9906c8c5350f2(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return p


def func_14464b256c724dfe8eb72f5860c1ef4e(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return i


def func_2ef2ed5f1853420ebf18c8705557aa22(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return allv


def func_63b9e772dbd649b78832670b1922abef(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return r


def func_d8f98bfbaffa4781acb3a22f4fb98166(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return sum1


def func_dd2a61cb17ee43e985fa6e987a714689(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return x


def func_4d17044e7cff45ad98d6dcd00cc665ba(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return bestAnswer


def func_66c0c9f5e4c24aab8c08ec51211c1c8d(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return n


def func_3e924ab553d440d7ae924163ece9843c(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return aa


def func_b34d79a475d64eb7a3b44f018adcd1a5(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return q


def func_00c42cd4fbba4c9aa77d2b0878d70b94(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return aa


def func_b11420c1969748a2ad81492d6e8ee488(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return i


def func_3618132e297d4fe7b7ea22d83497337e(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return j


def func_94fe07d133fa4a53bb240760cd614fbb(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return a


def func_12fc962036b44d9ba788218d5c99a714(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return allv


def func_86d413e7a9444f5b9636df577829ae56(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return bestAnswer


def func_0770dd90b25e4c5c96912e7bf0481713(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return x


def func_5146844e9a314c588cb4a3a862e9b586(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return sum0


def func_90d4c57877254ecca44daf8f9d3a6f06(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return sum1


def func_06b8d5038a8b43bbad2eba741a75ae4b(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return tmp


def func_1fadc6331c134885b44dd4563e36ca6f(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return bestAnswer


def func_66dbe008de0040aca5a02337d3b2c934(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return a


def func_7a1844e05d2c44d190ee678d629a8d01(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return allv


def func_0f126ac36b2142fd8d0b7b7ba86416e9(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return x


def func_9f6faaafeff34e159144c70e4c7ec567(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return j


def func_281e915febd9471dbafcde9176f2250d(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return i


def func_f995aeda22f84eb7aafde347855ec219(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return ps


def func_0e90eddf49b94ffc9dc1a6a29df4a4bc(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return sum1


def func_77061586d0ff48a1a9601c022aac5177(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return sum0


def func_d2d753163dfd4113a6f105ba2685f886(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return v1


def func_acb49691e51f46cead8fa7303fe82395(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return j


def func_57d221703297450cb9894561ede69905(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return sum1


def func_29bc710a3cad401d8423e25d1aa5cb2a(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return answer


def func_ab46d9e181594291be4a6074e9fa126c(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return ps


def func_214861888ba54f2ca47f7d655673b7a1(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return v1


def func_8aeb1bb1d7c74af8abedde5d8ab05e5d(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return sum0


def func_5891e2d8c06e4a5facd00af3678c8458(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return i


def func_de7a83fe3b6a471686e51fc7f80c0c9c(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return bestAnswer


def func_de9b0b98e18d4261b95b3cb5ed7ab18b(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return tmp


def func_34833f9e50af42fa9b4f4aeb8ce61e3f(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return allv


def func_804e896a253f46c996820f7ee27ba7f8(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return sum0


def func_351a1fd47b9c4075a00b0ac2ee3c9abb(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return allv


def func_878fd13dd2584ff89a14910c97ea0ebe(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return answer


def func_5faf2add46344504a002136247fe4020(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return sum1


def func_6b2af523be5f45188af3d7a9157cb806(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return i


def func_2c7c60d8c3104adbb1b60a5a928a3905(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return j


def func_47d393a6ad3c419085fd5b2fc4ee5383(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return bestAnswer


def func_6ca92be4360c4e5eaea232fa92c53363(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return v1


def func_6f3e1fae3e0f4f75a97f373b9315ceb6(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return ps


def func_e0e3e47d99c04a83b2629f62795ed35b(n, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return tmp


def func_449e97e67f28434688700109799c39dc(n, sum0, ouf, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return bestAnswer


def func_036a507bce984383bab65131f5e36c1a(n, sum0, ouf, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return ps


def func_f6fd5dcda2d249fcbbcdef0b67156fe1(n, sum0, ouf, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return sum1


def func_1bdc7d47e5ab405eb9cb6df80d7d7843(n, sum0, ouf, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return j


def func_ce50a14c09c040eba617aa0539136ade(n, sum0, ouf, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return answer


def func_382543952e004e59b4493136bfcac8c1(n, sum0, ouf, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return v1


def func_d40d81aff830449699e5c1cf32afc566(n, sum0, ouf, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return tmp


def func_a329ab3f81d14e4c9c6027306ff3da90(n, sum0, ouf, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return allv


def func_9331b690758a415fabf8579cd3f332d8(n, sum0, ouf, a):
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return i


def func_97f3ebacffba4eb280bbb715f97dee8d(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return allv


def func_bba40c5d397c431fa08cff49509dc5a3(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return r


def func_900c57d51ee04dde97e0dc7f5566040d(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return q


def func_9a2bf7cb0f1043b5ad810bc10fb87935(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return sum0


def func_b2c0d387902140e78b6208b93b2fd8c9(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return i


def func_3101822c2b3b4cfbb6ee041cc0470fef(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return p


def func_9e2f4a7385cc49bf876ae6a193f4b920(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return n


def func_9948b65a744c48cfbb4ebfc9e85cc4a0(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return sum1


def func_706798865b8a4d0a8c2b77eccec56135(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return x


def func_f840db3f64a84eb39d6232959970357c(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return s


def func_54c4267409a64f178c747768892e69a7(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return a


def func_90d29caf75344cce8169ad7b75373717(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    return aa


def func_5a349e35974a427b98c61cd78ff7b550(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return i


def func_432681e0a1c24ddf82147ae3b6a751e2(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return p


def func_ee393213a09d4f93b3d88dd2ef3d6a7e(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return j


def func_ebab4ba0a82a4077a9488e0f66cfb0a8(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return x


def func_333229244d1749c38bb6f9dd6029979a(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return q


def func_29cd03bad71247c49414a5610f4fc351(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return r


def func_f61f3ac171374f7ca2bbb8fc2bb20056(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return sum0


def func_61b85b191f064a7f9305769ba4a44320(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return s


def func_ec63d97c629d44dba0ee841b9598693d(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return sum1


def func_8019433ca33045a7a31db18fdaf0b29d(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return bestAnswer


def func_fa320b1c27924999a33e268d9dc504bc(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return a


def func_93a42f0db02949d0922ca182559d56e0(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return allv


def func_32b473e62d274b69b397b6720e6fd2f1(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return aa


def func_55b702d3e02d4c94ab4b1483f9596934(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return n


def func_8ee83f939b0147a3b9bae5feacca03c9(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return tmp


def func_56babf604b0c4f44bc389b761a92bd89(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return v1


def func_44f183800e4e42a29c95488eb1a73858(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return j


def func_9c6f86fab6ae41ac88c1e215212e6bec(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return aa


def func_d4114101af4c419cb0a78c0d96948ebb(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return a


def func_c746c61147d6423586d18dcd0d2c90b9(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return i


def func_1b1021798bfe4375aafb864658799dcc(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return sum1


def func_d01a5dbcb34947cbaf9a2f15250e46ed(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return bestAnswer


def func_182277f4a6694f21bb881e8f6812741a(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return allv


def func_25c8085f7955410584fa2958ad71ef0b(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return x


def func_0e2f8a514d5e41198292ba1133d91d1a(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return sum0


def func_03b4867f8d954e228c4091b565b63935(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return ps


def func_985ebb7466be44c8bb928f4662c082b9(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return tmp


def func_2510bed6d11c4c759a0b8a71cc1f631e(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return sum1


def func_0906b5eea35644d58ba702cb7d4850ff(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return answer


def func_a3da57f5236c4c0a886ba77dc8e53cda(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return i


def func_f387a10715b94634a24e2f4e3d535bfe(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return x


def func_8c445c38fd954331a06625dfdaa69efa(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return sum0


def func_8bea988429f643b388c7c11486c1bd2f(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return ps


def func_11a2bee1fa184ace9dc79473e0d008ce(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return j


def func_b229d9665ceb4ce29a8402a82a5c97f6(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return v1


def func_756a0a874ff54f67954cc1ba233edb4d(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return a


def func_46eb2d372a6044fa97dc8fe776c8c485(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return allv


def func_910121ec17214244bd88f570c131c249(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return bestAnswer


def func_c55ed46ba0a8408391bd82320e532267(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return sum0


def func_e16fa4015dc34fdab60a80c2abf62180(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return i


def func_cf058c2e5b424157bcc445607abd325a(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return answer


def func_1fec191469d2499fa403a3df99e45b33(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return allv


def func_7d0be09cd5184945aed50da4347270c4(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return v1


def func_0e2e1821126745f0a56d5218aeabe177(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return ps


def func_0a24e2b088174eea89d1cdf21cbbd20f(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return tmp


def func_c0c1d18b25734fe981416423bb8001e1(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return bestAnswer


def func_47d0ade5dfab4c1fb5663966996722c3(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return sum1


def func_4042606945d040328a0b10cf1fd1928b(n, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return j


def func_6fa3d4cdbe884d9e85f134b24f6c0fc7(n, ouf, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return j


def func_3dc1b6a07687417da34d6dfd2b38a4d5(n, ouf, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return ps


def func_2eead9b2b37b4ac0ae65e65fdc306794(n, ouf, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return bestAnswer


def func_5d3e248379c94a03ae12584b53c4de18(n, ouf, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return answer


def func_9f2ba0222d5e411c8d057e3ec13937d5(n, ouf, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return allv


def func_9a7af39b5eb640ab85e8992ae5910786(n, ouf, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return sum0


def func_b1268609c72a41b1b081574c01d76c6c(n, ouf, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return sum1


def func_2bd54001a1be40cf9f8066542f6bc27f(n, ouf, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return i


def func_b73d7a3086ae4034b131ab73e50b9aee(n, ouf, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return v1


def func_0a1f701dea46407a982fb4dcc747aeb3(n, ouf, a):
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return tmp


def func_2b1b79baf6d74393b90094c5079d463c(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return aa


def func_732a984ed7bd48a5a7ba62d2bbda87fb(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return sum1


def func_398089d011284e498cb947ec37e73534(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return q


def func_71dbb326c309465d82662e4cba14d834(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return bestAnswer


def func_c05747351635458fbc82fc9657f33f89(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return a


def func_a6e7f55060bc4a068f8ce73fce3f5e50(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return r


def func_1c271325d5be4ed6a087fa947ba30421(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return i


def func_3330f86fc595453b8fea4bed7fb9b364(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return s


def func_0afafb204b004acdb79573730ed2d2d2(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return n


def func_4c835aceb3f84c2785c3ca8526fc8175(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return sum0


def func_ecfd207a4c52431687585f0d03bf67da(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return allv


def func_e61dcb8290f14ad783bf2f0f3b6cffa2(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return p


def func_7157c9e608344e8893d2960de9f3d44f(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    return x


def func_614776fe032c4db98759fe0add0255e0(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return p


def func_25606cf29d054268a53a5185b19cc151(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return sum0


def func_5c21c0dc729647d58bb959a4a850e8f2(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return allv


def func_bfd3bad12780449892e046809dc3fd78(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return s


def func_7a8a9ab2b0574a38b8afbbce6528a67f(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return tmp


def func_f1a74b4ca6ce46d3bc4726420d6215f0(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return aa


def func_9090aba990054f8eacaba2bc7dcccbf5(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return j


def func_d7912c1483f943018c24a189f9a2b795(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return v1


def func_a175f22abc104b70b3c7b50a1180685e(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return bestAnswer


def func_0e628567d67849aa8cebe9cc8af469a0(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return a


def func_da0a01b1802540d6982a0300dd482a33(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return i


def func_c23d6396dbde45629692e84d960eb9f4(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return x


def func_b9f48b7fd439451a90fbb6ec7164a227(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return r


def func_36469aa2e3a54f2c9950f7e7cbde3ffd(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return sum1


def func_14a2dc10ba7147d59e3651b2de879b3c(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return ps


def func_98ebe8e7425440939e13553d1b85d2b6(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return n


def func_f867b30f84ca477c8c82803d3f1936ba(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return q


def func_43f3c6e5fffc429c8969aa46613f051f(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return i


def func_2ebbfdb3ce064966ab2b09cba774fdd2(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return v1


def func_35b60f51f5e04548a7da7c4650e12b4c(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return x


def func_ba8c9f75218d4f1eb3da868f0a7add34(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return j


def func_f3ec67a694dc41d19f84a88e7c306b1c(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return tmp


def func_2e73a10623c14b3a8d499a9952437e10(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return sum0


def func_015ffcb03a774240a5d1b63242621ff1(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return ps


def func_3d6cc37783284b88ab984d9c66c5230f(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return aa


def func_447af3d72a1f4d6c8af2fd7d429031f6(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return bestAnswer


def func_e3575d0a69644cc99dc79ac54e9d8d26(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return answer


def func_a979de60d91d4d7d9610e259027eae2d(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return sum1


def func_5277d0ea19ff41d99f67321ba2db34fd(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return allv


def func_7ebae28e86f2452c882ad696e170fcb2(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return a


def func_cb2b2c482b0e47db8ad555a24142607d(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return v1


def func_07b1247f3f58454c9e52c13cadccba55(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return x


def func_a79c5ed8c9194de2b34577bd71ecd09c(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return tmp


def func_bb4812c6cae04b09953963c3dc559262(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return i


def func_208a0d0cd1344f4b91f3154eac236121(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return allv


def func_f5dfaa07203b47b4a2e08777e4d158fb(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return a


def func_7dd1e2968cc14ad9acb1bf4f29ebbc2a(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return ps


def func_69d818f3e68c4866a31af17ce5add2eb(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return answer


def func_a56e638f973142b9b1abf7fdd21c3a8b(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return sum0


def func_a16117e2c1a545fea658f2116cc4dd05(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return sum1


def func_ecbff9e9587740ce9baf1da75c518c80(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return bestAnswer


def func_94c2d04dd8e54d87b513e88748924aa6(n, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return j


def func_ecfbb8b2104f43c097d594404d9d1d6e(n, ouf, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return ps


def func_5becaa76eb5246fea922984ed7508c4b(n, ouf, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return v1


def func_e8d0853a2fdf49bbb3894db76807d1c9(n, ouf, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return sum0


def func_d2de71f460694c219aef2969aea4309b(n, ouf, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return i


def func_c19c1c0a574d47d6980a266874cf60e7(n, ouf, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return answer


def func_a5aba63927094127b2cc096f7cba06dd(n, ouf, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return allv


def func_db92577439af43608089e277bab40dd2(n, ouf, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return tmp


def func_33156ee726814d2eb95bc5215d084928(n, ouf, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return j


def func_5c5d6292221148ad97d7ecc8cc6696ce(n, ouf, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return sum1


def func_b3b3cf8f598346d48abdfae66ae1507b(n, ouf, a):
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return bestAnswer


def func_3bf3672e66bd4031ab49ead7c2753bfe(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return bestAnswer


def func_5427208d7c764770a64fbb98f50e25f1(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return i


def func_64d1639af72c48b3b33d2ad8ea9887de(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return p


def func_1f717a6b50bc4e2ebb90cf5acc97fbde(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return r


def func_6713e7f5b66a4ecd8b59a9f2f3c48dc4(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return sum1


def func_50eaee1128af4f68a8c8b5a70da2f5c9(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return s


def func_ab5445954a234f90b127186693d015f9(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return n


def func_9fcd7604c2154906a9f34ad6ba57e989(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return sum0


def func_eb93498df8f54a7dabe9dc8a2697316e(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return j


def func_5b37aa76d12244c1b8e14c39e4ba904c(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return x


def func_459e62d5722246f2a835cd86f817e5fd(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return a


def func_23b2dbd8055b406c9d2213698a951df5(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return allv


def func_6d36a5c578f046beb2524142a7d9403b(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return aa


def func_8d03af1fb43b419596a86a10853a8023(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    return q


def func_b258cb3715164600972f1fec0778d534(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return v1


def func_194ea1e6c73d42a5b38ddcb3bd69a44b(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return allv


def func_247d0d1c357a4b3aa3a10d5fcf27e2cd(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return p


def func_76db762b51b74208910ceda7d2502e1d(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return a


def func_8031f33b2c0043579fcbbfc84405f1cf(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return ps


def func_61fee87cf8d44780a539b4b091c74370(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return r


def func_81f4cb6bef6d435f81dc2c03b0efba41(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return s


def func_70872dcea1ef483887d42f84359f7259(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return aa


def func_2f2683559088431e826ffcf561be3116(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return x


def func_8048c529eed84307b97ec4e21d643c92(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return sum1


def func_fa1105bb3cd94d5bbaa7a80e64235dba(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return i


def func_ed14874b0e254db4a7bc4f6a6ed5d26a(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return tmp


def func_4e27f7c838974342b840fc06b6c43686(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return answer


def func_faa679231aa24313aa3cf9b7b4d8e534(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return sum0


def func_d48e0d01b899495da7f98abd955111b3(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return j


def func_454b8619de394c83a5a1d88ced45610c(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return q


def func_4b5daa8a710c48128454f6e4153490fb(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return bestAnswer


def func_fb35ddbd61d44e198ec791a152d26e64(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return n


def func_925a4ca8674c4549a5135f55c000ba16(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return bestAnswer


def func_106326ff8ed9451c8b6c544b6a08cd8c(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return aa


def func_d07f626ed6a345cbad7ddd704f73182a(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return v1


def func_248a2bb21f84418aa6a276f691c580bb(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return answer


def func_efdb11c62025470fad4e21edf91928fc(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return i


def func_57c842040a9f420188a637e010138366(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return j


def func_918067a014f244c1ab372e211b4636aa(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return x


def func_69686462ea414544ae33e443865cf0da(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return a


def func_9af25729f0a34120b1e4cac4e9c6d9e5(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return sum1


def func_5c333391bc594253a95f9dd3b65d53ba(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return tmp


def func_a0645403d0d946f496a7bdcad114361d(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return ps


def func_7c1e4a13557d42958564892dca8407b9(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return allv


def func_a76c57432ece4319b1a9719f419f2463(r, n, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return sum0


def func_768dc55cf23942ef9ae09687010543c1(n, ouf, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return sum1


def func_51dc81ac69e24f0eafd7f43202edb45b(n, ouf, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return i


def func_29acfdf08b5045528c70fa5ac9955651(n, ouf, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return a


def func_5d04e744b5da4d55a90a0c9901a17baa(n, ouf, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return answer


def func_b8eab0f2185141df82065790e82d4d0c(n, ouf, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return ps


def func_e7dc48bc1df6455fbf7d3e556edf0d53(n, ouf, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return x


def func_205a7be4bed74dfab5f6f63e933e85e6(n, ouf, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return tmp


def func_1fc3e91f6b8e44cdb249f7603c860aff(n, ouf, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return sum0


def func_fdd7c827726345a4aca766b4fe5bddac(n, ouf, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return j


def func_ddcdc7bdb24a4a81be72c42ba96ac3bf(n, ouf, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return bestAnswer


def func_463f3372a0e741c987d004e93a1abd12(n, ouf, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return v1


def func_0c93c9bfd7274a5b8d3ef394b1bdcf99(n, ouf, aa):
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return allv


def func_fe8b9f2a1cbc4759acb5d535ddaa93fa(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return tmp


def func_45afc3ac5f814e5bbe298502c4c11fc9(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return aa


def func_47d28a0df45b42bf8bc9035eaf654af1(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return sum0


def func_0529f21679ab4b7f8c442f84e101364c(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return s


def func_92ca7e1e5a134443b2603119b216d98b(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return n


def func_7aa8d871cc99422e83d7d6f090b9ea5f(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return v1


def func_5a9469a48fbe498e82fb4cb3b2d3893e(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return sum1


def func_e60d05d47147489b88c4bcb0660e0886(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return r


def func_112e7845011d412bbd4b8bdee7ad0f00(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return x


def func_80e9cb2ac90044eba1adf95286070fc8(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return ps


def func_baab8f71e8f64d3fb28400c4199287ee(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return allv


def func_bea53c821033479886491f81d506627d(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return bestAnswer


def func_38bcfb5b36bc49cba11f79a259f446fe(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return i


def func_24b52fda97eb4fc5a8f7d928c8ee6f7c(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return p


def func_0d7ef27559cf42168fa33979b63d2f35(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return j


def func_438317cbcb0746b29e263316fbfc8902(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return a


def func_41afb4f0018b4e9fb63a536df4b341fb(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    return q


def func_05df08a5a0b94e4bac50e01cb3eadc9a(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return sum1


def func_1a4f2638614445e7b30d9938ad93376f(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return q


def func_7cfbd496c9474dc5b6688c10c57c9ebe(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return allv


def func_a974eab382084fff97ed49a359d8c858(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return j


def func_bb74da3a0f0a49529606cf76819b913d(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return bestAnswer


def func_befe41dfc19840f2a828651c6cc683ab(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return tmp


def func_b5d4fbee21e94aa2afaa7997a5a056ec(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return ps


def func_6d278d9d188e4123856f83131d1cc7a3(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return x


def func_2d245bf5772a4617921aef3ea6a7fed2(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return r


def func_5e4b9c3bd501446bbc8adbda7f60e34e(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return v1


def func_730545603b8d4b31b58a842bbd1f2c77(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return p


def func_eba5fed8b9414729b5a2fd78f10edd7f(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return answer


def func_2d7ab159b5f9456f91ecf237494fda1d(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return s


def func_abcf2b58c625478aa1c9ea99a0405314(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return i


def func_61dc134d67e24b91b52efdb29bdc5ba0(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return sum0


def func_326ba297ac704fe7b2aac76d1f0774ad(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return a


def func_8ff0240fb9474070b1a07804176a4bd3(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return n


def func_88b6a55dfe584e50a0c99804552f0ff2(inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return aa


def func_86eb879d557c4dea971c7870fb7f624f(r, n, ouf, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return allv


def func_7451318129734403a97eb4682f603d35(r, n, ouf, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return bestAnswer


def func_7f40b8428c1e4e12a1648d93bdc11233(r, n, ouf, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return i


def func_86d3c7db62a64503b9a482cf9ed1a2fc(r, n, ouf, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return sum1


def func_dd4007814596414ab0cb84910c8c8953(r, n, ouf, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return j


def func_0f4bd92120da4e8ba169c6b3bc051c93(r, n, ouf, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return ps


def func_5388507d69cb4aa4b9f93bce9cbb6d0c(r, n, ouf, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return a


def func_e9e3bc4a169f4d009a12639785702a0d(r, n, ouf, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return x


def func_78e3560d9707488dbece4056320d4547(r, n, ouf, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return v1


def func_0ccaf469f2d947ca9465f6e115da9602(r, n, ouf, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return aa


def func_0cf979edb3fd459eb00ff0779580947b(r, n, ouf, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return sum0


def func_46781e3680134113abdbe7f009b399b4(r, n, ouf, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return tmp


def func_657edadcc7684c90a83acd8b519c1cdc(r, n, ouf, q, p, s):
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return answer


def func_30b790d052f54d04882a37dfae1bacda(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return r


def func_82274935491348aa915ee9073db13765(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return a


def func_18ff9563af2b40218ca096cf87686b85(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return bestAnswer


def func_ad32272d63dd496cb4d322d648a73f14(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return x


def func_435014638a0d4ff599681dd41ea3a8cc(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return sum0


def func_02b9d554128949cf9e7f6b12b8aea82c(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return ps


def func_4f898a7094f74e54b88e6edcabccb38d(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return p


def func_147dce35bd874272ab272d15230272b7(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return n


def func_278daa9ead11483b8a2b44e441c071e3(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return tmp


def func_ef0f52937d5c4e52bb7fa72643867e6d(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return v1


def func_856033bc5ba74564b6e53dd1d0018b77(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return sum1


def func_5c2d7e7f790248d5b147e1aaa71ec21e(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return j


def func_25efcb7071e94b9a9cf6d59bcdce8430(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return allv


def func_44539c770bca44ae985536b928412741(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return aa


def func_6c3adfbef1bc4ac48323bac0c2b65b15(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return answer


def func_2dc5ddc014e74bb3a0a890f920ab9aa8(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return s


def func_8195eafcc8a242db8e854d2863354ac9(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return q


def func_63a1c23684a04cee9ffeb392d4a90fbb(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)
    return i


def func_b55386c2519848f4a97e7e4dec1bec68(ouf, inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return s


def func_1e4137fcdab24bcf9e2d16542aed0b23(ouf, inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return tmp


def func_c64851728a0c4a4ab43f30490540d9a2(ouf, inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return ps


def func_305c84dc6f2a4caf88f3b3b88fe9285a(ouf, inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return bestAnswer


def func_d3485b33e9f24753954ed060ec11feaf(ouf, inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return q


def func_0721fcae91874610b87cb5b543faab9b(ouf, inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return sum0


def func_3824f09f3d7f49c6ace2d6f242779eb3(ouf, inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return r


def func_15c6602e3a4f4f95a72cd736580e9ffb(ouf, inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return answer


def func_ddf59852d162421d9f25dcc4b8395052(ouf, inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return p


def func_b4c5e72566744767af688829db3fefce(ouf, inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return j


def func_595ac0dec3304cbfbfce23f44d6cc5e1(ouf, inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return n


def func_8d4517fa7e9e49569d98fb1412d62325(ouf, inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return allv


def func_77d9b4c9da37473bbacfc23a00cfc5b3(ouf, inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return a


def func_4342461c8c55445eb847b28ecbc63cbd(ouf, inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return aa


def func_0c4686a8c80a40cbb43d14321c5a8025(ouf, inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return i


def func_6fc6ec10942048b896e3af146c26459a(ouf, inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return x


def func_a0ebd0fde8f04185be8e6788a76e7a4b(ouf, inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return v1


def func_5205b4d452bf46edac07ba14fc76a37c(ouf, inf):
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return sum1


def func_2d295440a44b42f8bb23a5fbb277ca0f(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return allv


def func_2ab1310fd233438e8e0f82b73c9fa877(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return r


def func_4cf343b1fe874cf0aa46a12876785b14(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return sum1


def func_6a5408b296584550b40c4c7797c19029(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return a


def func_b1f53c94e1944e8fa1f3f33064bd2f89(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return ps


def func_9f712f0d119f418d9f36543897d4b2af(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return bestAnswer


def func_8976925932c646a6a24dd4de9769d0ea(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return x


def func_25ce795595d94d8d90162594e57839fa(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return i


def func_8a8972aa10a746b2b330f426cbe8b57f(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return sum0


def func_186dec27ed89443dad44ed05c94ad664(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return j


def func_86da39926ac944bf86e12d4470097d7c(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return aa


def func_c8f542871ff74c4b9f1284eeb25419f7(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return v1


def func_48973e69ddf04db4a2fecb64ae4164f6(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return n


def func_68956e03c5cf4a0293beccc550bb18c0(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return q


def func_28d9e1aba71240f988e4531ae3e7e075(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return answer


def func_df345a9276454a40bd65e36750f68fa6(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return p


def func_fcd168cae1b54e96929edf213e022473(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return tmp


def func_edc55e90e9ff4176b5a27435cbb3d36c(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    return s


def func_0ac25132092a4d8ea6a6a7d0de93a5d6(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return allv


def func_fd95f1b2e070429692d58d889b0dc122(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return p


def func_361867bb8133472f909e8442934ca9cc(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return bestAnswer


def func_c660b545cf8249d8b04823ae1f0d821d(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return s


def func_6076713b6e684e06a9ebf6575e5c98ef(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return ps


def func_9a037582aaf540f7bdbfe8357ed418e3(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return i


def func_f19d2ddb59b04276ac2365af266e9d94(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return sum1


def func_51206e4dc8fb411ea2ed963233170438(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return tmp


def func_ae2e61d889e24563a6f5dded0ac99a2a(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return v1


def func_4c2a8d013c614a559b9c22777b7b4bfe(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return r


def func_c76e63e8cc0d44d88735c69fc597ce96(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return j


def func_238048de3e5245469e86f8992c31aae2(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return sum0


def func_1ba5547614824a0ba85cf6ec3126e4e0(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return q


def func_2a233db07507480581a07ede866aa630(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return aa


def func_562f6189b99b4406a34ea11315bdef03(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return n


def func_97db999c21e543ff946297c0c83b4993(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return x


def func_9352579fe62d48e79c5ac9951e082126(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return answer


def func_eb859a6d46f64c5c9f5254610a2fdfd5(ouf, inf, tnoc):
    ouf.write('Case #%d: ' % tnoc)('Case #%d: ' % tnoc)
    n, p, q, r, s = map(int, inf.readline().strip().split(' '))
    aa = [((x * p + q) % r + s) for x in xrange(n)]
    a = [x for x in aa if x != 0]
    n = len(a)
    sum0 = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    for i in xrange(n):
        sum0[i + 1] = sum0[i] + a[i]
    for i in xrange(n - 1, -1, -1):
        sum1[i] = sum1[i + 1] + a[i]
    allv = sum0[-1]
    bestAnswer = allv
    j = 0
    for i in xrange(n + 1):
        if sum0[i] >= allv:
            break
        ps = allv - sum0[i]
        j = max(j - 1, i)
        while j <= n:
            v1 = sum1[j]
            tmp = max(sum0[i], v1, ps - v1)
            if tmp < bestAnswer:
                bestAnswer = tmp
            if float(v1) > ps / 2.0:
                j += 1
            else:
                break
    answer = 1.0 - float(bestAnswer) / float(allv)('%.12lf' % answer)
    ouf.write('%.12lf\n' % answer)
    return a


def func_1f1a07b3c24148fa96a15f67f7b04c18(ouf, inf):
    noc = int(inf.readline())
    for tnoc in xrange(1, noc + 1):
        ouf.write('Case #%d: ' % tnoc)
        print 'Case #%d: ' % tnoc
        n, p, q, r, s = map(int, inf.readline().strip().split(' '))
        aa = [((x * p + q) % r + s) for x in xrange(n)]
        a = [x for x in aa if x != 0]
        n = len(a)
        sum0 = [0] * (n + 1)
        sum1 = [0] * (n + 1)
        for i in xrange(n):
            sum0[i + 1] = sum0[i] + a[i]
        for i in xrange(n - 1, -1, -1):
            sum1[i] = sum1[i + 1] + a[i]
        allv = sum0[-1]
        bestAnswer = allv
        j = 0
        for i in xrange(n + 1):
            if sum0[i] >= allv:
                break
            ps = allv - sum0[i]
            j = max(j - 1, i)
            while j <= n:
                v1 = sum1[j]
                tmp = max(sum0[i], v1, ps - v1)
                if tmp < bestAnswer:
                    bestAnswer = tmp
                if float(v1) > ps / 2.0:
                    j += 1
                else:
                    break
        answer = 1.0 - float(bestAnswer) / float(allv)
        print '%.12lf' % answer
        ouf.write('%.12lf\n' % answer)
    return allv


def func_4cbc3b1f8d5142b9ab4f34c806a6a650(ouf, inf):
    noc = int(inf.readline())
    for tnoc in xrange(1, noc + 1):
        ouf.write('Case #%d: ' % tnoc)
        print 'Case #%d: ' % tnoc
        n, p, q, r, s = map(int, inf.readline().strip().split(' '))
        aa = [((x * p + q) % r + s) for x in xrange(n)]
        a = [x for x in aa if x != 0]
        n = len(a)
        sum0 = [0] * (n + 1)
        sum1 = [0] * (n + 1)
        for i in xrange(n):
            sum0[i + 1] = sum0[i] + a[i]
        for i in xrange(n - 1, -1, -1):
            sum1[i] = sum1[i + 1] + a[i]
        allv = sum0[-1]
        bestAnswer = allv
        j = 0
        for i in xrange(n + 1):
            if sum0[i] >= allv:
                break
            ps = allv - sum0[i]
            j = max(j - 1, i)
            while j <= n:
                v1 = sum1[j]
                tmp = max(sum0[i], v1, ps - v1)
                if tmp < bestAnswer:
                    bestAnswer = tmp
                if float(v1) > ps / 2.0:
                    j += 1
                else:
                    break
        answer = 1.0 - float(bestAnswer) / float(allv)
        print '%.12lf' % answer
        ouf.write('%.12lf\n' % answer)
    return q


def func_08a8e8fc537e42e09931145c81c0cd0b(ouf, inf):
    noc = int(inf.readline())
    for tnoc in xrange(1, noc + 1):
        ouf.write('Case #%d: ' % tnoc)
        print 'Case #%d: ' % tnoc
        n, p, q, r, s = map(int, inf.readline().strip().split(' '))
        aa = [((x * p + q) % r + s) for x in xrange(n)]
        a = [x for x in aa if x != 0]
        n = len(a)
        sum0 = [0] * (n + 1)
        sum1 = [0] * (n + 1)
        for i in xrange(n):
            sum0[i + 1] = sum0[i] + a[i]
        for i in xrange(n - 1, -1, -1):
            sum1[i] = sum1[i + 1] + a[i]
        allv = sum0[-1]
        bestAnswer = allv
        j = 0
        for i in xrange(n + 1):
            if sum0[i] >= allv:
                break
            ps = allv - sum0[i]
            j = max(j - 1, i)
            while j <= n:
                v1 = sum1[j]
                tmp = max(sum0[i], v1, ps - v1)
                if tmp < bestAnswer:
                    bestAnswer = tmp
                if float(v1) > ps / 2.0:
                    j += 1
                else:
                    break
        answer = 1.0 - float(bestAnswer) / float(allv)
        print '%.12lf' % answer
        ouf.write('%.12lf\n' % answer)
    return tnoc


def func_8504801b20904afa880831e2d40f9e5b(ouf, inf):
    noc = int(inf.readline())
    for tnoc in xrange(1, noc + 1):
        ouf.write('Case #%d: ' % tnoc)
        print 'Case #%d: ' % tnoc
        n, p, q, r, s = map(int, inf.readline().strip().split(' '))
        aa = [((x * p + q) % r + s) for x in xrange(n)]
        a = [x for x in aa if x != 0]
        n = len(a)
        sum0 = [0] * (n + 1)
        sum1 = [0] * (n + 1)
        for i in xrange(n):
            sum0[i + 1] = sum0[i] + a[i]
        for i in xrange(n - 1, -1, -1):
            sum1[i] = sum1[i + 1] + a[i]
        allv = sum0[-1]
        bestAnswer = allv
        j = 0
        for i in xrange(n + 1):
            if sum0[i] >= allv:
                break
            ps = allv - sum0[i]
            j = max(j - 1, i)
            while j <= n:
                v1 = sum1[j]
                tmp = max(sum0[i], v1, ps - v1)
                if tmp < bestAnswer:
                    bestAnswer = tmp
                if float(v1) > ps / 2.0:
                    j += 1
                else:
                    break
        answer = 1.0 - float(bestAnswer) / float(allv)
        print '%.12lf' % answer
        ouf.write('%.12lf\n' % answer)
    return sum0


def func_da20bf307a064051b864dfdbba175c34(ouf, inf):
    noc = int(inf.readline())
    for tnoc in xrange(1, noc + 1):
        ouf.write('Case #%d: ' % tnoc)
        print 'Case #%d: ' % tnoc
        n, p, q, r, s = map(int, inf.readline().strip().split(' '))
        aa = [((x * p + q) % r + s) for x in xrange(n)]
        a = [x for x in aa if x != 0]
        n = len(a)
        sum0 = [0] * (n + 1)
        sum1 = [0] * (n + 1)
        for i in xrange(n):
            sum0[i + 1] = sum0[i] + a[i]
        for i in xrange(n - 1, -1, -1):
            sum1[i] = sum1[i + 1] + a[i]
        allv = sum0[-1]
        bestAnswer = allv
        j = 0
        for i in xrange(n + 1):
            if sum0[i] >= allv:
                break
            ps = allv - sum0[i]
            j = max(j - 1, i)
            while j <= n:
                v1 = sum1[j]
                tmp = max(sum0[i], v1, ps - v1)
                if tmp < bestAnswer:
                    bestAnswer = tmp
                if float(v1) > ps / 2.0:
                    j += 1
                else:
                    break
        answer = 1.0 - float(bestAnswer) / float(allv)
        print '%.12lf' % answer
        ouf.write('%.12lf\n' % answer)
    return sum1


def func_ea2640c202ca405a8bac0c2c2af826f6(ouf, inf):
    noc = int(inf.readline())
    for tnoc in xrange(1, noc + 1):
        ouf.write('Case #%d: ' % tnoc)
        print 'Case #%d: ' % tnoc
        n, p, q, r, s = map(int, inf.readline().strip().split(' '))
        aa = [((x * p + q) % r + s) for x in xrange(n)]
        a = [x for x in aa if x != 0]
        n = len(a)
        sum0 = [0] * (n + 1)
        sum1 = [0] * (n + 1)
        for i in xrange(n):
            sum0[i + 1] = sum0[i] + a[i]
        for i in xrange(n - 1, -1, -1):
            sum1[i] = sum1[i + 1] + a[i]
        allv = sum0[-1]
        bestAnswer = allv
        j = 0
        for i in xrange(n + 1):
            if sum0[i] >= allv:
                break
            ps = allv - sum0[i]
            j = max(j - 1, i)
            while j <= n:
                v1 = sum1[j]
                tmp = max(sum0[i], v1, ps - v1)
                if tmp < bestAnswer:
                    bestAnswer = tmp
                if float(v1) > ps / 2.0:
                    j += 1
                else:
                    break
        answer = 1.0 - float(bestAnswer) / float(allv)
        print '%.12lf' % answer
        ouf.write('%.12lf\n' % answer)
    return r


def func_8bd8f18e82c94858b239faa401cf93db(ouf, inf):
    noc = int(inf.readline())
    for tnoc in xrange(1, noc + 1):
        ouf.write('Case #%d: ' % tnoc)
        print 'Case #%d: ' % tnoc
        n, p, q, r, s = map(int, inf.readline().strip().split(' '))
        aa = [((x * p + q) % r + s) for x in xrange(n)]
        a = [x for x in aa if x != 0]
        n = len(a)
        sum0 = [0] * (n + 1)
        sum1 = [0] * (n + 1)
        for i in xrange(n):
            sum0[i + 1] = sum0[i] + a[i]
        for i in xrange(n - 1, -1, -1):
            sum1[i] = sum1[i + 1] + a[i]
        allv = sum0[-1]
        bestAnswer = allv
        j = 0
        for i in xrange(n + 1):
            if sum0[i] >= allv:
                break
            ps = allv - sum0[i]
            j = max(j - 1, i)
            while j <= n:
                v1 = sum1[j]
                tmp = max(sum0[i], v1, ps - v1)
                if tmp < bestAnswer:
                    bestAnswer = tmp
                if float(v1) > ps / 2.0:
                    j += 1
                else:
                    break
        answer = 1.0 - float(bestAnswer) / float(allv)
        print '%.12lf' % answer
        ouf.write('%.12lf\n' % answer)
    return n


def func_94705492fc07421ea196f6c582c2bec5(ouf, inf):
    noc = int(inf.readline())
    for tnoc in xrange(1, noc + 1):
        ouf.write('Case #%d: ' % tnoc)
        print 'Case #%d: ' % tnoc
        n, p, q, r, s = map(int, inf.readline().strip().split(' '))
        aa = [((x * p + q) % r + s) for x in xrange(n)]
        a = [x for x in aa if x != 0]
        n = len(a)
        sum0 = [0] * (n + 1)
        sum1 = [0] * (n + 1)
        for i in xrange(n):
            sum0[i + 1] = sum0[i] + a[i]
        for i in xrange(n - 1, -1, -1):
            sum1[i] = sum1[i + 1] + a[i]
        allv = sum0[-1]
        bestAnswer = allv
        j = 0
        for i in xrange(n + 1):
            if sum0[i] >= allv:
                break
            ps = allv - sum0[i]
            j = max(j - 1, i)
            while j <= n:
                v1 = sum1[j]
                tmp = max(sum0[i], v1, ps - v1)
                if tmp < bestAnswer:
                    bestAnswer = tmp
                if float(v1) > ps / 2.0:
                    j += 1
                else:
                    break
        answer = 1.0 - float(bestAnswer) / float(allv)
        print '%.12lf' % answer
        ouf.write('%.12lf\n' % answer)
    return x


def func_ad84729e44284a8193f5ab00e5c42e9b(ouf, inf):
    noc = int(inf.readline())
    for tnoc in xrange(1, noc + 1):
        ouf.write('Case #%d: ' % tnoc)
        print 'Case #%d: ' % tnoc
        n, p, q, r, s = map(int, inf.readline().strip().split(' '))
        aa = [((x * p + q) % r + s) for x in xrange(n)]
        a = [x for x in aa if x != 0]
        n = len(a)
        sum0 = [0] * (n + 1)
        sum1 = [0] * (n + 1)
        for i in xrange(n):
            sum0[i + 1] = sum0[i] + a[i]
        for i in xrange(n - 1, -1, -1):
            sum1[i] = sum1[i + 1] + a[i]
        allv = sum0[-1]
        bestAnswer = allv
        j = 0
        for i in xrange(n + 1):
            if sum0[i] >= allv:
                break
            ps = allv - sum0[i]
            j = max(j - 1, i)
            while j <= n:
                v1 = sum1[j]
                tmp = max(sum0[i], v1, ps - v1)
                if tmp < bestAnswer:
                    bestAnswer = tmp
                if float(v1) > ps / 2.0:
                    j += 1
                else:
                    break
        answer = 1.0 - float(bestAnswer) / float(allv)
        print '%.12lf' % answer
        ouf.write('%.12lf\n' % answer)
    return v1


def func_788ba49943c647dd9a4c25237e935739(ouf, inf):
    noc = int(inf.readline())
    for tnoc in xrange(1, noc + 1):
        ouf.write('Case #%d: ' % tnoc)
        print 'Case #%d: ' % tnoc
        n, p, q, r, s = map(int, inf.readline().strip().split(' '))
        aa = [((x * p + q) % r + s) for x in xrange(n)]
        a = [x for x in aa if x != 0]
        n = len(a)
        sum0 = [0] * (n + 1)
        sum1 = [0] * (n + 1)
        for i in xrange(n):
            sum0[i + 1] = sum0[i] + a[i]
        for i in xrange(n - 1, -1, -1):
            sum1[i] = sum1[i + 1] + a[i]
        allv = sum0[-1]
        bestAnswer = allv
        j = 0
        for i in xrange(n + 1):
            if sum0[i] >= allv:
                break
            ps = allv - sum0[i]
            j = max(j - 1, i)
            while j <= n:
                v1 = sum1[j]
                tmp = max(sum0[i], v1, ps - v1)
                if tmp < bestAnswer:
                    bestAnswer = tmp
                if float(v1) > ps / 2.0:
                    j += 1
                else:
                    break
        answer = 1.0 - float(bestAnswer) / float(allv)
        print '%.12lf' % answer
        ouf.write('%.12lf\n' % answer)
    return aa


def func_a964c50b251843b2a8fcd0ab1aff5307(ouf, inf):
    noc = int(inf.readline())
    for tnoc in xrange(1, noc + 1):
        ouf.write('Case #%d: ' % tnoc)
        print 'Case #%d: ' % tnoc
        n, p, q, r, s = map(int, inf.readline().strip().split(' '))
        aa = [((x * p + q) % r + s) for x in xrange(n)]
        a = [x for x in aa if x != 0]
        n = len(a)
        sum0 = [0] * (n + 1)
        sum1 = [0] * (n + 1)
        for i in xrange(n):
            sum0[i + 1] = sum0[i] + a[i]
        for i in xrange(n - 1, -1, -1):
            sum1[i] = sum1[i + 1] + a[i]
        allv = sum0[-1]
        bestAnswer = allv
        j = 0
        for i in xrange(n + 1):
            if sum0[i] >= allv:
                break
            ps = allv - sum0[i]
            j = max(j - 1, i)
            while j <= n:
                v1 = sum1[j]
                tmp = max(sum0[i], v1, ps - v1)
                if tmp < bestAnswer:
                    bestAnswer = tmp
                if float(v1) > ps / 2.0:
                    j += 1
                else:
                    break
        answer = 1.0 - float(bestAnswer) / float(allv)
        print '%.12lf' % answer
        ouf.write('%.12lf\n' % answer)
    return bestAnswer


def func_cf44d815d7324af88e806f7f636c42bd(ouf, inf):
    noc = int(inf.readline())
    for tnoc in xrange(1, noc + 1):
        ouf.write('Case #%d: ' % tnoc)
        print 'Case #%d: ' % tnoc
        n, p, q, r, s = map(int, inf.readline().strip().split(' '))
        aa = [((x * p + q) % r + s) for x in xrange(n)]
        a = [x for x in aa if x != 0]
        n = len(a)
        sum0 = [0] * (n + 1)
        sum1 = [0] * (n + 1)
        for i in xrange(n):
            sum0[i + 1] = sum0[i] + a[i]
        for i in xrange(n - 1, -1, -1):
            sum1[i] = sum1[i + 1] + a[i]
        allv = sum0[-1]
        bestAnswer = allv
        j = 0
        for i in xrange(n + 1):
            if sum0[i] >= allv:
                break
            ps = allv - sum0[i]
            j = max(j - 1, i)
            while j <= n:
                v1 = sum1[j]
                tmp = max(sum0[i], v1, ps - v1)
                if tmp < bestAnswer:
                    bestAnswer = tmp
                if float(v1) > ps / 2.0:
                    j += 1
                else:
                    break
        answer = 1.0 - float(bestAnswer) / float(allv)
        print '%.12lf' % answer
        ouf.write('%.12lf\n' % answer)
    return i


def func_3bc8e6f003f24184bf894457bd9487ee(ouf, inf):
    noc = int(inf.readline())
    for tnoc in xrange(1, noc + 1):
        ouf.write('Case #%d: ' % tnoc)
        print 'Case #%d: ' % tnoc
        n, p, q, r, s = map(int, inf.readline().strip().split(' '))
        aa = [((x * p + q) % r + s) for x in xrange(n)]
        a = [x for x in aa if x != 0]
        n = len(a)
        sum0 = [0] * (n + 1)
        sum1 = [0] * (n + 1)
        for i in xrange(n):
            sum0[i + 1] = sum0[i] + a[i]
        for i in xrange(n - 1, -1, -1):
            sum1[i] = sum1[i + 1] + a[i]
        allv = sum0[-1]
        bestAnswer = allv
        j = 0
        for i in xrange(n + 1):
            if sum0[i] >= allv:
                break
            ps = allv - sum0[i]
            j = max(j - 1, i)
            while j <= n:
                v1 = sum1[j]
                tmp = max(sum0[i], v1, ps - v1)
                if tmp < bestAnswer:
                    bestAnswer = tmp
                if float(v1) > ps / 2.0:
                    j += 1
                else:
                    break
        answer = 1.0 - float(bestAnswer) / float(allv)
        print '%.12lf' % answer
        ouf.write('%.12lf\n' % answer)
    return j


def func_06ec545c9b2041779397bb48c42244c2(ouf, inf):
    noc = int(inf.readline())
    for tnoc in xrange(1, noc + 1):
        ouf.write('Case #%d: ' % tnoc)
        print 'Case #%d: ' % tnoc
        n, p, q, r, s = map(int, inf.readline().strip().split(' '))
        aa = [((x * p + q) % r + s) for x in xrange(n)]
        a = [x for x in aa if x != 0]
        n = len(a)
        sum0 = [0] * (n + 1)
        sum1 = [0] * (n + 1)
        for i in xrange(n):
            sum0[i + 1] = sum0[i] + a[i]
        for i in xrange(n - 1, -1, -1):
            sum1[i] = sum1[i + 1] + a[i]
        allv = sum0[-1]
        bestAnswer = allv
        j = 0
        for i in xrange(n + 1):
            if sum0[i] >= allv:
                break
            ps = allv - sum0[i]
            j = max(j - 1, i)
            while j <= n:
                v1 = sum1[j]
                tmp = max(sum0[i], v1, ps - v1)
                if tmp < bestAnswer:
                    bestAnswer = tmp
                if float(v1) > ps / 2.0:
                    j += 1
                else:
                    break
        answer = 1.0 - float(bestAnswer) / float(allv)
        print '%.12lf' % answer
        ouf.write('%.12lf\n' % answer)
    return noc


def func_4ab941dfc4f44034b39ddc019d504851(ouf, inf):
    noc = int(inf.readline())
    for tnoc in xrange(1, noc + 1):
        ouf.write('Case #%d: ' % tnoc)
        print 'Case #%d: ' % tnoc
        n, p, q, r, s = map(int, inf.readline().strip().split(' '))
        aa = [((x * p + q) % r + s) for x in xrange(n)]
        a = [x for x in aa if x != 0]
        n = len(a)
        sum0 = [0] * (n + 1)
        sum1 = [0] * (n + 1)
        for i in xrange(n):
            sum0[i + 1] = sum0[i] + a[i]
        for i in xrange(n - 1, -1, -1):
            sum1[i] = sum1[i + 1] + a[i]
        allv = sum0[-1]
        bestAnswer = allv
        j = 0
        for i in xrange(n + 1):
            if sum0[i] >= allv:
                break
            ps = allv - sum0[i]
            j = max(j - 1, i)
            while j <= n:
                v1 = sum1[j]
                tmp = max(sum0[i], v1, ps - v1)
                if tmp < bestAnswer:
                    bestAnswer = tmp
                if float(v1) > ps / 2.0:
                    j += 1
                else:
                    break
        answer = 1.0 - float(bestAnswer) / float(allv)
        print '%.12lf' % answer
        ouf.write('%.12lf\n' % answer)
    return s


def func_05267a31640d4cccbc1bb16f34806db5(ouf, inf):
    noc = int(inf.readline())
    for tnoc in xrange(1, noc + 1):
        ouf.write('Case #%d: ' % tnoc)
        print 'Case #%d: ' % tnoc
        n, p, q, r, s = map(int, inf.readline().strip().split(' '))
        aa = [((x * p + q) % r + s) for x in xrange(n)]
        a = [x for x in aa if x != 0]
        n = len(a)
        sum0 = [0] * (n + 1)
        sum1 = [0] * (n + 1)
        for i in xrange(n):
            sum0[i + 1] = sum0[i] + a[i]
        for i in xrange(n - 1, -1, -1):
            sum1[i] = sum1[i + 1] + a[i]
        allv = sum0[-1]
        bestAnswer = allv
        j = 0
        for i in xrange(n + 1):
            if sum0[i] >= allv:
                break
            ps = allv - sum0[i]
            j = max(j - 1, i)
            while j <= n:
                v1 = sum1[j]
                tmp = max(sum0[i], v1, ps - v1)
                if tmp < bestAnswer:
                    bestAnswer = tmp
                if float(v1) > ps / 2.0:
                    j += 1
                else:
                    break
        answer = 1.0 - float(bestAnswer) / float(allv)
        print '%.12lf' % answer
        ouf.write('%.12lf\n' % answer)
    return a


def func_c5851245b82e4ee3890e5a4b1c43810d(ouf, inf):
    noc = int(inf.readline())
    for tnoc in xrange(1, noc + 1):
        ouf.write('Case #%d: ' % tnoc)
        print 'Case #%d: ' % tnoc
        n, p, q, r, s = map(int, inf.readline().strip().split(' '))
        aa = [((x * p + q) % r + s) for x in xrange(n)]
        a = [x for x in aa if x != 0]
        n = len(a)
        sum0 = [0] * (n + 1)
        sum1 = [0] * (n + 1)
        for i in xrange(n):
            sum0[i + 1] = sum0[i] + a[i]
        for i in xrange(n - 1, -1, -1):
            sum1[i] = sum1[i + 1] + a[i]
        allv = sum0[-1]
        bestAnswer = allv
        j = 0
        for i in xrange(n + 1):
            if sum0[i] >= allv:
                break
            ps = allv - sum0[i]
            j = max(j - 1, i)
            while j <= n:
                v1 = sum1[j]
                tmp = max(sum0[i], v1, ps - v1)
                if tmp < bestAnswer:
                    bestAnswer = tmp
                if float(v1) > ps / 2.0:
                    j += 1
                else:
                    break
        answer = 1.0 - float(bestAnswer) / float(allv)
        print '%.12lf' % answer
        ouf.write('%.12lf\n' % answer)
    return p


def func_0d63871819cd46e397cfcb4b84293982(ouf, inf):
    noc = int(inf.readline())
    for tnoc in xrange(1, noc + 1):
        ouf.write('Case #%d: ' % tnoc)
        print 'Case #%d: ' % tnoc
        n, p, q, r, s = map(int, inf.readline().strip().split(' '))
        aa = [((x * p + q) % r + s) for x in xrange(n)]
        a = [x for x in aa if x != 0]
        n = len(a)
        sum0 = [0] * (n + 1)
        sum1 = [0] * (n + 1)
        for i in xrange(n):
            sum0[i + 1] = sum0[i] + a[i]
        for i in xrange(n - 1, -1, -1):
            sum1[i] = sum1[i + 1] + a[i]
        allv = sum0[-1]
        bestAnswer = allv
        j = 0
        for i in xrange(n + 1):
            if sum0[i] >= allv:
                break
            ps = allv - sum0[i]
            j = max(j - 1, i)
            while j <= n:
                v1 = sum1[j]
                tmp = max(sum0[i], v1, ps - v1)
                if tmp < bestAnswer:
                    bestAnswer = tmp
                if float(v1) > ps / 2.0:
                    j += 1
                else:
                    break
        answer = 1.0 - float(bestAnswer) / float(allv)
        print '%.12lf' % answer
        ouf.write('%.12lf\n' % answer)
    return ps


def func_3e5946c5cb344a2ab3bd1685f43513c4(ouf, inf):
    noc = int(inf.readline())
    for tnoc in xrange(1, noc + 1):
        ouf.write('Case #%d: ' % tnoc)
        print 'Case #%d: ' % tnoc
        n, p, q, r, s = map(int, inf.readline().strip().split(' '))
        aa = [((x * p + q) % r + s) for x in xrange(n)]
        a = [x for x in aa if x != 0]
        n = len(a)
        sum0 = [0] * (n + 1)
        sum1 = [0] * (n + 1)
        for i in xrange(n):
            sum0[i + 1] = sum0[i] + a[i]
        for i in xrange(n - 1, -1, -1):
            sum1[i] = sum1[i + 1] + a[i]
        allv = sum0[-1]
        bestAnswer = allv
        j = 0
        for i in xrange(n + 1):
            if sum0[i] >= allv:
                break
            ps = allv - sum0[i]
            j = max(j - 1, i)
            while j <= n:
                v1 = sum1[j]
                tmp = max(sum0[i], v1, ps - v1)
                if tmp < bestAnswer:
                    bestAnswer = tmp
                if float(v1) > ps / 2.0:
                    j += 1
                else:
                    break
        answer = 1.0 - float(bestAnswer) / float(allv)
        print '%.12lf' % answer
        ouf.write('%.12lf\n' % answer)
    return tmp


def func_7e986e899f894f8b899af104cfa87330(ouf, inf):
    noc = int(inf.readline())
    for tnoc in xrange(1, noc + 1):
        ouf.write('Case #%d: ' % tnoc)
        print 'Case #%d: ' % tnoc
        n, p, q, r, s = map(int, inf.readline().strip().split(' '))
        aa = [((x * p + q) % r + s) for x in xrange(n)]
        a = [x for x in aa if x != 0]
        n = len(a)
        sum0 = [0] * (n + 1)
        sum1 = [0] * (n + 1)
        for i in xrange(n):
            sum0[i + 1] = sum0[i] + a[i]
        for i in xrange(n - 1, -1, -1):
            sum1[i] = sum1[i + 1] + a[i]
        allv = sum0[-1]
        bestAnswer = allv
        j = 0
        for i in xrange(n + 1):
            if sum0[i] >= allv:
                break
            ps = allv - sum0[i]
            j = max(j - 1, i)
            while j <= n:
                v1 = sum1[j]
                tmp = max(sum0[i], v1, ps - v1)
                if tmp < bestAnswer:
                    bestAnswer = tmp
                if float(v1) > ps / 2.0:
                    j += 1
                else:
                    break
        answer = 1.0 - float(bestAnswer) / float(allv)
        print '%.12lf' % answer
        ouf.write('%.12lf\n' % answer)
    return answer


def func_50107e24869842e1ab5932a2dd303f94():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    return ofn


def func_1cb65c7313b0400085df336ac185f824():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    return ifn


def func_efd521eace5e49cbb84f876f1866af76():
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    return ofn


def func_6a8b5c66d42d4259a5f237e04f148f66(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return bestAnswer


def func_27fde57224e74f398a8b43af657938bb(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return n


def func_aefb2ea7c2054d7f850f160af7e043d8(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return tmp


def func_eb9a05953ba647cb85510f6b6161dbc4(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return aa


def func_30f8ef7d67ba491bb320825ecf5b9070(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return ouf


def func_6e3d49135a29435ab3643463395d7804(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return a


def func_327fd773bab349c78ab05fe9338ee4d3(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return p


def func_af7716c65ab64f4bbeacda772d88b2eb(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return i


def func_95dcdec5902b4fc59843460ca0ef3edc(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return inf


def func_2785c1c3553946c5a4a69ca8971031dc(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return answer


def func_0e7f5bbb9f2e4d4a8080754999525ea3(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return j


def func_6f1f4acedae04db1a3e9ec3f62953eee(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return q


def func_d93032d232774c369f2f0739799f0c87(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return x


def func_9855f079ceaa47ad8edc9938b0c6b15b(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return sum0


def func_fd907c3bc4e14cb8b17ead4d59687e3d(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return s


def func_f7d5e4e5a0d1400ca9788ff1c03cf9e4(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return noc


def func_3466191fca1744cfb0e319e3b9eb5e8c(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return ps


def func_928674202e014ac79c8f76a14ed9230c(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return r


def func_55f2d692aae54e19bcda9d69c9fdf8e2(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return tnoc


def func_2942d83424574e41bab4c26fcb76f0e9(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return sum1


def func_b26f5fb3b794409590738cfac9f37078(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return allv


def func_70cba03f06d44be5a7af4f15831c27a3(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return v1


def func_788eb9a35b0142bbb85690b75408e5b5(ifn, ofn):
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return n


def func_ebc61867fd3846a0a58758bbd8033205(ifn, ofn):
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return i


def func_dab8c5009b524f9ba793a57b4961a85e(ifn, ofn):
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return allv


def func_0ee0f8afa8c24befa99a97eb5fa094b5(ifn, ofn):
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return q


def func_8c7e4492410d417684d8368f893ebaff(ifn, ofn):
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return tnoc


def func_c79eeb75d48b4d80abafb22bdeeaf41c(ifn, ofn):
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return noc


def func_744b0f76d8d04aec9e24ba9a006b6386(ifn, ofn):
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return v1


def func_c79a55c28f6648a892db41d1db302192(ifn, ofn):
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return tmp


def func_4311c9edfcb741b5b97d1062de13c465(ifn, ofn):
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return answer


def func_9e052d57a2c645b2ad0c625691d3ac0f(ifn, ofn):
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return a


def func_4022b803fbb946338dd9e12f157dba98(ifn, ofn):
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return j


def func_968be4a8c88a4891a958eab189439b4a(ifn, ofn):
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return s


def func_b1208544b6fc4fd4a40132ab7372dc43(ifn, ofn):
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return ouf


def func_41d06cf49ef74b4a95f672286f59451f(ifn, ofn):
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return ps


def func_8690ce941e2948f7b9edb5d854f1a6ee(ifn, ofn):
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return inf


def func_22cc9453150344ff9adda33020c7eddb(ifn, ofn):
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return aa


def func_70b41dbc6dbf48c29fed546dbb308298(ifn, ofn):
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return sum0


def func_2ac4c259180849eabfa7285c0dd0828e(ifn, ofn):
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return x


def func_6c39015972914056b05a077872356a8b(ifn, ofn):
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return p


def func_9cd2159c4f9947e5ad62518a8fe5eb21(ifn, ofn):
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return r


def func_37211748a4a04ee3869f708b313eb5d1(ifn, ofn):
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return bestAnswer


def func_fb73cf162c884751b51a75d657845e42(ifn, ofn):
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return sum1


def func_e42652c2d5c9427d888974be2e452088():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    return ofn


def func_348a31f0f4df458ea3b629265eb1f770():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    return ifn


def func_2ba1ab990bee4f8f82c23034281a2132(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return q


def func_1ec3c9430ea04d439b5e0436c558f2a2(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return r


def func_555237381c774a019f5add6eabf2175a(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return noc


def func_e46dcb0b943c434d9a64c3b005f3ce24(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return ouf


def func_49f5e0c7887c4347a5f89ee421c8162e(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return a


def func_df6ca0e9c2834205b89deed0eb1e116d(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return bestAnswer


def func_c7da98a857394883b45bada9631f6fa7(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return ofn


def func_f9911c7e6f434f5dbd618207d2240e2d(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return v1


def func_2a62abbb441a4a55b8a46f95afb1629e(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return j


def func_52d11845241c48e4b61831566e955a6a(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return aa


def func_e688c849d3324c2cb9059272904490d5(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return sum1


def func_15ff9a63c4cd4921ba178c4c4d02b535(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return inf


def func_0a43252c255f498b86c85266764dbf4d(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return x


def func_3a6fabee87eb412eaa85d70e92f82ca4(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return ps


def func_b4be8e4c37ef489a94163ce7f6070408(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return i


def func_627793ddcdf841a1998e4859c7480829(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return allv


def func_b87f6985e4174ccca3ed148ef5be30f8(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return answer


def func_d7c372c8d85b4335b72453229b6f6783(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return sum0


def func_fab09c260e1d471fa34d53e7f686699f(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return p


def func_1c244e6749fb4e64a52bfb82bd870c61(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return tnoc


def func_bdd5283ba0ba4d169326f39d3a0a3c33(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return tmp


def func_cbfb9564454048fb85cce520a9fb0fc6(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return n


def func_3052157248c34db3a52e7b5ea71c24f7(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return s


def func_c47eb8ed200c4550b87c9a2302ba4fe2(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return v1


def func_db8c38a45b924051b507246c2e39568e(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return sum0


def func_e4e64cb7e6b242c88facd9c0524a28ff(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return ps


def func_fa92dcb8acfc4c25ad6cd237dad31e9e(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return inf


def func_1501b97c063d42fbafc1bb49bb4135d5(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return x


def func_367fde62d75643c694a4c8a2e0a076b6(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return sum1


def func_72d1beb13884470f86ed7ca5c8364bc4(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return j


def func_f7407e2ddf814bda98e07442bb4a1845(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return q


def func_6656a119c76f4e5f809bc2d01f2d1a12(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return noc


def func_15c20a3ec4ac4b56af16c17fc418fc0c(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return ouf


def func_9967b903d66d4b33b28c1593d058a973(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return s


def func_bb1d2cf1bfd94287904263601ec9d899(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return a


def func_e17467a7e6074d24940ba0da58a1269a(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return tnoc


def func_eebaa6b5418f4fc59f87746c3f3dc30d(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return n


def func_819e84878721491eaadd269a9e62b0d1(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return tmp


def func_8ba9fef8c8e94af28a3bc91fee473d39(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return r


def func_d3cdac165ea34367ba63ff84934de5a1(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return p


def func_47a6e53df8954921a7e70398e9156ad1(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return answer


def func_abe51c7dd8d64db0bfe0afb75a80a620(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return bestAnswer


def func_35ab7f37ed0e455aaab671bbeb4449af(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return allv


def func_167552bf7d1c4c4ca2d7e496a8f29d47(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return aa


def func_1e1e6bc8744e4d5e954c0b1524cd537b(ifn, ofn):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return i


def func_a1e71228497c4cf1adff18ec1f344d70():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return v1


def func_6cbc4c89406e4ec09262ef1ee2351bc6():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return allv


def func_b691a0dd5f5f45d18dff4b41fb2aa5ad():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return ouf


def func_f7249c751685485aa40e7682e24587f1():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return p


def func_d483c7b8957e45cea43e829954ca89c2():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return ps


def func_f29eec30872b4d77a94147b95b6c3461():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return i


def func_c28f7808cc5340a98479eff408ff4d21():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return tnoc


def func_e033430ee58143b98fa684d1635a20f9():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return bestAnswer


def func_d701f4f3db6d428da00f104fbc210443():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return sum0


def func_2aec5fd32b8f4d9d9f5f171879cc71ad():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return a


def func_efe0b0a7409649c39c5e175b98b5c433():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return ifn


def func_82f673c8f45544cd9b6e293fd6caa6b7():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return tmp


def func_83740ccbc3ce48b3bb11742bc1967dff():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return r


def func_0ca5f10099b5405e8a521de89772574b():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return x


def func_9a36941fe3e74b4aa43d337e9b8fe2e0():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return q


def func_8f3d17b7afb542f0af9774995108cf62():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return j


def func_cab326d645e2459d9a0236bcf2d80c77():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return s


def func_c622b09440084feeabf8315178ad61af():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return inf


def func_e19916faa55f46c08ab087792b4a367e():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return sum1


def func_814a786f93924b2a9e400ae6c129a812():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return aa


def func_02456ba0114a4704906819caa082fee4():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return ofn


def func_2f8834df28444355a0a01b4074986dfd():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return answer


def func_ae838bf256194c8f979d755fc191f419():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return noc


def func_5145d101abd04ee29f3f992a7fa2a5b0():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    return n


def func_247fba30384047338cfbbfec6e0c4efc(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return a


def func_da6dc6dcaed04123bdbc9bf743832d5f(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return v1


def func_0393286bb9ca49148459150f6e76eaf7(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return inf


def func_83a7e6a895d74c6eb437847188050670(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return s


def func_bc798ad9fdaf467c90949c7d35013e30(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return sum1


def func_551e5058e8e94a3789e084ecb7dffe3d(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return sum0


def func_c033f450c97144d59877ea3d45e804cf(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return noc


def func_aa0bf50262094cbe9c429754c42b106c(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return ps


def func_a1b18dd45d4a4c2b9973ed276a23ecb9(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return x


def func_acff33e08bf646bca48d89c74e099aa6(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return n


def func_853a2ec9a07e4f53b288e05818f08ccd(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return p


def func_aaee6decaae646079b60a134b22a28eb(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return i


def func_6c9e0878781d4ca9a96be97a2e413e2a(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return r


def func_1a652c6b46c24da9861d711b7da7a0b2(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return j


def func_87cf44ff64de42ea802dc9fc8181e31b(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return bestAnswer


def func_ac220ef64f0545d9b6554e3fcc810ed4(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return ouf


def func_f3aabaf3063d462d906fdb46dcad8fb5(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return tmp


def func_465aae1f5d8d4af5b482b32403994e29(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return ofn


def func_9b703fd78ebe44f19ceede166d6beed0(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return tnoc


def func_47b2551007024031a54ff3d798e64745(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return aa


def func_53aa7cb1c5254da2920d6d8f22ddb52c(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return q


def func_ea0a166769994d3b8d91c87b886a86ec(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return allv


def func_68baf3a04b4d4ee79138a0cba2198f06(ifn):
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return answer


def func_f3430b5b1a064ad8a90a879188f63947():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return tmp


def func_166efe02176140ff97063e9c86868905():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return v1


def func_1ac56c73208249038adcebc836afb015():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return sum1


def func_fa9c4fa86dd640119d4ed715faf456cf():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return bestAnswer


def func_1fd57506fd1a4b35acf8bba35025a7e7():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return x


def func_60d0f054a28c4a0eb2bbf8a834d7ebba():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return ofn


def func_1cdfbe489a6f4bdea6792f551f6fc8fc():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return ps


def func_2468feb4a2c74cecac74a91619e4f929():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return tnoc


def func_e92c7f7d481841488bb2207b5e7123b4():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return a


def func_f641ed287cb141de946d378888abf6b1():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return inf


def func_a0237e9417b44bbc96837f2bcbc834e3():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return q


def func_87012c2431104f49b16426e8717b669c():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return r


def func_f32ff8fe1c8642aead18eb959e6d54dd():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return allv


def func_5bca1d4aeca04fcd9586b9712fb1f4ed():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return noc


def func_b194671cd8484e04851254003cf6e38d():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return ifn


def func_9a9f20c7939a48f1b65461de2b7152ad():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return n


def func_efc5751c33e947c194ed32d3df281d88():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return s


def func_a5d4b9c668e24e79a4bf56e2cd3a9b8a():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return sum0


def func_6efc6591553c467bbb74d313917fccf6():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return ouf


def func_151dc80cc3ee450f936e08b2c69a5deb():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return aa


def func_22ad6de36e754983ad1fe58e17e3e27b():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return j


def func_0275663c1738495e91ce89a03ca0b68b():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return p


def func_11ab8032231d47c8a254f60dac3be02a():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return answer


def func_915511527e5444dd99a0fc362fe3aba5():
    ifn = 'test_files/Y14R5P1/A.in'
    ofn = 'test_files/Y14R5P1/A.out'
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn, 'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1, noc + 1):
                ouf.write('Case #%d: ' % tnoc)
                print 'Case #%d: ' % tnoc
                n, p, q, r, s = map(int, inf.readline().strip().split(' '))
                aa = [((x * p + q) % r + s) for x in xrange(n)]
                a = [x for x in aa if x != 0]
                n = len(a)
                sum0 = [0] * (n + 1)
                sum1 = [0] * (n + 1)
                for i in xrange(n):
                    sum0[i + 1] = sum0[i] + a[i]
                for i in xrange(n - 1, -1, -1):
                    sum1[i] = sum1[i + 1] + a[i]
                allv = sum0[-1]
                bestAnswer = allv
                j = 0
                for i in xrange(n + 1):
                    if sum0[i] >= allv:
                        break
                    ps = allv - sum0[i]
                    j = max(j - 1, i)
                    while j <= n:
                        v1 = sum1[j]
                        tmp = max(sum0[i], v1, ps - v1)
                        if tmp < bestAnswer:
                            bestAnswer = tmp
                        if float(v1) > ps / 2.0:
                            j += 1
                        else:
                            break
                answer = 1.0 - float(bestAnswer) / float(allv)
                print '%.12lf' % answer
                ouf.write('%.12lf\n' % answer)
    with open(ofn, 'w') as ouf:
        noc = int(inf.readline())
        for tnoc in xrange(1, noc + 1):
            ouf.write('Case #%d: ' % tnoc)
            print 'Case #%d: ' % tnoc
            n, p, q, r, s = map(int, inf.readline().strip().split(' '))
            aa = [((x * p + q) % r + s) for x in xrange(n)]
            a = [x for x in aa if x != 0]
            n = len(a)
            sum0 = [0] * (n + 1)
            sum1 = [0] * (n + 1)
            for i in xrange(n):
                sum0[i + 1] = sum0[i] + a[i]
            for i in xrange(n - 1, -1, -1):
                sum1[i] = sum1[i + 1] + a[i]
            allv = sum0[-1]
            bestAnswer = allv
            j = 0
            for i in xrange(n + 1):
                if sum0[i] >= allv:
                    break
                ps = allv - sum0[i]
                j = max(j - 1, i)
                while j <= n:
                    v1 = sum1[j]
                    tmp = max(sum0[i], v1, ps - v1)
                    if tmp < bestAnswer:
                        bestAnswer = tmp
                    if float(v1) > ps / 2.0:
                        j += 1
                    else:
                        break
            answer = 1.0 - float(bestAnswer) / float(allv)
            print '%.12lf' % answer
            ouf.write('%.12lf\n' % answer)
    return i

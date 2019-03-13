import sys
sys.path.append('/home/george2/Raise/ProgramRepair/CodeSeer/projects/src/main/python')
from Y14R5P1.kmod.a import *

def func_f2e9048a30bb4d57b9cba1ad5c24ea36(N, p, sums, total):
    needed = (1 - p) * total
    for i in xrange(N - 1, 0, -1):
        if sums[i] <= needed:
            break
    else:
        return False
    return needed


def func_b4f88e429f634b7fa0dde3accc3be9d7(N, p, sums, total):
    needed = (1 - p) * total
    for i in xrange(N - 1, 0, -1):
        if sums[i] <= needed:
            break
    else:
        return False
    return i


def func_950278540eba404aa9ab5a6d55680528(needed, sums, total, j):
    if total - sums[j + 1] <= needed:
        return True
    return False


def func_17be0a55b65d44b494fd4b9e968b7046(p, sums, total, N):
    needed = (1 - p) * total
    for i in xrange(N - 1, 0, -1):
        if sums[i] <= needed:
            break
    else:
        return False
    return i


def func_73ce7a1ca2a54251b6bb1b93c8eb0fdd(p, sums, total, N):
    needed = (1 - p) * total
    for i in xrange(N - 1, 0, -1):
        if sums[i] <= needed:
            break
    else:
        return False
    return needed


def func_d16021bb583e4e81abddde50aaf91cca(needed, i, sums, total):
    if total - sums[i] <= needed:
        return True
    return False


def func_67c03a0a7c9e482c86be05763e4a9119(i, transistors, sums):
    sums.append(t)
    t += transistors[i]
    return t


def func_e831239b16fe438ab73c44baea43624b():
    g = (low + high) * 0.5
    if can3(g) or can2(g):
        low = g
    else:
        high = g
    return low


def func_46e83c7c6f074d1d8512030839b954f5():
    g = (low + high) * 0.5
    if can3(g) or can2(g):
        low = g
    else:
        high = g
    return high


def func_223c8f15d7de4a1cad339bfb4a493d80():
    g = (low + high) * 0.5
    if can3(g) or can2(g):
        low = g
    else:
        high = g
    return g


def func_8c5621b0f9c64b06848c6643e4fc4830(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    return N


def func_1f09232c3e2b45fd9e06ec976b95dea1(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    return r


def func_bf4549ceb4784ab8b1d3c3aa70eff544(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    return q


def func_dd1d8e83f62d490c8eddf66fa9a98cc7(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    return transistors


def func_e6e290e4e278485b81b13d91fe7ea75b(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    return p


def func_076031b77573469c81d2b7eeb7f781b6(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    return i


def func_500420a79b6a4bb481ab5c8c7ba0d38a(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    return s


def func_2e6c74cd2c444cea9dc09f25bb0aa0bb(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    return i


def func_d04a1c3ac30841ba8d977e98d879078c(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    return transistors


def func_9008167b779d4ffcad47e4782a9244f2(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    return total


def func_73f0bbb727824422802b0161905d228d(transistors):
    total = sum(transistors)
    sums = []
    return sums


def func_42ba69ea24604bddbf989de31d8784e3(transistors):
    total = sum(transistors)
    sums = []
    return total


def func_d530bb5c019d44cea76fddab481bcee9():
    sums = []
    t = 0
    return sums


def func_ba16ca66f9f8479e98ebb3d482450660():
    sums = []
    t = 0
    return t


def func_9ee455e4a2e149a8916a85b23cd53007(N, transistors, sums):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    return i


def func_8550f8e589254e96afa8663a84f647fd(N, transistors, sums):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    return t


def func_6828e1de41ac4ac6a416ecbac3f75fde(N, transistors, sums):
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)
    return i


def func_5bbee9f240014fd58385c30d54db9818(N, transistors, sums):
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)
    return t


def func_213ced9b685f4c949d9cf3272ed61b46(N, sums, total):

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return i


def func_03f8eb9b31b64a65893babe13c48ece6(N, sums, total):

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return i


def func_0c7d6ed09c614f4e90147c647d057073(N, sums, total):

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return low


def func_e045c607483241da89ffb933e82933ad():
    low = 0.0
    high = 1.0
    return high


def func_815005d230db4a6197a7d4159dfbaa41():
    low = 0.0
    high = 1.0
    return low


def func_f647256238a24aa1a2f5c4c83d6c2431():
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return low


def func_d18f51b604a54ca4b7c1c9fcb22eb3f4():
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return i


def func_b9de5024a1a64dd3bdbbdc388d921f57():
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return high


def func_c07af56c194748e6b23c07ea4129cc8c():
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return g


def func_19b2bc528db34cc8937042c309ab6487(_T):
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return low


def func_ca07ae3a2c134b63aca8bbd07357b245(_T):
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return i


def func_23678f4cf1314d5587420baa1513f007(_T):
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return high


def func_774bb6b9e6124796b3f808343fcaf835(_T):
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return g


def func_a9ff04f9c64e4e32a14b4a35db7a5c48(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    return N


def func_739d1768e65a4bcf966516095bcb5367(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    return s


def func_7ea1860c8da849b0b1c7e0f80b9dabd4(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    return total


def func_07fb508d411e43829f9b654edea479e0(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    return transistors


def func_5b6ef9caa4634c51b93be1c87894fe58(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    return r


def func_dd2f6464e5d4472c8aecb0a805fdd1dd(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    return i


def func_5710589c428644e0badcba5c4f962f6b(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    return q


def func_e56c38484df64590a958ef6506da2421(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    return p


def func_2f18c02f15634bb1b4b8fefabc7d4a79(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    return i


def func_cff4ce68a3eb48a3bac9e298b4a9022d(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    return total


def func_d934b4abc87848dc933f47c5463fecdd(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    return transistors


def func_a7e107bfac0f4210b402f90622d366b0(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    return sums


def func_8720222c9a6645a3870a57ee02668c3b(transistors):
    total = sum(transistors)
    sums = []
    t = 0
    return sums


def func_def6229e546247e7822a7802cfea743d(transistors):
    total = sum(transistors)
    sums = []
    t = 0
    return t


def func_721374bb49b6444b8f2b83d968b3be75(transistors):
    total = sum(transistors)
    sums = []
    t = 0
    return total


def func_77153f093967430d9bf3bbf80ebc01f2(N, transistors):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    return sums


def func_6a6f5f35b1e649b6b8c64ff742c2e486(N, transistors):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    return t


def func_7246b94dceeb4f9389c27e8e798b621d(N, transistors):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    return i


def func_232d9c47ab014645ab9119a397f5874a(N, transistors, sums):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)
    return t


def func_7a72e8b16a6444ca8e7989799796018b(N, transistors, sums):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)
    return i


def func_18ed7f20b66044a78a63835835950f03(N, transistors, sums, total):
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)
    return i


def func_0e93e3504cc14f8b8f347f3e75d6fa4d(N, transistors, sums, total):
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)
    return t


def func_db8e91f4f5c248989fff917d9356bd37(N, sums, t, total):
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return i


def func_1313c5ebf7e94e51900033cbb66b194c(N, sums, total):

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return low


def func_0b555bce51694926a4572e3889d4974d(N, sums, total):

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return i


def func_9220f6daca7a49a6a9611188bfbe1d9a(N, sums, total):

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return low


def func_923b53def9c14227836ee6032cb52723(N, sums, total):

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return i


def func_553ed036dbde43759771aaeacea852c5(N, sums, total):

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return high


def func_757d8c207a2c4d1eb5cf95bd0d83a8e2():
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return g


def func_c237f993433a40a587748f2897041ce1():
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return low


def func_2c18588015834736a76356413cc1c7e0():
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return high


def func_5887cca7ee5e47baacd4fb4099d25e73():
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return i


def func_d586ba8f21c643e8832c254840157226(_T):
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return high


def func_290dccf6b7064c0f8555c1f824cab83a(_T):
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return low


def func_6a7e40b526d94e31b8d87ac5233b4fc9(_T):
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return i


def func_7761b5b95ec942b9867d03023b75f495(_T):
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return g


def func_916345ff75dc4fc2970fba1b8f752a2b(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    return N


def func_f626b952595e44f9ad2770e7d61a4ed1(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    return s


def func_722f139bfb1f4a88bbf2df630826f57e(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    return total


def func_a612480ff30742d8815b42c06d5d6c48(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    return transistors


def func_683b9997d9fb48a9a61ed2fbeb7dac1b(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    return r


def func_83734f0a72ce48179d95a361be02dda4(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    return i


def func_30116dd5cbc949f1bc790f4106763108(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    return sums


def func_30c795c02e10437da8a52ddfb8780056(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    return q


def func_58fbbf01ea27440bacf94d26bd1ee12a(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    return p


def func_a45e95ffc3c443e28c13dee964ea09fe(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    return total


def func_5b1d3dcc00914206bd1f61c019bae7ad(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    return transistors


def func_32a7ac2579d74950bcc9c0226f11b7d5(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    return t


def func_fe13ab0abdf24f71a500967ed68edbd9(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    return i


def func_5972758096e54dada12aa5c5f9413d15(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    return sums


def func_a979d1e88ca54848a7afd8ee177d9938(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    return t


def func_431e7dfbbb4e4dbd84501e06f40b318e(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    return sums


def func_3200f747c9314d98b86fc2f04df551b5(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    return total


def func_f156e89054104feb91656d213897198e(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    return i


def func_6cc922d4165f47d3891b463de93f4b1b(N, transistors):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)
    return sums


def func_2df969a6b3cd4f7f9c1158337afdde1a(N, transistors):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)
    return t


def func_f2f3f2508f2f4f88ba2314fc4df88fff(N, transistors):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)
    return i


def func_54bf4a285ca648c28409be617f815af4(N, transistors, sums, total):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)
    return i


def func_636011e10b2b45eba6c7f314b80e2353(N, transistors, sums, total):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)
    return t


def func_a98dc55151ee4c81add8d15867bef2df(N, transistors, sums, total):
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return i


def func_28d9248070674af59debfa610928c55e(N, transistors, sums, total):
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return t


def func_cebd71508bca4625b2d5b07eb0ac029a(N, sums, t, total):
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return i


def func_18dccc9aa2c24ada8f0fbdc87645b355(N, sums, total):

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return low


def func_cc914ad60ee94be2b5882f12cf0a0a94(N, sums, total):

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return i


def func_63b3a4cedbb442e0a844af16fcc9f383(N, sums, total):

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return high


def func_b3df0b478e8947019f89f579efa57066(N, sums, total):

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return g


def func_2fad288ea8694b1abe761f1dba8b4fa4(N, sums, total):

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return i


def func_96baee259f404ecd8eda934150336b57(N, sums, total):

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return high


def func_ac32e7481fe244f08d4e72c4a42110a3(N, sums, total):

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return low


def func_00023d4268cd49679d32d0028cfc895b(_T):
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return low


def func_353a95daca594f749b29ae35e32d6805(_T):
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return high


def func_a28a313ce5b446d1b1f1948fc734efe3(_T):
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return g


def func_0bffac17d175443c87c66e6798127a64(_T):
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return i


def func_b3dff63ca29147e5a38083c698bdddb3(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    return p


def func_44503af3ac3344bdbbe31000c17a8ae6(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    return i


def func_afc8c17a9c9645859ac1087d90ace900(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    return transistors


def func_7188c1233e4c4942a09a48be5803bd1c(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    return N


def func_24a16bacb9d8475fa97e41565f7859ad(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    return t


def func_5afc91bb62ab4c819720830def281f07(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    return q


def func_c533737dd8f04fc7954b64ada59e7598(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    return r


def func_7576b180fe3a4b67af41eac147d9891c(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    return s


def func_532cd346e4f445b4a0ee94655350a16c(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    return total


def func_107138b7683a4620b4d08c9c5cbc0347(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    return sums


def func_40b19f87096a49f99be36a0448ef0ce6(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    return t


def func_5232f6f3096a4ed0b47b9900c3a9d072(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    return transistors


def func_f55c0d6e5698478aa80e996058f18307(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    return total


def func_d6f1e6162db4402b9b47b7b0b1678d6b(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    return i


def func_e0514bfac02040b5b64575151a3664a8(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    return sums


def func_fa89fc5f522e499589a8b97c49850ce0(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)
    return t


def func_a113c897af1c443da8e82033c7a92260(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)
    return i


def func_88e3e7bedc9f437ca0fd41b24d959edb(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)
    return total


def func_24a164acc11841d7887212d7a08ce950(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)
    return sums


def func_2b26a487325244c8bcc66cb532ad9a62(N, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)
    return t


def func_5802e58848994c24a1400123a3a70ddc(N, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)
    return i


def func_d7486682b46c400a90c44475f31df285(N, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)
    return sums


def func_22b880c7a3604426b4a4ba2c74d7a55f(N, transistors, sums, total):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return i


def func_e59f08aedcb6496c93d179b151b105bb(N, transistors, sums, total):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return t


def func_3acb04f8a8454544a285fefa5aeefb91(N, transistors, sums, total):
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return i


def func_09131d8262ab4870b3c021b255ea94cd(N, transistors, sums, total):
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return t


def func_e8c55748191646bd8d9cdae7fca77021(N, sums, t, total):
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return low


def func_673d2beda43046178a0a67469d809774(N, sums, t, total):
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return i


def func_c854a98c64bf4694b0f996e96a4e5a4b(N, sums, total):

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return low


def func_5b8b4968b85744e6acbc99328888c1fa(N, sums, total):

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return high


def func_8d4f2b3fda6544f28fa1b45f03174667(N, sums, total):

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return g


def func_fb7e50aa5915413c8ee5e919d2a09a38(N, sums, total):

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return i


def func_ab09dbade9894a4c811f6738a8b1b844(N, _T, sums, total):

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return low


def func_12c068d7edcd45ec947994835a6ce5fd(N, _T, sums, total):

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return g


def func_1754fb0473994c75a85c4e92f5d5070d(N, _T, sums, total):

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return i


def func_07ed1d175be043eeb74339276c0a0b82(N, _T, sums, total):

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return high


def func_eb8f079ea9fe4534a859b51c1ca0d172(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    return N


def func_275b9c8c7eed4c1e8ef0b6aaf32c886d(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    return t


def func_f902d863381e43e485c54d0f69e21fed(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    return p


def func_eddaab61fca5418aa76dfe56f95d24be(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    return s


def func_cfdafc098ffb4df4917457c77b45f4fd(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    return i


def func_ba88ec5ee1254df7884b5186631d415f(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    return total


def func_3886f5d53bb54e2aa10a44d7f221ccd9(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    return sums


def func_bc689c3d1bfe4201bc856384d0bfccb9(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    return q


def func_e20c51a7ae4e4bd4bb5f2b13ba77e70d(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    return transistors


def func_155aa495319148c688e923ae41da913e(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    return r


def func_71bcfaac54704ef38189fa3984c1c9c5(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)
    return i


def func_90c274fec15240d5aff75998732abfbc(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)
    return total


def func_32e2642937424e318f4c8b0f0b1cbdc0(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)
    return t


def func_7a81763a340d4e72bc2ec5640baf5c17(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)
    return sums


def func_89321204b20a411a977ace1019f4b08c(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)
    return transistors


def func_54a26b0ebbdc41c68a80c8bd8c1ad255(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)
    return t


def func_97ea4dafb4a945d191bcc4a530136db9(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)
    return i


def func_aa4a1f3a653648df96cb59334f973009(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)
    return total


def func_7bb6b60e095a41e3a727848867d3bdd3(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)
    return sums


def func_c99ab0d07b50425fb6fbc94c272a187b(N, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return i


def func_895bdb5f3a104c1580b9c1fe61c27b4e(N, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return t


def func_197c3003347f40d79c9668bc535031c6(N, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return sums


def func_444315af7ac0494f87fa80c3546e878c(N, transistors, sums, total):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return i


def func_fcaf6c65c1974d87bbfff66d76924061(N, transistors, sums, total):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return t


def func_15ecded040f840d2993da2bed2215000(N, transistors, sums, total):
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return i


def func_6ff9b97a79484294a1503621cbb9fdaa(N, transistors, sums, total):
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return low


def func_6f16ea411467446485c2274d287afa75(N, transistors, sums, total):
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return t


def func_a0eb36fbbfe747ed9fe5f3d83d9d46ee(N, sums, t, total):
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return low


def func_8924d5ba3b874f9a97f441b48df777fe(N, sums, t, total):
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return i


def func_dc4b0a312f94407a9f59da3c75284a7c(N, sums, t, total):
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return high


def func_35c279a599784014b757c913c928b630(N, _T, sums, total):

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return i


def func_317decdd48324b819df8b1c3b08e3b22(N, _T, sums, total):

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return g


def func_2d72d3f68d5c44818f92d0c3ba821341(N, _T, sums, total):

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return low


def func_1c69a68b263141329db4f801db471375(N, _T, sums, total):

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return high


def func_9f3f2b3ef2c14683ba552ef8d0b79584(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)
    return p


def func_1daba1a708c548739e1d8c408f1043ca(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)
    return q


def func_7b8c294ae2934009b0309590e20f294b(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)
    return sums


def func_b5518c8e4d954696961c52d42869cb9f(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)
    return r


def func_06c01d00be89471395a2560c13cd679f(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)
    return transistors


def func_6b84b588b87f474b910f7f063f7a5d62(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)
    return s


def func_62fc4fa759ff402bac384a0ae27feda8(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)
    return i


def func_706fca2e9c7a4c42bece497bc5ffc978(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)
    return total


def func_e7e395f426e24b28bf032e943cd26f77(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)
    return t


def func_de41cb1256d84faa9ae9a9206064348b(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)
    return N


def func_9b31a08e9f424b2abf59cea13e74a0dc(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)
    return sums


def func_3f8b99a48a694a36bf534848a49e35f6(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)
    return t


def func_ef749bc7dc5c495cac097a184aafee83(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)
    return i


def func_f5b17b05521341e19d6de7c76a9cfa3c(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)
    return transistors


def func_198a83eed6b9472ab0bccc623e80c1d4(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)
    return total


def func_c5959606c09a4e54a0481006969729d7(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return sums


def func_448cf81fea8048de8544153399e3d4e4(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return i


def func_e39f34fedaa24b96820110f5fca3fd7a(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return total


def func_a790eb11f6534d239e6534f8b93d6df6(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return t


def func_44419de3e661461ca2b95819531b2ac1(N, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return sums


def func_737273929de84b51946b16581358f68c(N, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return i


def func_0b7689c762eb41b79bebbe869427b6f2(N, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return t


def func_314f9cfb399e4aa59efd75fa15d3e150(N, transistors, sums, total):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return i


def func_4234d92f3b884a6eb2d8a29be3b1f3c4(N, transistors, sums, total):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return t


def func_ba0e08b4344549a6aa21fa4481d68208(N, transistors, sums, total):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return low


def func_a02e0ef5276347b8b7cf0d09037edd15(N, transistors, sums, total):
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return low


def func_db1c0ae10ce740f6aa91aa07d4d19d6f(N, transistors, sums, total):
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return high


def func_87dff2615d704fe8a128c3983fbb2c9b(N, transistors, sums, total):
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return t


def func_a478e807fd0549b4a2cc8f67d3d875f8(N, transistors, sums, total):
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return i


def func_99519b71325a461bae728b1c905c352a(N, sums, t, total):
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return g


def func_41c20654d28a46bebe2afbab517d8e36(N, sums, t, total):
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return i


def func_cfd87fea760a468ea9c4fce203226cf8(N, sums, t, total):
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return low


def func_c4e6c7a63778450ca35cf751556084d1(N, sums, t, total):
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return high


def func_4b90037009804e339ba4a807a85f95b1(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)
    return q


def func_d96bb2e4163f43e3b3b2f6278a67ff38(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)
    return p


def func_8c88731d5bca4651a19ffe7015ef2b13(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)
    return i


def func_d772f88aa98a4385b2022699f0310f26(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)
    return sums


def func_becf6704db564e9fa9c43690ed494758(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)
    return s


def func_45d4c59bf64f4fef8aab154f9e2ba33f(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)
    return N


def func_3e335b58993246a188946ac9f882e695(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)
    return t


def func_b45364018f4f4d2db8cd4f569750192b(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)
    return transistors


def func_a4f74b39acc9439696f15a7dba22c55d(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)
    return r


def func_8fe7e6889eb84f07a6cf760517560b6e(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)
    return total


def func_c0f3340300e14e51a014b59a9bc8e808(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return total


def func_afba7e867b264205a94ba315354dd4ff(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return transistors


def func_1b9404662ccf4d6b87a4909f256bf913(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return t


def func_5aa781eab9564173805cde044dd08d54(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return sums


def func_85704098c50d4752bd8c1219cd75927d(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return i


def func_cb33bedcd6784c73b7e4dd3304c3f291(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return total


def func_e8a3e706602049c5b43f1b626962c867(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return t


def func_f4e74c5bd7ab43e5b2c2217714b6cc66(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return i


def func_a0ad955a8d034618875b1c89b6deae45(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return sums


def func_41d5d5d73e434b9697a0fe58ef36af0b(N, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return t


def func_7d74df7ceb12468b8d28260c34b0e45e(N, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return low


def func_48f8ed0cf4f24b49b1809b6bbde96f01(N, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return sums


def func_f4d2d87d032741349f462ede29962d1d(N, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return i


def func_700d39ade5aa459f98d2a362bf26b8a2(N, transistors, sums, total):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return low


def func_9fcbb02ea34240369c4880de50e7ff7f(N, transistors, sums, total):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return i


def func_102ac875308040a888c1c3871a5c261f(N, transistors, sums, total):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return t


def func_a250f678fd934decab5b3beb8064f442(N, transistors, sums, total):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return high


def func_28fb951b53f74751bd828f3a314b4177(N, transistors, sums, total):
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return t


def func_53b5274404b2428e9cf70918f8dd50e8(N, transistors, sums, total):
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return low


def func_c1d51955331e4134bccb01326a5b2a1b(N, transistors, sums, total):
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return i


def func_ba621a344f504b108e359aa836f55fba(N, transistors, sums, total):
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return g


def func_ce841cb4413c44c39efbc346edbe8b42(N, transistors, sums, total):
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return high


def func_ccccdff8e3784ea1b310c9a700e9a6ee(N, _T, sums, t, total):
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return low


def func_64e3f9027d21465ca42f8dedb8ef4ae9(N, _T, sums, t, total):
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return high


def func_0248b7333f284f2dbc8faaa9bad62ce0(N, _T, sums, t, total):
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return g


def func_78784f0237e84375a18a6bcb167d300d(N, _T, sums, t, total):
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return i


def func_f5c3c59866e24bf2b2efc45ca1df41e3(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return r


def func_1737ac79b9bd449990f6374d0ab04db3(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return sums


def func_2f7d71c57db64832ac45787a4f0c5d6f(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return transistors


def func_87c40d1745d54a5cb148301f7ca48393(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return t


def func_729e4ee5d59f4df6adb5a55c30973696(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return N


def func_cc27a4c27e4945ffa88dbf3760cf3c23(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return i


def func_d3ec6690fd604f0a9dd3829c0c24dc0d(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return s


def func_4dee6d3d0aea4e1c88ea2b95579a6f65(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return total


def func_27de583ee3584b548db996b629d84eb1(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return p


def func_2519e0dabb90430eb8fea7cd28d0e4ce(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False
    return q


def func_b7a9519b03be408e8f0fb4ede44dd7dd(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return total


def func_e09c3e9619c64029ba1266149e548287(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return i


def func_268efdb15abc428e811651f2e275d48c(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return t


def func_3848188ca8d9418e916a9e9f2756eaaf(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return sums


def func_9c28c4dbfac346e9860431997ee6f7fa(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return transistors


def func_55b90c71799a497a80e16f445c2bb813(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return total


def func_abae12d6ee1640579ca25cf81b34243a(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return i


def func_05db5b439c1e430faf6fbaa01b653f46(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return sums


def func_bec515a3aa2343979970254189bafc05(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return t


def func_47ad62cead2e4f73aff522faa4488e9f(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return low


def func_58eddff995144e0181205c0983393079(N, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return high


def func_fd6bccde82914176b26dae8e02192419(N, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return i


def func_fb71f2c1c6694f80a24a30e6bd3c869a(N, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return t


def func_c44a74a810d24e9f8004e6038fabfb31(N, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return sums


def func_6ddfc6bccd14405c9c2463c4072e5057(N, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return low


def func_4c950b6ae06a40fd82459cdf89b2a960(N, transistors, sums, total):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return high


def func_ab4530bd01834581b7bfb0631fd8c001(N, transistors, sums, total):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return i


def func_fc66c2237b664fa3bee11a3ea9ee9b6b(N, transistors, sums, total):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return g


def func_d69e58e04a184be5a6c355d617dbcb41(N, transistors, sums, total):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return low


def func_ddcadc1172e04ecbaa4d863692ba2065(N, transistors, sums, total):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return t


def func_0417c1bfb62e4ddb895b981543f823ee(N, _T, transistors, sums, total):
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return low


def func_61610c5fcdd447dba062589e7a3460c4(N, _T, transistors, sums, total):
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return i


def func_e2abd3a5f32d40dcbf2ccf882c91c068(N, _T, transistors, sums, total):
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return g


def func_d7ccc9126a92464a8e27ade13df9e6b0(N, _T, transistors, sums, total):
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return t


def func_5505ccc810814964805db82cdf586001(N, _T, transistors, sums, total):
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return high


def func_592d93ed032c42db853dffc7961e615a(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return t


def func_6bcfa74901994e47a72f0cf7e81d332b(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return total


def func_f0546dcd1fd6472a9546accbb830ceb9(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return transistors


def func_c789df0f3a51475d8aca0ce68f3a8c04(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return N


def func_4053758794dc46ffb5b6b701a1e52265(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return sums


def func_bc131c039055450fae4110c3c34b3daf(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return s


def func_8fe4e0c5ccb44bb2a0e0a338a40dee4c(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return q


def func_c2674b46c4cc40deba7810a4f117911d(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return r


def func_d6135b9535cc4208b49c97316647d1c2(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return i


def func_a95af946a8f046fca8343c6999cb3061(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    return p


def func_52e6f8a70b5940a5aa36b8c246707ec1(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return i


def func_5248f9d9087e477aae27a13e7a0920d5(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return low


def func_933423fd5d0848b4b0cba1b9d9a18d94(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return total


def func_19ae218fdaa74f7484be5f4ba54b6d30(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return sums


def func_209b75d493d34876aec6e35bee6adabc(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return t


def func_8ff9352344de40d8b2e200d64faf43f9(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return transistors


def func_73a1e9cf502d464da551b335f70a5309(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return low


def func_491038346738410ea775d0d56fce4509(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return total


def func_45635945dcb24a4883970606c7b19560(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return i


def func_72dbfc12ac434ed0a5777f390c0946a0(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return sums


def func_899ac934109246cf8002e77293cedd9d(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return high


def func_cf1dba23f5904130945bedbccb493943(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return t


def func_bf8210c8991e4ccbbed9e29f3c4c75a4(N, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return g


def func_4e84035626c44a55a6e406a14c453df6(N, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return low


def func_77923edff9a3491a8e4be68de23e6560(N, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return high


def func_142420fc0381422fb1f9e203a0eff259(N, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return t


def func_35253495dcd247c7a5d071c7f80e07ee(N, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return sums


def func_9a862420570e4cc9b85c35945ae86d57(N, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return i


def func_cd21fcad2b6b4154a77b291378ced2b7(N, _T, transistors, sums, total):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return i


def func_7101ce34b51c4ec3b17083c355c4e787(N, _T, transistors, sums, total):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return high


def func_4991c31ea39e4d4da294ce5afb4e6405(N, _T, transistors, sums, total):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return low


def func_ffb74b60076f40c0bdcf2836d0b75d5f(N, _T, transistors, sums, total):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return g


def func_8a858a43772f4c53916465ed9d8174d5(N, _T, transistors, sums, total):
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return t


def func_c5bf51851d444486bb6c6f65679eeece(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return t


def func_099133a239f04effa1b65d8ab4b53ff7(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return p


def func_1cd6dfd838804f08ac82fab8eb28562d(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return i


def func_c873552856144ab78a9e79f1e919ea90(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return q


def func_c8c057b209384cb690d2d880bb1ef2b2(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return low


def func_707346fb0b1e47fd9d01c61c9077d3ed(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return N


def func_737aa04f347b4b22b5db988b12c0a3d0(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return sums


def func_20182c5226ea48a19cfcdd8b7f798b2b(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return s


def func_89afd346eefc4682a8393d936596fddd(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return transistors


def func_8271c4a6e4d04a9585f2edf84e5761c3(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return r


def func_6f52eb0abd184a2abf3f9063c0316849(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    return total


def func_d2f109d9f47a47cb93890285d29163c7(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return i


def func_7bbb35128676454fbaa48b0416578eb0(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return total


def func_90060887ad7942f3a4aeb785fd9a67d9(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return t


def func_4555bf6b8d5b45dbb1dd38b8aa397bd9(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return sums


def func_9f299c109ddb42fe9df337c6750a63c4(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return transistors


def func_32df59dd0c8947748d7aaa351e939d8b(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return high


def func_32e265f732bd4c1cafd0de7db5662eed(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return low


def func_b89e4d6a039e4cb4908cdfc0a96b8fb2(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return low


def func_7875360d11014cd582a348b33b273aa8(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return i


def func_939c8b9db8ec40f0a6d476890ffd5661(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return high


def func_58099a53222e43a9ae02010e93258017(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return t


def func_03cc28bf86ec431394bd4837840a80b1(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return sums


def func_9d3c10d545114daa956780e3061c6e23(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return g


def func_3d49299dc3004a3a9ab4cc744a8bc3b6(N, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return total


def func_c14625b6c45649e390e86446d39e64de(N, _T, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return low


def func_3be11b7a16eb484d8f9f253a03ca14ad(N, _T, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return g


def func_84b4c17df803494b86564aec89723426(N, _T, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return i


def func_e60cabfbd90c4ec8afe374d834b72590(N, _T, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return sums


def func_0461cd42609f4e5099a942043e7406b2(N, _T, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return high


def func_4a9540fc812341d887dee3fff3d9abf6(N, _T, transistors, total):
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return t


def func_a995a6b1601d41c4af7213a107d9571d(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return total


def func_9e10e41a4c6a4b6b819a82b311537928(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return sums


def func_79af2ee43b5b416d8ffe892e468dbcbb(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return i


def func_5ce4b56523e34507b44d6ff9b6b5f229(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return transistors


def func_e4ccc92165b244d2a7dbaa1e47053148(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return q


def func_bf3fd880f88f414abc433327c13fb45e(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return N


def func_bc04976cc6ff47f28251ee51d8127a9d(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return r


def func_1e685d49250e4affa45ec1498c2dfb31(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return s


def func_5eb21083a26645808fa3de643dfef698(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return p


def func_a46e447ba8464a87812264436d027fc6(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return low


def func_f0c40fbf6de54d27ba69cc976e7c090b(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return t


def func_5f01fdd49ede47c5a6f649f4d697e775(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    return high


def func_aa56cff15b80458eb181338417c395a4(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return sums


def func_d7b54064ebc54b57a878900e12825c53(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return i


def func_14345da5342d4a35bd89701e07ff8b0f(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return transistors


def func_b3c59a2b7cde4e69b8c3fa290e1608d9(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return total


def func_f0ae085a462447a08c651cfb8876cfaa(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return t


def func_0494fdb03fed48dda584b2ca3690793b(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return low


def func_368178fcddd34c628e3410f84e51899b(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return high


def func_d8abc5f5ebd648b8aa389f165475f063(p, r, N, q, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return g


def func_db473563c8fc4b6db59747df5271753f(N, _T, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return sums


def func_d3c50c88c8544f5bb86d1adfa1d9e137(N, _T, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return total


def func_043b71cf39de4a82ac5ccf6ee65eccd4(N, _T, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return i


def func_488bdfff2ebc4cf59f6783bd355da12f(N, _T, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return t


def func_d610387401914c4083af196670802ba8(N, _T, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return low


def func_d9adce8018d74dc3bfabbaa0b4bd46d2(N, _T, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return high


def func_af8e5f9e60d3460dad40271667b885b4(N, _T, transistors):
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return g


def func_1e22ba66b7054ea1ab8fcdcdbdc607f1(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return g


def func_ac79f2d6e875474fa4cb8c0c4378b0b4(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return r


def func_f518284684354368b1a434097ad7830f(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return t


def func_854176f9baca479c8b00d18836744a3a(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return i


def func_1a0c8074d4f84a41a0c6e2594d935bd1(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return low


def func_85cd693fe0a247dfafd66dd3d93aa471(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return total


def func_83dbe1edfd234ca6ad6355a23ed5207a(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return p


def func_e091d67f5476407791f3006c9c5503f4(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return high


def func_0062502a4baf4200aa01c007b4ab9c05(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return s


def func_ae8836fe8c414d99ad9c581c70e7d3a6(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return N


def func_565638b775fc4dbca7103c875101d92e(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return q


def func_745a22d16f4645069a1020591abe2ef1(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return sums


def func_0d410c9ab2154ef69e16414f94362814(f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g
    return transistors


def func_cadbd0d94ce6447c8f0f91657d81fccf(p, r, N, q, _T, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return transistors


def func_f5f751a0ab0845ac82d177c832b5711c(p, r, N, q, _T, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return total


def func_2743f2b00ae9488a866adc4dfad2e2f1(p, r, N, q, _T, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return high


def func_250a2aa00f8d4c0a90865265f3f3f59a(p, r, N, q, _T, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return g


def func_285e071749934dcc87feddf380ac846a(p, r, N, q, _T, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return low


def func_3f9667aa2d5a42db9465b0352de25d72(p, r, N, q, _T, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return i


def func_bfe6582e1a074e7f9566ad0fb0c97298(p, r, N, q, _T, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return sums


def func_07bd68f170fc42a798b28632bda0a50b(p, r, N, q, _T, s):
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return t


def func_a8cf67d625914e8f955d8f81b466993f(_T, f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return low


def func_e56e801e65624b07b42bd4792f3a83d9(_T, f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return transistors


def func_8329c9c83b2d4cccb3852edd5d21e1a5(_T, f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return total


def func_21fc48b828ee429ead1bf56238123854(_T, f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return p


def func_648cd5eeb7dd42d49050c4b3a75c9c3b(_T, f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return high


def func_38015401d264458ba430b4ea2ba3e7b6(_T, f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return N


def func_63b42e8da9c94c61a3104131a8ea24a4(_T, f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return r


def func_d0f4cf211c1649db842c6c22cc926bc8(_T, f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return sums


def func_040a33732e8c4837b493ba8abc2cb62f(_T, f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return t


def func_87a04cafa7b94a3fa2216026c34f2559(_T, f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return g


def func_dddbd07caccc4dc5a275859237c39c8f(_T, f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return i


def func_b49b8ab214a248b0a7d06123999ff574(_T, f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return s


def func_a3647081d30f458bb735064c036b5249(_T, f):
    N, p, q, r, s = map(int, f.readline().split())
    transistors = [((i * p + q) % r + s) for i in xrange(N)]
    total = sum(transistors)
    sums = []
    t = 0
    for i in xrange(N):
        sums.append(t)
        t += transistors[i]
    sums.append(t)(t == total)

    def can3(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        for j in xrange(N - 1, i - 1, -1):
            if sums[j + 1] - sums[i] <= needed:
                break
        else:
            return False
        if total - sums[j + 1] <= needed:
            return True
        return False

    def can2(p):
        needed = (1 - p) * total
        for i in xrange(N - 1, 0, -1):
            if sums[i] <= needed:
                break
        else:
            return False
        if total - sums[i] <= needed:
            return True
        return False
    low = 0.0
    high = 1.0
    for i in xrange(40):
        g = (low + high) * 0.5
        if can3(g) or can2(g):
            low = g
        else:
            high = g('Case #%d: %.10f' % (_T + 1, low))
    return q


def func_eeaffa6ba2a040c0ac61d00ed96c6173():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    return f


def func_723577baf95d4a148dbf50916da3bea0():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    return T


def func_07271f4d5b104fbe87faa3b46a48493e(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return N


def func_6e3e74d8082142dbbbf41401a751f7bd(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return g


def func_0ea056c6065642c580aeca4a5f0f45d6(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return low


def func_22d50bc4a0b74fa998340ed29f3bdd12(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return t


def func_e15fe6608b294c0499db143e09ef39b0(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return s


def func_f432480877f7417687bb661ac26a249d(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return q


def func_7b45bf5cd0e448a98b4327ec818eccdb(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return high


def func_4931a50c39294270b0be2e3340b9aaad(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return r


def func_0b248f9567ac46d9b4feabf1b537cf83(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return _T


def func_c716a86d0c144f70879215c92b26ff9a(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return p


def func_aab1a6dc4a024278b355b4a1b0bcfc72(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return T


def func_f2a6ca1c65bf4f40a81829cdf41179f6(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return i


def func_3109ec7aaf0648f9a9b38860fa100f2c(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return total


def func_21b0d7f58d6349bca3a8a497b3837209(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return transistors


def func_7c2da7c6c32b4da49aa5bcc96a2c5b1a(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return sums


def func_58f023c32a7c4fc6a8446855ad19ca32(T, f):
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return q


def func_3921128d2589485ca51bc18f849690a0(T, f):
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return p


def func_fdfe355f57a64505b76f7ad01909453e(T, f):
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return total


def func_790035a0d12b4739a2242f2042b42de3(T, f):
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return g


def func_b3ba331c8dc94ac5a7762f27cf14bee3(T, f):
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return N


def func_71c368b303aa421883eb640fe772863d(T, f):
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return transistors


def func_9c3becca727a46cf8fedfea6f23b6b30(T, f):
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return i


def func_0771b1f949d044b69cb81cabafdaa038(T, f):
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return low


def func_6a0bef61e96b4b128e37b418295434b3(T, f):
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return r


def func_4f80d56676054c6fa5a35e463bb686f3(T, f):
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return s


def func_53d4e54b4e1e47668df79c75088eaec4(T, f):
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return _T


def func_65febc065c584cb483a106c79060417e(T, f):
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return high


def func_a6b836105f504aa59d22b95061f1f514(T, f):
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return sums


def func_379330cdaf5e4ff8813b1ca258400b6e(T, f):
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return t


def func_c547feda7bb340308043c1b9115561f4():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return t


def func_b061b574984f4694bb99e17e7656af75():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return high


def func_114636c3110d4c7ba5c7d9a735e2eac2():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return s


def func_cefb9af1bac04775b5860ae570f04d72():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return sums


def func_242ed4de7f5d45148fcc633bf9c53ef4():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return r


def func_ed9ef8c355d04f4c83dd0125cee84420():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return p


def func_845f617532fb450681a82e90f7ba736e():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return transistors


def func_4c90080b4a1d48c68f5e50d33f403e8d():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return q


def func_3a051ab13ff141a5b9705d6ca7a904ed():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return N


def func_e99eb3de608b47798b089c6607e30585():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return total


def func_43d220fe5e484585b711e7d5ce9a260b():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return _T


def func_e8068433c43249589c928a0880433af0():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return T


def func_0e88f835127e450db8bd1b8b812aedfb():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return low


def func_3e0f05f6965a4cdc9de324bf7fc75157():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return g


def func_cdfac37c60da41c3bd9e533eb2941833():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return f


def func_c18f73aa0b634175aff8723fd1d8afa2():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    return i


def func_2e8b66e37ffd4b9596da15a381453b74(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return sums


def func_11ea5cf5586d451a9cc4319192a6a6ad(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return high


def func_6799ff71329a45c1824b31f3ba7a8c63(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return t


def func_d1a0c4ef96fb497aa0a2b1314806c84d(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return i


def func_9e30a8015dfb492d834759ed14cded6e(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return low


def func_ab9a4337cc1445f48bdc6545587f90a0(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return T


def func_250a448e21b14f7f9265d8da32d6b7e6(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return r


def func_11579dfb7a4a472f9ad7e780738ff198(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return N


def func_d55ee79f498149648f8816a78ee05844(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return p


def func_9df9e7d2d07b45818ae23a4b70a4a9dc(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return transistors


def func_d233fe3f142743a69ea02b1d9c3596f4(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return s


def func_2253c43eeb8b4a318320945eb094e8f5(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return g


def func_035e5befbfb44c54bf63dc97a70e710c(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return q


def func_481418223ea2471495df4ae429b3f216(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return total


def func_43ef8324ba11453e8f0459282401d061(f):
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return _T


def func_a2c2b9c9cc524666bc7c43a3076550f4():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return i


def func_04ce46e477cc4967af767c96e5855274():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return low


def func_172cc9b2869d4c76bc3146a7564b1c5f():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return p


def func_799b34b00cd945d195c4989835fea6bb():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return s


def func_089aadb257aa47d1ab1438f009aac162():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return f


def func_e753bb3f7ea64b889871ccaf3c63ff76():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return sums


def func_7feb00abda964db48a15eb9aab54cdfe():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return _T


def func_63357f9673ea4fb3b90b1c293ec73574():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return high


def func_a0c267f86eea43a985b5b817364b264b():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return r


def func_25a6246053f54cc68ff50e0df2f37270():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return N


def func_efd4b8a745d143d78182df5046992619():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return transistors


def func_0ac9703dab8e4e548e6135ca9e85ef8c():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return t


def func_69c0364b23614087a2efe95f426e202e():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return total


def func_da8baf6d31b043908382c4259a4e8a71():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return T


def func_d696187c87eb4041b30d29a2b5428f1f():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return g


def func_3dd31426b6c3410782917e1abf8f2db8():
    f = open('test_files/Y14R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        N, p, q, r, s = map(int, f.readline().split())
        transistors = [((i * p + q) % r + s) for i in xrange(N)]
        total = sum(transistors)
        sums = []
        t = 0
        for i in xrange(N):
            sums.append(t)
            t += transistors[i]
        sums.append(t)
        assert t == total

        def can3(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            for j in xrange(N - 1, i - 1, -1):
                if sums[j + 1] - sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[j + 1] <= needed:
                return True
            return False

        def can2(p):
            needed = (1 - p) * total
            for i in xrange(N - 1, 0, -1):
                if sums[i] <= needed:
                    break
            else:
                return False
            if total - sums[i] <= needed:
                return True
            return False
        low = 0.0
        high = 1.0
        for i in xrange(40):
            g = (low + high) * 0.5
            if can3(g) or can2(g):
                low = g
            else:
                high = g
        print 'Case #%d: %.10f' % (_T + 1, low)
    f.close()
    return q

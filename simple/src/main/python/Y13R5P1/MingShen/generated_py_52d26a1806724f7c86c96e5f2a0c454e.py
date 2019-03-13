import sys
sys.path.append('/home/george2/Raise/ProgramRepair/CodeSeer/projects/src/main/python')
from Y13R5P1.MingShen.a import *

def func_2d4c2d98226c40b8bf514de3955cad0d(m, c):
    b = 0
    for i in range(c):
        b += m - Xs[i]
    return b


def func_9a6bf2b1fe4d4c508ef02df43ff41cee(m, c):
    b = 0
    for i in range(c):
        b += m - Xs[i]
    return i


def func_fa8868e04c0e415a9903d18bbdc4dd51(m, c):
    for i in range(c):
        b += m - Xs[i]
    gain = b
    return b


def func_0e9d63ea10a74aa28130e6d3b4f92743(m, c):
    for i in range(c):
        b += m - Xs[i]
    gain = b
    return gain


def func_918fcbdf6d2f430085215e802f94d220(m, c):
    for i in range(c):
        b += m - Xs[i]
    gain = b
    return i


def func_e2baf6440a714db6bd2191a39a771cd0(m, c):
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    return i


def func_6eca21bca12c476590975194c8e2b8b5(m, c):
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    return b


def func_a614a6ad80c1467e92afb6e55e0736b6(m, c):
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    return gain


def func_697bed7ecc904ba9abf318adb0234688(m, c):
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    return i


def func_c04fc46789bb447ab62f55a59a19299e(m, c):
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    return b


def func_4c2d2fabda2c4cb487efbea90acb1079(m, WRONG, i):
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    if b > B:
        return WRONG
    return b


def func_8740971f6a784f4eafdf6e3422c9f4ec(b, gain, WRONG, c):
    if b > B:
        return WRONG
    return 36 * gain / c - b


def func_91ad6b3ffbb84906bbdc090f84a2f037(m, c):
    b = 0
    for i in range(c):
        b += m - Xs[i]
    gain = b
    return b


def func_2b09c7fe0f604104ac45dc9acf306ec6(m, c):
    b = 0
    for i in range(c):
        b += m - Xs[i]
    gain = b
    return i


def func_1e4e89acef214fd98c3f67d32ef5df48(m, c):
    b = 0
    for i in range(c):
        b += m - Xs[i]
    gain = b
    return gain


def func_8293c464bb1a4a97ac04bb508eb89e48(m, c):
    for i in range(c):
        b += m - Xs[i]
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    return i


def func_189e33bd040b467b9948afd1e85090b4(m, c):
    for i in range(c):
        b += m - Xs[i]
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    return b


def func_c7a91734ac294fc09f3a5954ea086ad1(m, c):
    for i in range(c):
        b += m - Xs[i]
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    return gain


def func_bac4c440bf1748bebebaaeb12b9d15d6(m, c):
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    return gain


def func_b2bc338aacd94b01b54def479474085b(m, c):
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    return i


def func_aa610da1f2a04820bacae825c87b542d(m, c):
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    return b


def func_66c8b0ec13904732acf29c0ae7f9393a(m, WRONG, c):
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    if b > B:
        return WRONG
    return i


def func_199807575a574b1690dfce358095f8ca(m, WRONG, c):
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    if b > B:
        return WRONG
    return b


def func_588349d2bcf14065a3976a7a3e7d1191(m, gain, WRONG, i, c):
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    if b > B:
        return WRONG
    return 36 * gain / c - b


def func_c9c5bf8b9bea4d8bbe81dbca39324676(m, c):
    b = 0
    for i in range(c):
        b += m - Xs[i]
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    return i


def func_a3f68d86e5c04234b3ed8ffaf89237ee(m, c):
    b = 0
    for i in range(c):
        b += m - Xs[i]
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    return b


def func_cf05345ffacd426f82f0e263d3aa5c07(m, c):
    b = 0
    for i in range(c):
        b += m - Xs[i]
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    return gain


def func_a6e00057819a402994c2d59eeb9df192(m, c):
    for i in range(c):
        b += m - Xs[i]
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    return b


def func_3209bfac782d404c9bd7339c653b5051(m, c):
    for i in range(c):
        b += m - Xs[i]
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    return gain


def func_c3849453f00c46e48fcef96d4424713c(m, c):
    for i in range(c):
        b += m - Xs[i]
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    return i


def func_369726c893ad4d28acc6becf0db778bb(m, WRONG, c):
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    if b > B:
        return WRONG
    return b


def func_a2d057a5dfec4a7f95e275b502b6ca6c(m, WRONG, c):
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    if b > B:
        return WRONG
    return gain


def func_4c35ce71a7eb4f5b8d4dc6b283497402(m, WRONG, c):
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    if b > B:
        return WRONG
    return i


def func_206d954f210c4e29a8c8bb53e9ebc961(m, gain, WRONG, c):
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    if b > B:
        return WRONG
    return 36 * gain / c - b


def func_ec67f605e55848b0839273de2f4d1133(m, c):
    b = 0
    for i in range(c):
        b += m - Xs[i]
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    return b


def func_679ea72e334647db94992464288e5ac7(m, c):
    b = 0
    for i in range(c):
        b += m - Xs[i]
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    return i


def func_1a10af9c83d94bdab3c2421d828e0dfd(m, c):
    b = 0
    for i in range(c):
        b += m - Xs[i]
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    return gain


def func_5ee0a6887e5a4f2f84540a2e656abab0(m, WRONG, c):
    for i in range(c):
        b += m - Xs[i]
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    if b > B:
        return WRONG
    return b


def func_898337a49b2745b08bae7af75046a3e1(m, WRONG, c):
    for i in range(c):
        b += m - Xs[i]
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    if b > B:
        return WRONG
    return gain


def func_cae81ab60fc641ffadaadc166e498087(m, WRONG, c):
    for i in range(c):
        b += m - Xs[i]
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    if b > B:
        return WRONG
    return i


def func_4610285c169b416fa1b559e4fae1b13f(m, WRONG, c):
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    if b > B:
        return WRONG
    return 36 * gain / c - b


def func_43383728ac0e4ff093bc57bc0e6002ed(m, WRONG, c):
    b = 0
    for i in range(c):
        b += m - Xs[i]
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    if b > B:
        return WRONG
    return gain


def func_d6fef39d96ca4d83afab269827de2f34(m, WRONG, c):
    b = 0
    for i in range(c):
        b += m - Xs[i]
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    if b > B:
        return WRONG
    return b


def func_9e91df7e8b554cc0956ba7dffb9ff2e4(m, WRONG, c):
    b = 0
    for i in range(c):
        b += m - Xs[i]
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    if b > B:
        return WRONG
    return i


def func_25a6a9dbcfed4dc3bcc4aaf332b3f55b(m, WRONG, c):
    for i in range(c):
        b += m - Xs[i]
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    if b > B:
        return WRONG
    return 36 * gain / c - b


def func_a770aded047e451fa854461f0c757c2a(m, WRONG, c):
    b = 0
    for i in range(c):
        b += m - Xs[i]
    gain = b
    for i in range(c, len(Xs)):
        if Xs[i] <= m:
            b += m + 1 - Xs[i]
    if Xs[i] <= m:
        b += m + 1 - Xs[i]
    if b > B:
        return WRONG
    return 36 * gain / c - b


def func_6f53282591a945a49b2c89ab630a3ab8(l, m, ret, WRONG, i):
    ret2 = comp(i, m + 1)
    if ret2 is WRONG:
        r = m
    elif ret < ret2:
        l = m
    else:
        r = m
    return r


def func_09667d7c5f1448f096a3514710725cee(l, m, ret, WRONG, i):
    ret2 = comp(i, m + 1)
    if ret2 is WRONG:
        r = m
    elif ret < ret2:
        l = m
    else:
        r = m
    return ret2


def func_d70391a2502a4cebafeecf9911746d6b(r, l, i):
    m = (l + r) // 2
    ret = comp(i, m)
    return m


def func_a07d5f6f5de941a993c96e6f305d0591(r, l, i):
    m = (l + r) // 2
    ret = comp(i, m)
    return ret


def func_9aca902ceed54c93b6201770e472ffeb(B, Xs, i):
    l = max(1, Xs[i - 1]) - 1
    r = B + Xs[36] + 1
    return l


def func_cfee656373004312bc6cb291adf2a94c(B, Xs, i):
    l = max(1, Xs[i - 1]) - 1
    r = B + Xs[36] + 1
    return r


def func_74a06fa90cbb40e584dd1a694531fdd6(B, l, Xs, i):
    r = B + Xs[36] + 1
    while l + 1 < r:
        m = (l + r) // 2
        ret = comp(i, m)
        if ret is WRONG:
            r = m
        else:
            ans = max(ans, ret)
            if m + 1 == r:
                break
            ret2 = comp(i, m + 1)
            if ret2 is WRONG:
                r = m
            elif ret < ret2:
                l = m
            else:
                r = m
    return ret


def func_51b6c956125f40418aee150f10023a8b(B, l, Xs, i):
    r = B + Xs[36] + 1
    while l + 1 < r:
        m = (l + r) // 2
        ret = comp(i, m)
        if ret is WRONG:
            r = m
        else:
            ans = max(ans, ret)
            if m + 1 == r:
                break
            ret2 = comp(i, m + 1)
            if ret2 is WRONG:
                r = m
            elif ret < ret2:
                l = m
            else:
                r = m
    return m


def func_064cb5f84a924167ac92944eb518f040(B, l, Xs, i):
    r = B + Xs[36] + 1
    while l + 1 < r:
        m = (l + r) // 2
        ret = comp(i, m)
        if ret is WRONG:
            r = m
        else:
            ans = max(ans, ret)
            if m + 1 == r:
                break
            ret2 = comp(i, m + 1)
            if ret2 is WRONG:
                r = m
            elif ret < ret2:
                l = m
            else:
                r = m
    return ret2


def func_659a3d7a3c294ae6b6aff7ab4a247ce4(B, l, Xs, i):
    r = B + Xs[36] + 1
    while l + 1 < r:
        m = (l + r) // 2
        ret = comp(i, m)
        if ret is WRONG:
            r = m
        else:
            ans = max(ans, ret)
            if m + 1 == r:
                break
            ret2 = comp(i, m + 1)
            if ret2 is WRONG:
                r = m
            elif ret < ret2:
                l = m
            else:
                r = m
    return WRONG


def func_0328db00df06454db58ab0ad90523a92(B, l, Xs, i):
    r = B + Xs[36] + 1
    while l + 1 < r:
        m = (l + r) // 2
        ret = comp(i, m)
        if ret is WRONG:
            r = m
        else:
            ans = max(ans, ret)
            if m + 1 == r:
                break
            ret2 = comp(i, m + 1)
            if ret2 is WRONG:
                r = m
            elif ret < ret2:
                l = m
            else:
                r = m
    return ans


def func_ca04827960464da5a0031d92e312e74c(B, l, Xs, i):
    r = B + Xs[36] + 1
    while l + 1 < r:
        m = (l + r) // 2
        ret = comp(i, m)
        if ret is WRONG:
            r = m
        else:
            ans = max(ans, ret)
            if m + 1 == r:
                break
            ret2 = comp(i, m + 1)
            if ret2 is WRONG:
                r = m
            elif ret < ret2:
                l = m
            else:
                r = m
    return r


def func_445ec428f84048b6b7dc0c81953612b2(B, Xs, i):
    l = max(1, Xs[i - 1]) - 1
    r = B + Xs[36] + 1
    while l + 1 < r:
        m = (l + r) // 2
        ret = comp(i, m)
        if ret is WRONG:
            r = m
        else:
            ans = max(ans, ret)
            if m + 1 == r:
                break
            ret2 = comp(i, m + 1)
            if ret2 is WRONG:
                r = m
            elif ret < ret2:
                l = m
            else:
                r = m
    return ret2


def func_3c1131e8da124e0e8b8709d2fc350e42(B, Xs, i):
    l = max(1, Xs[i - 1]) - 1
    r = B + Xs[36] + 1
    while l + 1 < r:
        m = (l + r) // 2
        ret = comp(i, m)
        if ret is WRONG:
            r = m
        else:
            ans = max(ans, ret)
            if m + 1 == r:
                break
            ret2 = comp(i, m + 1)
            if ret2 is WRONG:
                r = m
            elif ret < ret2:
                l = m
            else:
                r = m
    return WRONG


def func_538780ebf9634a7ab563c45c994d376a(B, Xs, i):
    l = max(1, Xs[i - 1]) - 1
    r = B + Xs[36] + 1
    while l + 1 < r:
        m = (l + r) // 2
        ret = comp(i, m)
        if ret is WRONG:
            r = m
        else:
            ans = max(ans, ret)
            if m + 1 == r:
                break
            ret2 = comp(i, m + 1)
            if ret2 is WRONG:
                r = m
            elif ret < ret2:
                l = m
            else:
                r = m
    return m


def func_1232c1ccca5549c3b89e73310436238c(B, Xs, i):
    l = max(1, Xs[i - 1]) - 1
    r = B + Xs[36] + 1
    while l + 1 < r:
        m = (l + r) // 2
        ret = comp(i, m)
        if ret is WRONG:
            r = m
        else:
            ans = max(ans, ret)
            if m + 1 == r:
                break
            ret2 = comp(i, m + 1)
            if ret2 is WRONG:
                r = m
            elif ret < ret2:
                l = m
            else:
                r = m
    return l


def func_2f4650c1a3d549bc862617083ef13deb(B, Xs, i):
    l = max(1, Xs[i - 1]) - 1
    r = B + Xs[36] + 1
    while l + 1 < r:
        m = (l + r) // 2
        ret = comp(i, m)
        if ret is WRONG:
            r = m
        else:
            ans = max(ans, ret)
            if m + 1 == r:
                break
            ret2 = comp(i, m + 1)
            if ret2 is WRONG:
                r = m
            elif ret < ret2:
                l = m
            else:
                r = m
    return ans


def func_ef0b98ba88a94ffe894c786db68e98de(B, Xs, i):
    l = max(1, Xs[i - 1]) - 1
    r = B + Xs[36] + 1
    while l + 1 < r:
        m = (l + r) // 2
        ret = comp(i, m)
        if ret is WRONG:
            r = m
        else:
            ans = max(ans, ret)
            if m + 1 == r:
                break
            ret2 = comp(i, m + 1)
            if ret2 is WRONG:
                r = m
            elif ret < ret2:
                l = m
            else:
                r = m
    return r


def func_1d49afeee2cd4b6f9a51e6ac4fe5799f(B, Xs, i):
    l = max(1, Xs[i - 1]) - 1
    r = B + Xs[36] + 1
    while l + 1 < r:
        m = (l + r) // 2
        ret = comp(i, m)
        if ret is WRONG:
            r = m
        else:
            ans = max(ans, ret)
            if m + 1 == r:
                break
            ret2 = comp(i, m + 1)
            if ret2 is WRONG:
                r = m
            elif ret < ret2:
                l = m
            else:
                r = m
    return ret


def func_cac1a5b4484e4708bc440b30eed5e3c6(infile):
    global B, N, Xs
    B, N = map(int, infile.readline().split())
    return B


def func_53279d7c67804a3e9f57b101cc346070(infile):
    global B, N, Xs
    B, N = map(int, infile.readline().split())
    return N


def func_15dacd09cad84a7a9274ecf61e7c4357(infile):
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    return Xs


def func_406501120d4d4799b2f130fdd71a5ca2(infile):
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    return N


def func_629efab817954eaaacef94f2fc6bffe5(infile):
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    return B


def func_d4852e5145b54dc287f6ec3d2d8c38c4(N, infile):
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    return Xs


def func_dd6d7e5530cf4f5a849e41718422082d(N, infile):
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    return ans


def func_25b4d376dec14b0383a096e10fe48da9(B, Xs):
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return WRONG


def func_2853ae9c132a4964ad8ce6359bbc2b5f(B, Xs):
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return ans


def func_a65969cf76824269a9fb6b595b35739d(B, Xs):
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return ret


def func_fe944a8caba84155b7a630378bf1b688(B, Xs):
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return l


def func_a7b02f324c834db69d4b4da6102f4ac1(B, Xs):
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return i


def func_e9d511b50e9c4749824694f707a77dce(B, Xs):
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return r


def func_e293af8168db41d1b91dbae1a030a3d9(B, Xs):
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return ret2


def func_3bb25d15b5074a6e9dad29cc6fa055d5(B, Xs):
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return m


def func_6b0054ca291c44beb5449ac3bf2e66aa(B, Xs):
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return ans


def func_6c6cdc3097b64bb98ac38ce86d47e62b(infile):
    global B, N, Xs
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    return N


def func_f2f82012a51148ea838d2dfc88390015(infile):
    global B, N, Xs
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    return B


def func_fbd3beaf5a4943f3a225977292143503(infile):
    global B, N, Xs
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    return Xs


def func_8156f35bfaf3458c9d1c3ca9395d798d(infile):
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    return B


def func_d15b509749d843beaad39b8e43c67e71(infile):
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    return N


def func_741768af82c646fa913c7f2ab3da6fe3(infile):
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    return Xs


def func_b6542dcd11934ea58e4c79be33ac1f7d(infile):
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    return ans


def func_abe2de6fc5f348f884f0257c3b4bfdd5(B, N, infile):
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return m


def func_95036cddf487429cba08d07121a675f4(B, N, infile):
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return ret


def func_c75db0dcc39e4b9082ead8ead6e622fa(B, N, infile):
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return ret2


def func_d338591e0c464345bc5012958fad7feb(B, N, infile):
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return r


def func_3dcb7c6a008345159f8361cfb0a4bbb4(B, N, infile):
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return Xs


def func_c9edfe6843f0452787a73862122dc4fe(B, N, infile):
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return i


def func_81e65db61bde4d09b3b1550e42deef93(B, N, infile):
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return l


def func_c131a7ea51664bdeb0dc837508df5e7f(B, N, infile):
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return WRONG


def func_a0e025fe592e4a6eb1714d58e4cc39c8(B, N, infile):
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return ans


def func_37bbb8a56f044502bf36633e980b1f5f(B, Xs):
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return ans


def func_6e409dd2234f49eaaafa86a877bd59e7(infile):
    global B, N, Xs
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    return Xs


def func_141eb8498b524cbc9e100d63c84891cc(infile):
    global B, N, Xs
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    return ans


def func_13290adbaabf45ae9cfe723de1cf1bbe(infile):
    global B, N, Xs
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    return N


def func_0b9ddd3d296a46b7b5dcd295a3ca6ac0(infile):
    global B, N, Xs
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    return B


def func_7c97286ec26e46ecb7bd3de4ff59032c(infile):
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return m


def func_87320e0b6b2a40e8943f1cce5c6dca37(infile):
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return ret


def func_dc793ab0ecf74ec499e243064fc6d389(infile):
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return ans


def func_4f39bc495c56447599673d1ed119bba8(infile):
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return r


def func_8c1f335e5313400cacbb1c6934ac45cc(infile):
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return WRONG


def func_0deb7af1cc67416988b545d395180eff(infile):
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return N


def func_7c55a730e8b444078532e9f0658acfe4(infile):
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return Xs


def func_ff9a40ae62aa47a1a0e780ac42fe398b(infile):
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return i


def func_5e65e0fcf1a949f696cabdb04928ec09(infile):
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return l


def func_d2818a7c7f6e4a22a0bb4717c11c406e(infile):
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return ret2


def func_7cfad65e5b3f44c19a5bfba10495e43e(infile):
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return B


def func_7596e25169f84d98b4c425fdbe408191(B, N, infile):
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return ans


def func_4dc7a5dbd7384bafb57ff50d256492a5(infile):
    global B, N, Xs
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return N


def func_0187abcf4aa34593a497fb4010fb4778(infile):
    global B, N, Xs
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return B


def func_926869432c614e358b1cae46a292ef90(infile):
    global B, N, Xs
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return ans


def func_1b3c0bcf16354842a52e73e05b53b523(infile):
    global B, N, Xs
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return ret2


def func_b246c798aa7b40bca8c619f13fe9655e(infile):
    global B, N, Xs
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return WRONG


def func_21d5534e9ccd45b0a0686d42e3dbb323(infile):
    global B, N, Xs
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return m


def func_a03112ee41ca4b7f8b9448e54be39fd9(infile):
    global B, N, Xs
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return Xs


def func_e90ad07046424fb7a8d97e7d760d4b67(infile):
    global B, N, Xs
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return ret


def func_982e09a8721240dba55bdf7edb3d77fc(infile):
    global B, N, Xs
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return i


def func_5c2d156ff6094bffb231c727a2976fd9(infile):
    global B, N, Xs
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return r


def func_1c6eca0636414a54859b7f99a9387d41(infile):
    global B, N, Xs
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return l


def func_3bc3c4b1986c4dd38c83b1b8a7f41ff8(infile):
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return ans


def func_38fde33c37a24d9fa8549f50873eef52(infile):
    global B, N, Xs
    B, N = map(int, infile.readline().split())
    Xs = sorted([0] * (37 - N) + list(map(int, infile.readline().split())))
    ans = 0
    for i in range(1, 38):
        l = max(1, Xs[i - 1]) - 1
        r = B + Xs[36] + 1
        while l + 1 < r:
            m = (l + r) // 2
            ret = comp(i, m)
            if ret is WRONG:
                r = m
            else:
                ans = max(ans, ret)
                if m + 1 == r:
                    break
                ret2 = comp(i, m + 1)
                if ret2 is WRONG:
                    r = m
                elif ret < ret2:
                    l = m
                else:
                    r = m
    return ans


def func_676bb681a231474b94a32be26a48ec78():
    infile = open('test_files/Y13R5P1/A.in')
    T = int(infile.readline())
    return infile


def func_4d673981c6e54200b5af542705b53738():
    infile = open('test_files/Y13R5P1/A.in')
    T = int(infile.readline())
    return T


def func_2e03886e95524816b1e73253162babd0(infile):
    T = int(infile.readline())
    for tn in range(T):
        print 'Case #{0}: {1:.10f}'.format(tn + 1, solve(infile))
    return T


def func_e59ffad14eac4683b691c9e67dbb897c(infile):
    T = int(infile.readline())
    for tn in range(T):
        print 'Case #{0}: {1:.10f}'.format(tn + 1, solve(infile))
    return tn


def func_7203cc6fd8b540aea1b026456870d909(T, infile):
    for tn in range(T):
        print 'Case #{0}: {1:.10f}'.format(tn + 1, solve(infile))
    infile.close()
    return tn


def func_daea928ec6f845d78894f1f72a35d2fb():
    infile = open('test_files/Y13R5P1/A.in')
    T = int(infile.readline())
    for tn in range(T):
        print 'Case #{0}: {1:.10f}'.format(tn + 1, solve(infile))
    return infile


def func_96923b01f8db49a1a18fcfbf1a77b48a():
    infile = open('test_files/Y13R5P1/A.in')
    T = int(infile.readline())
    for tn in range(T):
        print 'Case #{0}: {1:.10f}'.format(tn + 1, solve(infile))
    return tn


def func_97f45be8a742493a8dbfdb7472a45409():
    infile = open('test_files/Y13R5P1/A.in')
    T = int(infile.readline())
    for tn in range(T):
        print 'Case #{0}: {1:.10f}'.format(tn + 1, solve(infile))
    return T


def func_b5e82dbf9c19427e94c3c1841f65e27d(infile):
    T = int(infile.readline())
    for tn in range(T):
        print 'Case #{0}: {1:.10f}'.format(tn + 1, solve(infile))
    infile.close()
    return tn


def func_2a329c0b1090472ab56425ca6f40907a(infile):
    T = int(infile.readline())
    for tn in range(T):
        print 'Case #{0}: {1:.10f}'.format(tn + 1, solve(infile))
    infile.close()
    return T


def func_b666723e2e644010b13a77ccd2effb71():
    infile = open('test_files/Y13R5P1/A.in')
    T = int(infile.readline())
    for tn in range(T):
        print 'Case #{0}: {1:.10f}'.format(tn + 1, solve(infile))
    infile.close()
    return infile


def func_4ae906360d63477ab18301ec271c4918():
    infile = open('test_files/Y13R5P1/A.in')
    T = int(infile.readline())
    for tn in range(T):
        print 'Case #{0}: {1:.10f}'.format(tn + 1, solve(infile))
    infile.close()
    return tn


def func_7a095c880dd04bbc88bb63e39070b0ce():
    infile = open('test_files/Y13R5P1/A.in')
    T = int(infile.readline())
    for tn in range(T):
        print 'Case #{0}: {1:.10f}'.format(tn + 1, solve(infile))
    infile.close()
    return T

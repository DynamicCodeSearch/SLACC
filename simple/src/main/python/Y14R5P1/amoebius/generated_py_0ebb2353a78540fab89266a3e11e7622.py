import sys
sys.path.append('/home/george2/Raise/ProgramRepair/CodeSeer/projects/src/main/python')
from Y14R5P1.amoebius.A import *

def func_bede9a6954a047ee86a680e57818652b(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    return t


def func_0298a342b71c4d5f99bcb4392d6521a7(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    return q


def func_0594901868bb41b18a6ae65567bd78cb(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    return i


def func_c80468bb892542fe8aba8b9c0e5cd432(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    return s


def func_e7e35578b0a54aba9639fd47b3917f55(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    return r


def func_561f8db8c1a64c2eb560d63b737e4a26(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    return N


def func_a3700d5e7ed54a45942b98f5e7f586be(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    return p


def func_84475cf441244a1a89010ba0363e1808(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    return t


def func_2bfaafcf75474ea5b8bc0d00d4dbe54d(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    return i


def func_2a6e47758e3442e3b226d7c330d3f48c(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    return total


def func_8328426d57a34863a8e0d6d227cd3c27(t):
    total = sum(t)
    c = [0]
    return total


def func_80d8f372e0d348e087ec4de55384b0ef(t):
    total = sum(t)
    c = [0]
    return c


def func_48fff3f7b29b40cdb17e537cc8764bbc(t):
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    return x


def func_5efcf8feb4684f118cf6fbb4d3d8e287(t):
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    return c


def func_d9a8029f4e544790b181b9a5e014e36f(t, c):
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return b


def func_f2f02ba660f44fef99d25315a446f105(t, c):
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return a


def func_3fc0c3f6f2294a0d9bbd3d141f7f80cc(t, c):
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return x


def func_4c5b64bc4a3147aa8d28d3175f678012():
    a = b = 0
    best = 0
    return b


def func_867a51606e454879b845d244fd40052c():
    a = b = 0
    best = 0
    return best


def func_61de3e4927e34278a3d19fe76db50da2():
    a = b = 0
    best = 0
    return a


def func_2065e89b61a649648fd7b1132e00eded(c, total, N):
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return a


def func_8b874bb0e15a4ec2844ac1559ce6249b(c, total, N):
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return b


def func_f7f72b1eb6084a8fa7d59d9e14a838fe(c, total, N):
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return best


def func_ea923f3f0eed405699beb1acba9f41cb(c, total, testCase, N):
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return a


def func_9ab1302e50b1452d8d5f6a826e139b26(c, total, testCase, N):
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return best


def func_2ac792c1fb53493abf9bf7026d0ff150(c, total, testCase, N):
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return b


def func_a35941883da1477eb3cf4649a86af725(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    return t


def func_03db7171dfda441bae61d925e2905d27(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    return p


def func_3ca563b2ae1d4a3ab4fec92b9ea264e4(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    return i


def func_a0e6508fd7fd480c962b1e6c5ec2c201(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    return N


def func_bcb4f9b7569c470e9d7aad5172c761cd(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    return s


def func_be80d0874dfa4a33b7ecba74cfd74bfa(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    return q


def func_9c81c6d29e1e444fa60c660f48df8191(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    return r


def func_2b6c2e42179e4f28863ec4d9bc15c92e(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    return total


def func_a53667646f06471ca0c7cfce22e8fc8c(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    return total


def func_0ef65e50ed9e4b1781aead609d82e0fd(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    return t


def func_ff3e6f1e51604390b70d9a7199c14b2f(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    return c


def func_befc7d6945494a30ae1171c0ea93ad9a(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    return i


def func_f0c341a89cd24da7a7ffa1ffb840ad02(t):
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    return x


def func_f7402311ae2a42afb047fd8e02c9f097(t):
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    return total


def func_9eaab0a45d8540d681f930c80c335c07(t):
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    return c


def func_4123f3968419431f812510253e4285d0(t):
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return b


def func_0f777cc89b5d4165bbb5fabcceccf6a7(t):
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return c


def func_7ddf3af8a07443b19442854eb9fac0fc(t):
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return a


def func_6c252ca9523b49c199d63982cefaa0c6(t):
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return x


def func_f3fb8821acfb401286ccb5c41bef1401(t, c):
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return a


def func_a9929a9c86da4148acacf463ba5245d1(t, c):
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return b


def func_534c6bd14a5945c38163cc04e1a6e5e8(t, c):
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return x


def func_b839f92fbce04a11a473e0cc5b0bb358(t, c):
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return best


def func_61c1a42db83849ddac9012b547cba973(c, total, N):
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return best


def func_c5acc87e47244b0485b955c3c7e28981(c, total, N):
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return b


def func_220384a73f3c4e18b01b08c94acd70fc(c, total, N):
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return a


def func_4b9a92e3cfea42bf81c123dd4430c90b(c, total, testCase, N):
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return best


def func_785eec469e0642a3bd44dd19b25626fb(c, total, testCase, N):
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return b


def func_64681edadfc24f0684fb104b1ec3b4c6(c, total, testCase, N):
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return a


def func_c3baf861a1ce4aa59665fd23b7460557(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    return q


def func_c735b1c276ac490cbb552af404770dfc(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    return total


def func_c1971fd37eaf42a1a9d0882f75c4d516(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    return N


def func_4079d39705134532afbfe8a9ee2b607e(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    return s


def func_67a244bfee39497083daac9ceb81df5b(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    return i


def func_f174e2d5100c40058b609f0cea80aadc(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    return p


def func_8dc3710d25ed4c44ac153b8154758949(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    return c


def func_eab1bdb22205476191bb000e072928c6(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    return r


def func_97f31c8620764357a2d5468ce7d4799e(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    return t


def func_b123470462bf402c85012735dd814778(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    return t


def func_8b217b67e845416bbfac752909a3e70a(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    return i


def func_cbe5937b716b4277b5326363a2c060f6(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    return x


def func_a9c9f1ed70a24a5896a3a9da05441e4c(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    return c


def func_c3d69ca0fd8a45098910af4e3fbf958d(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    return total


def func_73eb9647c9334e16997c1fab6b1088d3(t):
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return total


def func_b9d3bd1b42c7436399d47ff3442d4a8c(t):
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return x


def func_b9b06d7b67aa449c95d3277dfdaf6138(t):
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return a


def func_bb6a22d076e3471eaae962ad56e644da(t):
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return c


def func_9c86555699b14a97a39847862020b0ee(t):
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return b


def func_9640139a53a1495cace752aefa522be5(t):
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return a


def func_c579de5ca7e7452b812332ef737bd893(t):
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return best


def func_21f1d4365f454f1fbf76eb25146fd1ed(t):
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return b


def func_b6c3f619862c47e88654e1cbe99f50c3(t):
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return x


def func_caccb2df0a024a0badfc3b86d6e44db5(t):
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return c


def func_69deb2525aba418aad68e4d9efb9e2b9(t, c, total, N):
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return x


def func_3b572e53d9ff4107b7384b7abc0411a2(t, c, total, N):
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return b


def func_322f3105c40b40b8b3e89f04748008d5(t, c, total, N):
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return a


def func_18bc19c070bd4238b043c32df10299bc(t, c, total, N):
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return best


def func_af256d2d83fa49428787c3bb4b10bfed(c, total, testCase, N):
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return b


def func_1d30510261584c4fb187a7aed5f829ed(c, total, testCase, N):
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return best


def func_b816490620dc423bb7dd19e4b850c973(c, total, testCase, N):
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return a


def func_84492f57c68940e5a38e8f3ed194a55b(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    return p


def func_9d033b3e5fbf4574b00826e47721b5e5(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    return c


def func_3420ba92b14f4683a73deaf5cdb21f0e(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    return i


def func_c8d6d06b803e47dcbcfc2efddab40514(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    return s


def func_6f58a032975d46df9e7341550b0fdd29(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    return total


def func_740192225dc54f409be2db29cde724b3(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    return N


def func_dcf056a9d2ac4b248432ee15eb3aaf77(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    return t


def func_a6cb9bbaff424aff83a223bec5f92375(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    return q


def func_0627a8dd664f4356ad6ea74bf5e2440d(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    return r


def func_c3173460cb6948ff9b06533755a3d407(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    return x


def func_f7846e1f2fcc48929bb0aea15cdb7b88(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return i


def func_02c135412fff44c290735a3b2504516a(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return total


def func_ad67063aebce443ebf92f3759dcf360a(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return b


def func_421b36c83fc943a6bd37f5ac49bc9633(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return c


def func_b921d79ecb5d497eb6c7fc80cb3769a4(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return t


def func_c690f235526a452ca0830876817ba552(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return x


def func_9f22900bb29a459a9bd92fcd588f6347(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return a


def func_e0c8023538cb42bfb1f64a9510b196b9(t):
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return c


def func_651a5cb4ac5f4e63866a55a11cf609f9(t):
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return total


def func_e12301929b2640019a1d40bf60e3d693(t):
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return best


def func_f697f788209a4fe1ac54722db5a14fbb(t):
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return b


def func_fb20c415a029437382baa7c5d41c1735(t):
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return a


def func_3c30d1bc92b24f2a98c62479ac1b7918(t):
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return x


def func_6a694457c76b40beba83254a47b8a09d(t, total, N):
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return best


def func_5cd67e0735954f24949866017970a722(t, total, N):
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return c


def func_87c7d91972fe4c1b8fc9d8dfc64143a6(t, total, N):
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return x


def func_03a760fd82a14eb884012eb46fbb9770(t, total, N):
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return a


def func_07f722b24289454292a8f4b03f84e965(t, total, N):
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return b


def func_981d03bf3c404bd0bf07f3b2b822fed4(t, c, total, testCase, N):
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return x


def func_70e56058d0b64d689e2670b4afba3c7b(t, c, total, testCase, N):
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return a


def func_5e3caad5f10949b4a7bf6adc141d6507(t, c, total, testCase, N):
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return best


def func_4c8e2d5a756b4bd89a16bf0c14a8d348(t, c, total, testCase, N):
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return b


def func_5eab9f7b320e48fd879cb72b2a894a6a(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return r


def func_becd3957036f485eaa1bf3fe0b369a1b(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return N


def func_a8850c84fc9947f3bbe020eb20ef4b28(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return p


def func_fad58e2d2a1b40b58e64c0dcc651ae34(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return t


def func_83b45d1a6b86428388ab34dcd7dab94f(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return c


def func_838ef7cd3d4042a1885c8d9214f3cc86(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return s


def func_e91541b90e734c448d47605c4c8ad2f7(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return b


def func_51b7f135f7c8423a934b9f8af08db784(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return total


def func_0be2e6040ae440b2a66f7d73224c5ac2(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return x


def func_84da67faa56a4066be8fe731ca2acb2c(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return a


def func_c4dc48a6a011450290ef2effd88d8054(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return i


def func_ba5e9694d94745979cf9a9d4ddefa3b4(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    return q


def func_16c3dbeb6e5344458fe56e245ee9f017(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return c


def func_bbc97581cfc548b3b50c6aa2b0170e5b(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return b


def func_d83b79de8d0b4c37bcf692919d23b92d(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return best


def func_60a90e1921214646a2430f0e59c7665c(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return t


def func_e0f144d5b12f4802b60c02ceead825a7(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return total


def func_45606bd48326415c8106567d6a266583(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return a


def func_d5297eaab41943cb9ee1cbefe8756e2d(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return i


def func_6cff14fcaff04caa94aa1bf66a380dea(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return x


def func_6b63e648c3bb4200b08258fbafff6de8(t, N):
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return a


def func_287b0305205d43b188fbd35aaa169717(t, N):
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return b


def func_9dfcee1a2871469691a934a9a1845d37(t, N):
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return total


def func_3b2923ddc1a943cdbabb5144324d0b19(t, N):
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return best


def func_7091a227f97a4e348f067c9347919bf9(t, N):
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return x


def func_c141b72279b3449dbd1740e9008689ac(t, N):
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return c


def func_2cec7be19c084a05bbe08103d9a3d29e(t, total, testCase, N):
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return best


def func_ee6beb75e7a84f8bac306de8e6f6c2ec(t, total, testCase, N):
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return a


def func_03ed00615f744c0c9cf1218dda734d5d(t, total, testCase, N):
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return b


def func_6021d2d2a7e64f95bc5af61b169392d9(t, total, testCase, N):
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return c


def func_86dcc45d43d94299b6803370340a8d30(t, total, testCase, N):
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return x


def func_d0246e43c534483aa1119723b6696083(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return b


def func_33afe5b5338f42fa8e39cf98ddb7c1e5(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return x


def func_211965fb385e43c992c8e285f0ac30c4(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return a


def func_4448f55f8f4e4bd2937e8ab39e8256f9(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return N


def func_1e16e80d952d444c8e67d9529ef891d5(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return i


def func_c1ac46c435ac40bf8f6aa3a9594abbb1(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return s


def func_fc1d862aae2d4b18b15dfb4c896362fb(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return r


def func_e85800aab43a4107af5bfaaa2719512b(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return q


def func_03790b972b784328b63072841688c211(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return p


def func_547e89fef325498a919d2d948812c0fa(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return total


def func_fc64c494dd8b47469e71ef0c6b88096e(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return c


def func_f4d0ed819bf4456e85d088861499dd05(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return best


def func_1fb3a8fb388848d0aba1464355567bc2(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    return t


def func_94c26330ccdd43cd904318496588cc49(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return best


def func_2322768d63a74f69ac83964248537f24(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return x


def func_36f09aed72354da3ad1bc7f6d7fe20fc(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return i


def func_5dd6e58ff9d24c4b92f5cb7dd91c64b6(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return a


def func_3ad9d711ed97489889d1ee3b88e7d908(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return t


def func_76f7201ceeba4c41a3d457e9832e553b(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return total


def func_3d55382e92374176ab73fc20920159b5(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return b


def func_784ab946db8245568078b957ed591c5c(s, q, r, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return c


def func_ea598a3901bb4d8394ca77012e44450c(t, testCase, N):
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return best


def func_e9b89841685e4d56bea56ce9ef1dd578(t, testCase, N):
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return total


def func_27d6cb26009241118548c5c1c0b1dee6(t, testCase, N):
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return x


def func_a182801081ee4aa6a9d087b1f1ce0182(t, testCase, N):
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return a


def func_e2237a066b3640c99531b1da5ea85499(t, testCase, N):
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return c


def func_f4b04744031240338ba278c5d88ffd29(t, testCase, N):
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return b


def func_32f4df47f7c94b4c97aeb64ff2972aed(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return b


def func_507ffe3302ec499ca072c4d22bd76ec5(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return N


def func_118be3bc3f214379a58b6e71fcb4e0de(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return s


def func_716c5fa89e32418dbc47ad8d88a1c9d9(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return t


def func_58bad60853f243f1a059ba2e0871ed69(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return a


def func_6bb7db9e841846ebb070c5c6e6d5dc01(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return c


def func_c02301649f49447da773d4bcc1dbfcc2(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return i


def func_d65bed3f1a37449ab347d99682de7b50(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return r


def func_1d04c9c20ab04bd683f78d0c96e10cf1(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return q


def func_3a519dd7744343ca8de7a1bd6a84fb8e(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return best


def func_44b6cb666af14d6eb1e5c4a08fa389a1(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return total


def func_f45327ff48094b9aa28321aedbe8e04e(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return p


def func_406df213e5e34ec4a2105d4f6d69ef5f(infile):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
    return x


def func_9f8b23996854404f9bd24c11d210e4ba(s, q, r, testCase, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return total


def func_b7eef40d19d5422c8f9d2ff1683632e4(s, q, r, testCase, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return t


def func_fb40f7e57a654fa0b5e10d73dc158590(s, q, r, testCase, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return best


def func_6f9bbeab87bb47a5be5332a5d5fe52f0(s, q, r, testCase, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return x


def func_78444b5ebb88455f9653843212519652(s, q, r, testCase, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return c


def func_549f80cf756f40eb8140474f0eafcb27(s, q, r, testCase, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return a


def func_c851643bc0a541aa8275ef2fddd6c1c0(s, q, r, testCase, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return b


def func_99ed9c98b565492ea90e4a6364d35576(s, q, r, testCase, p, N):
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return i


def func_4efbc6814e8244a79cab2cf8d68c8973(infile, testCase):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return s


def func_3b6ef64e62094b2197d6bd4fdc837a8e(infile, testCase):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return best


def func_c45fa7fd64d8486aa278d5d72a330e06(infile, testCase):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return t


def func_4a13e52b15be49a1b47ae55ea86e275f(infile, testCase):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return q


def func_d0ac9f3ead7b4a3598b16cbc82f8e0b6(infile, testCase):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return a


def func_49fb1def787c4019bdd74a7e6cfda98a(infile, testCase):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return p


def func_71bb3d45584d4c2cab1a8b21268ae2c5(infile, testCase):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return c


def func_89217ecf92574925aa21e5e7d55388c7(infile, testCase):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return total


def func_a67fde96b9944fb1bdedb57b37f370ed(infile, testCase):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return N


def func_88ad799150474423b1dbc8eacd7c196e(infile, testCase):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return r


def func_359feb9d47704306ac8776237331c9df(infile, testCase):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return b


def func_4a8fbebd50424fff9b63cea2801ecaac(infile, testCase):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return x


def func_ac908baee262400d96400a128e800a74(infile, testCase):
    N, p, q, r, s = get(infile)
    t = [((i * p + q) % r + s) for i in range(N)]
    total = sum(t)
    c = [0]
    for x in t:
        c.append(c[-1] + x)
    a = b = 0
    best = 0
    while b <= N:
        if a == b or c[b] - c[a] <= total / 3:
            b += 1
            if b > N:
                break
        else:
            a += 1
        best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))(
            'Case #%d: %.10f' % (testCase, float(best) / float(total)))
    return i


def func_855e8511ec9b4fb5b11e89ac3860cf54():
    infile = open('test_files/Y14R5P1/A.in')
    T, = get(infile)
    return T


def func_5bf6290d9e8047f28c17e7752a515afa():
    infile = open('test_files/Y14R5P1/A.in')
    T, = get(infile)
    return infile


def func_b7bea83ae9e44cb2b70a4727a430d944(infile):
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return c


def func_6f0ea1600ad442779b473602b434de44(infile):
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return best


def func_91024bca8fbb4e0f86a7245e093c941c(infile):
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return r


def func_a630884a3bdb47ca9a0d58030fa8f541(infile):
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return i


def func_99da29760f3d4a8b887937fc0f766330(infile):
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return q


def func_ac22bf77261340b7911216426eac230f(infile):
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return x


def func_7c6980aed832411bb36f34922c7e458d(infile):
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return total


def func_437eeb06a80b42ca9843a60fab8f19c8(infile):
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return p


def func_8c91870c8c3740798b763d0f40f0e709(infile):
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return b


def func_bc4376f0459b44c8908d69758648bde7(infile):
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return testCase


def func_90fc6304d1634e2986f10c7745fcbcd0(infile):
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return a


def func_c559ee15fb7c46c2a6b34cedcc61438d(infile):
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return N


def func_073a4ab75e304ea1b71b38743747f16b(infile):
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return T


def func_c425e38f3ad447f3a8bad33b29cc3246(infile):
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return t


def func_3d4c68bd10ed40cdbee4a67141dea07c(infile):
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return s


def func_c2afccd626c247c6a28101366f62f86b():
    infile = open('test_files/Y14R5P1/A.in')
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return r


def func_51b9b1958bf44c378a0026f1ba32fbd0():
    infile = open('test_files/Y14R5P1/A.in')
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return total


def func_4a85473ffbdb4c27a0ecb984b607d13c():
    infile = open('test_files/Y14R5P1/A.in')
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return t


def func_03285c3a10884e92a57d43dae742142e():
    infile = open('test_files/Y14R5P1/A.in')
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return i


def func_a6507711c4cc4014bfa84382a83f9c0c():
    infile = open('test_files/Y14R5P1/A.in')
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return x


def func_807f46bb09bb4432879badef5af2e222():
    infile = open('test_files/Y14R5P1/A.in')
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return b


def func_2e176e31cfee4ef1838c910a336e48c9():
    infile = open('test_files/Y14R5P1/A.in')
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return c


def func_66faa68a2d3e4fb1a734409fde77e1c9():
    infile = open('test_files/Y14R5P1/A.in')
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return T


def func_639a1c16c2ed4714bb1af2f9de81356b():
    infile = open('test_files/Y14R5P1/A.in')
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return N


def func_f990d1deb00f4752be318519b5992e12():
    infile = open('test_files/Y14R5P1/A.in')
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return best


def func_dcb421ff113a4ce38651c03de6969f6c():
    infile = open('test_files/Y14R5P1/A.in')
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return a


def func_8f1f62be9e2a4c43be21a2842c59df18():
    infile = open('test_files/Y14R5P1/A.in')
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return p


def func_28ce4452b74c4a968213558c76a0ccd4():
    infile = open('test_files/Y14R5P1/A.in')
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return s


def func_61a641422f2744b79249707a6196565c():
    infile = open('test_files/Y14R5P1/A.in')
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return testCase


def func_2120e5be75a34e048da8e803b2fc886a():
    infile = open('test_files/Y14R5P1/A.in')
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return q


def func_208423fcb31843bc9bfc96974a4d9e98():
    infile = open('test_files/Y14R5P1/A.in')
    T, = get(infile)
    for testCase in range(1, T + 1):
        N, p, q, r, s = get(infile)
        t = [((i * p + q) % r + s) for i in range(N)]
        total = sum(t)
        c = [0]
        for x in t:
            c.append(c[-1] + x)
        a = b = 0
        best = 0
        while b <= N:
            if a == b or c[b] - c[a] <= total / 3:
                b += 1
                if b > N:
                    break
            else:
                a += 1
            best = max(best, total - max((c[a], c[b] - c[a], total - c[b])))
        print 'Case #%d: %.10f' % (testCase, float(best) / float(total))
    return infile

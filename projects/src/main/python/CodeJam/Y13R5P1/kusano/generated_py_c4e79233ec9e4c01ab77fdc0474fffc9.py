import sys
sys.path.append('/home/george2/Raise/ProgramRepair/CodeSeer/projects/src/main/python')
from CodeJam.Y13R5P1.kusano.A import *

def func_ea3ce92f952d4e0b8d00a58bf710bcdd(infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    return N


def func_8046c0b5b1a148e0b996f0c22074925c(infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    return B


def func_c19c14df1ff24ec5a5e94ab06ad67324(infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    return X


def func_bc04c7d9a437492f8dc42894594a7dd6(infile):
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    return X


def func_896f98fa8ca74a46a11fcc0423b69a56(X):
    X.sort()
    ans = 0
    return ans


def func_64f8c9e956324d5f9714d2ed39782e7b(B, X):
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return ans


def func_76030ee6260a449fa45576dccae83c65(B, X):
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return j


def func_c1ee5f079924408291627ef5299169ec(B, X):
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return i


def func_66b92e2576b148aa870e61c6fdd11ba6(B, X):
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return a


def func_7c09bff86a364659b3260c66b35ec246(B, X):
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return k


def func_70e18028b5364c5881af9a295a0d85ce(B, X):
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return b


def func_08d7f8a099ca468e887bfb7f28b13d76(B, X, test):
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return j


def func_abfa9026aba74a18892cb291f5d7b469(B, X, test):
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return a


def func_f386fc3051d045518214ade1a2275a4b(B, X, test):
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return b


def func_88764f870d834327835f456c1f49d409(B, X, test):
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return i


def func_0b6b71c0d09442cf934e10c66b7d49bd(B, X, test):
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return ans


def func_f9ccf69462634ec2a70959b46a225f20(B, X, test):
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return k


def func_93a59d2d64954c6e83e609e65e2874e3(infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    return X


def func_f3f77ac7d6b64cb6ae847db488d5b135(infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    return B


def func_40183ca13a924eec81c440639dc0d3b5(infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    return N


def func_43ae8377f6914a3bb6a88ac9e4d7b5a1(infile):
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    return X


def func_403d8e83b01c484289b0612f2ac9bd82(X):
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    return ans


def func_f61300c2bb274989ac8c2784fe2cbd62(B, X):
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return k


def func_8132564918414825bea512d6aa69132b(B, X):
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return j


def func_d865f5406eb245678cc0cacb2babd006(B, X):
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return i


def func_839d152be5f94e02810025768edc0ca4(B, X):
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return b


def func_0e5e6fd7406843c4b88ccc8b1b18a732(B, X):
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return ans


def func_05f6bacba4c44916889719a5b34f1ddb(B, X):
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return a


def func_77d143e68b6f472a99238934e99d2252(B, X, test):
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return i


def func_b373b3bd059f436bba0f3c27a95b1860(B, X, test):
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return j


def func_18eeb1c8967344c7a7fd085ffd7a3e98(B, X, test):
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return a


def func_05cd9f63ff34418b867183dffe071f50(B, X, test):
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return k


def func_763c770a61f74a978366217e5c76ef14(B, X, test):
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return ans


def func_61ad7875e41944af9bd76c1538f357b8(B, X, test):
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return b


def func_f8eb0c2c66b146b287afd7eb1100b6c3(B, X, test):
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return j


def func_94aba64eafe9432d8f14f84ee35044f0(B, X, test):
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return i


def func_3fb51acaabf34d8dbc550e5564cae468(B, X, test):
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return k


def func_885b89cdf8ae42659da5b3d559194911(B, X, test):
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return ans


def func_21a78d92aafe4d9fb4b082b67cd32043(B, X, test):
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return a


def func_76fd83b46d784db08e893f8a62c84c93(B, X, test):
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return b


def func_3f83e7a88258455490a68d1f4ae0803f(infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    return X


def func_ffad77d0457a4896a3b85d69bd8bf879(infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    return N


def func_067004f7efc2433fa2f43c2c3f171f36(infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    return B


def func_d4cf879b66b54b7883cecabfc11d5760(infile):
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    return X


def func_1b199ab53ef8436584f8d0481c2e070e(infile):
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    return ans


def func_01c32bba384646339bf93dba35306dbf(B, X):
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return i


def func_706d4509d16944518103b7562c39dd8a(B, X):
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return b


def func_85f0331e7fa9490fb49db8bfc003faeb(B, X):
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return a


def func_472cc1b6db5f4cfa9157b731f4af0f50(B, X):
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return ans


def func_c74ad67661a440828d0824f3481927af(B, X):
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return k


def func_93bf7fb23244459c9b5d54a2cd29c66d(B, X):
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return j


def func_625300e14370455793b0a36911ddbc77(B, X, test):
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return ans


def func_2986201160aa433a9dc01ebe41c997c3(B, X, test):
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return b


def func_8c243b226a3a4b2ca67f7c44833b3d72(B, X, test):
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return a


def func_161abbd63216498b8280f65eb37454f0(B, X, test):
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return j


def func_0f80a7b8183f4b9780387b97741fc006(B, X, test):
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return i


def func_6b3ebaf6f69b4bdc9f1132dfa528e8b4(B, X, test):
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return k


def func_1ced3afe96a04d589f4ec1d89020753c(B, X, test):
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return k


def func_5b1934166ff24a36922285e555fb2aa6(B, X, test):
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return ans


def func_2f6812daa533492a8572dcaf0f9b47c7(B, X, test):
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return a


def func_7cd90fdb989541d5a8cc7d801914fdcb(B, X, test):
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return i


def func_4c3e72a65acc44fcbbf040dd28babe8d(B, X, test):
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return b


def func_4907e46af3cf44adae16d289a4702aa6(B, X, test):
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return j


def func_bf70825ac38640a79f7e70d1d7853f56(infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    return ans


def func_a0b5d030768348be954fe92bf2c803df(infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    return N


def func_bad4531d9c2a4214a8141495ec042928(infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    return X


def func_d46f45a0b42644d08614e549f4c68b6d(infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    return B


def func_b7129baa144f48489b7369a85c34159f(B, infile):
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return ans


def func_6210642df30c4b8ba93146f47b7fdaf9(B, infile):
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return i


def func_8d531a1f198d4ce69e919b354cdd2a5c(B, infile):
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return a


def func_66fda1a9bd0145e49c2ed303c266841e(B, infile):
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return k


def func_02cb2d00280c43a08b5e60cbbf170cde(B, infile):
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return j


def func_60154794029d49a6bc6d8e55853d7ef2(B, infile):
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return X


def func_d4282ae260db446a959c5c09e9a6299b(B, infile):
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return b


def func_f70f8d3b82434c309c4ee4bef0b8509a(B, X, test):
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return ans


def func_62a3d655a83048f1ba35a7943e4ae40c(B, X, test):
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return k


def func_9a6343a29cad451ea12e0a4bda1005ed(B, X, test):
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return i


def func_383d97b56ecf4bd8853b24db83b49e48(B, X, test):
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return a


def func_3c1c6f5ea1484ff2af37ae92b54e8a1f(B, X, test):
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return j


def func_29d3c1ff25b2449c83d5bf887c2db6eb(B, X, test):
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return b


def func_97e39cf8833c467ca279de867fe4bea3(B, X, test):
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return b


def func_fdaa8ff02d6c453cb57d7f076a2df8b6(B, X, test):
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return i


def func_b283cb11761646b5a2e7801c3f7a1bb4(B, X, test):
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return k


def func_fc1a9bb9b01a4243a04deed83c8020aa(B, X, test):
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return j


def func_51bab6aea14c4dce88ae84960164a3a3(B, X, test):
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return a


def func_0438fc75327749e69d0141a390b04154(B, X, test):
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return ans


def func_ae0b48baf47f4b72aef908ee49ca5cdb(infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return k


def func_7e19a66e73b34a8faeeed38e3d9fff6d(infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return i


def func_437dcdd026ae400c8ec1695e5fc8c4be(infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return j


def func_864a2084b5174f1aa9c04e5c06bf995f(infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return ans


def func_9ea2958b91ff4717ba163003ca755e5d(infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return a


def func_e3cbc9944a4240d9a8bccaf2fed2dfb4(infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return N


def func_0bb96228d45945ce94a922615ceb5ff5(infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return X


def func_c27c198aa2044851a5694e02b9a258a9(infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return b


def func_506b868d3a514789a8e802a9679e8c31(infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)
    return B


def func_8cf69b7fdac34f0c9ece75b340bef9ba(B, test, infile):
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return X


def func_52af700738124acba6dc50527cc5a397(B, test, infile):
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return i


def func_e9db0c8699d340788650d53caf583014(B, test, infile):
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return j


def func_4743c3163b3b4286b28a0a8fb02e9f00(B, test, infile):
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return b


def func_23dcdd2b86fc4c9c973ba77ec9c55cae(B, test, infile):
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return k


def func_744035366e6547de877a9d0c74eee1ee(B, test, infile):
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return a


def func_f6ca21df8efe476c8f3a167b14d14e44(B, test, infile):
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return ans


def func_ad8ae6106fa74c04a22143092c246767(B, X, test):
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return ans


def func_b01577c4f425407c947d39d559ceb0c2(B, X, test):
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return j


def func_1e141e6a6ac14e71806ecbd611922301(B, X, test):
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return a


def func_e7d1feecf66846018eeae0e5f341499e(B, X, test):
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return k


def func_2e14a78db30f49fa95cb6327208a428d(B, X, test):
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return i


def func_51fc46b40890426cb78ad337f4da0c5b(B, X, test):
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return b


def func_c18c8ced71a54ae2811b3600e512e60c(test, infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return b


def func_ffb8351c65654318b44e6256f6782216(test, infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return N


def func_4f74adf84fa148328c9f409e7dd8d54b(test, infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return k


def func_ddb5abfb8f05484e929c5902720aea16(test, infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return j


def func_ec466335937b4caca5831a269ac533a1(test, infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return a


def func_77cad08260c041cc83ed6dc65d5c051d(test, infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return B


def func_5987ce728a1c4462a9407584ea460574(test, infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return X


def func_7dc0bb5bd21a4a0691010dd6b88e388b(test, infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return ans


def func_35793a1a8b0d4c528093d2b6e16c6acf(test, infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    return i


def func_5609cec8c6aa46c79f979232c9022731(B, test, infile):
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return j


def func_b7a0c149384b4e358e91af51e438d154(B, test, infile):
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return k


def func_6afdbdb1f89145baab49fa21b1182e3c(B, test, infile):
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return ans


def func_23ea319d02dd4d3bb17ffe1202ca12c3(B, test, infile):
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return b


def func_8aa9c4dd038442719f54ea8802007fb7(B, test, infile):
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return X


def func_3c9ede2ffc054715a1d26cd2b14b0b4e(B, test, infile):
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return a


def func_b32ae43709854e8ea2b23326792c533b(B, test, infile):
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return i


def func_a17cb36e821547d59bc6e2fabc7786d6(test, infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return a


def func_961e881dd90d4337b72ed8d102058515(test, infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return N


def func_a01a6805fca14c9a895c870b3e1a46f5(test, infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return j


def func_3f5b152e52ae454ab952dfb08a03a15e(test, infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return i


def func_39532b11f4d94164a6e12768cea39817(test, infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return k


def func_a4704213d861438f9ade4c6317e5dfc1(test, infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return B


def func_5412d33cf63f474ba4aa84b90a162ac1(test, infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return ans


def func_83ed068a95354013b8f49620ac6042cb(test, infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return b


def func_c3f8b20a6a084078bf3f2eb3e6e35cdd(test, infile):
    B, N = map(int, infile.readline().split())
    X = map(int, infile.readline().split())
    X += [0] * (37 - len(X))
    X.sort()
    ans = 0
    for i in range(2001):
        for j in range(37):
            if X[j] > i:
                continue
            a = 0
            b = 0
            for k in range(j + 1):
                a += i - X[k]
                b += 36.0 * (i - X[k]) / (j + 1)
            for k in range(j + 1, 37):
                a += max(0, i + 1 - X[k])
            if a <= B:
                ans = max(ans, b - a)('Case #%s: %.20f' % (test + 1, ans))
    sys.stdout.flush()
    return X


def func_5bc2bae0c9ec40a6b8adb4293c1ee35f(k, X, i, j):
    a += i - X[k]
    b += 36.0 * (i - X[k]) / (j + 1)
    return a


def func_0aff5b671e764a488b5d8504fe62bd89(k, X, i, j):
    a += i - X[k]
    b += 36.0 * (i - X[k]) / (j + 1)
    return b


def func_ee8430aadc71436fb9abe864cb53b30d():
    a = 0
    b = 0
    return b


def func_a3f4426d72594403a24b52a1df49acdc():
    a = 0
    b = 0
    return a


def func_c19bdad1be5e4d17a7acb00a40bb9336(X, i, j):
    b = 0
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    return k


def func_7ab192d4e53043d6987ee49bcb420afd(X, i, j):
    b = 0
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    return b


def func_58bf82aef59f48079fb9b64e6caaf30f(X, i, j):
    b = 0
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    return a


def func_4ca24b8b77074ee19a6e6e092765ea68(X, i, j):
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    for k in range(j + 1, 37):
        a += max(0, i + 1 - X[k])
    return b


def func_92a4c5a48e8a4825ab49a92af1e8c5ab(X, i, j):
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    for k in range(j + 1, 37):
        a += max(0, i + 1 - X[k])
    return k


def func_e24938f5376b499a95e92aea8dfb44d5(X, i, j):
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    for k in range(j + 1, 37):
        a += max(0, i + 1 - X[k])
    return a


def func_e226c65748bb43908efec1a0256925cd(b, B, X, i, j):
    for k in range(j + 1, 37):
        a += max(0, i + 1 - X[k])
    if a <= B:
        ans = max(ans, b - a)
    return a


def func_8ffbce51ae4f4377bc0c0d839bbc0671(b, B, X, i, j):
    for k in range(j + 1, 37):
        a += max(0, i + 1 - X[k])
    if a <= B:
        ans = max(ans, b - a)
    return k


def func_1bec05af26b34e75bb546932f00a6a30(b, B, X, i, j):
    for k in range(j + 1, 37):
        a += max(0, i + 1 - X[k])
    if a <= B:
        ans = max(ans, b - a)
    return ans


def func_035e108ba09c4ea0b7ff897a16472dc9(X, i, j):
    a = 0
    b = 0
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    return b


def func_6febcab1a52a43cf815549bee2fcb11d(X, i, j):
    a = 0
    b = 0
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    return a


def func_47f8a458a0964bafbb7e361a0e2844e0(X, i, j):
    a = 0
    b = 0
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    return k


def func_95f6bec95acd4a94ad62c6acebcfbb3f(X, i, j):
    b = 0
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    for k in range(j + 1, 37):
        a += max(0, i + 1 - X[k])
    return a


def func_19c74dba970049218e08b674b64339ac(X, i, j):
    b = 0
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    for k in range(j + 1, 37):
        a += max(0, i + 1 - X[k])
    return b


def func_66f90382318846029156fa6fdf8442c8(X, i, j):
    b = 0
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    for k in range(j + 1, 37):
        a += max(0, i + 1 - X[k])
    return k


def func_8a48acb877074522831429edf1b3b28d(B, X, i, j):
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    for k in range(j + 1, 37):
        a += max(0, i + 1 - X[k])
    if a <= B:
        ans = max(ans, b - a)
    return b


def func_2bd8e12f528441129b1e0b54945a0cbb(B, X, i, j):
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    for k in range(j + 1, 37):
        a += max(0, i + 1 - X[k])
    if a <= B:
        ans = max(ans, b - a)
    return k


def func_0dca9182073e4994a408712233c2b261(B, X, i, j):
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    for k in range(j + 1, 37):
        a += max(0, i + 1 - X[k])
    if a <= B:
        ans = max(ans, b - a)
    return ans


def func_4da0f0185a3f432ba1f2a13211a55999(B, X, i, j):
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    for k in range(j + 1, 37):
        a += max(0, i + 1 - X[k])
    if a <= B:
        ans = max(ans, b - a)
    return a


def func_13cd1a4a56bd46e7844c7778d667980d(X, i, j):
    a = 0
    b = 0
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    for k in range(j + 1, 37):
        a += max(0, i + 1 - X[k])
    return b


def func_3abeae6ed08d40e096e7f77ca7717f77(X, i, j):
    a = 0
    b = 0
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    for k in range(j + 1, 37):
        a += max(0, i + 1 - X[k])
    return a


def func_6a8592400296494bb42e14fa1f3aadb5(X, i, j):
    a = 0
    b = 0
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    for k in range(j + 1, 37):
        a += max(0, i + 1 - X[k])
    return k


def func_0b183be8233348db899c5c1e5ef509b9(B, X, i, j):
    b = 0
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    for k in range(j + 1, 37):
        a += max(0, i + 1 - X[k])
    if a <= B:
        ans = max(ans, b - a)
    return ans


def func_da7eb2380aea4e15b19d245cab9de600(B, X, i, j):
    b = 0
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    for k in range(j + 1, 37):
        a += max(0, i + 1 - X[k])
    if a <= B:
        ans = max(ans, b - a)
    return a


def func_41b345a53e5c4b8dbf73bf9a532fd296(B, X, i, j):
    b = 0
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    for k in range(j + 1, 37):
        a += max(0, i + 1 - X[k])
    if a <= B:
        ans = max(ans, b - a)
    return k


def func_3fcc9c0351234bfca69e081092499827(B, X, i, j):
    b = 0
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    for k in range(j + 1, 37):
        a += max(0, i + 1 - X[k])
    if a <= B:
        ans = max(ans, b - a)
    return b


def func_d1ee6e4faa99467b8d6e54fd29df3981(B, X, i, j):
    a = 0
    b = 0
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    for k in range(j + 1, 37):
        a += max(0, i + 1 - X[k])
    if a <= B:
        ans = max(ans, b - a)
    return b


def func_7024b103e68f4f6692a8283d601418ba(B, X, i, j):
    a = 0
    b = 0
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    for k in range(j + 1, 37):
        a += max(0, i + 1 - X[k])
    if a <= B:
        ans = max(ans, b - a)
    return a


def func_cf10eb1df19a4a8fb1c566ee36ec4bfc(B, X, i, j):
    a = 0
    b = 0
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    for k in range(j + 1, 37):
        a += max(0, i + 1 - X[k])
    if a <= B:
        ans = max(ans, b - a)
    return ans


def func_cf83278853474700a72c74e3821c96fc(B, X, i, j):
    a = 0
    b = 0
    for k in range(j + 1):
        a += i - X[k]
        b += 36.0 * (i - X[k]) / (j + 1)
    for k in range(j + 1, 37):
        a += max(0, i + 1 - X[k])
    if a <= B:
        ans = max(ans, b - a)
    return k


def func_074f475673b7487ebeedf232ed9bbbfe():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    return X


def func_76acffa2fe4c4e9ab11b61fd942de2c0():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    return ans


def func_a0ffa8f81d294187b5ab48971f79d24e():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    return a


def func_55e4750f354f440583dc3ed0f2f79600():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    return k


def func_a08022c8f3644ec08124c0d49448655b():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    return N


def func_e5a295f8e9154e06a0c2b175df593ba9():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    return infile


def func_f6be9e1a696443b59dcd2396225e3e74():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    return test


def func_cfa4cc216cae4c0d94cfb4fd43975cbb():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    return i


def func_1e4e4d11d97549188294de7116acfac7():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    return B


def func_b0b4cf4ebe5d432e9e956ac840fc96c0():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    return j


def func_ed98693f7ecc4128b1830e750dc1c236():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    return b


def func_4747ce6f113c4902b9d1003c247944e6(infile):
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    for j in range(37):
        if X[j] > i:
            continue
        a = 0
        b = 0
        for k in range(j + 1):
            a += i - X[k]
            b += 36.0 * (i - X[k]) / (j + 1)
        for k in range(j + 1, 37):
            a += max(0, i + 1 - X[k])
        if a <= B:
            ans = max(ans, b - a)
    return B


def func_56c6e9be7dcc46349fe9dc8f8996c02d(infile):
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    for j in range(37):
        if X[j] > i:
            continue
        a = 0
        b = 0
        for k in range(j + 1):
            a += i - X[k]
            b += 36.0 * (i - X[k]) / (j + 1)
        for k in range(j + 1, 37):
            a += max(0, i + 1 - X[k])
        if a <= B:
            ans = max(ans, b - a)
    return test


def func_09844ae40f0443929d3dd7d42cf69414(infile):
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    for j in range(37):
        if X[j] > i:
            continue
        a = 0
        b = 0
        for k in range(j + 1):
            a += i - X[k]
            b += 36.0 * (i - X[k]) / (j + 1)
        for k in range(j + 1, 37):
            a += max(0, i + 1 - X[k])
        if a <= B:
            ans = max(ans, b - a)
    return k


def func_47b60442c4a942a5ae38d3f0e6a3da4b(infile):
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    for j in range(37):
        if X[j] > i:
            continue
        a = 0
        b = 0
        for k in range(j + 1):
            a += i - X[k]
            b += 36.0 * (i - X[k]) / (j + 1)
        for k in range(j + 1, 37):
            a += max(0, i + 1 - X[k])
        if a <= B:
            ans = max(ans, b - a)
    return N


def func_c1f6121d9ed941b3accada37957b5646(infile):
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    for j in range(37):
        if X[j] > i:
            continue
        a = 0
        b = 0
        for k in range(j + 1):
            a += i - X[k]
            b += 36.0 * (i - X[k]) / (j + 1)
        for k in range(j + 1, 37):
            a += max(0, i + 1 - X[k])
        if a <= B:
            ans = max(ans, b - a)
    return ans


def func_c9ec6ed79bdd4c648868a0a4523a8a00(infile):
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    for j in range(37):
        if X[j] > i:
            continue
        a = 0
        b = 0
        for k in range(j + 1):
            a += i - X[k]
            b += 36.0 * (i - X[k]) / (j + 1)
        for k in range(j + 1, 37):
            a += max(0, i + 1 - X[k])
        if a <= B:
            ans = max(ans, b - a)
    return X


def func_e500bdfbe691420f92beea6ff200368c(infile):
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    for j in range(37):
        if X[j] > i:
            continue
        a = 0
        b = 0
        for k in range(j + 1):
            a += i - X[k]
            b += 36.0 * (i - X[k]) / (j + 1)
        for k in range(j + 1, 37):
            a += max(0, i + 1 - X[k])
        if a <= B:
            ans = max(ans, b - a)
    return i


def func_70d90596feaf46749a139c0f4dda981d(infile):
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    for j in range(37):
        if X[j] > i:
            continue
        a = 0
        b = 0
        for k in range(j + 1):
            a += i - X[k]
            b += 36.0 * (i - X[k]) / (j + 1)
        for k in range(j + 1, 37):
            a += max(0, i + 1 - X[k])
        if a <= B:
            ans = max(ans, b - a)
    return b


def func_6282fff2e74b449f8b203c2f5a23682e(infile):
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    for j in range(37):
        if X[j] > i:
            continue
        a = 0
        b = 0
        for k in range(j + 1):
            a += i - X[k]
            b += 36.0 * (i - X[k]) / (j + 1)
        for k in range(j + 1, 37):
            a += max(0, i + 1 - X[k])
        if a <= B:
            ans = max(ans, b - a)
    return j


def func_e8f278b76ea3420e862c1c52ee4f7ef2(infile):
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    for j in range(37):
        if X[j] > i:
            continue
        a = 0
        b = 0
        for k in range(j + 1):
            a += i - X[k]
            b += 36.0 * (i - X[k]) / (j + 1)
        for k in range(j + 1, 37):
            a += max(0, i + 1 - X[k])
        if a <= B:
            ans = max(ans, b - a)
    return a


def func_7543cdb387bf4a9a90dee074ca0b1ac6():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    for j in range(37):
        if X[j] > i:
            continue
        a = 0
        b = 0
        for k in range(j + 1):
            a += i - X[k]
            b += 36.0 * (i - X[k]) / (j + 1)
        for k in range(j + 1, 37):
            a += max(0, i + 1 - X[k])
        if a <= B:
            ans = max(ans, b - a)
    return a


def func_bacae0acfb7f411c96e26bf829ea7859():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    for j in range(37):
        if X[j] > i:
            continue
        a = 0
        b = 0
        for k in range(j + 1):
            a += i - X[k]
            b += 36.0 * (i - X[k]) / (j + 1)
        for k in range(j + 1, 37):
            a += max(0, i + 1 - X[k])
        if a <= B:
            ans = max(ans, b - a)
    return k


def func_8cf77fee222048c1a8ccbce01ff712b3():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    for j in range(37):
        if X[j] > i:
            continue
        a = 0
        b = 0
        for k in range(j + 1):
            a += i - X[k]
            b += 36.0 * (i - X[k]) / (j + 1)
        for k in range(j + 1, 37):
            a += max(0, i + 1 - X[k])
        if a <= B:
            ans = max(ans, b - a)
    return B


def func_cb6242a6dc034d7b83a8892ad93ac9b2():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    for j in range(37):
        if X[j] > i:
            continue
        a = 0
        b = 0
        for k in range(j + 1):
            a += i - X[k]
            b += 36.0 * (i - X[k]) / (j + 1)
        for k in range(j + 1, 37):
            a += max(0, i + 1 - X[k])
        if a <= B:
            ans = max(ans, b - a)
    return X


def func_7071e2063adb4ffcb8e77f879e753ada():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    for j in range(37):
        if X[j] > i:
            continue
        a = 0
        b = 0
        for k in range(j + 1):
            a += i - X[k]
            b += 36.0 * (i - X[k]) / (j + 1)
        for k in range(j + 1, 37):
            a += max(0, i + 1 - X[k])
        if a <= B:
            ans = max(ans, b - a)
    return test


def func_f3537e7bc7914159b87ef78f5ed14d29():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    for j in range(37):
        if X[j] > i:
            continue
        a = 0
        b = 0
        for k in range(j + 1):
            a += i - X[k]
            b += 36.0 * (i - X[k]) / (j + 1)
        for k in range(j + 1, 37):
            a += max(0, i + 1 - X[k])
        if a <= B:
            ans = max(ans, b - a)
    return N


def func_b1967f57b9804ce1813aa22e1e8d1135():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    for j in range(37):
        if X[j] > i:
            continue
        a = 0
        b = 0
        for k in range(j + 1):
            a += i - X[k]
            b += 36.0 * (i - X[k]) / (j + 1)
        for k in range(j + 1, 37):
            a += max(0, i + 1 - X[k])
        if a <= B:
            ans = max(ans, b - a)
    return b


def func_24c0959bc7a945ec9efbaf3818b423ce():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    for j in range(37):
        if X[j] > i:
            continue
        a = 0
        b = 0
        for k in range(j + 1):
            a += i - X[k]
            b += 36.0 * (i - X[k]) / (j + 1)
        for k in range(j + 1, 37):
            a += max(0, i + 1 - X[k])
        if a <= B:
            ans = max(ans, b - a)
    return infile


def func_adfdbd57b9f84cce97c30fe13fd34e4f():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    for j in range(37):
        if X[j] > i:
            continue
        a = 0
        b = 0
        for k in range(j + 1):
            a += i - X[k]
            b += 36.0 * (i - X[k]) / (j + 1)
        for k in range(j + 1, 37):
            a += max(0, i + 1 - X[k])
        if a <= B:
            ans = max(ans, b - a)
    return ans


def func_891ccb41084948338e39b8d6ce7d9dbf():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    for j in range(37):
        if X[j] > i:
            continue
        a = 0
        b = 0
        for k in range(j + 1):
            a += i - X[k]
            b += 36.0 * (i - X[k]) / (j + 1)
        for k in range(j + 1, 37):
            a += max(0, i + 1 - X[k])
        if a <= B:
            ans = max(ans, b - a)
    return j


def func_5f4720b85fa347eca019fe754fd2b868():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    for test in range(int(infile.readline())):
        B, N = map(int, infile.readline().split())
        X = map(int, infile.readline().split())
        X += [0] * (37 - len(X))
        X.sort()
        ans = 0
        for i in range(2001):
            for j in range(37):
                if X[j] > i:
                    continue
                a = 0
                b = 0
                for k in range(j + 1):
                    a += i - X[k]
                    b += 36.0 * (i - X[k]) / (j + 1)
                for k in range(j + 1, 37):
                    a += max(0, i + 1 - X[k])
                if a <= B:
                    ans = max(ans, b - a)
        print 'Case #%s: %.20f' % (test + 1, ans)
        sys.stdout.flush()
    for j in range(37):
        if X[j] > i:
            continue
        a = 0
        b = 0
        for k in range(j + 1):
            a += i - X[k]
            b += 36.0 * (i - X[k]) / (j + 1)
        for k in range(j + 1, 37):
            a += max(0, i + 1 - X[k])
        if a <= B:
            ans = max(ans, b - a)
    return i

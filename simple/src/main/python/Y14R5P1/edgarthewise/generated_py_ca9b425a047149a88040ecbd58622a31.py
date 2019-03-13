import sys
sys.path.append('/home/george2/Raise/ProgramRepair/CodeSeer/projects/src/main/python')
from Y14R5P1.edgarthewise.A import *

def func_8d656d9fa92940e2b7d8f7e5a785d144(a, S, PS):
    s1 = PS[a]
    b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
    return s1


def func_1f31624786e04aa8b4430a5e3d4b0b53(a, S, PS):
    s1 = PS[a]
    b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
    return b0


def func_7f8d928870f24d44b66b73c6c87f02ad(s1, a, S, PS):
    b0 = searchsorted(PS, s1 + (S - s1) / 2.0)(b0 >= a)
    return b0


def func_7311579e3c5840c1bc41f69bb8421f81(a, S, PS):
    s1 = PS[a]
    b0 = searchsorted(PS, s1 + (S - s1) / 2.0)(b0 >= a)
    return s1


def func_a26c96b8f9574d508d1d7b7a56bdfc03(a, S, PS):
    s1 = PS[a]
    b0 = searchsorted(PS, s1 + (S - s1) / 2.0)(b0 >= a)
    return b0


def func_e4e0168ce2934cb4b54263b6c965e781(s1, a, N, S, PS):
    b0 = searchsorted(PS, s1 + (S - s1) / 2.0)(b0 >= a)
    for b in (b0 - 1, b0):
        if 0 < b and b <= N:
            mx = max(s1, PS[b] - PS[a], S - PS[b])
            if mx < minmax:
                minmax = mx
    return b


def func_5b171776378d4fe8ade58556e0ca5334(s1, a, N, S, PS):
    b0 = searchsorted(PS, s1 + (S - s1) / 2.0)(b0 >= a)
    for b in (b0 - 1, b0):
        if 0 < b and b <= N:
            mx = max(s1, PS[b] - PS[a], S - PS[b])
            if mx < minmax:
                minmax = mx
    return b0


def func_107314e97cbf4acb95ddb5893b368e6f(s1, a, N, S, PS):
    b0 = searchsorted(PS, s1 + (S - s1) / 2.0)(b0 >= a)
    for b in (b0 - 1, b0):
        if 0 < b and b <= N:
            mx = max(s1, PS[b] - PS[a], S - PS[b])
            if mx < minmax:
                minmax = mx
    return minmax


def func_ed94061459424fa2aa0f18d364325bb3(s1, a, N, S, PS):
    b0 = searchsorted(PS, s1 + (S - s1) / 2.0)(b0 >= a)
    for b in (b0 - 1, b0):
        if 0 < b and b <= N:
            mx = max(s1, PS[b] - PS[a], S - PS[b])
            if mx < minmax:
                minmax = mx
    return mx


def func_00518c2259b34044a7c4b3e2080b2fe7(a, N, S, PS):
    s1 = PS[a]
    b0 = searchsorted(PS, s1 + (S - s1) / 2.0)(b0 >= a)
    for b in (b0 - 1, b0):
        if 0 < b and b <= N:
            mx = max(s1, PS[b] - PS[a], S - PS[b])
            if mx < minmax:
                minmax = mx
    return mx


def func_46802a8b7320468ab29f56f3f11173a3(a, N, S, PS):
    s1 = PS[a]
    b0 = searchsorted(PS, s1 + (S - s1) / 2.0)(b0 >= a)
    for b in (b0 - 1, b0):
        if 0 < b and b <= N:
            mx = max(s1, PS[b] - PS[a], S - PS[b])
            if mx < minmax:
                minmax = mx
    return minmax


def func_536a1e0260324f43bf0878875dad4b7f(a, N, S, PS):
    s1 = PS[a]
    b0 = searchsorted(PS, s1 + (S - s1) / 2.0)(b0 >= a)
    for b in (b0 - 1, b0):
        if 0 < b and b <= N:
            mx = max(s1, PS[b] - PS[a], S - PS[b])
            if mx < minmax:
                minmax = mx
    return s1


def func_85dd03c7833a45a3bc555bc2574c0b6e(a, N, S, PS):
    s1 = PS[a]
    b0 = searchsorted(PS, s1 + (S - s1) / 2.0)(b0 >= a)
    for b in (b0 - 1, b0):
        if 0 < b and b <= N:
            mx = max(s1, PS[b] - PS[a], S - PS[b])
            if mx < minmax:
                minmax = mx
    return b0


def func_b5460fe3506748f799b9846429b29c7c(a, N, S, PS):
    s1 = PS[a]
    b0 = searchsorted(PS, s1 + (S - s1) / 2.0)(b0 >= a)
    for b in (b0 - 1, b0):
        if 0 < b and b <= N:
            mx = max(s1, PS[b] - PS[a], S - PS[b])
            if mx < minmax:
                minmax = mx
    return b


def func_7eceaf15b9ab4b4fa78a621dcf70bf8e(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    return r


def func_0fd064c237164b3d908a6ece14cf6584(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    return p


def func_d2551bc98b6b4a3da8e64a991dbb13b4(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    return q


def func_9864c20dcd1845548b13bd229d069c9b(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    return N


def func_1883dc8d5f224dd1ab7fb08759a8cd1b(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    return s


def func_093c85f3f3624ba59633a4c038079b9b(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    return word


def func_8e2b92d7aead43eaa158562a03fc9534(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    return NT


def func_92f5b18429464a3bae9573274ea3d1bf(N, p, s, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    return NT


def func_bf31a7a022d94848bdf81acd3c84bbf4(N, p, s, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    return PS


def func_f62cde4678154f9083a4b80dc92c14c7(NT):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    return PS


def func_029a373755084dc6a974db6a5b276e9a(NT):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    return S


def func_bec09dea836d41b0a8aa465864e4535c(PS):
    S = PS[-1]
    minmax = S
    return S


def func_73ac5beb55904f7b9bd2e8c926ff3769(PS):
    S = PS[-1]
    minmax = S
    return minmax


def func_172387028af94fa9936046bad105a963(N, S, PS):
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return s1


def func_4e32cc5c75c04397ac600f6d194826f5(N, S, PS):
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return b


def func_bfac0291cdb346ffb8d783c1c8c29477(N, S, PS):
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return minmax


def func_0c7e2202b25f4324abdb6f5bb318687d(N, S, PS):
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return b0


def func_76300e5d0c614607b1a6a8a56a7bdee5(N, S, PS):
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return mx


def func_303c27bd8dec4e92ab1c85ad7c3a7f63(N, S, PS):
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return a


def func_23292fb94a554de09838e9098bceff33(N, t, S, PS):
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return mx


def func_12e62f4ae55c406c92ad1edbfefe06ef(N, t, S, PS):
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return b


def func_a154a36163724823bd35fdb4a6f9f535(N, t, S, PS):
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return minmax


def func_bca08cc8cd9340069d06506687890eb4(N, t, S, PS):
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return a


def func_dfbd63a4840743768a3f3d776de276db(N, t, S, PS):
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return s1


def func_07c6380fbcfe40e7a53eda3e9bbd2eab(N, t, S, PS):
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return b0


def func_594ca1c6829440f283b9141deaafabee(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    return word


def func_7363b0bf930a494aa2760940f47a8bcd(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    return q


def func_c3a463c667214e8fa23c31aa39bf8977(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    return s


def func_dba55cfeb6f34a0aa8d8e9fbbb951f2c(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    return p


def func_62eee7e6c0854ec686a87190e16c033a(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    return r


def func_49e1eeb446ad48d7b8d44ff276e50af7(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    return PS


def func_ca1556a23d7d4953bf63e81384c8ad97(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    return NT


def func_c6ae0f6526b24bd5836136b7424f7928(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    return N


def func_0456dce5c5314a539e7db2c7cb9f9c53(N, p, s, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    return S


def func_003df6ecd166435ca6a5e41bbefcfeb9(N, p, s, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    return NT


def func_1be172b7105d4b4db181e119b89acc55(N, p, s, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    return PS


def func_9e3016bc5c144165b2439fe26c2de214(NT):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    return minmax


def func_7dd5a190b2e24ae3b236e88f17d2d7b4(NT):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    return PS


def func_8b5f2880cb7848679a1ca5da98ff2c26(NT):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    return S


def func_971b723edf7f44bea81d9295f6a1e3b2(N, PS):
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return b


def func_7aff478c08984fe89885879c2b7b85f3(N, PS):
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return minmax


def func_92adc962d89f4ada8f8a08c4ce6c86a3(N, PS):
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return a


def func_77df161d631947f191e8c8d1013affaf(N, PS):
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return S


def func_cf271200a0ad4c7799e0cd50f026dfc6(N, PS):
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return b0


def func_69be44f6a6a441508c08cc010a24b0ae(N, PS):
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return s1


def func_d0800ee006e1412a81323fd7a22c81c3(N, PS):
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return mx


def func_2dd548afb2cf4b90bb8a76ac3847f483(N, t, S, PS):
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return a


def func_cffae667ef7c4994a9e583d50dc453fb(N, t, S, PS):
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return b


def func_b7210f0459244f76996896bfac275fe6(N, t, S, PS):
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return mx


def func_9fef00ccc1ad4cad85a4392bb7e9874b(N, t, S, PS):
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return b0


def func_9903521fe417412ebcd4be0e13d80c39(N, t, S, PS):
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return s1


def func_cf003fea537f462e99f5b174cb2f1a76(N, t, S, PS):
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return minmax


def func_1c3aaecbbf624bb4bf7c1b970b7b8162(N, t, S, PS):
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return a


def func_5c87246e03344bf5b86587d4aa136cd0(N, t, S, PS):
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return b


def func_c1a29b8d3d2b4b53ae9b4f6568805e1c(N, t, S, PS):
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return s1


def func_2a2bd67e33d04b8689f97b0bddeef42d(N, t, S, PS):
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return minmax


def func_8995a0b31eff4882acd4bb4c09d7e3cc(N, t, S, PS):
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return b0


def func_4d1f8f0535dc47899caea80c44b99425(N, t, S, PS):
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return mx


def func_25e368cd02cc4795a9f60c61f4f4d74a(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    return PS


def func_36c9a3ddcf834db8ae39945afd751cbd(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    return s


def func_94a0f3f55e814c469112faf4bfdc3d63(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    return r


def func_0c87d31025de4c9b9a6f077e498e699b(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    return S


def func_466c2cc81c154702b32933ce7f4f13d0(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    return p


def func_9bfa2adabb014e6d872a43e9f6ff9157(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    return N


def func_a9ba1a849c1f43eb90b64402af162123(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    return NT


def func_59e5ad26b9c846a79ac26ffff391b502(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    return word


def func_862fe37314bf4e2eb23d2a663f51112e(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    return q


def func_6b662c8ca92e448ca09c86d23c04eb4d(N, p, s, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    return NT


def func_ccbfd667235c40efadac5a3307a9c13c(N, p, s, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    return minmax


def func_45c34bb426154d98a3818ccb144b26ed(N, p, s, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    return PS


def func_e7168e20657f470d8d9607e23118302e(N, p, s, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    return S


def func_fbec01afab24448f835dd6ae289ed8db(NT, N):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return s1


def func_f145af3992ab4ee89b8c94e6e4729d4c(NT, N):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return mx


def func_76ea733a444c4f0899876c4252c44d2a(NT, N):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return a


def func_e9418372b55949c68144f49a4790a0c3(NT, N):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return b


def func_0ab015e50cec4a2e9fdc5baf31f1e8c6(NT, N):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return S


def func_537a627e84394014840fdf23be6c512a(NT, N):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return PS


def func_34188f6ed3ad4ef6b58a8fbacdc92200(NT, N):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return minmax


def func_101a7b985bbf402698d5ba8bde0b9f9c(NT, N):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return b0


def func_4efa17767ddc454cac8dbad8158ede15(N, t, PS):
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return a


def func_8edd7e1df44c4ccdb80d698e801daaa3(N, t, PS):
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return minmax


def func_e351e52b8241478e9f2ad9ec5c68d2c4(N, t, PS):
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return b0


def func_1e1d236d600e4ae68d5917b60957ad5b(N, t, PS):
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return s1


def func_6f5e07415fd24b17ab63dd4d413640eb(N, t, PS):
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return b


def func_0c3ab580436244f0b71e40861de01ac0(N, t, PS):
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return S


def func_3749de1c1f6b457a91c393b86db25aaa(N, t, PS):
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return mx


def func_b8a51455a04748fab9cfc86e68f4e423(N, t, S, PS):
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return minmax


def func_34b0c5b3b9ee4c8d935dc3372e7bb2e5(N, t, S, PS):
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return b0


def func_60712881e92c4581aa0b1c09c75046d5(N, t, S, PS):
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return b


def func_411bc44deb284fed99960d45028dde39(N, t, S, PS):
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return mx


def func_b0bd1f2ad3604636a0c79d4008f504e9(N, t, S, PS):
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return a


def func_ead90449600a4fb1801a6a6e8b9bfcfd(N, t, S, PS):
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return s1


def func_515de6869915441581ef03b49c9f1684(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    return S


def func_a0317b55d9134f6c81b5676a412abafa(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    return NT


def func_5d581c548ede43b5a3cb30d0685ac6f3(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    return minmax


def func_e90956be10a74eb499cfef17f96f1c24(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    return N


def func_1feb5e12b28c4b2aa45ed1f966e1d1c2(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    return word


def func_d7421a159f4f40389553956e7da28417(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    return PS


def func_351856c734564e8f862ab7ab86d734ba(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    return p


def func_ace9b5adac3741389660ce7ff0eef414(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    return r


def func_950179e0050c404bbe3b3afe97800461(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    return q


def func_17046cdd21c14c61b54c64b54c422b93(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    return s


def func_000df297957e4a52b21ecff077fc23e6(N, p, s, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return s1


def func_8fecef682f354d22a4b28b38a9a4162b(N, p, s, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return minmax


def func_f5dbf7c7bced4403a71db4c67a5e4fd7(N, p, s, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return mx


def func_a97890e02d174be69d072bc16361b5fd(N, p, s, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return b


def func_116454b6d5bb401c86abdf6e9084c720(N, p, s, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return PS


def func_8136225c6d744a79a5900d72e7631fa5(N, p, s, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return b0


def func_70fc9274815a4cb78733d1a5026661f6(N, p, s, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return NT


def func_8c4048a756e54a919ce8c600f0fa278c(N, p, s, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return a


def func_ce0e85f403844b9d949f4a5fa2f3b12d(N, p, s, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return S


def func_47b2f945ab8f49b89e17a3168b2e86a3(NT, N, t):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return mx


def func_44afc2b922d7410e9d6791d06f9a5e04(NT, N, t):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return b


def func_c020d459c0b1491e92e7102b1460b8e9(NT, N, t):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return S


def func_02026cb3cf194aebaf0ac66769d2545e(NT, N, t):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return b0


def func_403200ec30594986a3636ac5326549ef(NT, N, t):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return PS


def func_a2f425adcc7f4bfab21f8532d3348189(NT, N, t):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return minmax


def func_f760f9661c1b471c8a27731d3cd6de2d(NT, N, t):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return s1


def func_92731047dc44443c86be5886713c7d1a(NT, N, t):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return a


def func_cabd494064b24747869dd8b1762d514f(N, t, PS):
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return a


def func_7767201d521b4d9082ad16dfbf30a0c4(N, t, PS):
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return mx


def func_409baaab7fea4c84b5dece3bec52936e(N, t, PS):
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return b0


def func_8401f9f532064fd0b685b8b184158d6c(N, t, PS):
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return s1


def func_58ee11630b114f7a909b1a4aa881a1d8(N, t, PS):
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return b


def func_cbd6fb11c9b24e67b7c3f14f6b73d963(N, t, PS):
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return S


def func_2807ef466ed14538a887b2a24053dfda(N, t, PS):
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return minmax


def func_b1104fe8c51a418388fda0280edbb177(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return b0


def func_15b810bc053a4f918f41984fe264e007(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return a


def func_78a9a8baa49a4a66864567e8ce9b314e(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return mx


def func_8a2312e82c31480bb34df53a126511cf(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return s


def func_59b7fc4ed2ce41ceb8f87619addc22ae(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return p


def func_d26e4e92eb8f48139e64e0aff3dc1e73(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return minmax


def func_56164f8286bb45459cbb09a3e855307f(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return word


def func_e5ae6d3e86c546d6ac62453192f4f97f(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return q


def func_b02d5e3360c942e5a2752d4c7a6ae62a(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return N


def func_a83775d7915e4f69b4b2d1138a8dfd81(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return S


def func_14ab8c600b49450fa3c3ea1a137c9d3b(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return NT


def func_b7a0e73f050f407495ecc6020533beb5(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return r


def func_b4de4a13e6464b359536742fe2a669e3(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return s1


def func_091edd66c1da4cb1abc4a8251f43d046(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return PS


def func_218fc33c88494285b4c6ebfa929da865(infile):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx
    return b


def func_d1037ed735e94fa4afe64ed8be4d42bc(N, p, s, t, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return minmax


def func_f46e61ab04d04d44b490efa4029c04b4(N, p, s, t, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return PS


def func_1d9d54ab80e244b9b9534ada037d581d(N, p, s, t, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return s1


def func_34ca86274eae46dcab9357cfac6cd3ba(N, p, s, t, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return b


def func_2e8eb9cd40654de2b6b808956875e1df(N, p, s, t, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return S


def func_b8cc7fec15d24b0f8d803c68a8053f7e(N, p, s, t, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return a


def func_0d8c2e98b8f44add97dc88b7ed68a644(N, p, s, t, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return b0


def func_8150492940f6483881f6686fe47101d7(N, p, s, t, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return NT


def func_101056c9693f46cda0ca5298277c3e97(N, p, s, t, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return mx


def func_92c73b3431df417193bfe7b86298e63f(NT, N, t):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return mx


def func_6419e883247d4ef188f333f4b671d934(NT, N, t):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return PS


def func_347c4f60997f43bc8bd3db0e31be72ec(NT, N, t):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return a


def func_ad90b64b0e454382b30a60d1bc4305e0(NT, N, t):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return s1


def func_aefe033bbf204bc29a7f66398f3f4ee4(NT, N, t):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return S


def func_3a47b9db13e8407dbd4979bd7bbd92f3(NT, N, t):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return b0


def func_a80e44018b4941a8a534b3434ecd5a79(NT, N, t):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return b


def func_38d4e5a228e04829a03c7cc87433355b(NT, N, t):
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return minmax


def func_fe39e5b0bba54549bdef7255b6f739a4(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return p


def func_118969101a274c9487ec36df7c14a5ee(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return b0


def func_d5660849a6a24ff88c27abe211aac7a4(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return b


def func_f95ff34826f742d29cad145b87405b94(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return q


def func_959e19641c0b49fd94b986b05d2b7b28(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return a


def func_94275f4108eb4f4fb16ed0d8d14abe3c(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return minmax


def func_ccfcaa6ee1af4f28bce5b6ec9f19ca83(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return mx


def func_51efa4a1fa314e8abdf54a475a721b42(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return N


def func_e27ba1105d124d19b7acc5fd2ab8036f(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return S


def func_672fa45fcd284b5cad981fce9d014971(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return PS


def func_c9187ba0bf4d467ca719511b1dd189d0(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return NT


def func_b206039bc2344737ba593d2f2fa50eee(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return r


def func_a1b16f253b734dd9892a2195ab31a80d(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return word


def func_c237d67ea7a04915aea7fe4be785bc5b(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return s


def func_c1d2b4a186c8408a8765367511766b16(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')
    return s1


def func_fec84390578149748fcfa0aa88a6cbac(N, p, s, t, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return a


def func_f5258bca361a4a4a9b963db80cb43c6c(N, p, s, t, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return NT


def func_e73f9d80b66f4831b3e120d1a7bd6035(N, p, s, t, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return mx


def func_69488627326c44dbb73e158f37102b3d(N, p, s, t, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return s1


def func_0d150e79b70f40b6abcbe633bf426980(N, p, s, t, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return b0


def func_6b23dcfb62ef4fb59e214836d7ab7ec2(N, p, s, t, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return minmax


def func_8bf2bc242b4e4474ab3b550720cdd2c6(N, p, s, t, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return b


def func_3c18229021524489b3e173c81e5c636e(N, p, s, t, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return S


def func_d8a6019f7dfb4548a995525a0d67999b(N, p, s, t, q, r):
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return PS


def func_6db0d98701bb431b86f1dbcb32c20cbd(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return b0


def func_c207ad9def5247db89d92ed6d960cb8a(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return r


def func_b28f791e987949d9bc344f8be45be572(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return word


def func_371a732b29b14090bcbc97016153c3aa(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return q


def func_8e5b024ef36443b7884286d7a8ec01f5(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return a


def func_a6e1b011b756436f87aa89d4a3e81733(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return s


def func_6deea5dffc8e4b8696620dc40d22d99d(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return NT


def func_5be98448193f4bc98e770e249b0714aa(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return PS


def func_33b38455108149f891c0ef4f1bba694e(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return minmax


def func_71d827260d174a4aa62657a14673a9a3(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return p


def func_2bac9c6735ad41b8bb5bd1b7e1c62c2d(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return s1


def func_373b8b64c5d249a38fd7c3707080809a(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return N


def func_d7ee25943bc94441b565a122edbbe59b(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return S


def func_9527dbb0ed0f42248d0402990c69b88f(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return b


def func_a398dc3d6b844fb2bc2fdb2867f4bbe1(infile, t):
    N, p, q, r, s = [int(word) for word in infile.readline().strip().split()]
    NT = (arange(N, dtype=int64) * p + q) % r + s
    PS = array([0] + list(cumsum(NT)), dtype=int64)
    S = PS[-1]
    minmax = S
    for a in range(N):
        s1 = PS[a]
        b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
        assert b0 >= a
        for b in (b0 - 1, b0):
            if 0 < b and b <= N:
                mx = max(s1, PS[b] - PS[a], S - PS[b])
                if mx < minmax:
                    minmax = mx('Case #' + str(t) + ':')(float(S - minmax) / S)
    return mx


def func_2bac005397ac402983a44194d768d682(s1, a, b, S, PS):
    mx = max(s1, PS[b] - PS[a], S - PS[b])
    if mx < minmax:
        minmax = mx
    return minmax


def func_9ccd666c541a4323bf31a9b4ccdaa006(s1, a, b, S, PS):
    mx = max(s1, PS[b] - PS[a], S - PS[b])
    if mx < minmax:
        minmax = mx
    return mx


def func_a47472ee89974769a85da21a1ecfdaf3():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    return infile


def func_c0a21f0954e24972b36671d1308e9b50():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    return T


def func_ff1ae1c1c8844255b430d955086f8dce(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return S


def func_ff9f460025e64540b2cc9d451844f249(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return N


def func_b10ed45f0b6648a990318cb3ab978eed(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return PS


def func_671247c16c824b21882e863fb99cd25b(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return s1


def func_b5fb9283db214d67bea1a5997f5c1721(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return b0


def func_7ad1d6bed96e4b149413e7308c43823c(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return a


def func_d98d2e0ad55d40f091e235b1cc4125a6(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return NT


def func_69bbbbded375425b8a5fd04e730056b7(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return mx


def func_c101c56875e14f7580e183729de2975a(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return T


def func_bca20c797af6450cadefe36f97174770(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return minmax


def func_b1f5bc1a23d04ab6927d827a15fcb652(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return p


def func_b2cbca489b164d6ca8a69a364382416f(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return s


def func_0a7ef52a38204f8cb6845c845d9f0e28(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return t


def func_4c92f2cabc50421d86a0c7a50f4cfcfe(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return b


def func_d4a5bf7e715c49aeb0ebe3d820cd207f(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return r


def func_728c2d82ce494e70a2454a4969711369(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return word


def func_91aa242acaf4460cb303f9962c65811d(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return q


def func_13a05abcd0604224b78b8cf9fefb9863(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return b


def func_59d084678db2407c8eac7a0e2a1eb10f(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return minmax


def func_c79549d89ee24277a207d5b574a97fc8(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return N


def func_fe1bc5d8699042ed9e051723c8008647(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return a


def func_b7b088945c4f4aaebf05441e23301f53(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return word


def func_7790b2e65b0443a7a7a0668eb1c74122(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return q


def func_fa6498c3675b4706ab299b707e49a2ea(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return S


def func_713388631e424b16a0602b352db65e5f(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return s1


def func_0112ec31cbc74dfd92fffbf1b0c7614e(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return PS


def func_f6d84341f2ab44b586186508ee9dcce2(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return r


def func_66278a6013d44eb39192b3f47c365ff5(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return t


def func_e04b725c7ad5417a928822c2bad6128f(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return s


def func_6e840dbe38074f498383ec73398355af(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return NT


def func_ea655536991b4ab09a61d76e78c410ba(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return b0


def func_53a54d5cc8b444f48ea5b1ffbc948a4e(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return p


def func_7c0ef6877fb44aedacbb14ad38a08482(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return mx


def func_fb687b8a8647426d921be12bf90c675a(s1, a, infile, N, b, S, PS):
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return minmax


def func_54012d328fff4139b9ce4a0ef968edf8(s1, a, infile, N, b, S, PS):
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return mx


def func_4dad50b712ef4c5b999a55aa90738966():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return q


def func_d40d7e0918ff466eb88bd81b710921d0():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return r


def func_40f0a9984f85423e94f21801275e3f42():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return p


def func_94e54eadae144bc49f65bed0058f9204():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return minmax


def func_ae11956878a344268d2679e8fdee1727():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return b


def func_6591bf0ca1b84bf39816d60785cdf9a3():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return b0


def func_0991bd9a48f4495f8a6799ad04dca937():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return S


def func_eba659ce30d64cbba3ded36ae0b3c29d():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return PS


def func_88b6e537e4524da1acf4e896c777de96():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return s


def func_40cd4ae65eed470e86f086f251d1fe31():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return a


def func_249855a103d5456393dd51ae2bcbee13():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return s1


def func_fef2122fd9c44f749c5f1625c97db011():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return t


def func_28f32345a7c446388aff938a27affc80():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return word


def func_a57cbe7181454a65a245432ba82e9c70():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return mx


def func_747e01cdf9b94590aa671972061529cc():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return infile


def func_72b224e930d1433b9cdf54ea367574a4():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return N


def func_1a2d4629717543adb7464e8e0cdbd9dd():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return NT


def func_580ca06ac3ba47a58da471734d54b104():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    return T


def func_57b439fa553d461cac153499d84fb133(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return b


def func_14ba639abbd24dfda4216b307a5e0990(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return q


def func_1d44e73a66f74e2193f353f4c51489c4(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return s


def func_d756ac2ea8dc438ea14559310d5a2734(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return b0


def func_26b7629807c94567af654cf50fcb5c7b(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return p


def func_d5a90b287c584335a6da361edcdba1af(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return t


def func_3cbd1706bb784b75b482a01a4430c8ed(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return mx


def func_68cc5391077c4a1f9afe7e85eea936cd(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return word


def func_82e95df8610a4a27afdb08c61eac5539(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return minmax


def func_0a73b9cc03db4fbc95bd3f673561a5ba(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return N


def func_4b841040bfd64105b132dd309f347539(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return a


def func_7e5dbc48da0d4aaea29e5ac2f91ee9b6(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return r


def func_93b45b3f3b104355a40fb3bff892c86d(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return s1


def func_a39c4216a46346139ffa3d17ab490994(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return S


def func_cf80ccfcce2e49ce83c7db9c29a61fc4(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return T


def func_72f7bf6504e34356810d9518dd1388e0(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return NT


def func_8efa9ee807514185893608dfa64eecdd(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return PS


def func_8c77a4760bc94fde84e69bbc5931f27d(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return minmax


def func_3c4b1ffc95e04fae8abd1bd835997d4b(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return NT


def func_e5371c97a8db4f498e98a0c3902347fb(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return s1


def func_485c7f34d7dd47b9bd0e36c4f61da33d(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return N


def func_d03e2b83b8424f858d52e1e9dc3cffae(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return s


def func_4a596458f1d741f7b0dc11dc3086b4df(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return word


def func_2af24939474c4b2daec5c56cfbbd248b(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return r


def func_7a41cc433be543f690dafa3f2190d475(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return b0


def func_8252e0e3c26e4fad89063bfb3b8270cb(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return p


def func_021fd9c1a3474bb485be1281a6ee20a3(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return PS


def func_c6881c66257d4c0999dd0276085b4038(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return a


def func_beff020af4114e71a960f567906a4705(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return b


def func_2270a6c6d65743e7bf8778879abcac69(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return t


def func_10f3185cdf614da7ab5dd249c8d24a76(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return q


def func_cce70f6b0f6f4dd4b6d0af43ad401da6(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return S


def func_6d0bea523c584a7a8cc17d66c3139ef8(infile, T):
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return mx


def func_a9c02e2408564e56b6328d5b6753bc5c():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return minmax


def func_1e0042fdb45c432ca563002cd4beb69e():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return PS


def func_e1fb619305414b31aab64b0469281ae0():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return s1


def func_380e667fa6b646b395fbc29c1471ee89():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return N


def func_ce6fd06c0d5d40ccb6e9d1400f7d65cd():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return a


def func_508ae45bd2f24a0caa1a579b8ec742e1():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return mx


def func_d90d55c78848445cb6a7a112223f62e0():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return r


def func_e396df229b604eb2adeee02966ca2d12():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return t


def func_e95dbc3f56b348289cf7e908cdeed9d3():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return q


def func_037525235876492d965ef84a04d2c93c():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return word


def func_85c6706f38684208b4c7a49b3399034d():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return p


def func_698f6f04d7754271bec19c92aa326dd5():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return s


def func_331f35099d1742048537120a5cb6a932():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return b0


def func_75d0dd97ecbc413fa7cffab27e740e28():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return T


def func_d95d54bf0a9f44b188f7dac6d0ef4ab5():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return infile


def func_916381b54afb4754932448d103d00e0b():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return b


def func_17b5663022c848e69e1d4a3cfec9bf56():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return NT


def func_0616ca3d732743819b7a35ca761f75cf():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    return S


def func_19a458e8c4a740e0b392942a8f7fec73(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return mx


def func_584ac5fb7d5c49b58ad31fb3723c8026(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return s1


def func_af23fef9f4c44a2baac74dac65dca893(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return q


def func_07ad5bfb7c2643f0855ebf38a4f6a55f(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return p


def func_e792ad46bdc348d49bd30dd7e9bdbe8c(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return T


def func_ea63e64158a14236a03ade1c90a1db66(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return PS


def func_da4e4945f01e450296232b1a25dc8576(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return minmax


def func_6b5d7997e5714030a120b3d9699c018b(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return NT


def func_84fef091103b40b4b545d3092579f6fc(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return word


def func_0dd46a6a32f847279612ef09b12fa1ad(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return b


def func_ff10ef3573b54d48a1f9497b39db2c1c(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return b0


def func_e1628f9c83424323af86d227354cfa07(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return N


def func_be1ed039baef496291756c7e735c6440(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return r


def func_b7634abbdf3d4b1994e3b006dd5fed74(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return S


def func_4e7179246c5741258b9f41448e601459(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return s


def func_835ec0091e58461bbf4e61257b6d0d64(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return a


def func_eff3aa4a0a0845c4923cd3cd9489a97d(infile):
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return t


def func_d0f4932bdad74ed9be9b8f17277f43e2():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return word


def func_0f1f1ec30a8f47f6b220a52eff8fe083():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return T


def func_7aea97807c1f438da6ecc0beafba0a8e():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return q


def func_250ee0eb7d744feaa20a0c663a8bc2f8():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return PS


def func_70d6026b13ad442a828f76717dd9a912():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return minmax


def func_bb905e7de2704a388c44f9b8de9baacf():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return t


def func_634dcc8379454f88b5316a1e8aaae2b5():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return b


def func_db95cfdfa12f4b428f5ee199c09d5d9d():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return mx


def func_7b83ef0b8da64852a7dd7480271fe71e():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return p


def func_c5331f97a49f42b690ceb9616cc8659a():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return N


def func_c30eee0ea5d4480e8855972fdb629fb9():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return r


def func_e967d0a11ae248858eb15a6616378635():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return infile


def func_d97252fef3cb40118dab8ee34798bcf0():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return s1


def func_ddd8ab17376c469ebd1b0fdd853a2831():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return S


def func_e7c2b0934dd74162acf100ba8b751733():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return s


def func_00e9fc6cac22470583c7c27e786ceb1d():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return a


def func_65906efc2d16441bb2147768d42a8e53():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return NT


def func_33c4a7e7b0c541ef86794343cdef647a():
    infile = open('test_files/Y14R5P1/A.in')
    T = int(infile.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = [int(word) for word in infile.readline().strip().
            split()]
        NT = (arange(N, dtype=int64) * p + q) % r + s
        PS = array([0] + list(cumsum(NT)), dtype=int64)
        S = PS[-1]
        minmax = S
        for a in range(N):
            s1 = PS[a]
            b0 = searchsorted(PS, s1 + (S - s1) / 2.0)
            assert b0 >= a
            for b in (b0 - 1, b0):
                if 0 < b and b <= N:
                    mx = max(s1, PS[b] - PS[a], S - PS[b])
                    if mx < minmax:
                        minmax = mx
        print 'Case #' + str(t) + ':', float(S - minmax) / S
    if 0 < b and b <= N:
        mx = max(s1, PS[b] - PS[a], S - PS[b])
        if mx < minmax:
            minmax = mx
    infile.close()
    return b0

import sys
sys.path.append('/home/george2/Raise/ProgramRepair/CodeSeer/projects/src/main/python')
from CodeJam.Y12R5P1.francoisvn.A import *

def func_24b09638ec17428f94417df6cf8b8c10(i, P, E):
    e = 1.0 / (1 - P[i])
    E.append(e)
    return e


def func_b7c5fcb5ec6c4441bf0233fea28b59d2(i, E, L):
    x = L[i] * E[i]
    if E[i] == 1:
        x = 0
    return x


def func_2d66f35941744c0898ea2f025af9fa08(i, E, X):
    if E[i] == 1:
        x = 0
    X.append([x, -i])
    return x


def func_3b097c81e9764796b61b7cf19920365d(i, E, L, X):
    x = L[i] * E[i]
    if E[i] == 1:
        x = 0
    X.append([x, -i])
    return x


def func_9f67cf2e8de54d2a9c63bc7d24eaa3c4(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    return toks


def func_9dc44e24282b4f65ab2169fef867304e(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    return N


def func_433dfe05c0524fe6a4bfd8adde8516b5(infile):
    toks = infile.readline().strip().split()
    L = []
    return toks


def func_b72c4a40add0417d9d908def71f1ca61(infile):
    toks = infile.readline().strip().split()
    L = []
    return L


def func_3688038b8d424c638d69bbde71f17f6f(toks):
    L = []
    for tok in toks:
        L.append(float(tok))
    return tok


def func_d5e3ba9c213a461192b79117d1327fac(toks):
    L = []
    for tok in toks:
        L.append(float(tok))
    return L


def func_ea7505ad4d984e64a962a94b5391e914(L, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    return tok


def func_e2ada1c095394ecc9cee51e127035b75(L, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    return toks


def func_bfe3c9381341442ca83c74bcb3874240(infile):
    toks = infile.readline().strip().split()
    P = []
    return toks


def func_770ba4c539b944f7a65eb4dab07fb79a(infile):
    toks = infile.readline().strip().split()
    P = []
    return P


def func_52fc9c410b6d48d896c5d60fae47867b(toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    return P


def func_2080b4693b0e4d34be7d282ee4e60ac2(toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    return tok


def func_1b620174ec43492f8a1fd1c570682b2e(P, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return tok


def func_c3ea71c54f944a7580d11514c55358d8(P, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return E


def func_141a4f5212b5412f9811e08a18adbe22(P, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return E


def func_0ede68f488284e8991a3ab23ac4ffe62(P, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return i


def func_6a11e765481643a389e966e5c03294d6(P, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return e


def func_017cad6324e149789b9ce17b176dbc01(P, E, N):
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return X


def func_8ccf652d98e04dde9f434390927ccd7f(P, E, N):
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return i


def func_7d1f417f6b1f4163bbd37176d216fb21(P, E, N):
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return e


def func_dc7d3e38a4f34307a0f36270657d55b5(E, L, N):
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return X


def func_ac66f230c0154a3fa8986476e3c81edd(E, L, N):
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return i


def func_977d27b14ad84621a89fe433c8fba575(E, L, N):
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return x


def func_2790903790704b8dbcb82d965b888c1a(E, L, N, X):
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return i


def func_e6c81dd7ceb54b5e91dbad71c428d6a4(E, L, N, X):
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return x


def func_c54bd0253d564447a1e9a73137034847(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    return L


def func_cfb924e4a9584907b705f16033e8345e(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    return N


def func_4dca61bd931542e7af34a00e1ecf9773(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    return toks


def func_15c0d40688184a56a54715705b6a3798(infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    return toks


def func_f709402ff1924003a3884297c8b2abd3(infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    return L


def func_c2a2eb7de5a14e678b999ac248fda8b1(infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    return tok


def func_390a34dbbf194bd6b210b7019e032f16(infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    return tok


def func_70254e8935ec4677912c4838e1580d50(infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    return toks


def func_5a1f545a5cfe423f9f8ebc87b7b2525f(infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    return L


def func_4a2dbb931323462f8ca0241db58d7a4c(L, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    return tok


def func_8f65e7732815466fb4e22fadd8526684(L, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    return toks


def func_d59a1282c1ca45ccae5399027a90b2c0(L, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    return P


def func_58567c79b0864d89b4546f8bcc3772f7(infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    return tok


def func_416be3b938d44976b5209e41b5cdbe24(infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    return P


def func_b415e121eb7e4df4bd846af23b618f7d(infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    return toks


def func_327c20b494694465ae058285812e931c(toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return E


def func_cd15f4811c944edf87a5318dd4bddbb2(toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return P


def func_d5b556e265124341bf70be8a3fd6201c(toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return tok


def func_c276fe85f1d7448eb2b837fea6a784d9(P, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return tok


def func_9de649ce45444a85bd91820138aeb9e3(P, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return e


def func_a1bc977fca17429da5ad12dbf04d000e(P, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return i


def func_ffe5ba9b78524764b565ff3e891ccea4(P, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return E


def func_56551af7704340deb6c873a278914c24(P, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return i


def func_491b64531b6d46d68fbdf38ebac986f6(P, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return X


def func_a3db286709f348639765112d76281ed1(P, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return E


def func_eecb0d6639f84e87a40d57bc2b324aa8(P, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return e


def func_1f0b7cfedd9848e098d3d19ef7414c9e(P, E, L, N):
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return X


def func_b4c6d2f23785487cae67a19fe8170212(P, E, L, N):
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return e


def func_1b1b9b0cd9e74348b0183de9ffac08bd(P, E, L, N):
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return x


def func_67776de75c4d4b4287afb703c7960cb1(P, E, L, N):
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return i


def func_581591c645974ca39487f79283df1138(E, L, N):
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return X


def func_8e237359a7304e63a30ae76201263fba(E, L, N):
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return i


def func_04031093a83c457aa220381fba0e6486(E, L, N):
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return x


def func_14424c04b27945ddbf9f9452c5b6b4af(t, E, L, N, X):
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return i


def func_12a2e7d89fbb4b2f8a4ee26c3922d8ef(t, E, L, N, X):
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return x


def func_9f687eeb1259444f8c234acc57be4a8d(t, X):
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return x


def func_b716529f60ed46f49ffc6f1e72c4183c(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    return N


def func_be574d5b40264f5faa8ad68123d792c5(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    return L


def func_322119b615d942809bfa778836b4a13b(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    return tok


def func_ddef35fb1dc2478d8633cef880b1c2e2(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    return toks


def func_6f03328c2c5e4e569a63cbbbc2131299(infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    return tok


def func_837d56f108014829a5b20f1c444b5cf6(infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    return toks


def func_16b053d53a7e4baebbd255ef48f625b1(infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    return L


def func_e2952ecb6f9347e7b2b7280239bca59a(infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    return L


def func_631b8050af44405a94e02cd9a2f181b6(infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    return tok


def func_c0f43c6363584f1ba7e035f0b34b5392(infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    return toks


def func_a56c8880d83b44eb824ab82340eae903(infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    return P


def func_db0bbb51e65d4804bd4709bd5f096857(L, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    return toks


def func_d550aa8e41b24e9d9a403c74df086713(L, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    return P


def func_663f45eb27244920a5ef6bf72d3bf5aa(L, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    return tok


def func_54a4eb006c5b45c8bf4d11f07985f29c(infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return P


def func_bc223804e307440eae13d45eb1d732bf(infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return E


def func_dde81e324de240c18790ea5f93a50729(infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return tok


def func_81183c5e149144a28793d0744dc0b2bb(infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return toks


def func_87a5c57d154f4e8092f73a1d457ff04f(N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return E


def func_174c317d81ee40b2b55bd40c989784d5(N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return i


def func_51c9baa171f6415ea7c0243531408e11(N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return tok


def func_275b81b694d54a12aa94f74291ec391e(N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return e


def func_e2b1d9574065451aa1df97eb11684354(N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return P


def func_67d5a3d966a144a1b62351c87fb17c30(P, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return e


def func_6eb5605ff2084aa2a0c95c5871112d77(P, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return tok


def func_4314aff48f8745f78a73fedef15ca28f(P, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return E


def func_de0130e38d35425b9f25c8550b11d9f7(P, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return X


def func_a4567b90bbb5447bb45232ecb0ed732d(P, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return i


def func_e9e06fed0352401fa79ead2492933fe7(P, L, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return x


def func_303cf160acb644249cd2a97c14f48d16(P, L, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return i


def func_e188c1222df94ee595117826b0507118(P, L, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return X


def func_abb205afa0624f86a9969e09c9a34054(P, L, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return e


def func_ff8a75da792d4800a516640f5ea4c501(P, L, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return E


def func_3f8c9dae10164986986e3f53ebd82d13(P, E, L, N):
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return X


def func_41b635712e7d43a8a86543acade92678(P, E, L, N):
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return e


def func_23ec8e7e411349fc9597762dd8af93db(P, E, L, N):
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return i


def func_67949f7d859e44faba3652df80a01c2a(P, E, L, N):
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return x


def func_716140bb99c64f2abb3208a36ed21b05(t, E, L, N):
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return x


def func_88b43d6e2ce64923b16468495b1d2062(t, E, L, N):
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return X


def func_5c73f9de2b364d87ab6d495b9c067285(t, E, L, N):
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return i


def func_fffac378f9624084b2244fd4c1f2ac6e(t, E, L, N, X):
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return i


def func_69320f70649d4566a2f26943ab009384(t, E, L, N, X):
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return x


def func_5fd49d8b5f6f4d178947bbfbd1eb673e(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    return L


def func_22329f7bb9974eee89a6346c6622cad0(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    return N


def func_00abd93dd64e4ffca611bd91fb7d6692(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    return tok


def func_01729b46955b4a36840e66e2ac6b2d09(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    return toks


def func_eec793bb97b649aeb395731bd8af5362(infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    return P


def func_41293a409467469dacf53f4c4bfc2da8(infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    return tok


def func_68c093c6eca24230b090569a3b702f0d(infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    return toks


def func_8ad90e68ed7b43108cd8a90c414377e8(infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    return L


def func_14e3bba96b3c4b0eafc4b6579e1f800e(infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    return P


def func_1902d50e24834e94a632dd1a387dc04a(infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    return toks


def func_0cd0b4462d574dee92480d90a13c5d07(infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    return tok


def func_de471113d1914e32b6b719d52032e9ad(infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    return L


def func_31e91feac0fa470b94c8f4ee1164abde(L, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return tok


def func_14e3188016d84e84b422f498902b345f(L, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return P


def func_67c8ef73e1fd4ec1a4a2211334d6c052(L, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return E


def func_9c8266f82b3b455d83d9fe20a270d471(L, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return toks


def func_52b30ff7f81d47098113233825d8bdd9(N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return tok


def func_daee6729b72c4b919249b669b54136d7(N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return P


def func_b9452b47ed874b47b031d5e8e56499e5(N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return i


def func_0e2b15f8af0340fb8aeff8cd35f2e226(N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return e


def func_6910a1aa14c84da0bc5421529c7acdbc(N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return E


def func_49d39dafc7134c228e96627984c720b0(N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return toks


def func_764764e7c64d4d28ad7bc53bec4bc87d(N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return tok


def func_a6f5cc8ad7454677bf689379657901b8(N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return i


def func_5c65fabc20d24e3ab1fd158e59f7a8d4(N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return E


def func_7aee9bc9bf9f4714b0347174df094075(N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return P


def func_0d0ecac488a0423f954f9ad6aa12becc(N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return e


def func_33f704feb6604b6ab1ef39e3777ab65f(N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return X


def func_ee9af05f28104abc9eb15a7ad3a0b09c(P, L, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return e


def func_fd969ac592de4ff1b815706b6a1066ac(P, L, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return i


def func_cd6f266430854636b240fac9464e8982(P, L, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return tok


def func_4a1fb12a52014d17a667c2fd91c12b9d(P, L, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return X


def func_8cffebfab28c40abb94d9a00153ef35a(P, L, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return x


def func_f1bb6411b50f44be9d257073c70fe286(P, L, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return E


def func_957a91dd8ce64c2c81caa31eb3b1a70e(P, L, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return e


def func_85a409f06046487393725afb57b21885(P, L, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return E


def func_8035ae37ccf3450fb4428c2613e65225(P, L, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return x


def func_3a5f0316cc5344339ad09d8bcfedc5eb(P, L, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return i


def func_19352b59f762457c934c20296cf117cd(P, L, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return X


def func_aa1fe0afcfbd4c63a10c8725f94b6d40(t, P, E, L, N):
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return e


def func_421aa9ecce074c5eabdfbb61dc7a21f2(t, P, E, L, N):
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return X


def func_95d176ae3f554489801fa67cd2b9b849(t, P, E, L, N):
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return x


def func_d401c5aa470b4bb9b67333b031d446c0(t, P, E, L, N):
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return i


def func_61d65ac5e3094902a59915a626300fe6(t, E, L, N):
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return i


def func_e64a6cb9eee94253a3eea11887182827(t, E, L, N):
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return x


def func_60cf8ed63a04487fa134d0a29dc75041(t, E, L, N):
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return X


def func_52e9d870845f401c829beaba7067d260(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    return N


def func_17b254cb6cd646218cf02d22ff9de73a(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    return L


def func_c8b29929d73942588bf0d8bc6e46b55c(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    return P


def func_2565e2cd7b714e0c9704523ab87582f4(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    return tok


def func_4739bba690fb4707b4b25037018687f5(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    return toks


def func_74a50a80b8a3409e8b124ca7a35945d5(infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    return L


def func_f7a7977fef6b4ca1990e5930d1844b63(infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    return P


def func_1ffdc630492a4d3c8d07184d1f735294(infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    return tok


def func_fd1130619f9c42ca9ff2fba94da419d2(infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    return toks


def func_c5d451204123444c9984c1528a266c97(infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return tok


def func_d260cc5bd7974cf99cdd49feebb1d35f(infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return L


def func_a463831b93dd4d038bb827fac3fe1e09(infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return toks


def func_d84ffa0dafb843c5a211510ca3762c44(infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return P


def func_5ebaceadbe7f459d8f3747b8cefb56a8(infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return E


def func_75ac9bf941224ed6b49924459fe7a912(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return tok


def func_bc31d645b9444138b43a7cc10c37ffa5(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return toks


def func_2e061a1536f24ff68c71d21fbe4da70d(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return e


def func_8cfd67349a0b440abbc46a1569443a24(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return i


def func_36e2115b54934d2ebfee0416e59b6474(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return P


def func_5cd37d1768d7420786b12d4ad45eb9f4(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return E


def func_1a29f692391442a59d69e2564f843eb7(N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return toks


def func_f7ce8f379bc746aba0c20dd9c1487b04(N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return X


def func_efa8718b85e84c2e911cc1fa50a9d399(N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return e


def func_95e65e531495462f86d940c6dd24a232(N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return E


def func_2458e285e76c4888814cef4c323ea162(N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return tok


def func_8e9dbb471a51422a89a36c656fa7b46d(N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return i


def func_669a766dae7a4475ad277ab966c2c563(N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return P


def func_fead6c65f5134170a8863c7205d53989(L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return i


def func_29f27a4612794ee5ba555b7093507662(L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return tok


def func_86c9dba2366244debc5f6830399dbd92(L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return e


def func_ccfca17d31b740aa882c2f80e58ce45a(L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return P


def func_66ef441b34e54271870a8d8321bf0a7f(L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return E


def func_88617090ae724c2fbb0ed5d3cdfe8338(L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return X


def func_6f8fe6ea6e0a486db77edd40a52b1663(L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return x


def func_24c318fab4dc4cd8a869dbc63b6dcd8b(P, L, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return i


def func_ad17fb320d514ceaba4a8666f5315102(P, L, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return X


def func_1502c7c6e48c4e88bea8af49472a1891(P, L, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return x


def func_c62a5f3d736f4890aa3a591b60354e04(P, L, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return E


def func_441c1baaca244effbdc7aa169a47669b(P, L, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return tok


def func_0f2bde2ac39246cda8048865ff7a9455(P, L, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return e


def func_3a7572563a7a4a26aad6e82f073a5949(t, P, L, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return e


def func_c885fbc0993b4b558bd2bd67c61e1646(t, P, L, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return i


def func_7a5a8979c95f48fe8ccd73317468c997(t, P, L, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return E


def func_d3d7045007954a7c8c87945d5e0dbaa0(t, P, L, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return X


def func_587709dae0b44a89968327520b6315a7(t, P, L, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return x


def func_e8cfa2de1c2e418cb4f40c67a442108d(t, P, E, L, N):
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return e


def func_469c297af9f54f1d920ea8a53b08bb73(t, P, E, L, N):
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return x


def func_7a530bbbc6754a24bbcca7d0e9eac6ab(t, P, E, L, N):
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return i


def func_c1dcedd0ced849a7ab75f4b270d94269(t, P, E, L, N):
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return X


def func_bd77e0e051c74eabb17bc3b907b63380(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    return tok


def func_498ec5eb7a5249a895bac00a4576026c(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    return P


def func_417e58e7ec9e4a30900a2a0c19bacc82(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    return L


def func_14dc75ebe2b5425c86833dc5d0aa5d2c(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    return toks


def func_db4c7adb12164f1885de171ebbbc5a35(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    return N


def func_3260a6b1154e43158476d506759c6d9e(infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return tok


def func_341d3bc24718483b8787696405d70fae(infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return E


def func_5ae6eb6a717443da980ad60422311ec6(infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return toks


def func_05a0433c9d13463d9d3d805465352100(infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return P


def func_a2d0992b51da4a7bb8546dcbe518dd46(infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return L


def func_f70db959ed714171a6b1d987d61da0df(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return L


def func_4031b025a0484b7f92e4b111f5f59f98(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return toks


def func_f16dd5f7eaae416095b9a085e676eb2c(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return E


def func_e86aa2b65851419586c815389e8ee04c(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return tok


def func_d9be1215302c46078d5810c3e239d57c(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return e


def func_54b848b2ce05481297d69082ba9b4151(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return P


def func_dbd152adaf494365a660d0e50e660a28(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return i


def func_565bf8d52f7944f98e4ff02a06b383c8(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return P


def func_68da9b58e9ad4b179bd99e071c7277d3(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return i


def func_e947e2b13032499581e4eb5727125f2a(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return X


def func_dec2ff9ccef441948e3454700886fd88(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return toks


def func_44b158942c2d4ae1a3d142351fd895af(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return tok


def func_73a1552dc7d1494ea8e87d615bfd7ea6(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return e


def func_c5d7b5c41de249d3bf7adbeb513fa0e5(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return E


def func_03c95e0302254ae281ac3e3fee7205b3(L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return X


def func_597d016f390a4a64aa57b8894006ea1d(L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return x


def func_675892f679544363a495dda3ab86fe47(L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return P


def func_948d61ae2116423791a1541747e7cf73(L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return tok


def func_cdcd8cf451b54c558f1a82303b4e7ed6(L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return i


def func_3e00593167234fd28f437131e53a6f26(L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return toks


def func_a27577ef5d75470ab144ae6b62e4574f(L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return e


def func_bc85e0ed534c43a9927f3b3ea4452a6b(L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return E


def func_f7e3d576f9f941bcbf2272d7c1cf26ca(L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return x


def func_74c4f4c1b92d47529d6e5bd0db1475d0(L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return e


def func_4b39d83424694ec28c5c277930922d53(L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return i


def func_bc5a9327ace94b74a1ad572880533ffd(L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return E


def func_d48a579105914d758d083859e271ff58(L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return P


def func_8f14c28332e24bfcbfebbb2a6d6f18af(L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return tok


def func_0c91562a17204fa09939c632874672da(L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return X


def func_c81438f107564cb6b29f4452c8dbaa72(t, P, L, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return i


def func_18a5a62b8301420b91c608ddd038083b(t, P, L, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return tok


def func_7e5de128c5aa4e0b81a1de51c2d73dd6(t, P, L, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return E


def func_b1dc9d516d934229bcb115e73fa5edb7(t, P, L, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return X


def func_6f9d8f76c4db4c079fe47626ac9ae922(t, P, L, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return e


def func_ef2e1a5061f947e99a647118f8a1b4fd(t, P, L, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return x


def func_cdddc9d6a92841a1b693d46dbdbe19a0(t, P, L, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return X


def func_17882f7adba04da0a877ffa6d0e8835f(t, P, L, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return E


def func_91cf052b221441e4a341a80aa53772f1(t, P, L, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return x


def func_17d4816bff6840dfbd263d7ecf673c71(t, P, L, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return i


def func_6f9ae9b49b5c40558ba1912b5bbb7318(t, P, L, N):
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return e


def func_343b5c5ef5364f1bb200eb2792b4aaa6(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return P


def func_c2d87ee7a9e0407ea6bed093aadec572(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return toks


def func_fdcd433453f44912bc17bece2666aa87(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return L


def func_87a1d2006ae646bc8a58989e94d140e9(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return tok


def func_5c8ecd33984a41ae9274e53ceaa06966(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return N


def func_65b1fcfe2e814a19b4b79f6e62967c27(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    return E


def func_4691fed2e8474950b72bc90d1a808e1e(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return e


def func_884e1ec424e842e790bacab9c533b3d8(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return tok


def func_b87b8d23180f437aacd0ab649c5df1b8(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return L


def func_888dde10a76e40e682550c00db436456(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return P


def func_0cb9ecbcc7054dbc8aba3f16d6c77a71(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return E


def func_6d7a547ffd284b0982a96c3b74979706(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return toks


def func_57525691d9004a3395bf26f0a77fd222(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return i


def func_0f3a6eb0c4cd4843851c3b47bd83c4a2(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return P


def func_2919832f77454e18a81b52044c8711aa(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return E


def func_ed42d6998f3a4ced831ac46d4785cc54(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return e


def func_cc0e8f36d6254588ba08af823ff08392(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return tok


def func_fa29266679d4414a9608b405e4a1b135(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return i


def func_c7ed0364a9114b24b499df096507c501(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return L


def func_25832180dc1e4a4eb95be0b5ed6b56f4(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return X


def func_daedd521b5e24ff9a38b866e77a988eb(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return toks


def func_6e5abe2b111a4946a424ebe3b943d93a(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return X


def func_8869793c41f7496e8a79f9074a5545e8(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return e


def func_57fdb066aaf541fb9fb6b74eb176d815(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return toks


def func_72c1da64d1e741038f57e2b25efa2bd5(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return P


def func_9190feb773a8463587c015e72b1fa905(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return tok


def func_ac192a410204412ba24da99d644c6ebc(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return i


def func_e03baf0fc94842edbc62844f70ab3551(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return E


def func_77752b8f2ef74c27b567ba0d29355291(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return x


def func_e89bb54398b5438cb7d1d3f9d6e60c2e(L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return x


def func_cde6dc9873264ebf843fb82b04651056(L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return e


def func_65b15d6371e247c5b065aedd9548112a(L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return X


def func_9c34b7ff6deb4507993ad9d89982c6a0(L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return P


def func_e1a4689cda2e4a0bb7a90d8cc62babd1(L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return E


def func_93c4ed45dd1f4c1ba097c8391ec442ba(L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return i


def func_31d358904c7a4b33b2b5fcd10f690c84(L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return toks


def func_97271d4c184c448e81ebb50f551daa7b(L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return tok


def func_a9ff964c8f26422ebe56f9b001cf9e39(t, L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return P


def func_af993986b74244648f08516caa1895a9(t, L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return i


def func_3883638fc84d49e099b51ea5b135e16a(t, L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return e


def func_d1d62bf3556b4bbdb072fa8d7955ae10(t, L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return x


def func_13aa699c6ead4014ba5c1f1933bb7b7d(t, L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return X


def func_f8407a2f564e46329532aa3502576119(t, L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return E


def func_1965fa9ab94a4e6db3ccc701a5b5d975(t, L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return tok


def func_84872c2e5dd9463ab4d74bd1fc54ccba(t, P, L, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return e


def func_529811be507b4d03bacf01373378c9a9(t, P, L, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return X


def func_44e351638e2349d4b433e5e678b9c388(t, P, L, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return tok


def func_225aa205cb814961911150f7b4073ef2(t, P, L, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return E


def func_775a26120d1b40ef90c7137b7dcac089(t, P, L, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return x


def func_233513693e4d4ef2bd0bb47f30c15258(t, P, L, N, toks):
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return i


def func_972d766be4b94f4cb9108915b6c3e9d7(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return P


def func_c26407f8dde14d8db99711d452b42f67(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return e


def func_2b9a43fb4dcd43d4a64fd59fe5642a6f(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return N


def func_51e6182084534d05aba88e0647f143e5(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return toks


def func_7addccd0a5c542e6a8822500a82b96db(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return i


def func_963b2604c0c84cc7ad9b664e449b4472(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return L


def func_39c8011c3b2f419386219b3c2ee925c1(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return tok


def func_b935765e59944f4aa97eed17ef2e2ebb(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    return E


def func_e622a888f2824d6087f9c8d974bbbef7(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return X


def func_5d1e62d456f44c76b902f785a2423398(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return toks


def func_444de10e1c7c43ffbf173221c0219b99(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return e


def func_b1cdc02cab5844ab8168bea85eac7da6(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return L


def func_f82bba3cfd454558afead6db636f6e96(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return P


def func_a0b8d382424346cd800813a90bc9d429(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return tok


def func_9e5b0aa891284b67864faa3ad4e0d65d(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return E


def func_0462e611e00949e99d1e048f9c52bde7(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return i


def func_7a4e365559e74fb08c8606f07128e1fe(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return x


def func_2de758d05d3743b196298bf2647e406b(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return toks


def func_7b6843664c6d4dc585000c90f776c162(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return E


def func_e4f6b19e0fce4b93b24e667c35738da1(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return i


def func_86a7147a034b4e7ba23b61153d476c0d(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return L


def func_db0e15319ba4499d814fdd3447224f78(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return e


def func_71ee0a1293804b4bbbfdddaa1453dd16(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return P


def func_8e43024e7b6449f099b4b3faa025a9ca(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return tok


def func_1f19147d070c42aa87e97d53188d0eaf(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return X


def func_a11f562f18cb40cc97c7253fb7003b17(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return i


def func_b66427e59a2c443e951a403270c8cff9(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return e


def func_1ca6e0445f8f4cd68ebe164a1826501a(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return x


def func_c9abec93e0e946d8978c43903e4e03f8(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return toks


def func_f63d4e4623ae4c0b8ddf5c93920c1fe8(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return E


def func_e9cdfe25e46c460d9a97baec6d4ec45d(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return tok


def func_21a42f330a6c4732b1970d6330fb7db9(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return P


def func_2c4a74f59c1f48ccb32286eb75f5eb1a(L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return X


def func_07691a20a4c744979c0a047ee69051d4(t, L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return E


def func_c9107ace00e34c7a9379e690b8490bcf(t, L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return toks


def func_302a5d748cbf42f88bc7cc463ec06b58(t, L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return i


def func_6472e91c56e745a2aa499923cee681a4(t, L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return X


def func_62a39d82983d48a7a63b1ed2979965c2(t, L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return x


def func_e982069827af4cf7970db6504bc7a22b(t, L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return P


def func_7ee628e60b704ae0912c7f987649e854(t, L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return tok


def func_d526a6c0f9394390a43aef96cfcf0154(t, L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return e


def func_bfbf40cb2c50450f83aeec1a5d5c16ff(t, L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return E


def func_6858c57ab37e4d6ba96e5ca8e584ccbb(t, L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return X


def func_f2d6c8d6e8054940a2f715766e7ec69b(t, L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return x


def func_8002c02f5e774e459b300ed577396e0d(t, L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return i


def func_ab07534c90bc46d4ac5031a23e4bcedf(t, L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return e


def func_ee899b0e8a1d4e67877ffd823c5dd473(t, L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return P


def func_03a8b042236144f6996a8a672ce208c2(t, L, N, toks):
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return tok


def func_728bf26a14324740b73525387002f4a4(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return L


def func_de4a6174ab044e7bab0c210484c9ba7f(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return toks


def func_52a2ebe263ee4b06801b92953b1c23aa(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return X


def func_05c1f3f9e8124d72994e89d2fcc1f7b3(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return N


def func_b31208894471470dabb62ac7d636fa10(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return E


def func_8b336857877d48adabc054010196d097(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return e


def func_45e780aa5abf40ff867bc9682b8e0886(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return tok


def func_e77dca00803f45b286a96d7f571c9461(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return i


def func_17f0c69de46e470d8dfc7fa3f61f9b48(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    return P


def func_ff0b27d99b8a4371bd4d502e579a65d3(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return toks


def func_d21bc9e3a5e4405282e0c6512fec2d29(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return X


def func_68739d0eb77b447dbf4d0022773312a4(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return x


def func_d18fd85e782e4e3ca380bf8bb01c8097(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return e


def func_ba11f8c7b96a42a59343ff7c56fe6cb5(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return E


def func_909cc640f4ce47e8b5a24e4900f8a2b8(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return tok


def func_bb2b4d95c00143ceaa4f625b37a05c44(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return P


def func_f107894a163d4f3ba66b0e2ec9f7bdf7(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return i


def func_32caad42ec494674bc430d70a626e260(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return L


def func_185fb237baf94900986eb21b8b9ddb1b(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return e


def func_6a20b56cd5524c07b3ed8b565bfb3110(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return P


def func_c4bd740c4bd44c8ab31156223b4d8aff(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return i


def func_3383c81b6b54401dad4173f4b41eb122(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return L


def func_3a951f5d97bf429891259767e67dcf6a(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return E


def func_229d8000a44b47d18cd2d947c0a6920b(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return x


def func_cf2d8191d9cd4f1cae4e1ee86b1bde1e(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return X


def func_99076a104ab4433eb5cc07b3b50a25b9(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return tok


def func_b6c9e526cc2843b18978b827d73902eb(N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return toks


def func_985b4282f08d4617a113c6d0537161bc(t, L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return toks


def func_ffabd88a9bac48b6a7ac505f00b989b9(t, L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return X


def func_f9e4dd09e938412f908663ef1c0107e1(t, L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return P


def func_77ccaf5cbdea4fb288c5425e3ef0f829(t, L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return tok


def func_11d1aa0107414bbd8073d46ff9a31ac1(t, L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return i


def func_573f5232117b4f0bb49a8cd4172d2ceb(t, L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return x


def func_4332f4b374b64d1aac6c27c943834c30(t, L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return E


def func_582a62e60cb14472ada351b2218e97cb(t, L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return e


def func_5f2720cea38844c0ae4e6b2aa3eb8e3c(t, L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return e


def func_1c7a672f00ca4ead88b558611cc4a369(t, L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return P


def func_a97908af5c414b6d805f3192c03eb994(t, L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return tok


def func_24c7baa19f6a41538fdbe93d694369b8(t, L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return E


def func_21b24b96659e45f096de451dbd6b6db7(t, L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return toks


def func_7af60f8734c64980b6a5aae35e47ee43(t, L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return X


def func_4db4af99b7ca491e9f240a2e099620e3(t, L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return x


def func_5df0e79c67644abd95c9e509e59dcbeb(t, L, N, infile):
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return i


def func_ec396697296942128b4663483530a26c(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return tok


def func_eb16ceb0abd04decb1f3f86b988ab68c(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return X


def func_c1fffd2ef3ac477183adc58a6799c1a4(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return e


def func_eca813b4fef749b1bd0cbf1f0cf9582c(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return E


def func_4d4101488a5a48f08222f1a39f08b6d5(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return i


def func_a0ec44ea41654490bbe35b59c355b008(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return L


def func_3a15742b311543fb859f51fe0443eefb(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return P


def func_06e6221348154cbabb626a0ca474a294(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return x


def func_b9d2a272be2042a7b36c3050a27875d0(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return N


def func_5a8fba00b78c41c28213b33bb197f560(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    return toks


def func_dd52659b2b0b4819808fb21ee4e09d46(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return tok


def func_5e275e45e7bd4537aa3df50b6693fe3b(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return e


def func_cd7aed2f35a849229203957c02fd4c9b(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return P


def func_19be4ac38aa3480d90c711601f7e7fc8(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return i


def func_d59842f8bf314e11bbb0cf0c711167db(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return E


def func_b0a5225143954fd58715f9e3c8161cab(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return L


def func_44fa213871cc4109b36f99e449149c51(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return x


def func_cd65ae78cf6d4ab78b2891e55118f2cf(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return X


def func_4f1fd74c17814516bc9bf544313706b7(N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return toks


def func_15773cd145c04c88a64da0c143cd0694(t, N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return toks


def func_ded78ad9fdd64b16a325556948285f5b(t, N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return P


def func_5f3358a9273b48d9bc97990b7396f260(t, N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return e


def func_2a68efb6e16745f1858163f4d43a0f2b(t, N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return x


def func_2a59a212def54110975b464783f1375f(t, N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return E


def func_bb06dce77d3c40149318d04ca21de414(t, N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return X


def func_6a101ebb09bb45869b1f8b55700fe7d8(t, N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return L


def func_8ae3b6e6e08249f8afbfd385ef4d009b(t, N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return i


def func_9b4cd29aa7bd4d7389a16e2127c80b34(t, N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return tok


def func_705aed4d6d3a4571a602a000fea5aaaf(t, L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return e


def func_4b8c16e0033f4e6f8554cbb36ded4645(t, L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return i


def func_4db0b10ddd484751bfc5f1950b873a12(t, L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return tok


def func_5e30c878cc284522a611035a1e8a7468(t, L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return X


def func_385b778c73f847398a95b34434682efa(t, L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return toks


def func_c5b36e32d7724f9895353f65883fb385(t, L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return E


def func_be5f8f74e4e14e8c8ba3e856c909219f(t, L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return P


def func_b8eff4dcd173464e8b9bc60f8799942f(t, L, N, infile):
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return x


def func_7dbba44772e44a2eb2fdb33de9061a51(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return E


def func_d69ebf0c765548409e96c5d87a92a9ac(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return P


def func_92714fe471ba4ccfb80bc08084017e37(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return i


def func_7f6dba2ae0c04876969b70f1c0650e2c(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return X


def func_512cbc48eaf8468b81af215384ecfbc9(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return x


def func_3c6d491fe2cd4aec90498e597620f529(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return L


def func_10702c71c1f844758c4a334b4cdedd1d(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return N


def func_1f498890da694b65bc14b8d161e6c09b(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return tok


def func_a96bb25d9f2b44118eef98aa9dcfa544(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return toks


def func_bb61c7496143449592e40476475e4ebe(infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)
    return e


def func_b4b31f397a584ce5bfae9c527d0e8d53(t, N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return P


def func_b7c59e183e1e49e0b16018aa1506678c(t, N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return E


def func_7f26f719def44d8bbb9e292c2f3342ea(t, N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return i


def func_a5b8ffe2445c458aa921a0c27900501f(t, N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return X


def func_6e3583346c6d4e57a775d4340d95c05e(t, N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return toks


def func_7a5151aca8c94b04997cc90d394dbfc0(t, N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return tok


def func_b657b716ed5e4e9796d29c0c9efdcf4c(t, N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return L


def func_a2a4e47199a54fdab34613ddc22dfd5a(t, N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return e


def func_56740ea5b5284c3b812148cb48e43731(t, N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return x


def func_cda86ac548b3492e8f4597226e69427f(t, N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return L


def func_206cefda16a34cf48e147e3ff2886dc8(t, N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return i


def func_3506a0400b63409f91455ea894da363e(t, N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return tok


def func_1c32acf620d144cea4e7508441beac58(t, N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return E


def func_9deb6cadb52a45d1a21c72d1cb6ed592(t, N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return X


def func_9cf6a2c4e6e84208b6206eee4c40cd35(t, N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return e


def func_ceb56c0faf2c40b8848d0f19ce1ad91e(t, N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return x


def func_213f1ac3ce1e4d12b5e2a682c8cb53b2(t, N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return toks


def func_b9f143afe2524d9c928654892bbc24fe(t, N, infile):
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return P


def func_ba9216e90de64254aebd7d39e6116adf(t, infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return toks


def func_d3f7e0e1d7344339be77e7d284115a7b(t, infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return i


def func_db07a0c98c654a6d8806f787620aa385(t, infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return x


def func_91814026714440dcb1efb3a899d504c0(t, infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return X


def func_eb066151fd6d4dc39e2e0f3db21f7bf6(t, infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return e


def func_b7e295fd5c7a49009eaccca20dedfb08(t, infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return N


def func_f6ba64b505b44248b52f4c948443987c(t, infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return L


def func_89c87edf3faa45739a2bff80916c14ff(t, infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return tok


def func_d5345cc193c242969f56bd9673c6bbb4(t, infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return P


def func_cff3e7bc2c56428c9543022f418b1bb6(t, infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    return E


def func_20cd7abec8a44d47ac60cb13e47fbdda(t, N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return i


def func_ff4482986c244020869c0616b0be859f(t, N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return X


def func_1e4e79153cca4f68870e112acb501e0d(t, N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return toks


def func_8c445119edd64193aa8e90c24844f916(t, N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return E


def func_55a192822b7246c4905b52a5ccdaacc3(t, N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return tok


def func_e130c752834a4b7b9f9ad89f0617a2d1(t, N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return P


def func_881cedf9d4b64c75bf11704ff5d643ab(t, N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return L


def func_6be8534620c648feb128bd43b4748552(t, N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return e


def func_b85970e0fc5741a0819c11583e34c3a4(t, N, infile):
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return x


def func_e1809a7042b149d2a2cf7800c8391f9a(t, infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return i


def func_7ec2acbd9b9645b281f2b167183bbf72(t, infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return x


def func_7736e74eb3a54e21bfed06c87440c23b(t, infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return L


def func_e2e496e313774edfbfe5dd3beea19603(t, infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return X


def func_fa20e69b9cb4481ea762d8a781c8373f(t, infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return e


def func_05be88bdb6ad4caebf4e83218c854659(t, infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return tok


def func_0457d00651fa482e8411b22413b079c9(t, infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return N


def func_fc276d345f1e4355bbe1d728471710e0(t, infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return E


def func_78436b6a3f1a4bbfb2e92a5a8e94baf9(t, infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return toks


def func_4c0a2ac8d6414593ac8b72f25e9057a8(t, infile):
    N = int(infile.readline())
    toks = infile.readline().strip().split()
    L = []
    for tok in toks:
        L.append(float(tok))
    toks = infile.readline().strip().split()
    P = []
    for tok in toks:
        P.append(float(tok) / 100)
    E = []
    for i in range(N):
        e = 1.0 / (1 - P[i])
        E.append(e)
    X = []
    for i in range(N):
        x = L[i] * E[i]
        if E[i] == 1:
            x = 0
        X.append([x, -i])
    X.sort(reverse=True)('Case #%d:' % (t + 1))
    for x in X:
        print -x[1],
    return P


def func_b540a5d36f5d4025891cea7a10283dd5():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    return infile


def func_e2cdb6dfd45149e1857fca825b32a766():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    return T


def func_ac7e758e1e7f4ca3a903a22242cdf80f(infile):
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    return T


def func_f27a888473d64a3e913c861715d1d303(infile):
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    return N


def func_51b95c65b02d46fdbfc2cb2eb1b4f053(infile):
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    return t


def func_5c560317333e41488b06f6e1ffbfa55f(infile):
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    return tok


def func_d1e98471641949c4a665eb4d808eade2(infile):
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    return E


def func_aeb3e594f95b4d98a5ad1f072733ba31(infile):
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    return i


def func_7cac312cf91040fca8bb787c398083c7(infile):
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    return toks


def func_a4254c93913648dc846125681c058c63(infile):
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    return x


def func_1a2e51ed7fc1458ba2fe1ee9ce686cf7(infile):
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    return e


def func_f4027c567e4f4d539f30fd2720e5c059(infile):
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    return L


def func_d11231f8fea044acb3a89b9b5ffb469f(infile):
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    return P


def func_ef1382aac87d4eb9954bc532a512f4af(infile):
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    return X


def func_9e5dc7eb11314aee95556586cce05156(infile, T):
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return L


def func_a4fd09342a5a4a879c0feadbb71ad996(infile, T):
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return E


def func_18b8dcdd26e641dca52b3d1f93ad2a95(infile, T):
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return tok


def func_1d01cb5013e24bccbe01f691bf776778(infile, T):
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return x


def func_ae6d998c05c44f459c3037a87280bca7(infile, T):
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return t


def func_675cffd087a54dfd8799716ef9f3b220(infile, T):
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return N


def func_aa3c44f69f194db6aa0af5b130c59762(infile, T):
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return toks


def func_8ada4f3bd5b74793b1457e83c9682197(infile, T):
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return P


def func_bdce7534c05e4add82b41f8476e51994(infile, T):
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return e


def func_9df4d3881d0b4c788fc77112b97ef73b(infile, T):
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return X


def func_86843a33401344dca6e7689f4f74fe29(infile, T):
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return i


def func_16a5e81c3ed74d6da9de39b0598f0cf5():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    return L


def func_ad273104cc1c43f6a153bdcd8c016a3b():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    return tok


def func_bc8c4478cd9c4c5bb03cc610969e2bf6():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    return T


def func_5300f83a35ad4d4d8a528ce2d0644470():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    return x


def func_353cdb40b80f4405ba17a6d2c22c0e62():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    return e


def func_f8f6e3a299ab4ada9ab9163c72560c9b():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    return i


def func_301c5a1687464952afa6db87877d84b7():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    return toks


def func_b8c01c61794c42a5a5ebd0c6a59c7eb7():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    return E


def func_4a4ba8cd81a3483d81341de2523742b2():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    return t


def func_1ba8e1fb3dc340f897e6d23197501fdb():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    return N


def func_34c242ac795344888c1ab2719514407a():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    return X


def func_0afe6d6c22e147eeaf9f27f16dc332da():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    return P


def func_7c175d5416b749cb9f4632a2b506732b():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    return infile


def func_6d7c58455390444abfe7ef091857228d(infile):
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return L


def func_a22e814be56c40339fe3877a390e0289(infile):
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return toks


def func_c1a08a3c50054befa6fd93a51b8b8b5e(infile):
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return E


def func_22358ca877a541bc8f9768e0d729729c(infile):
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return t


def func_ef73aef1574e48dfb9a64531bf32335e(infile):
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return tok


def func_0ca916b3702b4b95a2cba724aa394acc(infile):
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return e


def func_615c063c1a674c958ca5a0a9e35c3bb2(infile):
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return P


def func_ab352a4ba3c04395885a6ef89f995295(infile):
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return N


def func_c21af8203b17435b910d9634729ee0c1(infile):
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return T


def func_2f24834f907e4e32b5af6d9f72502920(infile):
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return X


def func_7ef9d2f7f4f14cb6b803468b9a48bb00(infile):
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return x


def func_334d3bbd13d549a3bc62880ffdb4adff(infile):
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return i


def func_28f5c99aeb4e45ca8b764edf19211aee():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return P


def func_bccdda75bf8a4685b1202874aab9ea23():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return infile


def func_90e5e2dca9fe4b568b1e082a80abf5a6():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return i


def func_a4d125a7bc3c48fd857b99dc4b379d5e():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return toks


def func_1d3663b9a1be494484678602a71fd483():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return T


def func_b67b1e0ec0f1442f950e344c8b508a8c():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return t


def func_6701db7be20b4217b3e9261c3f592a88():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return L


def func_0a56187d4dd242079f93d942e2a39019():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return N


def func_29402f6f5e3147a78c6f911671726cb4():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return tok


def func_2b111a8efaeb4924b53ae88b6cea9f5c():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return X


def func_46b456dbee4c482da6bb7c4193e90de5():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return e


def func_96f4f8e766774fb19fba86c55d89029a():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return E


def func_64589b8e7cb04facaf23f4214d5147f2():
    infile = open('codejam/test_files/Y12R5P1/A.in')
    T = int(infile.readline())
    for t in range(T):
        N = int(infile.readline())
        toks = infile.readline().strip().split()
        L = []
        for tok in toks:
            L.append(float(tok))
        toks = infile.readline().strip().split()
        P = []
        for tok in toks:
            P.append(float(tok) / 100)
        E = []
        for i in range(N):
            e = 1.0 / (1 - P[i])
            E.append(e)
        X = []
        for i in range(N):
            x = L[i] * E[i]
            if E[i] == 1:
                x = 0
            X.append([x, -i])
        X.sort(reverse=True)
        print 'Case #%d:' % (t + 1),
        for x in X:
            print -x[1],
        print 
    infile.close()
    return x

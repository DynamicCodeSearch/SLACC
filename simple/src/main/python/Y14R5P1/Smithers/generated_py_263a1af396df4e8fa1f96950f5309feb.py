import sys
sys.path.append('/home/george2/Raise/ProgramRepair/CodeSeer/projects/src/main/python')
from Y14R5P1.Smithers.A import *

def func_ea3c32ac3a344e51bf403a21bc0c326a(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    return q


def func_386516c708c74d7180fb882be129261d(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    return p


def func_ab14e8d3b5ff4bc09b8b8ccd9cc00952(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    return s


def func_702dfd9645be4e328b1d62929e2e8c93(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    return r


def func_9583dba1085140bf8e228da956fff202(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    return i


def func_11e36d8ca9184716b5af1a54282d99db(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    return x


def func_84cb44f603c642098ccecf622882b190(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    return dev


def func_0a1ec7a5583744cfa3db6c0bdeae010e(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    return n


def func_2d4b2147433e45a09eb13a81fcdcde87(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    return dev


def func_d434c7dc34034f14b8fd758d8dbb616a(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    return i


def func_3e611df74a4c4274b48fdd589d8ea39c(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    return tot


def func_36c6ecc1c1f14c6b9c50527375afde8b(dev):
    tot = sum(dev)
    i = 0
    return tot


def func_4b71c47defac4535893472a037532f5e(dev):
    tot = sum(dev)
    i = 0
    return i


def func_6dbdcddbbf0640a38154ad0eb195fcbe(n):
    i = 0
    j = n - 1
    return j


def func_c0c9e03388b74aff9de6c9b80160d9c0(n):
    i = 0
    j = n - 1
    return i


def func_c0276670d2f84727be199711b51bd9e7(n):
    j = n - 1
    ltot = 0
    return j


def func_ad3dd30375be4940b61c56336955abaa(n):
    j = n - 1
    ltot = 0
    return ltot


def func_d838544df6354e2a858fa02f4f881867(tot):
    ltot = 0
    mtot = tot
    return ltot


def func_db02d60c0ff648779f08f411414afb5f(tot):
    ltot = 0
    mtot = tot
    return mtot


def func_e2d346a5a11c4a5ab62a6dd13accd8d1(tot):
    mtot = tot
    rtot = 0
    return rtot


def func_05cb7726bfb9450da2c621af1b9884d3(tot):
    mtot = tot
    rtot = 0
    return mtot


def func_54225522e17d4325805b4c130d2a154d():
    rtot = 0
    best = 0
    return rtot


def func_6bbdcf73b02c4a5799127af4530eebba():
    rtot = 0
    best = 0
    return best


def func_547241f3cef947439af141e721a37565(dev, tot):
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return j


def func_cc0cdc8680cf4910a264fa2fa894c228(dev, tot):
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return mtot


def func_d4f6f32333d140e3a2798e8342eb8f6f(dev, tot):
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return ltot


def func_4c99bad6c32f443b8cd1ef17357b7ab6(dev, tot):
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return best


def func_2a29458b5a7f4d26b9e669ac92d6b9ba(dev, tot):
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return i


def func_3c5283515c3b4c9ca99d1af83e27d03f(dev, tot):
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return rtot


def func_8738c02cc2334188bdfc62a796bc6cb6(dev, ti, tot):
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return mtot


def func_8e1bf2caf31b45198de3d9fbb0f5528d(dev, ti, tot):
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return rtot


def func_282177f996614dce808159ef6bc294fa(dev, ti, tot):
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return j


def func_f9f3626e435d45d09309cae1e10b512c(dev, ti, tot):
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return best


def func_33475cc43f7042359db03bfa7ac423c3(dev, ti, tot):
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return i


def func_f367f194ac304dedabce9dcc60d20f03(dev, ti, tot):
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return ltot


def func_e9a1f6c71ac54c578afb8648c1782ff0(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    return q


def func_6af7b65fc3bd454b99be20cfd093db95(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    return p


def func_f5a9ea0088d64a8b88a88bf2b6f64137(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    return s


def func_d29846cb0fb7400d9fcab2530dd9866d(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    return n


def func_11d235b7b59d4cd38bc63927639b71c9(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    return i


def func_04e7bc7c82904ce2b459d89bf66ce6a3(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    return x


def func_51640e5c6f46470b909caf5f0ac0617f(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    return tot


def func_608b6333173042bba5dd719ec20eea01(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    return r


def func_ae827cd1d01d4801ba541079986c19e8(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    return dev


def func_5a9b9f5494d540dd9d6cf930280a50e1(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    return tot


def func_43f2bd9b4c454d0a81683526ead25aa7(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    return i


def func_3993d2807cae47bcb103bc79254d6390(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    return dev


def func_b7e9d5dec7b94f61839665ff8430c667(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    return j


def func_8069991748c64267868bd14434574c11(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    return i


def func_e87238d7f4aa4aa5aea5bfeee63a94b2(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    return tot


def func_efa5c3f0b0fe43e3bf5a6244ee76bcc5(n):
    i = 0
    j = n - 1
    ltot = 0
    return j


def func_f70c6d4faa804a49aeea0be183b4934d(n):
    i = 0
    j = n - 1
    ltot = 0
    return i


def func_01d57c7c1296432ba93a3bdfe4067c4a(n):
    i = 0
    j = n - 1
    ltot = 0
    return ltot


def func_e13b8bb355624a61811945f9f8c7d010(tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    return j


def func_3ac9c2f94cc24a93a1e022aa3293101c(tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    return ltot


def func_c9f94246cb5044809b23061365245a1f(tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    return mtot


def func_95a123ae7f3c450d880586ca37db191f(tot):
    ltot = 0
    mtot = tot
    rtot = 0
    return ltot


def func_bef8e0f5378b4fdb9163cb423ef189c1(tot):
    ltot = 0
    mtot = tot
    rtot = 0
    return mtot


def func_5471e3489fd947b0b8a3aa10c9c30f93(tot):
    ltot = 0
    mtot = tot
    rtot = 0
    return rtot


def func_49367036d93445dc85669435a96efcec(tot):
    mtot = tot
    rtot = 0
    best = 0
    return rtot


def func_0633bced4e374ef58539f42471baa641(tot):
    mtot = tot
    rtot = 0
    best = 0
    return best


def func_2375fc92bea44c78b160bb029e018b8c(tot):
    mtot = tot
    rtot = 0
    best = 0
    return mtot


def func_e91ab631259e4574afe86a9ae0327b14(dev, tot):
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return best


def func_b475c527826a4176ab0a3d1499d7b76c(dev, tot):
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return i


def func_9d1b98dc472649a3880943f297ce4554(dev, tot):
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return mtot


def func_1398caab360742ee939ac3024cb7586a(dev, tot):
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return rtot


def func_1a547c3ff03348b993975a2a8812e871(dev, tot):
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return j


def func_e1e8dbac2c62499b9ea53b7c75271b8e(dev, tot):
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return ltot


def func_fd5254f6021a47c99b8157e0df080267(dev, ti, tot):
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return rtot


def func_8a7281cbae194d239d5c0637a2e77fd6(dev, ti, tot):
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return mtot


def func_7c07af207ceb4aaf99273743a7c9103e(dev, ti, tot):
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return j


def func_9dfdc636131a47edacf3fe61745a446f(dev, ti, tot):
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return ltot


def func_7e4dfdc04f6941e28ab2be5f4c0f64df(dev, ti, tot):
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return i


def func_073d78d95d924137807ae1e56a461dfc(dev, ti, tot):
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return best


def func_d81c467c2a4848489c3abb65009f369f(dev, ti, tot):
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return i


def func_01544bb9d3c542c99c7f0a7e08ba1477(dev, ti, tot):
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return j


def func_4fc99d337c20410d8089dc9ea4b5b573(dev, ti, tot):
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return mtot


def func_479e1143f0da450ba2efb3e2dbdedd92(dev, ti, tot):
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return ltot


def func_4c33068d79a14321b24052ab797496d9(dev, ti, tot):
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return best


def func_3a5b06aca7cb4397b171141ed4cd6a17(dev, ti, tot):
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return rtot


def func_3180f6db4a234b9cb798b401525294f4(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    return n


def func_5906b1ca6c0249a98626d6e7768af1e1(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    return i


def func_e3efa10e5dc742d6ac9eee9e68b8dd6c(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    return tot


def func_a8976ea60858480b8435b03ea5d2209b(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    return p


def func_40dcd506a3794834bb4947ce168485b4(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    return r


def func_fa5c7e0e042f44f889537f77f47fcae4(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    return s


def func_ebec8146fc9841f9ad68a227b971502c(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    return dev


def func_b420b03e351843a2a76a3bb1a304dd16(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    return x


def func_645e7dad5f4c4c1db11925e9517ff3b9(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    return q


def func_c109f1ec82ad4a6483ca57fc7728bb79(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    return dev


def func_b0e3cd7ae0a84532bcccdaba82c3f363(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    return j


def func_1a88cb05ef2d4bb7a266e84531ad9a8c(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    return tot


def func_6adbdbff94924167a1fc39f642ba3ec5(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    return i


def func_bdaf8913fcaf44ceb69c5af92978a32d(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    return i


def func_c837eabe85494e979afb028fef0fca25(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    return tot


def func_70bf3801836c48129c8519be48f9d937(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    return j


def func_4df9189b967e43539184cd9e1afdb1fb(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    return ltot


def func_cd7813ef02be4e3e9238f7dd40aa4d06(tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return i


def func_4ccfb130c1f14c138caec84e94ef614f(tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return ltot


def func_15bdb0a282c342c49ced38d577cb3f17(tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return j


def func_a6e12eade4d04ccd8e95a2c660576015(tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return mtot


def func_72e2d1e48b8548ba86ccb0ed5add516b(tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return mtot


def func_08131d9388fc42bdb609372e3a2b37a1(tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return j


def func_527be06d2c2d43b0814e12ae53283b94(tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return ltot


def func_9bc0c05db56240248a2eaa720987fb29(tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return rtot


def func_3ccd3d2e3b8d434f943523ef4b0c2df0(tot):
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return ltot


def func_469b0bdb84c44052afe57210939ad870(tot):
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return best


def func_ac8bc5098f314342a8213aead4aa4172(tot):
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return rtot


def func_16a16e1141944913a7f621866bd637d3(tot):
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return mtot


def func_4e9b43c6262e427d86effd62a4e2760a(dev, tot):
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return ltot


def func_ee869506400845f59bcf36e764613fcf(dev, tot):
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return i


def func_8d1159ccd2504e4e97038a7eeab815cf(dev, tot):
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return best


def func_f10b7fad28e545c7a9a156531def516f(dev, tot):
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return mtot


def func_f904127f6cb94d76847c46797b002525(dev, tot):
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return rtot


def func_303e454260a44fb8b9a5ef20b311864b(dev, tot):
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return j


def func_491e3f6bdc6b480d9a4fc23418089049(dev, ti, tot):
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return rtot


def func_5971333b55fb418a8d23fd1076c9d426(dev, ti, tot):
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return j


def func_58aefa011cee45c298452c20574a72e0(dev, ti, tot):
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return i


def func_ebe10953778245568d9dd40653b229fb(dev, ti, tot):
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return best


def func_b88b9aa9df514a07a579c029468aaeb4(dev, ti, tot):
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return ltot


def func_f181f99ed772461bbdd2a6ac6e6ae119(dev, ti, tot):
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return mtot


def func_fa783ee8fc4547148d000a9259c59ca4(dev, ti, tot):
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return j


def func_3a178b7187c241028982a338c775d4d1(dev, ti, tot):
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return best


def func_912eb22ddbbb43588025ea138b0b00f1(dev, ti, tot):
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return ltot


def func_e61e4e278ebb42658c9a37177fa0bc18(dev, ti, tot):
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return mtot


def func_550a898a8d7144c09eb61e8cb88d52e4(dev, ti, tot):
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return rtot


def func_b40f2a604980443bba3f68a3ce6f5479(dev, ti, tot):
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return i


def func_17c39b6f920f427595c4bd6359a5a4de(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    return j


def func_0805913c18e74c249be396818caf12ec(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    return i


def func_f609d6853866490a82f8b30161a43c56(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    return q


def func_cc6539ced33141afb906310f0dc3c03b(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    return dev


def func_3e53c2cd80194ac587bbdb95cebcdade(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    return r


def func_4c259f450d8743a1a78225bdfdb6f8ab(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    return s


def func_d4e8bb38d3f647f38e8bb895bbfe96bb(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    return p


def func_10e10a62bf3f4a919e708a59f672c96e(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    return x


def func_83e9d77d97804cd5b10468317356852a(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    return n


def func_6778a4159a664fbeb4c241b9de10ee7d(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    return tot


def func_0e336a93d96b47ebaec25403249d51fc(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    return j


def func_3ca9166ebde44938a692d3dc80ea0367(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    return tot


def func_9ec89400651542868b39028174433a5e(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    return i


def func_693b227803b94627999f1bd00c014d00(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    return dev


def func_0d4d457c7f044981974422bcdbb0290a(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    return ltot


def func_30da14cb41ce4108bd481f98050174cd(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return tot


def func_5e8e073ce42f4b0e91a6647be0a93e8d(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return ltot


def func_daa752527cf8448eb3537efc6bf3265a(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return mtot


def func_07ecb73b43d4471dabe6ce9249b106f7(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return j


def func_188fc331a91941b5a9ef238f5ff7254e(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return i


def func_1f969e2a84fa4b7081201b7e669e664a(tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return rtot


def func_148d74ad2c8e4449be514af82bd99614(tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return j


def func_01470a041b3645f8aeab234a26799eeb(tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return ltot


def func_6d1c348d601b4835b3c87775a5ca5502(tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return mtot


def func_1aa9ae1cd5fc41959ee98c105faa937c(tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return i


def func_566ca948ff5b4b6f90bc6fa790af5f35(tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return ltot


def func_bb57cbd34f0f4408ae0f0fd3db24fa47(tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return j


def func_f3aa19355265496fae7de2b8e3fc4139(tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return best


def func_6a6bf662c3bd44a4b3dd1c92575def94(tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return rtot


def func_53f2d023c8244dc18d216348b917782c(tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return mtot


def func_6d71a56d688a4018b7aabe352996d7e8(dev, tot):
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return rtot


def func_8d0a091791494c448a1318b14731bce7(dev, tot):
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return best


def func_f88b47631a724113a303739553e3732b(dev, tot):
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return j


def func_bd49a0d077c8420797a7be98c18cb4cb(dev, tot):
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return ltot


def func_f2d926dbef984c9b8bbd85b3b4e98146(dev, tot):
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return mtot


def func_1c21a69483334c23b3e66d144d23799e(dev, tot):
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return i


def func_c48cf75439fc454a9eb056622daa4b52(dev, ti, tot):
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return best


def func_bf22fe303be74c6ca73645a59da730ff(dev, ti, tot):
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return mtot


def func_63de04e20c3249f2904e5d51e0eb80dd(dev, ti, tot):
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return j


def func_dca113c033834490b61792b359d3bb04(dev, ti, tot):
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return rtot


def func_5fa80ab9af3942bdb8f92d2d05a5802d(dev, ti, tot):
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return i


def func_384ab3b10a93454cbdcef99852cc986f(dev, ti, tot):
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return ltot


def func_1456b81e3b0f411eaba0a218d99e192b(dev, ti, tot):
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return mtot


def func_3f4ff28db33d4885ad3a63a4e3065938(dev, ti, tot):
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return j


def func_8a155761d19248f0b545dbef717848c2(dev, ti, tot):
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return ltot


def func_2da272355e874317b5f0297a86b3f0d0(dev, ti, tot):
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return rtot


def func_2f37ab34526e4891be530d32685ced5e(dev, ti, tot):
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return i


def func_ac75c15e517941088bd248e231e70668(dev, ti, tot):
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return best


def func_4ad9de24cc0a49d18d5f2aec520f43ea(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    return p


def func_1e1df6288f6249cca5e66099267f5202(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    return r


def func_655173ac2a764a889aa972b64759eeb2(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    return j


def func_d7405620892c43ee9e9407389ee80596(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    return x


def func_899f5aca720a4945a1dd3f55dcf0db78(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    return dev


def func_8f809f9e7e99438dbf7cda9a2fe03ed8(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    return ltot


def func_747d1c7dd3af421bb67f976e018ede6c(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    return tot


def func_bc94ce5405dc4ef0bdaddc84d0aad10f(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    return s


def func_d267acd4acf84b38b5a008189bbc01df(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    return q


def func_25a94d46dec3423da208ffcd22b9c256(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    return n


def func_b2d2f1dca2da4632823d11dc37c5dda7(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    return i


def func_fdaab430cde6486e9070efb28f150461(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return tot


def func_a77be68914464c6d9b6b3b7ab74e09d3(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return dev


def func_4fa58e9997294ee392a7aedeb19ad9c8(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return j


def func_065e212ce4e44e579d331ddd63011451(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return mtot


def func_33954dedd5604e2590fde8d372726951(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return i


def func_0b35d0e1a17a41baa6a92661ffb04794(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return ltot


def func_def4833cae4d46a68e3b1a9670eeeb66(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return rtot


def func_02e4da32debf474281b452239311df55(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return j


def func_278708de0eec4a6c84123a22f3083ecf(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return mtot


def func_e41a139e09e545f2a00d281f11c5988b(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return i


def func_5e0b9d5f06a94a4cb3e0801b45ea7a2f(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return tot


def func_fc8997b78faa4243a6984ed7d69b15b1(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return ltot


def func_f8c42547855949e3af4e47ac1f7b00ec(tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return best


def func_cb99b0f7646d41b8ab080352512d86ee(tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return mtot


def func_4f1b9d3c82924b568560147d79c34036(tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return rtot


def func_afd52de558b04a11955acc4a28def3b6(tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return i


def func_ac09a6fddb2544efb7088426e5e56010(tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return ltot


def func_d67500c4eeff4e3189af34385d646331(tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return j


def func_884cc024c7fb464a8432feb6fa40500a(dev, tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return rtot


def func_8b390c21ee544a28bbcb78156a003090(dev, tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return mtot


def func_5767a06635b94a04a03adc53ca326557(dev, tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return i


def func_352d6a4b915146578c09276de457e9b7(dev, tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return ltot


def func_eb014fa42d4e4306b69857dd1edb5f1b(dev, tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return j


def func_50529ce9465b496096d60312c68f12f5(dev, tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return best


def func_db499af67c344cbe9b3f071a2158cbc2(dev, ti, tot):
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return ltot


def func_844928ab35e74731b66c1aae79122418(dev, ti, tot):
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return mtot


def func_bd9ce88488d94752ab8fba62a84c5a8c(dev, ti, tot):
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return rtot


def func_617d453b814a45ee9d778e9473fe4576(dev, ti, tot):
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return best


def func_1e52a7c58cdb41f2934af5887a41d509(dev, ti, tot):
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return j


def func_aeb58dfc8daa43899f7672f6c3a23238(dev, ti, tot):
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return i


def func_ec7f76a04e9241749410a301ab7b731c(dev, ti, tot):
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return best


def func_5d363f42c05246d394c48e708796f33a(dev, ti, tot):
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return j


def func_bb1b7ac9bbf446469b1755b511a3483b(dev, ti, tot):
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return i


def func_3a3b0857d0294b279e96fb7e323bbb0d(dev, ti, tot):
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return rtot


def func_3e41ad2e177947bebd48649beeaa8070(dev, ti, tot):
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return mtot


def func_c8b200caa4094111a64f4268fd60c7c2(dev, ti, tot):
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return ltot


def func_3a8ac7f7b3164306a5737258b08eea87(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return p


def func_3bdfb35d8c3f4740951a4f8d6688e0c5(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return ltot


def func_c52738396e444b0b87d04f1f072d19ac(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return j


def func_605549769581441a99c35027884d5020(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return s


def func_24ddb9ecf2014a8299385259def2f939(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return x


def func_f1cb849bd7974e5096b9d68aa6e26aa1(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return tot


def func_3888ed7d94b44a24baae96b8693b0baf(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return dev


def func_4d228e71bc604696977c0956d18b029b(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return r


def func_e5c42ae96a004602b0626a1e5fc09a40(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return n


def func_278083fc775446fa9b86fee3bb4848ad(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return q


def func_9449826997eb4e1bb906f655e7c13e29(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return i


def func_de92625da8674d2f8479d20df81c711a(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    return mtot


def func_acafa283124e472ea282d1bf82a46e9c(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return dev


def func_5e6c33e96366438393ba4947e95a9f1e(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return tot


def func_e088969077244bc3bc6a5b1095dfa639(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return mtot


def func_feb45e07f7274c5da23ee251a3097c86(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return rtot


def func_91c9dcad92e74bfca9558891ff8ff1a4(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return ltot


def func_3ac162436909400281887ae16c088b21(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return j


def func_0e89aec831a547879439bfd21c9432ff(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return i


def func_6465fd1d2516469b8ae53910fc29ed81(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return j


def func_007693496f454dcba329c7f1a0be4068(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return ltot


def func_f663968d50b9494e8564f5e9c768cd33(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return tot


def func_17b13622532340d3a3e4b327d4245417(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return mtot


def func_ec9c7a29ff8942f9aff6a550dead32b1(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return rtot


def func_13578962d7304dec850b1d44fadbf91d(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return i


def func_8b62a28f40a54714b20099dc69017099(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return best


def func_239a29283328476089fb0f73b5570160(dev, tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return ltot


def func_29b326f72e854bebb3ee578b4fc8a79d(dev, tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return i


def func_e43bfe3481504a1bbe2d9076343a18c2(dev, tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return mtot


def func_b46fb818a07a446d9301a4ead2038b65(dev, tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return j


def func_4dc9d23abee843abb2b071a95e166110(dev, tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return rtot


def func_616ecdf2871549279903dceb47352834(dev, tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return best


def func_065aa76adfb94e3b9f9f9a2a0a2d0ac5(dev, ti, tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return j


def func_8f4ff4f0a8ca4885a89ffdbb91218b0a(dev, ti, tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return mtot


def func_2fbb5e9434c346a580328f0d895381ec(dev, ti, tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return i


def func_96fb5d2c95254850a73fa9ed7ab5ccbc(dev, ti, tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return rtot


def func_b2ab4994e73a4392a899e7fc52ac7241(dev, ti, tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return best


def func_3f3d100705fc4791a0f02a7f8292b963(dev, ti, tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return ltot


def func_727e870587984a66963b11ee6ae6de01(dev, ti, tot):
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return j


def func_5c12ecdc98944742b4c88f3b93b0438d(dev, ti, tot):
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return best


def func_cae8324bb52e4f5b89c35958476e2b7a(dev, ti, tot):
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return rtot


def func_fc3456605d994d52a485c72a278b05bf(dev, ti, tot):
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return i


def func_64318234762d4e41a029c2cc09921694(dev, ti, tot):
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return ltot


def func_eb24cd0092434e4a867956641cf32134(dev, ti, tot):
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return mtot


def func_3bcd2d46e6d6422780c4942e31cdaa85(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return s


def func_66730478901e4bd0a519001cba5fc5c6(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return q


def func_ddf341e5c74d4ec08abb92e7e04bc29b(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return r


def func_bfc60a6694624482888756db93a8a059(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return ltot


def func_7936ddc5351146008da5b3e4b7075e7e(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return tot


def func_3b3ebbd1ffb04b4d89325dc429280498(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return p


def func_32e68ff94d854fc8b79a7958c2218765(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return i


def func_50a3cd986e3f404b9f887d7c13c33ab3(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return n


def func_2caa227476a249239f619d41bb697e62(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return mtot


def func_958980e728bc4ce391219fe267571105(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return rtot


def func_8b40f6d092e645e583fa257e7b3eea72(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return x


def func_c0250cc3024b4c9da732768cd13b7f8f(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return j


def func_b070e92e7b9a440cb330e68fbf8b1c19(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    return dev


def func_7fed60a2b75e4d3195bd0bfbe2aa9750(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return i


def func_52bc3fb7c58c4b9faa78d9f42ca9a8cd(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return tot


def func_d27b1c37a63d4be0b423b0c3eb800970(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return rtot


def func_08c8d39d8a7d47b2a0556970a0a98746(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return best


def func_d3c8b9350817402a81f19f64987019ab(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return ltot


def func_45760d7b68444aaf88126d15d89cfca1(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return mtot


def func_b72a72a040ec402280d0f9255329aeb6(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return j


def func_32ecb752aea74d0cbec6141c096d2fe7(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return dev


def func_9db76dfad16543c0bf02a0cc3b561dd9(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return rtot


def func_aeaa632ea55c4a81847901930730f6e9(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return mtot


def func_0757d861596a47838a2a376056a15dfe(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return ltot


def func_185cbba1375a4cf98c60c4f589cb2e67(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return i


def func_5d22389568324ecb996ddbdf60cf49f9(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return best


def func_0abe9ad11099423f9cc34049cfa18366(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return tot


def func_a47716808a3a44b4ac00042aa1dd0e71(dev, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return j


def func_e420555aa7b8416088d60d5934b08a0b(dev, ti, tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return j


def func_75972e7d0fbb49d19d7bc3c2c2c27d5f(dev, ti, tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return best


def func_935718f29061409685f8494ee04507e7(dev, ti, tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return ltot


def func_87fec14436d74ab69be1922cf50b1875(dev, ti, tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return i


def func_5d8764bab2654d009cf7c8ff07d1728d(dev, ti, tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return mtot


def func_4f1895ae857f43cd846f4cb3fb410914(dev, ti, tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return rtot


def func_0c91c47618364fcf849376c70daf9781(dev, ti, tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return i


def func_87566d0ca9ea4f6284e65ff52e5d0005(dev, ti, tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return j


def func_cdf61ee2c80a4555a38e07053a20ede0(dev, ti, tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return mtot


def func_3029f6a66b2f453f89ff3b13fcdec7cf(dev, ti, tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return rtot


def func_0f686827bd484231aa493a549706441c(dev, ti, tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return best


def func_6dd5e6bcbdcd413ba4d8837f755d687d(dev, ti, tot, n):
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return ltot


def func_685cb4ca4af84f478e4d77bdac8a9656(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return best


def func_440376d6362441eb950cfe3a22f11ffe(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return tot


def func_ca4c50ad8f164e2bb4d8802a2faff175(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return s


def func_7c83810adebd4c84967c01e88991de41(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return mtot


def func_df60e7fae4ed412d8a4013cfffe45b39(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return p


def func_38c80122190542f097eb761ab818b42b(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return rtot


def func_54f3c07e59c9485cbda287229e1e3948(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return j


def func_e6baa02126d9419e8ed82418078267ca(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return q


def func_e48b997dd8c142c384a57c871d27d569(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return dev


def func_245a1693a0da4c57bd315001f4c1e749(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return ltot


def func_dd8f8decc9b34de1af688507def83374(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return i


def func_74917bbab7c446e1b6712e612dc3450d(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return r


def func_d34d76854530483b97a59d238ebb9d0f(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return n


def func_bcf898f7f3d34453a79d7545e30fb3b7(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    return x


def func_8b5be7ae61df44539ea546f0cf3fb1b0(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return best


def func_6f651a959b644df2a853aca134a35023(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return rtot


def func_c668790ec7ed42fcbeb4197c25712eba(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return j


def func_e76a731f24cc4acb861ef354c6d8400e(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return mtot


def func_3475a57dab334348bf32eca3a2d53e6b(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return dev


def func_7c87c4ca7ba840d6a5dd1a3ae7fd31dd(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return ltot


def func_47774f1f0593438484dbeba096aa2ba3(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return i


def func_9fc71cd3e402473f8088a92dbc349dec(s, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return tot


def func_48dc26eec0e244f19dc8616000bdafb0(dev, ti, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return j


def func_1b5e478f355949b4bc890dd4a216cd60(dev, ti, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return tot


def func_c91469ac56a74cdeaadc2f1fa9bcc7a2(dev, ti, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return rtot


def func_1ef47252ae694c4a8fca18e33d34824c(dev, ti, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return best


def func_7c030f0873d84e18915163cd72657633(dev, ti, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return ltot


def func_465a26922a5442aa800ddc3e487382ef(dev, ti, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return i


def func_a431e9f87c924597ab7013e6f414fbea(dev, ti, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return mtot


def func_b5ac850a30f747629853f9b1713f771e(dev, ti, tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return best


def func_dee962d460d14ed697b544805290b2e4(dev, ti, tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return rtot


def func_3eed8e5b93f84d0fa99d0e7d950469dc(dev, ti, tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return j


def func_5681641770604e61bf0a22970aae4d67(dev, ti, tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return ltot


def func_179e44900069425f938e8438452b7d6f(dev, ti, tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return i


def func_d54fda7ee49041909864c480d7a52cd5(dev, ti, tot, n):
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return mtot


def func_99189f18cdac466393a9e6ec281c7e46(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return s


def func_83672e796e93429e93d130763360ba58(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return r


def func_5169eabb477e42e6a3901f71656e8176(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return best


def func_c2ef95966736406d8ffc84cc1fb97d51(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return j


def func_5148895cb90b4612b30976f53e00d733(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return q


def func_59ddf308bfc84674884f3136e9771b03(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return x


def func_431eefc2f84841fda590b6679d424150(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return i


def func_27c5e2b771e6449c98457c37da263358(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return ltot


def func_8529357ef2024da4b34a3d97a150fc3d(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return tot


def func_839a903a992942e5bd74815ae06620f2(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return n


def func_a0564ed5b1f445d18328e91b2ac98396(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return dev


def func_4b8aebf77ceb423e9d6bb4085cc5b945(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return mtot


def func_a22a59dfdc41480c942b94ff5199361c(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return rtot


def func_10fecd07713e439c800fa9006820a641(infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))
    return p


def func_514cc1bf02514c54990c3f210f74aabe(s, ti, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return dev


def func_6cc3b7fc722a4051838898693e6bc70b(s, ti, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return i


def func_884ad6f03b6c4a268c029ba390203ff3(s, ti, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return ltot


def func_cafe858aebc74bc6936335b6369e0706(s, ti, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return mtot


def func_152b10ce97c14103b337fca2945adedf(s, ti, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return best


def func_5b8b9d9c775741a4b19cf889808e1431(s, ti, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return tot


def func_9516b963fdc14e32a2da7525f8668dbb(s, ti, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return j


def func_aebed105d3a24ade95ae580d13b6c645(s, ti, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return rtot


def func_4c51aaf2ae994cf1833f0963f859a552(dev, ti, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return rtot


def func_410cdb4289f0453695a7d2dd42ff768a(dev, ti, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return ltot


def func_1641bda795644b68b36d6a393918f227(dev, ti, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return mtot


def func_adb4cc1156c5402a9ef9b21b1e95af9e(dev, ti, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return best


def func_8e035f659c20433d83b264eba92d7935(dev, ti, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return i


def func_a76b3ad53d894e64b108d45a1be9fa0b(dev, ti, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return tot


def func_8e2a0b3c49fc4bb1accda2e1488144c5(dev, ti, n):
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return j


def func_825e5d3d1789414e938c0499a8c5352e(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return dev


def func_302ac800606b40ca969e11670e5364df(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return r


def func_185a39a5220348daa98d68d624da9fbd(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return best


def func_c00a3560a66b43aea4e8511f96baa206(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return ltot


def func_abb5c04e92734381979ed0f26e7abc55(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return j


def func_f461f300316f409daad5ebe79e74859f(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return p


def func_c3e6e008857b4ccfa2d9b5c9f33720c1(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return n


def func_1101011fe8a54504aae14c1d13ac0247(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return tot


def func_c0071c21cbda43758cdfb6a2a259ffba(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return s


def func_063552f25a5d4aecab3339d727c88a8f(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return i


def func_9175db0b0eec44f0baa561b01bd2597a(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return q


def func_edc1e4469a6a4805b2cbdbcf8a524922(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return mtot


def func_7be098754bf34134b0262ca7af952f6d(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return x


def func_d8d97f7986884cf9b94d800da9100ff5(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')
    return rtot


def func_b1e5a40384884710b6185a1fae20796d(s, ti, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return dev


def func_d1d0c75cd5cf4b1db4a22e5e84e81f93(s, ti, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return tot


def func_13c9aab2092c4231b3f2d6eeb769f001(s, ti, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return rtot


def func_598647fa5a4a416aae1d9e7aab6eba24(s, ti, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return i


def func_393415ed1b6346829db518159c7d0c37(s, ti, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return j


def func_c89479984ce047558edcac331586f711(s, ti, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return mtot


def func_1d6b9e5579184166a977fc0626411a9b(s, ti, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return best


def func_0af05d0f80cd4a63a0094f0d35edaaa2(s, ti, p, r, n, q):
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return ltot


def func_e71fda2c3f6d486c904f66f4c9c43b39(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return tot


def func_2aeeb9baef3b4ec685ac358fe9a1b6e4(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return j


def func_5f14e5e91cb2476bacd9c4f627f2732c(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return n


def func_2be97657b0904c15b00e100bfc5d6bc3(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return p


def func_fca3e4d376774bfbbb98bbe19681b3f0(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return s


def func_469a41504fa0427c8a92f7ac86fedc9b(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return x


def func_80c51dc2ac68424a9e966822043e073c(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return mtot


def func_9c5397f821d24769a352815cf06441bc(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return rtot


def func_966feddf07a9424ba05277cded0977c1(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return dev


def func_6cc0bd942bc741f8b6008eda714c590f(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return i


def func_96cd5cf93f964abf9a13f19b759e5d16(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return ltot


def func_76552323f34a48b6965f40dac066a673(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return q


def func_3c96a93e0d554685bce3aff8892fb7af(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return r


def func_3e4fadec6a3d4d52b5f38e306c0126ee(ti, infile):
    n, p, q, r, s = [int(x) for x in infile.readline().split()]
    dev = [((i * p + q) % r + s) for i in range(n)]
    tot = sum(dev)
    i = 0
    j = n - 1
    ltot = 0
    mtot = tot
    rtot = 0
    best = 0
    while ltot < mtot > rtot:
        if ltot + dev[i] < rtot + dev[j]:
            ltot += dev[i]
            mtot -= dev[i]
            i += 1
            best = max(best, tot - max(ltot, mtot, rtot))
        else:
            rtot += dev[j]
            mtot -= dev[j]
            j -= 1
            best = max(best, tot - max(ltot, mtot, rtot))('Case #' + str(ti
                ) + ':')(best / tot)
    return best


def func_13ff50cea55a423493b8c7c461077f8b(dev, i):
    ltot += dev[i]
    mtot -= dev[i]
    return mtot


def func_8ed045471e9b425d8418854b38af35ca(dev, i):
    ltot += dev[i]
    mtot -= dev[i]
    return ltot


def func_ccfbbd7746fb476399729c0b328d83e9(dev):
    mtot -= dev[i]
    i += 1
    return i


def func_dab1142432ca41df9eada94be3c21133(dev):
    mtot -= dev[i]
    i += 1
    return mtot


def func_5327c2896648482abfac6743664837c4(mtot, rtot, tot, ltot):
    i += 1
    best = max(best, tot - max(ltot, mtot, rtot))
    return i


def func_01272825390c49dc8d1f9fd909a1465e(mtot, rtot, tot, ltot):
    i += 1
    best = max(best, tot - max(ltot, mtot, rtot))
    return best


def func_2c5b55630f284f41bdc3e4cae209a112(dev):
    ltot += dev[i]
    mtot -= dev[i]
    i += 1
    return i


def func_b5e7d8074cc74c5398b1ee005dc95c99(dev):
    ltot += dev[i]
    mtot -= dev[i]
    i += 1
    return mtot


def func_61a1047ea9914f2ca4111e76dbbe9fdc(dev):
    ltot += dev[i]
    mtot -= dev[i]
    i += 1
    return ltot


def func_29512becc98c45aa84eb8ee6146f9e70(dev, rtot, tot, ltot):
    mtot -= dev[i]
    i += 1
    best = max(best, tot - max(ltot, mtot, rtot))
    return i


def func_690d26e41dd5440898f808ce278f93ce(dev, rtot, tot, ltot):
    mtot -= dev[i]
    i += 1
    best = max(best, tot - max(ltot, mtot, rtot))
    return best


def func_6577c3fa8c964be388a485bc7350c80e(dev, rtot, tot, ltot):
    mtot -= dev[i]
    i += 1
    best = max(best, tot - max(ltot, mtot, rtot))
    return mtot


def func_29242b35dfdc4a4680b4d54de07e2650(dev, rtot, tot):
    ltot += dev[i]
    mtot -= dev[i]
    i += 1
    best = max(best, tot - max(ltot, mtot, rtot))
    return mtot


def func_bc248cb86b7546aa83854c11c8a9affa(dev, rtot, tot):
    ltot += dev[i]
    mtot -= dev[i]
    i += 1
    best = max(best, tot - max(ltot, mtot, rtot))
    return i


def func_9a77de4152f8427894b1d96ea8d2ff78(dev, rtot, tot):
    ltot += dev[i]
    mtot -= dev[i]
    i += 1
    best = max(best, tot - max(ltot, mtot, rtot))
    return best


def func_4f58d635b05d42d298dfd0928ba86d76(dev, rtot, tot):
    ltot += dev[i]
    mtot -= dev[i]
    i += 1
    best = max(best, tot - max(ltot, mtot, rtot))
    return ltot


def func_1a40683d7cf24030bc89318bcaa3b70e(j, dev):
    rtot += dev[j]
    mtot -= dev[j]
    return mtot


def func_3b80939348ad4a53b32fe0eec6b6c8b0(j, dev):
    rtot += dev[j]
    mtot -= dev[j]
    return rtot


def func_ddd423a07eb648ba93c120d213e24fd8(dev):
    mtot -= dev[j]
    j -= 1
    return mtot


def func_da340f5f8231490481c3108aa72d113a(dev):
    mtot -= dev[j]
    j -= 1
    return j


def func_09b42f3bf3d44fb59b9ae68c229ddb84(mtot, rtot, tot, ltot):
    j -= 1
    best = max(best, tot - max(ltot, mtot, rtot))
    return best


def func_39c213db72ec43458bccdedece407bed(mtot, rtot, tot, ltot):
    j -= 1
    best = max(best, tot - max(ltot, mtot, rtot))
    return j


def func_e6a99edd17c443b490643c66a843f538(dev):
    rtot += dev[j]
    mtot -= dev[j]
    j -= 1
    return rtot


def func_e3a5a55399d6442295f956289f43dc31(dev):
    rtot += dev[j]
    mtot -= dev[j]
    j -= 1
    return mtot


def func_ae41bba675344f9eaf79687659481d48(dev):
    rtot += dev[j]
    mtot -= dev[j]
    j -= 1
    return j


def func_564920f469254a659926289b466cf539(dev, rtot, tot, ltot):
    mtot -= dev[j]
    j -= 1
    best = max(best, tot - max(ltot, mtot, rtot))
    return mtot


def func_06b9c244a75b427a9a46954a0ea827e6(dev, rtot, tot, ltot):
    mtot -= dev[j]
    j -= 1
    best = max(best, tot - max(ltot, mtot, rtot))
    return best


def func_4b2c275da3e8458b9c17957e1a9688ef(dev, rtot, tot, ltot):
    mtot -= dev[j]
    j -= 1
    best = max(best, tot - max(ltot, mtot, rtot))
    return j


def func_74a697c801594841a6e16e4445d3bd02(dev, tot, ltot):
    rtot += dev[j]
    mtot -= dev[j]
    j -= 1
    best = max(best, tot - max(ltot, mtot, rtot))
    return rtot


def func_ff151797541b4443b967d8f87a0a1f75(dev, tot, ltot):
    rtot += dev[j]
    mtot -= dev[j]
    j -= 1
    best = max(best, tot - max(ltot, mtot, rtot))
    return j


def func_a23c2e695f8b49458aac562d6683c574(dev, tot, ltot):
    rtot += dev[j]
    mtot -= dev[j]
    j -= 1
    best = max(best, tot - max(ltot, mtot, rtot))
    return mtot


def func_3fb9e0e3e7ca4e5da758f7a228ce4a5b(dev, tot, ltot):
    rtot += dev[j]
    mtot -= dev[j]
    j -= 1
    best = max(best, tot - max(ltot, mtot, rtot))
    return best


def func_e7302a51bd8c48ec93abf4d507438c3e():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    return tot


def func_a1dff2b8edf54cb28b31e581ca7c1e50():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    return p


def func_99b146df2852491d90843e6aa32082fb():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    return r


def func_e06c19b861f44b07a2a05ef2a0741201():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    return ti


def func_c142970de8b64d20989ad5db7b825966():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    return s


def func_1fb0df66afe44e7a8cc715587c099c51():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    return j


def func_35097966ea8c4fb8aed20d8ef10c4632():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    return rtot


def func_3f2b622e95254d889dfb1f50dcb377fd():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    return x


def func_80961c3628434586a1945cca55ef222f():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    return i


def func_43809fedb8c44c33a1ef6c274b924058():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    return best


def func_5ffda4fed5554147a4442cfbf83064fa():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    return mtot


def func_4783e5c7eff14f548d568d30daee2cd6():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    return q


def func_32a4f18cf9ed48578c1aa4f97c354e06():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    return ltot


def func_0a54c74d2fd7496d8e5ef3354fad62f6():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    return infile


def func_c4ef43e0396f49c5938675a984b1bc65():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    return dev


def func_e8ed52f3a063417c97450a45e2adc109():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    return n


def func_9e620dbd3e62403ca16c3e2ec5c3f97f(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return x


def func_1173b2d302d245de8cebffa03159a1aa(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return best


def func_1b2c4b540598436ea33f9a9e9f1a00fd(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return j


def func_26360934e3ac4b7bbe2f505a9f0542d4(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return n


def func_448f946fe1c549b4b196cb936ce4506b(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return r


def func_c43072ef332d472293f8cb7b249b6d64(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return ltot


def func_041a7ac8ea8148779360cc208ae599dc(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return s


def func_cb4ce54e57da4e99abfb3933640dc785(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return rtot


def func_eb907412684a4687bcea4628efca672d(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return p


def func_e6ec59c7164040caa9562bb80f2b0ffe(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return tot


def func_de448d5c999d468c98997de9ceaf344c(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return ti


def func_d513eb5dff1a4d08875e10e1af27fe4f(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return dev


def func_a2b38438b49f40539802dd89ee1140a3(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return q


def func_99cf5b72eadd44e29b5f00d61ef3defb(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return mtot


def func_1a6cfeece18340329512e7ecbba3afb8(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return i


def func_305e2d66b9e644c6b0ef27639a7613e8(dev, tot, infile):
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return i


def func_c09fab36315f48aea44e9b0b74838076(dev, tot, infile):
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return rtot


def func_ba2a76dbcd9d4e209f9f4ad214de8983(dev, tot, infile):
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return best


def func_ac9e2dffe66d4805a024da7e1bf5d233(dev, tot, infile):
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return ltot


def func_3b28e86a0e0047b5813f31810b78b7c2(dev, tot, infile):
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return j


def func_7f1e8a2ccf2d4a50bb447de5bee9b006(dev, tot, infile):
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return mtot


def func_5ebfa9990a634a02b3338ed60653adbb():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return dev


def func_5f01be39684940d493021a38de4979ce():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return r


def func_21d43e10745742d1b043d4e531a6a724():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return q


def func_0cb7415bcc684168942b7bfae34e591b():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return ltot


def func_b8cd38354b1d42368acf87263cfbe6b0():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return best


def func_72a4eb2ed4d34106bea19010d251d574():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return n


def func_42639d87409d425681d6ac9e3119f227():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return j


def func_cfe01cfa1614466281ee17441d17d3c3():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return tot


def func_1d082b2b80c94e008dcf0be8e7c44cb8():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return i


def func_9a632118fe0a48adbe868a67d9a9295a():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return x


def func_abc004f86ae341ad81972263380d77f1():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return p


def func_44faeac4be9147da9867f7f14176ab39():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return s


def func_9e04d9b86a484e3f9fc9237383b4d7ab():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return ti


def func_a793980938394594b3a496b6809a5195():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return rtot


def func_02dbba8015ac435a9676391849c27ab7():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return mtot


def func_1a43209757c045beb79eaf097c92f4b5():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    return infile


def func_10fc0077e4fd4e768643c9807f60b3f5(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return r


def func_9a892821b33640b885ccd9d13ce2abe7(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return i


def func_515f38823ca94e9c88de8d808b581727(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return x


def func_87e62d85d2444ff098441731e7bbf2b8(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return best


def func_840c8d1012854071a316215bcdb333f4(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return s


def func_5635c574cf574e26a4ba755db2554524(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return n


def func_c7a7da14b4184a1ca02921c3362dd858(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return rtot


def func_e1c08f6d6fdc47299f351d358a5b3941(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return dev


def func_b638d51b1eff429b805716e4c61ceabe(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return tot


def func_3ad10b7bdf14401ab9d693222abc5a52(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return p


def func_ffcb4529355c4b6ea056d9770059151a(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return j


def func_21c35874b3c84255bd0eefdda868fced(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return ti


def func_f356676025aa4f2a92edf46fdcffa17d(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return mtot


def func_616242bdb4174483821320850d901ad6(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return q


def func_caba27ba6f4a466392943f32ca7c270c(infile):
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return ltot


def func_346fd70f1a0a4a1fbc48d0d8b1b00cd7():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return n


def func_51a9897709984fb18aae04a8a614fc63():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return r


def func_1c720fe65d344ad59e1dcfa15cbb6c9f():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return tot


def func_bcb90107b6dd4bef95735eb6a9c31900():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return i


def func_635716d9e48748388476acba0fd68cbc():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return dev


def func_a6a464a107bd4c8ea01ecb24a0b88799():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return rtot


def func_0c4f967c09c349d19bebcca84f23caf1():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return j


def func_26eb23bec3434e9a8218e5983009a82e():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return mtot


def func_506af92fbf0c40fa88913bcba17a0a57():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return ltot


def func_0ab4927b6b1141d0b26fd1b7038a0524():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return best


def func_69e89d2870cb4511a3d1de33eb4ec241():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return p


def func_bd363b43aebf43e4a5501958cef70e51():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return ti


def func_13c0ec319068474a8c213e741e51da94():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return infile


def func_004b3757c9ed4cf9a2323c4acb912df9():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return x


def func_acf5d5ca4fc64120bab9e317f6cf9c70():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return q


def func_861891c55b424ce9bf74c0d099297bea():
    infile = open('test_files/Y14R5P1/A.in')
    for ti in range(1, int(infile.readline()) + 1):
        n, p, q, r, s = [int(x) for x in infile.readline().split()]
        dev = [((i * p + q) % r + s) for i in range(n)]
        tot = sum(dev)
        i = 0
        j = n - 1
        ltot = 0
        mtot = tot
        rtot = 0
        best = 0
        while ltot < mtot > rtot:
            if ltot + dev[i] < rtot + dev[j]:
                ltot += dev[i]
                mtot -= dev[i]
                i += 1
                best = max(best, tot - max(ltot, mtot, rtot))
            else:
                rtot += dev[j]
                mtot -= dev[j]
                j -= 1
                best = max(best, tot - max(ltot, mtot, rtot))
        print ('Case #' + str(ti) + ':', best / tot)
    if ltot + dev[i] < rtot + dev[j]:
        ltot += dev[i]
        mtot -= dev[i]
        i += 1
        best = max(best, tot - max(ltot, mtot, rtot))
    else:
        rtot += dev[j]
        mtot -= dev[j]
        j -= 1
        best = max(best, tot - max(ltot, mtot, rtot))
    infile.close()
    return s

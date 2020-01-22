import sys
sys.path.append('/home/george2/Raise/ProgramRepair/CodeSeer/projects/src/main/python')
from CodeJam.Y12R5P1.kmod.a import *

def func_6f7a60ff95a5430cafffcf8cc1a232b0(idx1, idx2, l, p):
    if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
        return 1
    return idx1 - idx2


def func_0cf0b423eb914d7e8bc26be000f755f7(idx1, idx2, l, p):
    if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
        return -1
    if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
        return 1
    return idx1 - idx2


def func_df3a048727c24f62aed20af55c603a80(f, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    return l


def func_b4018aba03484b56860b5f35535384fa(f, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    return n


def func_e7e9ae566f58421aa45e501fd9404fde(f, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    return f


def func_ce91211b89d04caaa9b05e53aff5c115(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())
    return f


def func_2b6d6caa74cb4ced8630993da85da329(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())
    return p


def func_74db6412983d4e2e8d1c33b22ab0170a(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())
    return l


def func_b3e56949a51141e79079fdb7f3e2e199(l, f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)
    return f


def func_b3aaa706be8d492db06bec0564a2ee07(l, f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)
    return p


def func_bf7127e3ed9244878b80b7661042ca53(l, f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)
    return l


def func_6f1f94700b3441c1a20447c8ad92abd8(l, f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)
    return n


def func_e86f6c9957a14be78ad33b627f5cd001(l, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(l) == n)(len(p) == n)
    return l


def func_975f1823fa12444c9b34d79a411bfc37(l, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(l) == n)(len(p) == n)
    return p


def func_78663e6b4b3b4ce4a3414ccc69ef30ae(l, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(l) == n)(len(p) == n)
    return n


def func_1fb1767d42df42e0bd87a89d96c8f2f1(l, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(p) == n)
    idx = range(n)
    return n


def func_d97619ea782b4ea7a7f8abcd5208f494(l, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(p) == n)
    idx = range(n)
    return idx


def func_bcdeaebc766745119e90c50c12ceb8db(l, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(p) == n)
    idx = range(n)
    return l


def func_fd7c77c7ebfd446bad535b27a084bc92(l, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(p) == n)
    idx = range(n)
    return p


def func_a5e434966dd1494fa4ba3df6cd9c0bc1(l, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx = range(n)
    idx.sort(cmp=cmp)
    return p


def func_dbfe90a40b5444cab94e6a360aea660d(l, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx = range(n)
    idx.sort(cmp=cmp)
    return n


def func_038716315e984118b64ea930897a336f(l, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx = range(n)
    idx.sort(cmp=cmp)
    return idx


def func_467893eeb9fe4ea28478c789fa325a73(l, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx = range(n)
    idx.sort(cmp=cmp)
    return l


def func_dd42025f12be4fe6a4a364593e63474a(idx, l, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return l


def func_6cf0a201a2004cf99632d2a2f3ad2d4a(idx, l, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return idx


def func_189823bf50ca422a9e8faedfacc97ea0(idx, l, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return _t


def func_7b7011a47ad54cd4bb32f241fd9d15a1(idx, l, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return p


def func_7160e54ae0f244f394638e3628aa7c10(idx, l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return _t


def func_b5cda45188714ce298557627fd161aeb(idx, l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return l


def func_1e959ff85ba641c2894bc1bd23167556(idx, l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return _i


def func_4c633eeecf834542ae18fda6e5857f28(idx, l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return p


def func_f77f6af4492c48bc9d39fe9788e9039b(idx, l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return ix


def func_4588ef8a638947ac93adf7f3b233ec4d(idx, l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return idx


def func_38d608ec286040fdad5b1df8dc11e50b(idx, l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return n


def func_09ccbcfbbe6346dcadcf358b39cea97b(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())
    return n


def func_8136661a6f0849cc84ed59b9ce9731ba(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())
    return l


def func_bc6c37838dce4392ae30bf7594cea009(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())
    return f


def func_269d916836394357962cbdff39dcc866(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())
    return p


def func_a5bba859598142569c9f08cb6436b9dd(f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)
    return l


def func_db1b1c3cc2754e70a8181e31d8f3eb7e(f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)
    return f


def func_b247a53362f04d27ab1d603bfb1f09b0(f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)
    return n


def func_8b58dbe7976243528a7db6dc031b07f0(f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)
    return p


def func_651216ed8e4d4d75b2efbede421dd8d3(l, f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    return l


def func_43109bc1bbb24af886725bb73b30cecf(l, f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    return p


def func_61120cfc9a5d4d58b11e73c5f17e0f37(l, f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    return f


def func_3564baa698a14bfe864ded98405dd2a9(l, f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    return n


def func_a7b980422cfa456e90cdde9ae3a3bc34(l, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(l) == n)(len(p) == n)
    idx = range(n)
    return idx


def func_75c643f6d7be45f0a09d4a4a9a9d4742(l, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(l) == n)(len(p) == n)
    idx = range(n)
    return p


def func_745f164856774bb48a7025f73906fc2a(l, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(l) == n)(len(p) == n)
    idx = range(n)
    return n


def func_4bdf00b6ea4943b083f7cf95adfd827d(l, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(l) == n)(len(p) == n)
    idx = range(n)
    return l


def func_68633a7dd7e5437fa0efc234ffa85a1a(l, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)
    return n


def func_3a8012b47a0d4cdb8c076f2674c0ce96(l, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)
    return l


def func_791f8043777244a5a57497b04344c706(l, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)
    return p


def func_d292949f4629439ab4d5ca9e7a6e9551(l, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)
    return idx


def func_060f1d867b8f4cc49cfa6f5bcfd1512b(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return _t


def func_d3f6a0edfc9a41b1a568e3bf86c30db2(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return n


def func_7412d089188b49b8a195868e6c7cc0a0(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return l


def func_9f559a3d8bcb47ee98f4937cb04b65a1(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return idx


def func_e60941f702d1438d9d43bf5d12e9dd6a(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return p


def func_a6b295b547ab42d898615f4693af25a4(idx, l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return _t


def func_50dae65c298c4884a5fcb06176a54e0c(idx, l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return idx


def func_18c558105f394bf5be0d30346ce06c5e(idx, l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return n


def func_cbcf1257dc6041e6b742680a7e654504(idx, l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return l


def func_6fb3bac52ba84a03b9ba57bcaf71f86c(idx, l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return _i


def func_cce8807b409b4e869282ffed8df7961d(idx, l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return ix


def func_fc8b2875b0aa468b9eb55febb32ac828(idx, l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return p


def func_a4f05726f5054ea188b1d4b774dbd3f5(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)
    return f


def func_04894ebca30446a69d969034e7e88a00(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)
    return p


def func_7dbb02fc38344a969a09a8eee17793f2(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)
    return l


def func_33e68e0ea1624dda82099d13d1ff8823(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)
    return n


def func_ebfa5f10a92c4b58b837b1ac372dd0bb(f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    return n


def func_5453cf70c29a4201a711ab0c99d4f3e7(f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    return p


def func_77983b0c2cdb494286792f5159c6028c(f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    return l


def func_8a686ff9e17244a39d3103eb09c64d58(f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    return f


def func_e90c5e3ba6a0410b91010d0a1a453a48(l, f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    return p


def func_f76d536cbf9b4187996734a21709f1c0(l, f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    return l


def func_028625557ec542a28e8ea01ef29990d6(l, f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    return idx


def func_af386ef647a848d3ba5b9e8bff3cc00c(l, f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    return n


def func_a357be89685c4e0a91556584de5a77f5(l, f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    return f


def func_937a52a7e4fc4ed6bdc75580bf298966(l, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)
    return idx


def func_bf733f31d02f46f7a973c5e2bb5ee91d(l, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)
    return n


def func_5ff61c293bff49c0ae205945213c78c2(l, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)
    return l


def func_cf45ed5e5c41479eaa4e6f4e588fd430(l, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)
    return p


def func_cd3f27c0a13143ec82aef99bd520572a(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return _t


def func_876c5b8f97ad4e5888d948ed030ae829(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return n


def func_ecf428ea8aab46b3bccd7da84517160c(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return l


def func_3386ab41d23e4b7088678031a56111af(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return idx


def func_0f9096ccda314f97801224489279c366(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return p


def func_b6325d480a2747b9a79d45a89b48f2a8(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return _i


def func_3b43249a86b349439c590bd2b1e8ad77(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return _t


def func_799ea175e73b40498ded9edb55549c3f(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return p


def func_035a5d0764164c22b2448988e84cfa78(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return n


def func_776da4d9f6eb44a8aea7e6505128e04b(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return l


def func_b807b30007704917adea19bb0753c488(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return ix


def func_3bf341908bd14a959af36035da0fbdc7(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return idx


def func_1a6295e682494d4abb9fda675af8198a(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    return l


def func_578b991fc8764e69afcc7591b7cf8485(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    return p


def func_0bc362fb278b4359b6b4d3b4d4095e5a(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    return f


def func_10c4586faf5540ef9eb3049533bf3ab2(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    return n


def func_6f4b0092e2f044a2ad6982205b028fd0(f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    return p


def func_72804d678cb648db87d8e6b4533cc377(f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    return n


def func_f721096e85a342aca4561e754c0089b4(f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    return f


def func_dabca126d0954c7097e2cf62bafee4e8(f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    return l


def func_fbd032e5050c46e68e66a81e71129dba(f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    return idx


def func_a6b0503503404e658a1adc54d292b349(l, f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)
    return f


def func_c5d008eba6ca43ee8200c1bacdbbbf42(l, f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)
    return n


def func_d5ff4d78e61147f7b53fc16bc77c9fbf(l, f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)
    return idx


def func_4a1590f22b6e4814a563cd32a5c814ac(l, f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)
    return p


def func_9df8f9ed52d145d89394a0b29ceae3b7(l, f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)
    return l


def func_b6b08a2af8ef4a2999aa132f310438b4(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return _t


def func_af7d0718ad884c29b431817971cdf215(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return p


def func_2fa4f9ab4bac46339f4fb2a263729057(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return l


def func_c2af2dfc068942da84a18f2cc18bc451(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return idx


def func_1b9abd6b0b304c1b9c994ea933c487b0(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return n


def func_1860b4ab903b4fbe8414042179bad657(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return _i


def func_14dd1509a7b04eaabd2c3e1639411638(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return idx


def func_12e43e0c93b1485ebd8b3eae308531dc(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return n


def func_84ccb66cb91c4d61b336fb440dabb1ec(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return l


def func_d6df52c0938448f2bb874eaa2b41c635(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return ix


def func_1257c6987a7246cb80beeac346468fe5(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return _t


def func_4e6ad0344ade4ae7877e7f80fc7f22ad(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return p


def func_909b52d81c7f411bb361b89400cb66c5(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    return idx


def func_b0821209987843f2a4ac86f2b26d041d(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    return p


def func_fbf2eefbebc24823957d6de7fefe0933(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    return l


def func_71beba829061492082db93187a67f53b(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    return n


def func_ec271d1a0ed94738ae2cbadef36ef071(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    return f


def func_dcfe90c969584e909e286a3c6342a330(f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)
    return l


def func_69a00f03814e4d4db6ca0498e997fb18(f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)
    return p


def func_2698fcf1462f46a79a9c4c4f3fa39c09(f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)
    return f


def func_2b994cfde08848c6ba04bf8d0db18dd1(f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)
    return n


def func_ae586fb49dfa430c8f2e33066070498b(f, n):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)
    return idx


def func_c40c57bdeff243a0bd08e0e62cf0ace4(l, f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return n


def func_fe7aae797ff4407da202a829b717d641(l, f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return idx


def func_4168139cbbba4a8aaa5e861d4c6e1909(l, f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return f


def func_3294af1ebd2b431bbadf23bf6c8c9ec9(l, f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return l


def func_9fd2e0939f364538abb16e2139baf9bd(l, f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return p


def func_4ae0e52b2b6247a3ab5d6e4105a6f3b7(l, f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return _t


def func_7e0d58620f0240d78074177178f27531(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return n


def func_1ba18f86207b4a52bd34bb01a098fbf8(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return _i


def func_180fc8665cf34ebb964951983125ed44(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return ix


def func_172e9042ddfa47b899ddf04a65805a4c(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return p


def func_a02fccb11c664d7aa214044184bc8613(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return idx


def func_5d4c595179e543958d8824f4c193f377(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return l


def func_7ebe45197a4f402f97e60c466fadb0ca(l, n, p, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return _t


def func_cb479cb7bd224b42a2eaefe35d31fc25(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)
    return l


def func_ffe12f16789b4896affd0a951ab4170c(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)
    return f


def func_d77ce19309cb47508507a016df4a3dbb(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)
    return n


def func_5165c1531ea84003add0c7e64112cd5f(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)
    return p


def func_8fb112e1b2704a59b5c6d37e82659954(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)
    return idx


def func_f8b81336d4964c7db2fd94c3bf01b212(f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return f


def func_fec89a827ffb458eb39aad7cfe5342ee(f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return n


def func_8283d0391e874b63bc84e270c1bdfc29(f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return _t


def func_f5d39d0c08334371bd203f46813b85db(f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return l


def func_0bbdfd647bac4cf98545fc80a2baec47(f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return p


def func_b7945cde5fd147278a1af0e8ed7ee739(f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return idx


def func_902960d714e5456da9c0cf1009a5a648(l, f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return _i


def func_a1621435f57b40498f633c7cb8ecab43(l, f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return idx


def func_56dfc59aca1f4703926673bdc6ed7abf(l, f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return p


def func_c7c95c3456724096922c466472813271(l, f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return _t


def func_8b512f0fe125478bbab5e448d1f7a93b(l, f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return ix


def func_e8334c58eff14baaaee8dbd07ea52381(l, f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return l


def func_8a5dee05ef894109bfb578383d793801(l, f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return n


def func_5341a42b1f8249fd958d79ef95b292b3(l, f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return f


def func_0f34f636d50543888226ae8bb47e2c44(f, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return n


def func_66093292a3344133bea469b7315eedd2(f, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return idx


def func_cc3fdd7fc3d54ca18cba35ca5634e37f(f, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return _t


def func_7e1820e4f1af4139b1aafbd193e755ed(f, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return f


def func_78350f7fbcd34ccd97811f6552334279(f, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return l


def func_d30d7ecb5d7843419f677287d832c1b2(f, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    return p


def func_6bfce8340b76408ba3fbbebf4ed60c4d(f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return ix


def func_44db3e6d85aa4aa0bea269758fc1e235(f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return _t


def func_3286ec290f424adaa09c339ba3d2063f(f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return l


def func_015dcf35780348d2a9a266e32b648c2c(f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return n


def func_05e15176604847979133fcb1a8fea6ca(f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return idx


def func_c643e1f8da7f4a9b955c9c836574a610(f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return f


def func_15400335d4d249a3b5601898402feb03(f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return _i


def func_124dc76f65de4170b0bcb2d6dd1656ae(f, n, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return p


def func_13e27a6057fc4db38afe9fa8294dca0d(f, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return _t


def func_d77ab0db60f848bea206f4af0fd9df79(f, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return f


def func_1209b5638d0249e5b359b86c964b49e9(f, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return ix


def func_d6d28988f5ef412983139f12a2391bb8(f, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return idx


def func_bc438553c9434d95b520e4f07241cac4(f, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return _i


def func_6be6dd8c6bfa4a2e8e86fa55e8db48cf(f, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return p


def func_799ffc9a76014feca93153cf45492c82(f, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return n


def func_2c4e0c5e3f8b4498b0c22ddec3fe8830(f, _t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    n = int(f.readline())
    l = map(int, f.readline().split())
    p = map(int, f.readline().split())(len(l) == n)(len(p) == n)
    idx = range(n)
    idx.sort(cmp=cmp)('Case #%d:' % (_t + 1))
    for _i, ix in enumerate(idx):
        if _i != n - 1:
            print ix,
        else:
            print ix
    return l


def func_03ccfe1a45c14303aab26279e5a087d1(l, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    return f


def func_3fcb23bfa97941f391deeca3206ef28a(l, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    return t


def func_0f2f1d1999074a10888dc0f940ea3b5d(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return idx


def func_719998d060074ac3a0242ae24ac5cac4(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return n


def func_20943c27564e4ec991d2e92df10faeaf(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return l


def func_6a4204540a4245559d882722d8671f6f(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return t


def func_eb412b3d1ba34742b28cf48ad3d63fb4(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return _t


def func_2cb80b317ea444c985d9b5b2e4713885(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return f


def func_24368e21f9534b1bb3a1149d3226cb0c(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return p


def func_30e13bb299264702991a726318fd0f71(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return _i


def func_659d7dfd42b4419d9565a8e101429fb2(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return ix


def func_5ad499a7e5084a27877e828d497b6514(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return p


def func_c0842300a5494e5b9c5438eb523a9f00(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return _i


def func_7df71f63bde04a6582e501df252f42ac(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return _t


def func_d3853f59084640e3bf44c28e5288c050(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return l


def func_332799381c4f4d61bf584ab145e8c878(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return n


def func_6d7e267fb1f746debd5d52aec3f811e2(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return t


def func_c2b5aae19bc346c7a8c62924b5140fe5(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return idx


def func_f28d65dfcc8c45b49ea0c7e86c99703a(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return f


def func_69368393ad4f479d80d75c1cbaa5b1ea(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return ix


def func_f2f172c923e34a9f9c94d7de2d7e53e9(_i, l, ix, f, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return ix


def func_72b197b3adef47a9a89da790a6b8df3d(_i, l, ix, f, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return f


def func_b814cafa70e346d98a0eff8122d3d34c(_i, l, ix, f, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return _i


def func_7e1de85e9df0437a916cf259b1e84914(_i, l, ix, f, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return l


def func_439795d75ee245dfa263433c9be83aaf(_i, l, ix, f, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return p


def func_9d87efa77880484f9988813f211a3467(_i, l, ix, f, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return n


def func_07f99c1341434b3493e4f5d00bf1c55b():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return ix


def func_a8202435de414d64a65156c28c7c8347():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return idx


def func_6e183becd4b54e499b6e5e2bd0489e42():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return f


def func_0dc5057bd0ee490ab58b44481d63ece5():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return p


def func_2f0fb2f9f66f43868f3082d375fa0ec4():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return l


def func_8d9af47573524d8ba199b9614459c2aa():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return _t


def func_e14806f99b09421db16a2ae0f73a3edc():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return _i


def func_c3b3cd68177443acad8d6d1f5187653b():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return n


def func_91c679e6e35e45239577bb63b4e43a2d():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return t


def func_75b8a4c968fc4471b0f5495a1a6b54d4(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return p


def func_524d6dbab056473bb41647e973cd4da1(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return idx


def func_8770e306a4544c1f828881334bb821d6(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return _t


def func_4dafd8a8b7414070b7acc88170132096(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return l


def func_72b93e27adfb49a5aec96024f453d95e(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return n


def func_a3002c794d4247e6a03296cb8843bfc6(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return t


def func_e4566d4ad3294c6c9812e728e295d27c(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return _i


def func_1c14feee7f474d629e1626d35296d64c(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return f


def func_1dd83b42af21402eae02974be8421214(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return ix


def func_94a6288ba7be44d8ae7af5d7e7b7cd5d(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return t


def func_48f07d6ded244a4586c06f7a83a3601c(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return l


def func_53cc00a4807d4d91a0e43ed2ea06f820(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return p


def func_81f0e9e87cb74c929b7f5367516d393d(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return ix


def func_908ddd02fdea44e7a951c63cc2035678(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return idx


def func_5c885276585a43d191c6c545b66924fc(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return _t


def func_f96dd4ba043b44f4ae17c0301c1e9ce1(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return n


def func_6204a68aaded4429955305f954e99a0a(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return f


def func_82d3d843d78f488cb5bb0986633cac50(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return _i


def func_3cf0adf9413a4e0289820f5ba5ed59c9():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return f


def func_12b667d2b07f46788b95cf34df1e960d():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return _t


def func_2d8bf803214c494c854153df4a090342():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return _i


def func_6df2282e28c7454a90a392d744361ba6():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return idx


def func_844800436b934eb486ff9fbb47c19c1b():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return l


def func_645b924f56eb4335a602fe4de4d593e7():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return t


def func_d889c4aa0d5543a7a46a7fbe32e9e98c():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return n


def func_b4da8167ceff4df8a572e1c831d4f5f1():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return p


def func_737622a22738460c93026f1008068b6b():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    return ix


def func_1a4cde10fe9d4b06b10d714f837bdff2(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return _t


def func_9890ed1c9cb24fec8554ba2cb9f25b1f(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return n


def func_56e1a51faaab426083263f6c462f1220(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return _i


def func_7b15e886fc9c4ffe809f94e91dbe72fe(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return idx


def func_eec35fe0017440f3be64f9dc349c1b5d(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return t


def func_01ba2346c3aa4e82b257646375217cff(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return ix


def func_834776f47a0a434d8030755156983193(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return f


def func_1999d52abc8a4467bc512bf6d89d5102(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return l


def func_473d158e367547b79149699329d10eb8(f):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return p


def func_b64a8b343f0c4a3bb08eea3133d9e128():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return idx


def func_09e393aee66246b4966ad8db4d60947f():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return ix


def func_042ccd2d0e444068b4b268c1cd194807():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return l


def func_d6319031ba9d44bd8a057fe4deed201b():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return _t


def func_b8d32ea8204743a4bd888914cfb46325():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return f


def func_d35ee87bbd61450a9f1acd7a038d2382():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return t


def func_077fddbeb1084e9d8f2daf07bbd65cc8():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return p


def func_841ff7fc6de84595807ba5b10f55065b():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return n


def func_24e15b3c93d54c36bab8ba719d563fbd():

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    f = open('codejam/test_files/Y12R5P1/A.in')
    t = int(f.readline())
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    if _i != n - 1:
        print ix,
    else:
        print ix
    f.close()
    return _i


def func_19e1161b36284337bea05d4cb0abef5a(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return l


def func_c214b178a8f84449ac41899ce936df6c(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return n


def func_baeeb6ebcbec4be18b25fd7db8d61c27(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return t


def func_7d8282287db34f42bd67f0b0465d56ee(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return f


def func_23d192593ba84dd9a921805d7fe02d9b(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return p


def func_a0c45844a960429fa35ab850d9591bf8(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return _i


def func_fed6d7e19a14429e9b812236d9d6aac3(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return _t


def func_175c68b9ab914dcb8518565f5905ebf5(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return idx


def func_8e163476f03c4f40aeca16c53ef5f418(f, t):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    for _t in xrange(t):
        n = int(f.readline())
        l = map(int, f.readline().split())
        p = map(int, f.readline().split())
        assert len(l) == n
        assert len(p) == n
        idx = range(n)
        idx.sort(cmp=cmp)
        print 'Case #%d:' % (_t + 1),
        for _i, ix in enumerate(idx):
            if _i != n - 1:
                print ix,
            else:
                print ix
    return ix


def func_964d2743bb444b28af4c8dcd6c2dbe85(_i, l, ix, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    if _i != n - 1:
        print ix,
    else:
        print ix
    return _i


def func_8a3f9e2ca6604f13929e2cabd50097e1(_i, l, ix, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    if _i != n - 1:
        print ix,
    else:
        print ix
    return p


def func_cc3a06cf130f40a89dd443170c7e42fa(_i, l, ix, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    if _i != n - 1:
        print ix,
    else:
        print ix
    return n


def func_d636e107dc9240bc80002d88b19e6d14(_i, l, ix, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    if _i != n - 1:
        print ix,
    else:
        print ix
    return ix


def func_8bd399474fe84f1588c7707209b60caf(_i, l, ix, n, p):

    def cmp(idx1, idx2):
        if p[idx1] * l[idx2] > p[idx2] * l[idx1]:
            return -1
        if p[idx1] * l[idx2] < p[idx2] * l[idx1]:
            return 1
        return idx1 - idx2
    if _i != n - 1:
        print ix,
    else:
        print ix
    return l

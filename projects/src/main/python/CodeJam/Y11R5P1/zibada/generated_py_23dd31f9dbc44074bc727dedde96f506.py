import sys
sys.path.append('/home/george2/Raise/ProgramRepair/CodeSeer/projects/src/main/python')
from CodeJam.Y11R5P1.zibada.a import *

def func_83daa174c57d4f799b51da35113148d1(x, lx, nx, ly, ny):
    p = (x - lx) * 1.0 / (nx - lx)
    return ly + (ny - ly) * p


def func_7821e424c66e428fa543899014745476(x0, y1, y2, area):
    m = (l + r) / 2.0
    if m * (y1 + y1 + (y2 - y1) * m / x0) / 2.0 > area:
        r = m
    else:
        l = m
    return m


def func_eb6077beeae94cc6af971da3d9bfb1a7(x0, y1, y2, area):
    m = (l + r) / 2.0
    if m * (y1 + y1 + (y2 - y1) * m / x0) / 2.0 > area:
        r = m
    else:
        l = m
    return r


def func_438a85f8008f4efd851be77d5b9009e8(x0, y1, y2, area):
    m = (l + r) / 2.0
    if m * (y1 + y1 + (y2 - y1) * m / x0) / 2.0 > area:
        r = m
    else:
        l = m
    return l


def func_411308085fcd4e90bb653e1deb2bbacd(x0):
    l = 0.0
    r = x0
    return l


def func_b7012de1e8f54a8996b1f046af848c08(x0):
    l = 0.0
    r = x0
    return r


def func_a47eb3300f12452aade739d586631dbd(x0, y1, y2, area):
    r = x0
    for i in xrange(100):
        m = (l + r) / 2.0
        if m * (y1 + y1 + (y2 - y1) * m / x0) / 2.0 > area:
            r = m
        else:
            l = m
    return r


def func_b518357497734000b430a3536c7f3694(x0, y1, y2, area):
    r = x0
    for i in xrange(100):
        m = (l + r) / 2.0
        if m * (y1 + y1 + (y2 - y1) * m / x0) / 2.0 > area:
            r = m
        else:
            l = m
    return l


def func_8ea3a2f916cb49cd9416f45e39709841(x0, y1, y2, area):
    r = x0
    for i in xrange(100):
        m = (l + r) / 2.0
        if m * (y1 + y1 + (y2 - y1) * m / x0) / 2.0 > area:
            r = m
        else:
            l = m
    return i


def func_fd4a2dd9d32b40aaaa526558762d8c09(x0, y1, y2, area):
    r = x0
    for i in xrange(100):
        m = (l + r) / 2.0
        if m * (y1 + y1 + (y2 - y1) * m / x0) / 2.0 > area:
            r = m
        else:
            l = m
    return m


def func_f02088b19e4145fdb4d8c2db919bd881(x0, y1, y2, area):
    for i in xrange(100):
        m = (l + r) / 2.0
        if m * (y1 + y1 + (y2 - y1) * m / x0) / 2.0 > area:
            r = m
        else:
            l = m
    return l


def func_7c9c5b2cc8514e6d8d375c5d0a211e8c(x0, y1, y2, area):
    l = 0.0
    r = x0
    for i in xrange(100):
        m = (l + r) / 2.0
        if m * (y1 + y1 + (y2 - y1) * m / x0) / 2.0 > area:
            r = m
        else:
            l = m
    return m


def func_cca4d5224f80482d8d95947e9a5efcbf(x0, y1, y2, area):
    l = 0.0
    r = x0
    for i in xrange(100):
        m = (l + r) / 2.0
        if m * (y1 + y1 + (y2 - y1) * m / x0) / 2.0 > area:
            r = m
        else:
            l = m
    return r


def func_6c41e11d415442d4afa9c6537cb29dce(x0, y1, y2, area):
    l = 0.0
    r = x0
    for i in xrange(100):
        m = (l + r) / 2.0
        if m * (y1 + y1 + (y2 - y1) * m / x0) / 2.0 > area:
            r = m
        else:
            l = m
    return l


def func_9a56f5e97e754e52ba56e26364c7d5f1(x0, y1, y2, area):
    l = 0.0
    r = x0
    for i in xrange(100):
        m = (l + r) / 2.0
        if m * (y1 + y1 + (y2 - y1) * m / x0) / 2.0 > area:
            r = m
        else:
            l = m
    return i


def func_3b65257361f44717a69791a84310d17b(x0, y1, y2, area):
    r = x0
    for i in xrange(100):
        m = (l + r) / 2.0
        if m * (y1 + y1 + (y2 - y1) * m / x0) / 2.0 > area:
            r = m
        else:
            l = m
    return l


def func_7eb4ba7e441748e98bfba2ad32356e02(x0, y1, y2, area):
    l = 0.0
    r = x0
    for i in xrange(100):
        m = (l + r) / 2.0
        if m * (y1 + y1 + (y2 - y1) * m / x0) / 2.0 > area:
            r = m
        else:
            l = m
    return l


def func_db83ec1fe81848b38ef5128b977bb726(y, x):
    area += (x - lx) * ((y + ly) / 2.0)
    lx, ly = x, y
    return ly


def func_74dde78afc454ba796b96ea53935f34c(y, x):
    area += (x - lx) * ((y + ly) / 2.0)
    lx, ly = x, y
    return area


def func_9a8c12ae70234421baf6250399abbc5a(y, x):
    area += (x - lx) * ((y + ly) / 2.0)
    lx, ly = x, y
    return lx


def func_7366aa213c734c22ba84183925696d39(y, res, ly, x, curarea, lx, G, area):
    res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
    nextarea += area / G
    return nextarea


def func_55da56aaaae64890aa10b5b80ab6e5e3(y, res, ly, x, curarea, lx, G, area):
    na = (x - lx) * ((y + ly) / 2.0)
    while curarea + na > nextarea:
        res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
        nextarea += area / G
    return nextarea


def func_0bb4c64b603c4b7ca547826820a0ad09(y, res, ly, x, curarea, lx, G, area):
    na = (x - lx) * ((y + ly) / 2.0)
    while curarea + na > nextarea:
        res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
        nextarea += area / G
    return na


def func_5a06f13998dd4f8bbda678c9099b38e0(y, res, x, curarea, na, G, area):
    while curarea + na > nextarea:
        res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
        nextarea += area / G
    lx, ly = x, y
    return lx


def func_3992d125790f42cbb648dc6e2b3163d4(y, res, x, curarea, na, G, area):
    while curarea + na > nextarea:
        res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
        nextarea += area / G
    lx, ly = x, y
    return nextarea


def func_a8177afcc8d34b19aff256a6818c06d7(y, res, x, curarea, na, G, area):
    while curarea + na > nextarea:
        res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
        nextarea += area / G
    lx, ly = x, y
    return ly


def func_5d00295205e24406b983f99f92ff18cb(y, x, na):
    lx, ly = x, y
    curarea += na
    return lx


def func_f55934ade96443889214f0d445ebec5f(y, x, na):
    lx, ly = x, y
    curarea += na
    return ly


def func_0f89c80719d04d32b95e957c124f6fa7(y, x, na):
    lx, ly = x, y
    curarea += na
    return curarea


def func_80ae067e570647dd9153c0eee6428b5f(y, res, x, curarea, G, area):
    na = (x - lx) * ((y + ly) / 2.0)
    while curarea + na > nextarea:
        res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
        nextarea += area / G
    lx, ly = x, y
    return na


def func_2e284c9798404cf682e89c19d61e9f4e(y, res, x, curarea, G, area):
    na = (x - lx) * ((y + ly) / 2.0)
    while curarea + na > nextarea:
        res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
        nextarea += area / G
    lx, ly = x, y
    return ly


def func_2e8247c07a2c4614a4ac408f99296b38(y, res, x, curarea, G, area):
    na = (x - lx) * ((y + ly) / 2.0)
    while curarea + na > nextarea:
        res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
        nextarea += area / G
    lx, ly = x, y
    return nextarea


def func_76a51452cbca4dbe9ed6eb310363847e(y, res, x, curarea, G, area):
    na = (x - lx) * ((y + ly) / 2.0)
    while curarea + na > nextarea:
        res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
        nextarea += area / G
    lx, ly = x, y
    return lx


def func_e4247086bd8d420f8a18ef8d45e41140(y, res, x, na, G, area):
    while curarea + na > nextarea:
        res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
        nextarea += area / G
    lx, ly = x, y
    curarea += na
    return ly


def func_5d252fa6eb1f4ccca4590c7b671c2e78(y, res, x, na, G, area):
    while curarea + na > nextarea:
        res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
        nextarea += area / G
    lx, ly = x, y
    curarea += na
    return lx


def func_3651edbcacfc4d569f06f1ae9df5ac68(y, res, x, na, G, area):
    while curarea + na > nextarea:
        res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
        nextarea += area / G
    lx, ly = x, y
    curarea += na
    return curarea


def func_8f5589b6f83c4e86820c5ae477d751c3(y, res, x, na, G, area):
    while curarea + na > nextarea:
        res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
        nextarea += area / G
    lx, ly = x, y
    curarea += na
    return nextarea


def func_9be37eb056c7487aa1cf7d8b2742608c(y, res, x, G, area):
    na = (x - lx) * ((y + ly) / 2.0)
    while curarea + na > nextarea:
        res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
        nextarea += area / G
    lx, ly = x, y
    curarea += na
    return ly


def func_c08d90f5fd7845d991dd788dc5c3c137(y, res, x, G, area):
    na = (x - lx) * ((y + ly) / 2.0)
    while curarea + na > nextarea:
        res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
        nextarea += area / G
    lx, ly = x, y
    curarea += na
    return na


def func_5b0fa1bd9e364cdc9fd3d1112758c883(y, res, x, G, area):
    na = (x - lx) * ((y + ly) / 2.0)
    while curarea + na > nextarea:
        res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
        nextarea += area / G
    lx, ly = x, y
    curarea += na
    return curarea


def func_abf040f1f9ec4c58afe72fa9f47a3cea(y, res, x, G, area):
    na = (x - lx) * ((y + ly) / 2.0)
    while curarea + na > nextarea:
        res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
        nextarea += area / G
    lx, ly = x, y
    curarea += na
    return lx


def func_ccfd3c4ef4254f37891ef4c11babcb46(y, res, x, G, area):
    na = (x - lx) * ((y + ly) / 2.0)
    while curarea + na > nextarea:
        res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
        nextarea += area / G
    lx, ly = x, y
    curarea += na
    return nextarea


def func_9ebfd71147434ac887904471e1a8cca1(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    return U


def func_7320d0f554d442098df16f1973802311(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    return G


def func_861c27cf222741c183b11306f5a5d286(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    return i


def func_01495b3dfae5496ca1e103dddb39296e(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    return W


def func_a2d14a02ca2b401fb69a49a3f8b311d4(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    return low


def func_a165e40ac2bf444e902f0b9e434082d1(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    return L


def func_10eb10b74cf045c7b3fc90eb2a89b67a(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    return low


def func_29e5def69eda4bf996672b997d9ebd65(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    return high


def func_0bf34c8920174eaf9abd00afc1938eab(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    return i


def func_7318d577303a45d498a70c8b352de7c3(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    return i


def func_de893f0670c5433382158382b119bbba(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    return xs


def func_b39657d6d6764823819c145da385b727(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    return high


def func_5f34fa184da7458a8463fb47f1cd435b(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    return x


def func_990ef3981c8c4530be5113ed11b367e5(low, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    return x


def func_86406fb551584e5d9ae8f6792654b1f9(low, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    return a


def func_a1baa1459f1e46c4bd844b3fb1a22dc0(low, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    return xs


def func_25bd0e6c472641c3a2a01d9c782b0e38(low, xs, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return x


def func_79a9c97b0b19474fa16aa634c2e59021(low, xs, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return a


def func_2389b73904b04fecaf61fb1755e6e369(low, xs, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return area


def func_0602812e9e2440ea888fbdd453a3317e(G, area):
    nextarea = area / G
    curarea = 0.0
    return nextarea


def func_ac5ab1f2e2c441fcb6451056239e850a(G, area):
    nextarea = area / G
    curarea = 0.0
    return curarea


def func_e235a9f50711461baf3a74cd4b4b32cb(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    return high


def func_bd7f28f0741f47c7ba8485af674eae0e(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    return W


def func_a66e1c41bfc24f7ab377922e7dbd772c(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    return L


def func_fe6831cc50714a52af3707f886e33512(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    return U


def func_98fa7fe804e74d278d914506b90c937f(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    return low


def func_e3a19d7109434a86b5a00ac6798c96eb(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    return G


def func_9f07a175c5c1456bb0c4765288581208(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    return i


def func_2d6dba7779b942e9b1aa014eb1b94135(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    return i


def func_35449b33e878478a9b98c0746efb152a(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    return xs


def func_9aae6bf04be84e1383cde4da3fd926e5(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    return low


def func_77a7a73820724b8da54fafff22fa284b(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    return x


def func_f91f8571f1034398839003c419f197b1(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    return high


def func_75faa5151ffc43249dab6f38c8b5b9ef(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    return xs


def func_b2f3c60cdbbd42debbf163f4c36e410f(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    return x


def func_c688eb637d8f42c48e90bd133f351b3d(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    return i


def func_9bb71309bf5d4e5e8a7b3e47f66fe0d0(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    return a


def func_40c85e237a0b4f73a117fde191b3f9ab(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    return high


def func_947baed5afa9494fb18d8684a9f91df3(low, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return a


def func_4b2b3386d8da4770a5596ff86eda27c8(low, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return xs


def func_7ce9d0229ee04ba3b6fcd4bf1823e900(low, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return area


def func_e590123d8d59479ba0b3f0d1d3065d83(low, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return x


def func_475bf259764349a1bb1bbe8a286d00ff(low, xs, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return x


def func_6ff52fcbe6d24e8a826b5cd680f7cac7(low, xs, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return area


def func_21bb1843f5a947be9b0767ec5cbec4d8(low, xs, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return ly


def func_73a17507489642b9aedf415c543459db(low, xs, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return lx


def func_c8fd94e05f104461af0898bf07a753f8(low, xs, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return a


def func_fb5e94c95a714405b2df4797597c4100(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    return i


def func_fcf35200e71b47ea8979e3b246ea16b9(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    return G


def func_740ca2d41c424e7b85194790b193a136(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    return xs


def func_a9a064b9dfe445cdadb618dcd27ec3a3(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    return W


def func_f3cdb73b481b414085aab4171b540a4e(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    return high


def func_bc4cd570a8274d65a17b30cd43202d01(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    return L


def func_64a4ceb3d7f84548aaa37ecbd26e9c39(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    return U


def func_ae79893298aa41538b8391ebd667a959(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    return x


def func_af8385e6231d430c9713bde704900334(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    return low


def func_d41bd35515444c399ce3b6387b6e359b(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    return x


def func_26bbb78ef94c4c87800f547cdbf83fea(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    return xs


def func_b92ff31f71d34833b6986e96c95bc6b8(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    return a


def func_9afad06b95794931a8c85a96b3490dbf(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    return high


def func_7605d1fd85284d97b6689e2c59eddc80(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    return low


def func_57cebf04c643410da2c6865f282dc886(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    return i


def func_406b8c90e39745568ec63511d95ad627(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return xs


def func_60c4499b4d0c45d7abf318241a7e3b17(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return area


def func_95095ee7a8ea4a8f9e9a708968082a4d(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return high


def func_a6510a0fbe8447db8f6a981a72057fa5(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return x


def func_2a6abe82c694401085f844b4ebde3736(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return a


def func_7611642a9dfd437fa87b5fe520815ce5(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return i


def func_50edf618ad5d481ea354ea09cfe2c86c(low, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return ly


def func_4495a5999232432488f2ca0deec93ef2(low, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return area


def func_13efc9bbee4846c4af98aa1c3804265f(low, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return xs


def func_80cdb5359d064b998931f34f00444966(low, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return lx


def func_02737b2b6e0c41c29fccc66537322492(low, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return a


def func_90cb643096d242fe80b31a875cc85628(low, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return x


def func_10b2521d62de4434a2a5e43c97d515bd(low, xs, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return x


def func_d2b1ae7e01574411a8572d78646f84bf(low, xs, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return lx


def func_0a1464a12c7441758c75b7d1b5af42ad(low, xs, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return ly


def func_84f39258481143e78c3c719eac80f2c8(low, xs, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return y


def func_e79d1f99105f43d88d11cbefdc582531(low, xs, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return a


def func_6956bdac46394e0384de112fa16f3945(low, xs, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return area


def func_326418460967415c84c3342a3611ed54(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    return x


def func_2a3279c038864d35b40b630b38c228cc(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    return G


def func_33694eb7f9b54c2cac59f8d812e269e7(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    return xs


def func_b5e53569ab42451ab804ab982b97550e(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    return W


def func_d04cff9d3b2249399b420fccec9b35be(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    return U


def func_f62a5ec4290742389edca22e07cf6699(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    return low


def func_68148d5e33864c249ff3e6f5824254aa(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    return a


def func_0034782200a04848ac9ba02a9dd06f20(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    return L


def func_909fa163e569409fa821b7fcdbf04940(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    return i


def func_e0cfb9f0e109476585941c24404089bb(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    return high


def func_0e1ade63df494e2dacfea9973b03b921(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return high


def func_d68f1e8e380c41a9be0c44c8077d6d6a(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return i


def func_37c9f47cae454f03a828e3c07b49ad48(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return x


def func_37e666d3cc87493880a25e49f23f6775(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return area


def func_b56b73220265439a80f603403c55892f(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return a


def func_532c6b1eb5f5497db8df808c48e1bc61(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return xs


def func_33cc3d60df2040b18f3b2b470f5ff465(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return low


def func_9c295b72611940a78192956aafcb9d88(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return x


def func_10c9ab754ee04f64abee0091effd5242(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return high


def func_4e48896b6fec4063a54a241429308454(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return lx


def func_9659e952dba248c08945f0ff21ba9a1f(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return ly


def func_6e73c76a31c84579b9ae2016a9684b67(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return area


def func_ad403b933ef5493dbb72d0c215951449(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return xs


def func_4694be457efa49519984a17589550c42(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return i


def func_5e5bc85b21d34760a459cf220c590634(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return a


def func_aaea862d07fb4ddc93a0e2d5d8e31e01(low, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return xs


def func_f7d331eb35454e27b3c01a4a4deb9936(low, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return ly


def func_2b120ed4216f4505908bb4330bd094d0(low, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return lx


def func_13f4972b8a0f4385b74988561ce29395(low, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return x


def func_26c7e8679aa148dfa085b02c4dfc6af0(low, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return y


def func_6ac9d23440b8418b933fcb8333568128(low, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return area


def func_7314ef30cdb2489589a99df1f8fa66b9(low, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return a


def func_de20dfec32bf4aa9a351926ca76f95fa(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return ly


def func_385c25816a21429e87d5cbfa81f633ef(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return nextarea


def func_929529d307a54444a64427d862f04591(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return lx


def func_1fc6d73f9dbc4607aa7bcb7fc112df2a(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return a


def func_d21874e2139f4d3fbcea87ccd95cbcbd(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return area


def func_ab2ac701d70841d6a5136ec8dcb21356(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return y


def func_1ff6cb110b4e429b948839764f661d29(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return x


def func_bb4bc93e8cd64c9bab66499dab250166(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return high


def func_82ae83ef80494fd6af7c7ec07f021d97(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return L


def func_845bdb9dd6234c55ad5494eef2b42735(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return x


def func_07abc143083e4cafbf8a43bb1f7d4e51(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return low


def func_7fcd72694d514214a6705fc3fb599b83(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return W


def func_bd65e116e9634f7b917b89bd2aa99577(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return G


def func_96bf3cc5d67c4b45b182d029c88d18c9(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return area


def func_79904cfa1d584d838af8b2363b36d243(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return a


def func_409491c9b0bd46c5bf94a2e8327eb7df(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return xs


def func_44fdadfefe0746e4ba9eb0fa99aa879d(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return U


def func_fee97cc20f0b49deb82f6c503ea339e6(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    return i


def func_f30c32aacc6548a7bce566d334340d56(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return i


def func_f205640f8323490ab5bc8a311acc85b1(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return xs


def func_f9ebeb7e7c3a4f89a401d6b90a120c1b(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return a


def func_f6465355a9a6422bbec2bdae3250ddea(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return low


def func_c509cb2e3ef44655b2a6343a11a59c2f(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return x


def func_133e3eca8e8944c9b6016c6ce2c4078f(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return high


def func_a0d84ade1dce461eadc5577f4374cbba(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return area


def func_5f496a03b40c44758903e8261f1ca4ca(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return ly


def func_709b33e5ba7d49238d69c8a72d54c8dc(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return lx


def func_ab11c49361d24369adf715d5f1bf24ee(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return xs


def func_09638c160be34150bf77c8475d3a22de(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return ly


def func_992615b3b23242e4a41f4b909bdeb9d4(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return high


def func_57df84a56c694ea680ec252aa6858ef9(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return lx


def func_9450e86511be4b6095a5862e0e93f4f3(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return i


def func_6c8e98e628fb461e99203878fe35772f(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return area


def func_4577d145ee254972af8aaf0c0123ac48(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return a


def func_09d7f17466904123b85f748be13a3bed(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return x


def func_7fc0db95d7ea4d329cfe821fbf7497f8(low, infile, U):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return y


def func_1b8cab24390240d3ba6f47b1d66dbe8b(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return area


def func_aa532576775b419f9582fd5d7d454538(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return a


def func_c65720d00bc747418a628f8784a8dde1(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return nextarea


def func_2b04471482134eb1b3e0aca26522edef(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return x


def func_32e5001413a04b2fa7658f8a3ff1e379(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return xs


def func_c25d7976e64148c999e42f1a9ff650e8(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return lx


def func_a6bed99625e14247857c61b0631878d5(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return ly


def func_cba799e6206a4e07b58d2fa3f645bb72(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return y


def func_0c766a9173aa44d7b51f4db1db8734fa(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return x


def func_99a0f15c7f614ac08d675b7edf8e9364(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return ly


def func_ca3830b293b94c9e9b0907bf3d8a7d6b(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return y


def func_4944248c167a4cbba024c54de0dd5dc3(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return a


def func_c79406f39b04476b96c7cdde3b2546ef(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return nextarea


def func_c9ddf70f429040728e0fc8a9a1b7f3b0(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return lx


def func_1c8aa9dbe7dd4f84bf88b5a05504c79b(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return area


def func_d7bc65f3e79d4c0eac901abb5e073a7f(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return curarea


def func_d646f5c305ce4bfebf69bd3aaa169323(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return a


def func_275db35cfd774ab1a671c0545cee0b5b(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return xs


def func_6a86345f94c34e3cb26628a1a7a77703(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return U


def func_9352d0c3c1bd42b49f485919f4ea6dc9(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return low


def func_1bc721abb1834c8c8a267065b126d39e(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return ly


def func_f9cd9321a6ef40da882da92ff0f02f70(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return high


def func_7cb85f7994af4f2ab3bc8e995f5a5619(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return area


def func_2878921837664cf7b81d0d356b6cc8a3(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return G


def func_f6762b2cb8964836adc850b19e944622(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return lx


def func_db0ca6bdc6bc48d19006bce9ac8b7e60(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return i


def func_e50912217a0b4d37b735a100606713cf(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return x


def func_e3129104db7e4bf083ab0dd07fe579af(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return W


def func_73a73d2f806f48ca8b843fa908a91512(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    return L


def func_3111524e563241678f5136ab86ae1e76(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return a


def func_750fbb27ea984a2a9c176c36ef2dfd36(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return xs


def func_2ca99b3d4a00423685eff78e9bf52165(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return lx


def func_9199a14173ee489cbfbef0803a8fea6b(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return low


def func_063728c6a22b4cd5b9e3dfe937ceb0cc(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return y


def func_ffc6c358db864391b9cb76fcaa68f295(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return ly


def func_4d0bec2bea5e451182173e0f8112453d(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return x


def func_5456b31bb56944afb47e990e944b6084(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return high


def func_758ecfb3b83848a98f3e35dc6f8d0b2c(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return i


def func_c3bec1a097b9401c86977cc46f8a5c04(infile, L, U):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return area


def func_d1f4367ae63a461d8894ed6247fac70b(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return ly


def func_bdc3afa82a0340e1b290eafd4a1dc690(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return area


def func_fa18dcdc6bb84d1b815eb56f12679e23(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return xs


def func_b038cef4aaa94d538ca8e3fffe65f2b5(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return a


def func_f15e9192a54941afa5df5719000083a0(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return lx


def func_720be87672644549b916139a15b96a8c(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return x


def func_1a838a7dfaff4e95974f8b69478afcf5(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return i


def func_7e1bcc29120d4ae3ab71351b264312a1(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return nextarea


def func_20192683dcad4064bdeaef2a5692898d(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return y


def func_cfbd73ea8b414fcc821b386ddc907534(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return high


def func_2a116ee9f1354eff8c3290dd656e3873(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return curarea


def func_727ec1876137400a868e5b7c85271960(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return nextarea


def func_48894b3aa2c74ef5b2534f2c233810ae(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return a


def func_0d45b789edaf4a2184707d28ae820de5(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return y


def func_46f6a3cdb9f1466e821e2352b361f807(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return lx


def func_5692fb5e5a4a43b88361475eb268e064(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return ly


def func_390c2d07ee7e41c6a6fc27cd68fe2add(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return area


def func_6545c4a8bd444043b852f998f4e6d06f(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return xs


def func_bf04e767f9b84a53b9b871f166e6ab0c(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return x


def func_60d3207db7594040b20f6916be0d15ec(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return area


def func_0c2627e820294459bef7df607e4a3ee9(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return y


def func_d207de4340c84fcfb3a772aa4caffbda(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return nextarea


def func_109f34052171437faa5807013a2343e9(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return curarea


def func_588c27e6362444a788d2cdc171c89df2(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return lx


def func_83be91df772b4f3e99ddc61d044ed4c0(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return a


def func_f5534b939b1f462687b3bc977ba408f8(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return x


def func_aef820d2027a4a4c92f66d7cb6078aa5(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return ly


def func_76b2b166234449c68aa7b299118b5739(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return y


def func_ba828d5825934f36a0ebb23c555e7015(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return xs


def func_b5c9f15ce87f4b8c87b21139dfd4597f(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return G


def func_65a6ab9294c0420fb255c3cf8153b129(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return L


def func_210dd819e8f64116b87736e91315520d(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return U


def func_9e21a6ff204d4999a0dd0eed0332291a(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return x


def func_e84fc46e33e348afa83f1c324d2a7a5a(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return ly


def func_1199172e2487409bb82e90b4a8a253a5(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return high


def func_7d7a6c3a41174895bf8ac219784e977b(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return W


def func_0ea564e84fae4d4eb59ac80ffa006c8f(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return lx


def func_9287a004c25c4ba5b07f347d03fb5aa9(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return i


def func_6e1f1ad0023b481d8e23e8ec57d41515(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return low


def func_04bd0d1fad7647958fa1987580d2912d(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return a


def func_d5219d6d98104463828cc08683ce7584(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    return area


def func_2973eb2844b54a018bf83288c4c8377f(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return y


def func_3aa37f9037ac459cb1bf6fb0d14da3a8(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return x


def func_4cd96b5dfb0645fdbd20d5005e18057e(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return i


def func_21a95eef11ab484188ee46ed0c958c05(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return lx


def func_8152a6d2fac84c148b9da456ca4eae69(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return nextarea


def func_9242b0757b9b439da1d041078cc03376(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return a


def func_387280e2a89147d99fb877081036047c(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return low


def func_9c345b1f4c8f4deabb23a30d759fa7d8(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return high


def func_95a0fe988f1140a589f9cb0b61c18db2(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return xs


def func_eb6d9f4b00114b5ba73f0f9bff23c6e1(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return ly


def func_71a3306e5b86442f881e9eaf9209c4b2(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return area


def func_fb78ae5617c64a658b5df99b4760069b(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return ly


def func_8acaa27c404a43d4a22f4932689a5e3c(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return i


def func_58fa8e5f466c43d2a1dc906e53ec8675(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return area


def func_e8b46c25fbea4a9e887f6cb3573e2961(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return x


def func_33a839f24fc44e718ecd4d528659cba3(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return a


def func_cbbf235ca5c647ebabd170fe0c7cf55d(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return nextarea


def func_c75c52096b7844d0aec1ae3b5263978c(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return y


def func_c2db1c1323ab417080736914cd394064(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return high


def func_1755ae58cd394a60b81091f00320ce0c(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return lx


def func_2881ffacbac94d2eb9b92d8c1eed4daa(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return xs


def func_f2d541d982674a09837dc7fda90ef36f(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return curarea


def func_6ac6ea2b6e7b49b69459a3100c11dc7e(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return ly


def func_0d2eaf5242784544865cb01174fc63c9(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return a


def func_fd2855bbdeec4fd380ee0710e4098451(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return area


def func_245ae5dfce794a189109095df19ca947(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return lx


def func_38796e2ed3134f80b69255ffb7613f9e(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return nextarea


def func_35d26768dcd941109f650315bf7e0c31(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return xs


def func_631fbb98cb6a4e6a85607dede0fc9bdb(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return x


def func_0f6a386fb1f94e3eae178b62b90d9b89(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return y


def func_78206388d4dc427aa94126bbe3b7de6e(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return curarea


def func_c0ed7c43bcd941d0abc3fa2fd8d1a54e(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return ly


def func_93440c80b0d047eebdd7cf359847db41(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return x


def func_9f039fbeb59c44b6838baf87608bcc1d(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return res


def func_b854b376c3bc4c0bbced8cd20351bc5f(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return nextarea


def func_d545664d162645eb9c4f2e444b0eea86(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return area


def func_f57371e1d9a44796b1c0d2f031e154fc(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return a


def func_9c2b6cbf94a94bc7b43a6989d904c03e(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return lx


def func_11b4a554ed1d46a28d09cc4d96efff41(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return curarea


def func_6fe2c74770a44e9e8bed2eb5f5dc61c3(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return y


def func_4dd93b7763b94faab4fc83188b503d36(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return low


def func_ea2d08f2d1b24cad981b3f826b2f0a22(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return high


def func_664d74dc96064de6a80aad6d4ba1f171(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return U


def func_4ee593c72fb24562a812beb7239c2864(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return L


def func_e813f1c5d04d488582281a569a17d507(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return G


def func_e5fc11b381354a429aaf61ae2fff5846(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return a


def func_80c7cd793f6e4dcf86f207c946f2ae15(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return xs


def func_3a75ed9dc2694ee8a0d41149441286fc(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return y


def func_4310572328ff4e4f82ba7715f128cdc9(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return lx


def func_b313d93ed1ef44fcb731aaebe73a2ddc(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return nextarea


def func_70a4483678da440bb2e38fa6ba416004(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return W


def func_12feb497ce0c4d56a9ce3246545fa62c(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return area


def func_d0729e0038024bf38a5079a521bd43a8(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return ly


def func_7a38beddc7164d05977f365ae762a20f(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return i


def func_97bdca97d2914fecaeb789fda4f8abc2(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    return x


def func_b3aebff27bb44d8b814b85bd265fa460(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return y


def func_e5e5bb28a4c4408694dfae56e9ce6c16(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return high


def func_1e85a183b1f64606b842b8884e6023c7(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return nextarea


def func_508ea54b2894452f948dd492ea9a0348(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return lx


def func_07da7c05c45f42bb8cfd4461031dc79d(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return curarea


def func_b22b0f21c9c14ee6bacd17296159e9d9(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return xs


def func_29d1882f38fc4b97973aacb00769ced8(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return i


def func_4b63531fc81b4afab30df8dac76747b3(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return low


def func_c2a3a809f37245a59cc7337c8f19b31d(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return ly


def func_c51dfb7dc37f4e1a90060e166987bf5b(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return a


def func_757bd6ceee1e4ddbabae24334aab702d(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return x


def func_d9ff0d15ed7046839ada80c331dfd1a2(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return area


def func_c0283213bdac4a1295724e729d3bc512(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return lx


def func_a42c5c0ca51d4a61a58dab921ddea4f5(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return a


def func_55e0aacc5ad14bb98f265e6def1608e4(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return i


def func_64de69baa0604f7bb2ebb418ac17d8d2(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return high


def func_fedea16ad0204ed3b169a78c19314ee6(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return x


def func_827854649f0c4140b110fb02c458f487(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return ly


def func_0251f3aba94e4bbd9e414aa0139657b9(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return xs


def func_7d5843ef4ce04c47801dd8de3502356f(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return curarea


def func_3b4734669e9e493ea95e9a5282022ba7(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return area


def func_8897fbd206c64dc88bca022f502e7ff3(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return y


def func_fd1b8f83a25a4d01b1973e7db8513e66(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return nextarea


def func_4a798d8e325643c4898f105f1725c7cd(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return curarea


def func_783d2f61634e4e8a95e0b7658e1d634e(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return ly


def func_1a8b867f638549258c0a3d8527e63f53(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return y


def func_ccc0e024fe56496ab148a69a0bb6c8d3(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return a


def func_d922937a6f844349842448870d7b7ea0(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return lx


def func_288fa7fb83394b2d86948fc7b760ae24(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return x


def func_318513888b344b1f9e2658f89886f42c(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return area


def func_2b87082b9f82422c9a60ae34d0390c3c(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return nextarea


def func_475b0e7e2b3940069557805c33222899(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return xs


def func_5a839063722e4708ae3d4c8210e50d8b(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return res


def func_e5f69f05b0bc4ad596f44311bbecf65e(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return na


def func_a0176f69117149cb818f9fe6bc52450e(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return a


def func_185f784a341d4db296658afb67af1cac(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return curarea


def func_a803c8d66ae54d89a06eaf9790279225(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return x


def func_1b7f066a0f8f49a6bff6f3044ff4de00(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return y


def func_24d1aa461164449c966b832a95ace3b0(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return nextarea


def func_9e05c609994a4744b5492ac68c4b4047(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return ly


def func_354a521f377e4be391f0f8c6e88abbfe(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return area


def func_2ad89d66cbb84eb4a140ea9168a5984f(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return lx


def func_75954b8893154d48804d216b3c2b9530(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return res


def func_6cbc144543a8490cb8c465acd89190ce(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return high


def func_c92e2d7b8dab45e18c3cf5255513af3a(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return a


def func_5bf6cb1cd3344ac39db3d7dd8654122c(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return nextarea


def func_a38643513d7b4d0085dd9aca21119084(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return x


def func_a9031993349444129b4bf1ad0fa2c339(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return curarea


def func_6a71ed59059e4da896b2c793c21f8db8(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return G


def func_e85a63077aa74c069127329624f7d04c(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return L


def func_8e49c885394b4a0ea937cee28c635b04(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return lx


def func_bcd68404085a4571b948bf255711c48e(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return ly


def func_ea1b9dc668cf43b7a742951e1ad72213(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return y


def func_68d06c050577411ea0a22d986ba593ae(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return area


def func_589883555f92402bb4e0b0ce90077686(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return W


def func_29f03d37b87645748004ef6c7852bf7b(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return U


def func_22d123e789ce4b018e0eda95faed1d0e(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return low


def func_6121458678564142ba04539f38dbe2a2(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return i


def func_80eefcce8c3748a48e71a83c7cd3d86e(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    return xs


def func_06a1835a028d4164982157ff224d3fe8(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return area


def func_ad46eff800264ecd93d11a9b7f6772fb(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return i


def func_e5614c960ae64536bffacef52bd70f12(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return x


def func_aada229126f043478d2499ca45ad3b0e(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return nextarea


def func_39d6d907613f4e0198b939d362f4f758(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return y


def func_9d617da5bdfb4e9cb0292bb0c89834a3(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return a


def func_3cfbe37241f94d729c353680bd0679ad(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return curarea


def func_82aeeb3abba94baaab65d8260f3c6f26(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return xs


def func_89a6774b8887498e8c4ac6185c00e3ee(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return high


def func_8a88d236f08a4863b12ce924b5df4b58(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return ly


def func_1bb81f5b6e8d430fbaefc7cd0f273841(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return lx


def func_920460edd1114ad68d04bff9d31d68aa(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return low


def func_20b8118b18dd43a5b3afa2a6627c055f(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return x


def func_bf238072ca0d4ed5af60f249060ecc7e(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return lx


def func_66ea4418bfce497ea2e08958346ef52a(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return nextarea


def func_c52c70a3b55f4afab1a213508c1349da(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return high


def func_25c256cee43949b9abd579dcbb1a6111(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return area


def func_ad408a5253e14cbe9ad139542291df83(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return xs


def func_f9a9aa30b79b4c808c8d8f582da88c56(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return y


def func_64ac44b54c62465c9c28870d598eaf73(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return a


def func_81ecc8e4bd354de9b2d6b881d9279af0(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return i


def func_45f83af5c93e45c19eea2df4b6f20a1d(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return ly


def func_9f17a26dcc204cab845c19817efd0948(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return res


def func_cca40e21922141f98c97a338ae426878(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return curarea


def func_7c42ba70501146b19ace91caee23a425(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return area


def func_7c5c9b440c3a4ab7b70bdf5dd4934a00(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return na


def func_eda43848ead145c287f1d81be1f2aa1c(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return x


def func_1d4ee9cf35a641f0a8e4789d1aef3e82(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return res


def func_fa02d416588a4f4a926e5c0bab2513b1(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return lx


def func_3bb1985c434a4c0bb71602426b8249d0(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return a


def func_e7ff3a42ef7c46f3b7fe3ea12dbe285f(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return ly


def func_1f4d63c5727c446fa3ac7bed841e9337(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return y


def func_680aa986dcc64fd9a2c77ab3534bf6b6(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return xs


def func_f0543446b31e49beb90fa10780cc4ec2(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return nextarea


def func_b1815a5af48b42e8a24108255eb1574a(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return curarea


def func_e63ece7930984d1cbb1baed65e751a99(low, xs, G, high):
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return res[:G - 1]


def func_f2f6e23abc2244758ee8ec4921968e8e(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return xs


def func_08062d9f0a2f4eea81ce88d7df0d71a6(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return area


def func_7fa5866563f641dd9ae792e431040103(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return y


def func_7bb0fe29f14349d99562c1afdb601afd(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return low


def func_a6c26cc919ee46f09f05cbc965d45126(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return W


def func_5d524a9fcd32484682a1a455ffc4d0d3(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return x


def func_6ab1a26d3f264c38a6745be6a0fa129f(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return ly


def func_626e3969121343c9be28c01e1dc0ce63(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return nextarea


def func_cd781f45052e4573a1738bff366c1ee4(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return lx


def func_eb0d1488091149839c6d675fa866bb61(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return L


def func_ae559d0ac7894a1a94c70524f7b91283(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return i


def func_df8c4ead57cc458a8e37ec683cacaf5a(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return a


def func_d4641e3114ff4c7c844bf3d04a6bb0d8(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return U


def func_8cd043de15e34c24bae07b38d0faa28b(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return G


def func_8ca74508936441b6a20f748fcb20575d(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return curarea


def func_a693de2d1f6b4642b31910ef7283fab0(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    return high


def func_1f45955629144925a6b291d8f7ebfa69(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return x


def func_998f27c0880243f1b1f2c23056b96f85(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return xs


def func_610d96a6483b4054a90de49e5545ead3(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return area


def func_361933e0741d4e38b7048acc9c395852(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return ly


def func_21b4adaca70f4fa7999b4504da998036(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return i


def func_ed3df92b2c5a45fd96440e124e3867e1(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return nextarea


def func_b4e7b863775a4f088e98745c71a39b58(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return lx


def func_fdb4251eecda4a7e9efb98d9e32e0fcc(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return high


def func_cc2677c118304ac2be241dd86b81ed28(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return a


def func_3294e71fd1324b42b9be67ddc08f52c9(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return y


def func_750f36ed976b43c0bda046919efdbba4(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return curarea


def func_671be99eb1bb4a1aa29eadc1dba5bf3b(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return low


def func_a2fa081affaf490696cfdbdd7ff41d5f(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return res


def func_0b7da2131f8447d0b5dde8896ca29891(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return nextarea


def func_a5544a704b4e4428ba08d8f9b19abf01(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return curarea


def func_c6256c5fcc0345e0b4928844b990a6ce(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return lx


def func_83d9da3e25b24a549c77c9a45ba39890(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return area


def func_fa7719af9abd42148183ad159717f760(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return y


def func_8c4b1bf9345e49179d498186700f84f9(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return i


def func_5d44a2f7de15462db1f89a30e3da365c(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return xs


def func_13f75e2a86714ae6b65c16a84570d77e(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return ly


def func_531d471db52245ae83e35e59bc954b4e(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return a


def func_24200876b47949cb80ecc0bdc5d0b3b9(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return high


def func_d1fdd73449b5450c9d8c7309968037d6(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return x


def func_5f028c299a514f23a4fda81621f4f8d4(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return res


def func_44086f14ea15415a8d42334fdfe4434f(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return na


def func_afe7a12ed2b04b23bdb7d93cbd32082f(low, G, high):
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return res[:G - 1]


def func_228bf2dca5474690b9623d0202c00546(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return area


def func_2809b224450b488f86ca9bee9db43b9c(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return i


def func_a339f2ffec964f26aa4fdeb7b02b8d3d(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return L


def func_80ababb4de4c4bbcb5c93b2da01ed382(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return U


def func_36eb8285559142eaa9a4ce0267be5496(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return W


def func_0518320e0a1740ad89e64e13b35a1426(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return x


def func_5a3cb6a5757c47eea54a2061949bbb60(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return res


def func_6f79eb1de638427c850157c7394350ac(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return a


def func_ebd8c4b8bf0b416cae1890ec027bae7e(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return y


def func_f2c0c1c517824062bf50cafc23331fb2(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return high


def func_900b0a1072954461a05e6b455c458453(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return nextarea


def func_2e4394c68be340bd9aa5dec9bfb18505(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return ly


def func_cedb0ed92d1e4ec6b10579287d5f047d(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return curarea


def func_26b1f73ff15b4355b37a55b47fef0ac4(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return xs


def func_a86f974e85924a2db01c61a8e0b1e07b(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return low


def func_19c68691320b4ec58c7f8ab4d2a6f22b(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return lx


def func_5b5da877806247b29bbcde09b935b079(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    return G


def func_c286a3125f3c4d449e73026d5bc89bf0(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return y


def func_4e3fcd2d7b1344cda87b6cce0c49b513(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return low


def func_629114d924ca460b9042fe949f680408(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return x


def func_e060362cbc06426aac5725f4f6f3b831(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return na


def func_02cc876a47a14155bf1f544fada62099(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return i


def func_c8440e481fff4014acec240f9e025251(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return area


def func_bc9a6ae71db243e3b65e6586d3485f30(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return curarea


def func_7c5fcc14241c4d068ce419a4a4a4f4f9(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return a


def func_9f646df495df43968afbf3bddb892724(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return ly


def func_c02db8046c474b11871108492a5d4f17(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return high


def func_84a2db8a1f0b43eba8b26c010d684ca0(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return xs


def func_aedd4e2bbcf344a694ca1f74a16c0b71(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return res


def func_42f9c68b25b84074986c14baa08e7b8f(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return nextarea


def func_b7d7916313664a71a72054890bd695c1(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return lx


def func_4fd15af38d0f48dab0d601ab4f5a2231(low, infile, U, G):
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return res[:G - 1]


def func_5d6b5bf0bc2142ae93b5e41f3113d1b9(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return xs


def func_3c360e1c23874540968e25af28f37367(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return area


def func_c82f5b1957e54886b37fff03b117708d(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return U


def func_5f473a7ac7e4402ba75bb090f2ff851b(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return y


def func_0a6588cc7ac24f2a9a69f9b3d4745604(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return W


def func_54d2d1c9db1b428db8751950e6895537(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return L


def func_a20632c692214c0984ceb00d544dd5fd(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return res


def func_f7128fede4a544bc86111763fa4c3712(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return i


def func_5a045f103dce4f72803bc14079af4b4d(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return a


def func_4f133567c28247a7a2dce370f0a154be(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return nextarea


def func_719fb918a1854da8ae4b6b680fa21f63(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return low


def func_4550f08c2b6441ac8a0aabae14178437(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return lx


def func_d7f183d29ac54b4dae128f574831ffde(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return G


def func_11f2e5898a614f00a61b0ebf8daa27a0(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return curarea


def func_d567258bd4a442bdaf84f42b936ddcc8(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return ly


def func_23635835d38341978b699801bf0228ce(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return high


def func_276b9efcaf2b4e40a02e8d43189b750f(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return x


def func_decd1a44172c433cb13af994083b0328(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return na


def func_64a57b7bc31849bf856232416b7a9c44(infile, L, U, G):
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return res[:G - 1]


def func_c9c5cfd1848b4b3fba953f562d3bd74f(infile):
    W, L, U, G = map(int, infile.readline().split())
    low = [map(int, infile.readline().split()) for i in xrange(L)]
    high = [map(int, infile.readline().split()) for i in xrange(U)]
    xs = sorted(set([x[0] for x in low] + [x[0] for x in high]))
    a = [(x, find(high, x) - find(low, x)) for x in xs]
    area = 0.0
    lx, ly = a[0]
    for x, y in a[1:]:
        area += (x - lx) * ((y + ly) / 2.0)
        lx, ly = x, y
    nextarea = area / G
    curarea = 0.0
    lx, ly = a[0]
    res = []
    for x, y in a[1:]:
        na = (x - lx) * ((y + ly) / 2.0)
        while curarea + na > nextarea:
            res.append(lx + findx(x - lx, ly, y, nextarea - curarea))
            nextarea += area / G
        lx, ly = x, y
        curarea += na
    return res[:G - 1]


def func_ccb1a388d5d842d7ac8601f59922a75e():
    infile = open('codejam/test_files/Y11R5P1/A.in')
    for test in xrange(int(infile.readline())):
        print 'Case #%d:\n%s' % (test + 1, '\n'.join(map(str, run(infile))))
    return infile


def func_7f55bcf7096444d38c73d517222ab8d1():
    infile = open('codejam/test_files/Y11R5P1/A.in')
    for test in xrange(int(infile.readline())):
        print 'Case #%d:\n%s' % (test + 1, '\n'.join(map(str, run(infile))))
    return test


def func_16b3ead5beac45a0976dde42b6ac9704(infile):
    for test in xrange(int(infile.readline())):
        print 'Case #%d:\n%s' % (test + 1, '\n'.join(map(str, run(infile))))
    infile.close()
    return test


def func_fd2b9c17bc014e4b80e4471f8cb3f372():
    infile = open('codejam/test_files/Y11R5P1/A.in')
    for test in xrange(int(infile.readline())):
        print 'Case #%d:\n%s' % (test + 1, '\n'.join(map(str, run(infile))))
    infile.close()
    return test


def func_0e5e36a98ab847b29f44fe81157ba222():
    infile = open('codejam/test_files/Y11R5P1/A.in')
    for test in xrange(int(infile.readline())):
        print 'Case #%d:\n%s' % (test + 1, '\n'.join(map(str, run(infile))))
    infile.close()
    return infile

import sys
sys.path.append('/home/george2/Raise/ProgramRepair/CodeSeer/projects/src/main/python')
from CodeJam.Y11R5P1.dP.a import *

def func_22e238908c77460fb2838c37eb7e776a(i, L):
    dx = L[i][0] - L[i - 1][0]
    d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
    return d


def func_eb7fd806795c41958a2fe354088fa428(i, L):
    dx = L[i][0] - L[i - 1][0]
    d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
    return dx


def func_60556d21d4524477a0194df727380985(i, dx, h, L):
    d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
    for x in xrange(dx + 1):
        h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return x


def func_01229215fdca4336a28b1257f3abb832(i, dx, h, L):
    d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
    for x in xrange(dx + 1):
        h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return d


def func_d22a185008324aec8478c2448f99f4b9(i, h, L):
    dx = L[i][0] - L[i - 1][0]
    d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
    for x in xrange(dx + 1):
        h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return d


def func_be5dfba3ef1a488e8a65ee375d3052f9(i, h, L):
    dx = L[i][0] - L[i - 1][0]
    d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
    for x in xrange(dx + 1):
        h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return x


def func_be560f304026480ab1e794ef00e431b2(i, h, L):
    dx = L[i][0] - L[i - 1][0]
    d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
    for x in xrange(dx + 1):
        h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return dx


def func_a2bdf125333f47a087ae10649704edc0(i, L):
    dx = L[i][0] - L[i - 1][0]
    d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
    return dx


def func_003fd77ddbb84c28bf20105d8bf164fb(i, L):
    dx = L[i][0] - L[i - 1][0]
    d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
    return d


def func_77f8ff1ad1224eada87e83c447c4a244(hl, i, dx, L):
    d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
    for x in xrange(dx + 1):
        hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return d


def func_6ccae83b31d84064802f5eb537901be2(hl, i, dx, L):
    d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
    for x in xrange(dx + 1):
        hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return x


def func_e48a0d18a6be4f8d91b01382532d8326(hl, i, L):
    dx = L[i][0] - L[i - 1][0]
    d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
    for x in xrange(dx + 1):
        hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return dx


def func_8b1bc3e358df47d08595a5135fe9c41c(hl, i, L):
    dx = L[i][0] - L[i - 1][0]
    d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
    for x in xrange(dx + 1):
        hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return x


def func_119c508320314fb8a5c836446620187c(hl, i, L):
    dx = L[i][0] - L[i - 1][0]
    d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
    for x in xrange(dx + 1):
        hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return d


def func_8b8e7e09c6d1418b89bae76390540a27(i, h):
    hh = (h[i] + h[i - 1]) * 0.5
    c += hh
    return hh


def func_f968247c683b4ded9a945a0ab6f0795b(i, h):
    hh = (h[i] + h[i - 1]) * 0.5
    c += hh
    return c


def func_11397e2e790e4404b2d9d54621dcf42e(rr, ll, i, h):
    m = (rr + ll) * 0.5
    ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
    return ap


def func_e44b9cc7a53d4d20a544387412c487f2(rr, ll, i, h):
    m = (rr + ll) * 0.5
    ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
    return m


def func_a8bef0a32b5d4f3691dd6757d5090a49(c, m, i, h, d):
    ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
    if c - d > ap:
        ll = m
    else:
        rr = m
    return ll


def func_81cce3bb18784705a51c34c4aa87fe85(c, m, i, h, d):
    ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
    if c - d > ap:
        ll = m
    else:
        rr = m
    return ap


def func_13c2a210de6b4f7c9edaa19db6578eec(c, m, i, h, d):
    ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
    if c - d > ap:
        ll = m
    else:
        rr = m
    return rr


def func_4e0591a2ec8243378ebcf6591b77cfcd(c, i, h, d):
    m = (rr + ll) * 0.5
    ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
    if c - d > ap:
        ll = m
    else:
        rr = m
    return ll


def func_a701d2af9ba5487091c2f2f789ce2c43(c, i, h, d):
    m = (rr + ll) * 0.5
    ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
    if c - d > ap:
        ll = m
    else:
        rr = m
    return m


def func_e62b0ca7f29d49faaf99310bb2552b6b(c, i, h, d):
    m = (rr + ll) * 0.5
    ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
    if c - d > ap:
        ll = m
    else:
        rr = m
    return ap


def func_4f6f531ca88349ec96525c85c9eb72ea(c, i, h, d):
    m = (rr + ll) * 0.5
    ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
    if c - d > ap:
        ll = m
    else:
        rr = m
    return rr


def func_36a07db4500545dd8d1a5f48ccc6f6d2(c, i, h, d):
    ll, rr = 0.0, 1.0
    while rr - ll > 1e-08:
        m = (rr + ll) * 0.5
        ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
        if c - d > ap:
            ll = m
        else:
            rr = m
    return ap


def func_d9c59f168b24409f8d20d32867688600(c, i, h, d):
    ll, rr = 0.0, 1.0
    while rr - ll > 1e-08:
        m = (rr + ll) * 0.5
        ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
        if c - d > ap:
            ll = m
        else:
            rr = m
    return m


def func_2d11a9a5fde24b5fb12b8b4d21bf1293(c, i, h, d):
    ll, rr = 0.0, 1.0
    while rr - ll > 1e-08:
        m = (rr + ll) * 0.5
        ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
        if c - d > ap:
            ll = m
        else:
            rr = m
    return rr


def func_226381463b404fbcbec1d3118eb09a11(c, i, h, d):
    ll, rr = 0.0, 1.0
    while rr - ll > 1e-08:
        m = (rr + ll) * 0.5
        ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
        if c - d > ap:
            ll = m
        else:
            rr = m
    return ll


def func_03503af3ad7c404e83749bfad6a2e92d(c, r, i, h, d):
    while rr - ll > 1e-08:
        m = (rr + ll) * 0.5
        ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
        if c - d > ap:
            ll = m
        else:
            rr = m
    r.append(i - ll)
    return ap


def func_f9b8615d1a20464ca8b01f4d89108bad(c, r, i, h, d):
    while rr - ll > 1e-08:
        m = (rr + ll) * 0.5
        ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
        if c - d > ap:
            ll = m
        else:
            rr = m
    r.append(i - ll)
    return ll


def func_e176e15526ca48ea83d0dd722c8d9879(c, r, i, h, d):
    while rr - ll > 1e-08:
        m = (rr + ll) * 0.5
        ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
        if c - d > ap:
            ll = m
        else:
            rr = m
    r.append(i - ll)
    return m


def func_bf6b2bcf01f243f89a135e7274fb2fa9(c, r, i, h, d):
    while rr - ll > 1e-08:
        m = (rr + ll) * 0.5
        ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
        if c - d > ap:
            ll = m
        else:
            rr = m
    r.append(i - ll)
    return rr


def func_ec150f1c45cd47ff96771e6460c1bae5(r, ll, i, d):
    r.append(i - ll)
    c -= d
    return c


def func_6638d5852d8d42c38b0a1b13ff7d8a0a(c, r, i, h, d):
    ll, rr = 0.0, 1.0
    while rr - ll > 1e-08:
        m = (rr + ll) * 0.5
        ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
        if c - d > ap:
            ll = m
        else:
            rr = m
    r.append(i - ll)
    return m


def func_4cc47b7e9eb846d9ab6a2841c736d1d7(c, r, i, h, d):
    ll, rr = 0.0, 1.0
    while rr - ll > 1e-08:
        m = (rr + ll) * 0.5
        ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
        if c - d > ap:
            ll = m
        else:
            rr = m
    r.append(i - ll)
    return ll


def func_784578a099a0483ba6218b1eb1622dcc(c, r, i, h, d):
    ll, rr = 0.0, 1.0
    while rr - ll > 1e-08:
        m = (rr + ll) * 0.5
        ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
        if c - d > ap:
            ll = m
        else:
            rr = m
    r.append(i - ll)
    return ap


def func_2d6664c9cc9940eb9b2388b493595f3f(c, r, i, h, d):
    ll, rr = 0.0, 1.0
    while rr - ll > 1e-08:
        m = (rr + ll) * 0.5
        ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
        if c - d > ap:
            ll = m
        else:
            rr = m
    r.append(i - ll)
    return rr


def func_2c9185103fd845e0a5f4f3486b04adcf(r, i, h, d):
    while rr - ll > 1e-08:
        m = (rr + ll) * 0.5
        ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
        if c - d > ap:
            ll = m
        else:
            rr = m
    r.append(i - ll)
    c -= d
    return c


def func_4673e72139c54704aea47bef924939d9(r, i, h, d):
    while rr - ll > 1e-08:
        m = (rr + ll) * 0.5
        ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
        if c - d > ap:
            ll = m
        else:
            rr = m
    r.append(i - ll)
    c -= d
    return m


def func_455a22c6c2e444b8981c3d3caaf2cdb2(r, i, h, d):
    while rr - ll > 1e-08:
        m = (rr + ll) * 0.5
        ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
        if c - d > ap:
            ll = m
        else:
            rr = m
    r.append(i - ll)
    c -= d
    return ll


def func_e8e1c44dea2a40b9a7e19350ec7c9abb(r, i, h, d):
    while rr - ll > 1e-08:
        m = (rr + ll) * 0.5
        ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
        if c - d > ap:
            ll = m
        else:
            rr = m
    r.append(i - ll)
    c -= d
    return ap


def func_aa468f780bf946a588729c9ec8afa82a(r, i, h, d):
    while rr - ll > 1e-08:
        m = (rr + ll) * 0.5
        ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
        if c - d > ap:
            ll = m
        else:
            rr = m
    r.append(i - ll)
    c -= d
    return rr


def func_2578bacb45784d41926cb4202f4c1499(r, i, h, d):
    ll, rr = 0.0, 1.0
    while rr - ll > 1e-08:
        m = (rr + ll) * 0.5
        ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
        if c - d > ap:
            ll = m
        else:
            rr = m
    r.append(i - ll)
    c -= d
    return ll


def func_fe86576b292e4521b9ae52b464c03699(r, i, h, d):
    ll, rr = 0.0, 1.0
    while rr - ll > 1e-08:
        m = (rr + ll) * 0.5
        ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
        if c - d > ap:
            ll = m
        else:
            rr = m
    r.append(i - ll)
    c -= d
    return ap


def func_d586b5aa05f24b50b00d72b9cee78f5a(r, i, h, d):
    ll, rr = 0.0, 1.0
    while rr - ll > 1e-08:
        m = (rr + ll) * 0.5
        ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
        if c - d > ap:
            ll = m
        else:
            rr = m
    r.append(i - ll)
    c -= d
    return rr


def func_d73ddd54412e4a01a9b712cdb0df17cc(r, i, h, d):
    ll, rr = 0.0, 1.0
    while rr - ll > 1e-08:
        m = (rr + ll) * 0.5
        ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
        if c - d > ap:
            ll = m
        else:
            rr = m
    r.append(i - ll)
    c -= d
    return m


def func_e3616311702a4cc1893dc2bbf55b4fa3(r, i, h, d):
    ll, rr = 0.0, 1.0
    while rr - ll > 1e-08:
        m = (rr + ll) * 0.5
        ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
        if c - d > ap:
            ll = m
        else:
            rr = m
    r.append(i - ll)
    c -= d
    return c


def func_55a3d1333b6941f5a24a9e3815d218aa(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    return w


def func_1c6ee729f6da4f3dbf9d38ab9c1ca776(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    return L


def func_ab38ae323da44b318132858628130324(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    return g


def func_37b382e40bbf4ce8a0ea1ffd1ebdeed3(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    return u


def func_2cc2087564224c99beac7246169adafa(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    return i


def func_6e3929f36eac4072b661479e994e37e9(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    return l


def func_ae5d1b0d2dae4c7faec1d4e877f28696(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    return U


def func_468424a84eb04721be0f7c6d58331120(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    return L


def func_28fc28c202cf4df3a6ddbe21211775f0(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    return i


def func_eb763c1d3cb743888c848b2f48090d7b(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    return i


def func_b8fef0060c084164957b7a00ac7db634(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    return U


def func_2c4dbe6445574c43bbe91733cb077326(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    return w


def func_49eaee45c9d743e098871b225458b737():
    w += 1
    h = [0.0] * w
    return h


def func_dcaf4b33672e46be8bc6223e7fbfceca():
    w += 1
    h = [0.0] * w
    return w


def func_5e4a98bcb56148ad83ef1a7915681787(w):
    h = [0.0] * w
    hl = [0.0] * w
    return h


def func_07c1c9e6f0ef4c5e9d7cdd105d64e1b8(w):
    h = [0.0] * w
    hl = [0.0] * w
    return hl


def func_e24d6d7019bb4d6ba5055a8301f83bfd(w, l, h, L):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return i


def func_614e1368f5794f219a772beb7964e893(w, l, h, L):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return x


def func_7f509701c69a4edc8095bfcd8b49b68f(w, l, h, L):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return hl


def func_a62a6beee8464694b4bde175945b30b2(w, l, h, L):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return dx


def func_58178e8776764a949d39471c30858812(w, l, h, L):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return d


def func_73ab45761df643a99c0629d6ca625181(u, h, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return x


def func_09bb809e35cb443280c1a090d302aabc(u, h, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return l


def func_f9e572cac74f482296c2f1104c59cbdf(u, h, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return dx


def func_5c867dcc9b604b469e4a0b3dee25846d(u, h, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return i


def func_94aa3ba23e2a4755a2102cc19f7fedef(u, h, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return d


def func_66ef14362b6247768d5923ff2d5a8c32(u, h, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return L


def func_52563592b83046e2a13e7c19aab6d795(hl, u, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return d


def func_58b2bc96edd9455cade1d1f274880283(hl, u, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return i


def func_8bbf191a1ee242ea8f96aa36e93b859e(hl, u, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return L


def func_e9121124479b45f9bc07728599b82c04(hl, u, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return l


def func_69a485586312493cbee0abd868a8e85f(hl, u, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return x


def func_b66665d48583411dbf9fd95c2929ec05(hl, u, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return dx


def func_6bd94709b87c4f7db545076e978db595(hl, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return dx


def func_c928601fd1fb4215a16ea45609f1a5a8(hl, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return h


def func_ed355665ee0d4d6f9268a69bcd426f99(hl, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return y


def func_71fe74c7ed4a4c4197214b3c3e6fa476(hl, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return x


def func_bb7e576bce144585a7a54820a2592ee8(hl, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return d


def func_ecaf513c3f194833a9f513e9c7eff987(hl, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return i


def func_4b20300a77704e7e855662a053b18396(hl, w, i):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return x


def func_dd0d8f609f12466bbc8d5c3eb416004b(hl, w, i):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return a


def func_82c2b2962f1e4a01a093d724d1d8d7b0(hl, w, i):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return y


def func_226a9a78bce3480c8d9ddd6ea40771a3(hl, w, i):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return h


def func_16e6d3766c514f2b9926b5ce7319d9e9(g, w, i, h):
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return d


def func_32e80ca7467f44f4aaa95562f8de5c6d(g, w, i, h):
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return a


def func_7265964539a944a2b9b8d21765412861(g, a):
    d = a / g
    r = []
    return r


def func_c89504b3ee324d7d901adbf0aa7af66d(g, a):
    d = a / g
    r = []
    return d


def func_2ec88bc116bd40fa92d6daea01b9d1bc():
    r = []
    i = 0
    return r


def func_5f3dcd25ee8941f9af9a5f0a5a6bfd42():
    r = []
    i = 0
    return i


def func_7bb79099e1cd470ba6f4e9e30f59a40f():
    i = 0
    c = 0
    return c


def func_16c48a2fb24e405196f8c394eea840e3():
    i = 0
    c = 0
    return i


def func_dea27ae62828436981b0db132ecb8011(g, r, w, h, d):
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return rr


def func_9a95d54efd9c4fb1ac83e47813a959a0(g, r, w, h, d):
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ll


def func_3e761513713a4b6eb54c1e3318ecb564(g, r, w, h, d):
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return eps


def func_2ea6e7d076d742cf87b35452485c386d(g, r, w, h, d):
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ap


def func_9723fac5c3db4d33bf7171e5cdca1952(g, r, w, h, d):
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return m


def func_0b3c41f4105947ee9d8cae9bf9b65367(g, r, w, h, d):
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return i


def func_521716ce7c084e379ce460e8f691a5c5(g, r, w, h, d):
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return c


def func_8c34a3e8ca4843aa895068a0552958cc(g, r, w, h, d):
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return hh


def func_0b834a1282644a458042c13f6e7d4fd4(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    return U


def func_d4f1afeba1d64d908c7e124ef91c03a5(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    return u


def func_285a62330a144402bd5737ddfb4a5619(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    return g


def func_9245b1bcf2bf42ffa09ee81ba050d2ee(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    return L


def func_ac0ed28fd0324f31955a949b00590d12(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    return w


def func_90f73a1b231c40b8ab32151d9c0257fa(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    return l


def func_999c636471324925bd6ddee4e1b05e7b(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    return i


def func_597e16f354314e0eaf616c94b5d1d241(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    return w


def func_f9370205284b4b3587c7537751ae95e6(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    return i


def func_1a775dc286884ee59f2773b6b1c8e8fa(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    return L


def func_56c8fe6f53874dae8509cfa512c9c27f(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    return U


def func_06eb3a542cbb4bfd935fab25ddf3bd83(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    return h


def func_315fa2298af54173bd49593b585e39e8(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    return U


def func_8f01acb7f3904185a17529c8bedba7b1(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    return i


def func_7f27faeed89c4a83bf6b206f62ed7dc7(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    return w


def func_be2ecd3d663b45099afe420b992b0c54():
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    return hl


def func_bef264dd10de420a8ae0f775bac3cdb1():
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    return h


def func_7f2f7000d88e4cb0900e0f60dabe956f():
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    return w


def func_c6d9f64c04d24767b9ddb3107b703fab(w, l, L):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return h


def func_3958bcfdcc2f4659a6853a496a1ec1cb(w, l, L):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return d


def func_1b101c82acb64363955e905e4f135301(w, l, L):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return x


def func_9151b59773f64e6f9d0ba1b26ec66fb8(w, l, L):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return dx


def func_b63a09ed2fa64fcbbb93c1f9ec1cbb3e(w, l, L):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return i


def func_190d2e3357f949458033374c04030c8e(w, l, L):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return hl


def func_cfe25c703ff24bb1a379f4280e2ecf3a(u, w, h, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return x


def func_376aa6807d904e5eb5f0f3b64b12e850(u, w, h, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return hl


def func_86378239cfd54f04bb1850e7dddb13e7(u, w, h, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return l


def func_a37a1a9a145842fd923180ab2895ffd0(u, w, h, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return d


def func_caf6f21472c446ce883ffc2bc154fb7c(u, w, h, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return L


def func_af5e5a9be3654a57a11c5ea49e91966d(u, w, h, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return i


def func_0e64207fff854a27819c41a9dbe250b0(u, w, h, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return dx


def func_512883f1089a4f43bc65ba2f62515e94(hl, u, h, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return L


def func_18484a16c431490ea501d1e4b47a787c(hl, u, h, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return i


def func_14ad3109bd9346fc955f608136103cfa(hl, u, h, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return x


def func_ac345c6075fb45f3b99118ef60c87615(hl, u, h, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return d


def func_ab2ebf2a9dac41739b93ff6202b90728(hl, u, h, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return dx


def func_292df703be1b41e1a5b1081e3e299461(hl, u, h, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return l


def func_0c4d68e680ee4e1188618b6bb6ec7512(hl, u, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return L


def func_4611da1f1ccf41008f2514a3cb86cb44(hl, u, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return x


def func_a5260a95a88e417d88a87c460bcef750(hl, u, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return h


def func_3761dc2f5f7e4f89abc431f55771b387(hl, u, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return dx


def func_e629c5b4137b4b41ba2e0c051beca779(hl, u, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return l


def func_f7984a059ab247f4bc04b812b70dbf63(hl, u, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return d


def func_2bbf7cf4a9fc4e6c87c18ca38f45935b(hl, u, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return i


def func_3a7e5892f0174d74967564b3ebe03535(hl, u, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return y


def func_9681d62c1cbe477db39bff99a65ef86c(hl, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return dx


def func_2504b9c5e06e430dad8e5dbeae0d5ea2(hl, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return d


def func_85b28ee6860443e88a74aad13c1e98d5(hl, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return a


def func_a0853dd3155f40ce9d9d365b67a96c8a(hl, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return x


def func_500dbd75b45d4a61939931941997e94f(hl, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return y


def func_6af7c38ddead49e6b0277a24bf4ef5ba(hl, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return i


def func_d1f01196f6154c31a92e5132a804d9b2(hl, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return h


def func_071a4cbe9b4e45a6af872ebaec32358f(hl, g, w, i):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return y


def func_875b1a0ca2a0498f8ad7c757d89d2776(hl, g, w, i):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return d


def func_334fd066bc684e47b48cc8a1ed4c4300(hl, g, w, i):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return x


def func_517c710a61a5410fa4b8ab354ec0bc72(hl, g, w, i):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return h


def func_ce898d1f26574684861e25e1dc242fef(hl, g, w, i):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return a


def func_190bb224a2d44587ae171cac573d33ed(g, w, i, h):
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return a


def func_b2ea3183b1d64679bc4f8ff61f045cb8(g, w, i, h):
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return r


def func_693c51c3bc3748acbdc367a44e9d1bbb(g, w, i, h):
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return d


def func_2817b92a42b7482eb5d4cc9233287e83(g, a):
    d = a / g
    r = []
    i = 0
    return i


def func_8c161db15e5846dea4ea0cc0dcbadaff(g, a):
    d = a / g
    r = []
    i = 0
    return d


def func_25a24c2127564b50a90715b87f12a3c0(g, a):
    d = a / g
    r = []
    i = 0
    return r


def func_54dd81cd0c294bff8df7f0fac2fcebb6():
    r = []
    i = 0
    c = 0
    return r


def func_8fe63e66ef114b6fb5d3fe1a67c9394a():
    r = []
    i = 0
    c = 0
    return i


def func_dabe6aad44494a7299e207f759503b56():
    r = []
    i = 0
    c = 0
    return c


def func_665acf691c2742768eb955b851433d0a(g, r, w, h, d):
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return rr


def func_cbadf3adb7be4aa6b274aee1c682e6bc(g, r, w, h, d):
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return hh


def func_b2c0a5e4d8c944eaad10c2e5da78bc89(g, r, w, h, d):
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return c


def func_a080ff1ed50144b3af06abc6c0c3b735(g, r, w, h, d):
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ap


def func_a8cdd2c428c44d91b663c7a8ce5849ea(g, r, w, h, d):
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return eps


def func_b0cf9d68832b4453afdeda2aa843daf5(g, r, w, h, d):
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ll


def func_5eccb0b52c0244418c3bf7c96fdf1120(g, r, w, h, d):
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return m


def func_7a0b60e93d7047a5b4e7a0f4dcce9ac7(g, r, w, h, d):
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return i


def func_45519a6eea654240b7e14cac073c8ade(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    return i


def func_dd0ea69a4ff24e91ab21b81495a5149f(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    return g


def func_595c413267b04c39822295cc839eb7ee(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    return U


def func_3195350140554abaae71e9414ca83975(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    return w


def func_4cf7b88e6ed947e0afd98501ad2c3150(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    return l


def func_052bb02ce7b94c088922a3bff5dccb76(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    return u


def func_04e6ce142d0744a7ad528eb2d6c08b27(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    return L


def func_1a71c56c26884bb8ae62b770ca4fd701(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    return w


def func_4e32d408ec504573bc36c97ececfdb29(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    return U


def func_ef3a823118384f1a94eaaad20ceb196e(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    return h


def func_e0d09671fbee4d04a8db9fe7f11f849d(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    return L


def func_8539238c65344ed084953295d19813e7(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    return i


def func_fc3df215d4a84fdf9cc6fd0ea753ddfc(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    return w


def func_af0406b9728f4c87a052049c8d3e3b3a(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    return h


def func_2556228f7b2f496ba818ec7ae58f0d75(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    return i


def func_c02206c60bfe40cabe649527b7a27b8b(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    return hl


def func_a9beb313efba482fb7850166501bf255(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    return U


def func_7b8007c428c140a2a01190471a277eb8(l, L):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return h


def func_ba6efe9c55eb4e1f8a9dd4bd532b8432(l, L):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return w


def func_8f3c11577838473f8656e2b208298885(l, L):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return d


def func_089ea9f0d5754821b2f5bf4dcd5a43b7(l, L):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return dx


def func_647e5626d1cf4717b013dfdb80bbb5cc(l, L):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return x


def func_6556e35345d04c7ead531d915b337d15(l, L):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return i


def func_ea62601e95744e9190d45d377757fcad(l, L):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return hl


def func_ab2e3abf13a8464992f918cf1fefa013(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return dx


def func_7f4a0face56b48e29b1235da2be5b62a(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return d


def func_d4897fd3949b44038948ee4ebef98db7(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return i


def func_442785e644c0462d86e22515b2242285(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return L


def func_9c67e55b086547c594ebfd11ae481bc4(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return x


def func_a2e4bc80db454ae8b25b0f0db0305cd1(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return l


def func_f1eb1a966cae47e48d36251f156f4f4b(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return hl


def func_9e4de2079805434fb11c31c91b749e1b(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return h


def func_b53b8feb3c074bd3b61422fb93fa4da0(u, w, h, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return i


def func_dc92ac16a050420b9f2c488f4a5cc8be(u, w, h, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return x


def func_708ab2fa6ecd45559a2dfb4af3270d7a(u, w, h, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return d


def func_92e8f30a6f574dbebef3b780473f7981(u, w, h, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return L


def func_3b55aa61ec874424b5d28d509276684f(u, w, h, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return l


def func_15eec5c3655246bf8bbdf546db195bfe(u, w, h, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return hl


def func_e917f81dc21d4d4cae512f96450492d4(u, w, h, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return dx


def func_6ae6087642804e7caa07b15b327267a3(hl, u, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return i


def func_2340f74bca2c4aaa9e214558b1c88aa1(hl, u, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return d


def func_8743ec51dada4747a06a87692febb5ba(hl, u, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return dx


def func_f44ca377bf224ad4b00e97038440940a(hl, u, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return h


def func_52558a7d5ff1461582f1ab74c8c3e78d(hl, u, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return L


def func_7c0f91c36b0f4f4d99469d21b09950c6(hl, u, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return l


def func_2a44fe9fe87344299d71b9d4adf036e6(hl, u, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return x


def func_131e56bc231443fb87f1b92e5b61d680(hl, u, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return y


def func_3dc3bb8c482248b39ff6a5aa9c22981d(hl, u, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return y


def func_9cbe772007f94aa18b77f1d43f25c2b6(hl, u, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return a


def func_7b0a8ab75d584c53b98f3dbc72d74311(hl, u, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return L


def func_e60fa76890d04a77b6b7c2ec3f06ea80(hl, u, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return dx


def func_8bc2be5774d646caa649465b5f9d292c(hl, u, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return h


def func_701c1e49bb8444b9a7c978ab7fbb617e(hl, u, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return d


def func_deeb5c64aae64881b7002c3682fad519(hl, u, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return i


def func_fee2a8bfaff741b1a1c02833d9b2ddd5(hl, u, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return l


def func_38e8915daa6a452098179c1fec4cdb45(hl, u, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return x


def func_f85118f0ba5c40bd89d9f7c15cfb3445(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return dx


def func_9fd5410f166245a2afa3f1608f32d994(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return d


def func_e134bb1317864ea0921534af364e4393(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return h


def func_55e3610bc9cf4910bc71c96e73e454bf(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return x


def func_3ac92fb05d1343f899c1ea88aef22270(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return a


def func_3470d7713616406d806db9520fa26757(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return y


def func_fc6bd91dee0c4a79b59b8762caa7f38b(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return i


def func_e92cb16a9672489882e2e20b613a4dae(hl, g, w, i):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return h


def func_05cd3b9660a34e1db27823b68df0ebdb(hl, g, w, i):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return r


def func_c0f7c92cd8774589b6368ed310f711ac(hl, g, w, i):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return d


def func_54bcf662ace9464d8efcced3ed85ccaa(hl, g, w, i):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return x


def func_0b83862473a84790aac500fcfadab23c(hl, g, w, i):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return y


def func_3bf724d4c030492a9a08c2f7beea2b4c(hl, g, w, i):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return a


def func_9cb7ebef12f34233a6dbe7fc2a140239(g, w, h):
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return a


def func_63ca31bd2614401e9f4b287b9f53debd(g, w, h):
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return d


def func_e4784b9a173d4999a863b96a1d480ee0(g, w, h):
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return r


def func_b49af43882de4ccba54d63968df78989(g, w, h):
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return i


def func_eb6eede4695145dbb5bae9e3d868d85c(g, a):
    d = a / g
    r = []
    i = 0
    c = 0
    return d


def func_d1170006704b4729a3201a0326150894(g, a):
    d = a / g
    r = []
    i = 0
    c = 0
    return c


def func_8fe96ab90e4943c39e2dcd09a1309e66(g, a):
    d = a / g
    r = []
    i = 0
    c = 0
    return i


def func_74ded0ef0ec24730ba5a3bcf9408b4a8(g, a):
    d = a / g
    r = []
    i = 0
    c = 0
    return r


def func_3aa6d5953f1f47309a715cd856655b36(g, w, h, d):
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ap


def func_04214e3865064b729fb4dd2ae26a5f44(g, w, h, d):
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return c


def func_2372c015fddb41b09eb37c866b83ea48(g, w, h, d):
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return rr


def func_8aeb0250c74242088c065e11bf02180c(g, w, h, d):
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return eps


def func_97e1364c2905405db99c61505a569ba5(g, w, h, d):
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return i


def func_1fb8b113b24749e099147c632ed6f0a2(g, w, h, d):
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return r


def func_b5a16bcfbb58486dae44297632d5651d(g, w, h, d):
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ll


def func_a8cb841de9ee401aa0cf2f0d5e52164c(g, w, h, d):
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return hh


def func_9d6af063653642a8900b4eee6b670026(g, w, h, d):
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return m


def func_b0d17ec65e884425adf6352840cec334(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    return l


def func_05e9f4332b08497192b9b7ca628e8b03(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    return h


def func_b0fb012215904fb8b59b0f1a860b55fa(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    return g


def func_63fc5e8fbc1f4c92a4213440c037cd6f(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    return U


def func_f0d80136766f4f7480eeda3eb3cc8e6b(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    return u


def func_2a29c82ab6ed4df6bc594f974ce325c4(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    return L


def func_d69620c01b554ea588e6e43e815f6697(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    return i


def func_17427630678f44a282e979e436912db2(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    return w


def func_622cacb11ba5448ebcadd903ed15edda(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    return i


def func_533c78b5d05549669286c3d0921924a3(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    return L


def func_44728330b1c5474a93c80caac9972060(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    return w


def func_062134712c52426683125021394f81d9(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    return h


def func_c258b76fe9ef4b5aa38a23fec802172c(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    return U


def func_6ed22c369eb44e04bd1b17b9d6b0ad15(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    return hl


def func_542d1a09d4ac4b4185180d524dbe93e6(u, l, infile, L):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return w


def func_5ca378d8b0964e0ca93c072d6f100da8(u, l, infile, L):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return hl


def func_d362a3d324944e398953fe41ac9bf387(u, l, infile, L):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return U


def func_aa7d18ddfb5f49faabe1300aae8934dc(u, l, infile, L):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return d


def func_c8149f083f9841caae705f1780518ff4(u, l, infile, L):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return h


def func_10c464b1f28f490fa34011d2ec35269b(u, l, infile, L):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return x


def func_e3b74494d6e24dd2819a1f38118eff24(u, l, infile, L):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return dx


def func_9d7f96238ff1493d860266fa83d73647(u, l, infile, L):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return i


def func_3bb8c91921734faab3a1b48e5412f211(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return i


def func_0edd7c7965014d75bb0206b0a79b2b35(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return L


def func_9ab0988f4bb64a38b4ee567d3a3eaa19(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return l


def func_be907b443c2b40598fcbd991f393f21a(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return w


def func_13da3de6999e47239ef9dd0eff531425(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return h


def func_cf7a0a6618bf42d5a006d0f79a06fe8e(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return dx


def func_dcbf63f11079481780fc7a371141d7b7(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return hl


def func_68a0b95c608b49e28ba453d07b63fd1f(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return x


def func_28621f40fda6470a99d31045f85472b2(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return d


def func_26e46ed782584804bb98559a4b02274c(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return d


def func_e0362b958865433db91581c655e54281(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return dx


def func_b4073dc3fcfe4753a801010ce1a9f71c(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return i


def func_c8c9e677c0d0469cb5371a335fc72bec(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return x


def func_c4ab6498165b4321bb45eba87b3d35df(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return L


def func_de875be2ab9745fd9279450f9268a31a(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return hl


def func_bcb2dd918d594f4d829b4dc8461a8ede(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return h


def func_9b243cf0f70b4f978abb46281b2592fa(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return l


def func_28a1c0e061304b0a8faa4a8fcbcaa68a(u, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return y


def func_0b7b07540f244340aa36444b5331b7fc(u, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return l


def func_005d254bd2b34326938ff9c8012ee0dd(u, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return d


def func_a67ba29c57394338b954d79c8581ef4e(u, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return L


def func_40202cc7435547ea9da6e09face7a9e8(u, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return h


def func_010fa25d56f044c18098db3cb2885823(u, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return i


def func_01f7762b94164a6da5535e475d1072bc(u, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return hl


def func_db9316cf0fe1472db3c879f68562b70e(u, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return x


def func_a7d2a3e1171e4d8696fec8dac3899214(u, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return dx


def func_a3b4a607ee304d79846cf1c2309975d2(hl, u, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return dx


def func_4b3f3541ee3d49a6a647b64d5e1cc195(hl, u, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return l


def func_d6a23a36f66a4dff85187de507d4fa22(hl, u, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return y


def func_6b4f60ac0e8a459595c31c731f1749b5(hl, u, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return d


def func_42df8ba327f34afdafa026b280a3c010(hl, u, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return i


def func_ed0a619c79894e9b873cd492481b8c9b(hl, u, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return x


def func_607bf73097ad4450a32262a344d0174e(hl, u, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return L


def func_5bf2d231fa7140699ee7d2449fd420df(hl, u, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return h


def func_764574e1bee74f4b8a550772b142e7b9(hl, u, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return a


def func_3351d705999f4d0eb93d9c4da8ba3560(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return a


def func_5d043c4bc9694dccbf2399878bb13e32(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return dx


def func_2c3e41ebaf884e59a9895c8d4a6ae10f(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return i


def func_8035d479c4ab4e3cb6eae1777b4f130d(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return h


def func_3b8060827c594b8bb76f1cddbe341020(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return x


def func_6a649ad83d3540d7a4b26c6e6f7f92a5(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return d


def func_2cf39acc55854671b4f65e3ae1528b7b(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return L


def func_8ecc5e66b7c44fd18b79736cd7a85e4b(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return l


def func_dbbff6e805e8445eb0836486a5725506(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return y


def func_4170ff1471cb4bb6a7d1323ec68f5165(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return d


def func_4528e3c88f2d4b3faff71eb2cb78eb9b(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return r


def func_b499b9400ae34f12a0397b21b194bca8(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return i


def func_7f46430c4e4242d7a52f155ee8f5ae24(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return y


def func_218f18820ef946a3a98d25ab99f50877(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return a


def func_1c0b28aee38442df925295d8775f5334(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return dx


def func_4b97a37328234082828a4e3c248fe323(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return h


def func_7dbfd3ae922048c396ed9b410051748b(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return x


def func_f78be10adc91434ca46a4ef4b5e4fc02(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return x


def func_62dc09fb5401485b8a0dfeba60d6ac50(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return y


def func_f279d31ff985449c8cb95ccfa87506e9(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return a


def func_4ab5f8ed25604075aec1959f598b9048(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return d


def func_2ed7bc962353469ba9bbc4a7940133cc(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return h


def func_f6dae0f367984f4f9351bdce9c98e7ff(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return i


def func_af1c5244d309439e94d73761b9eabb5f(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return r


def func_91a433f794774291a5e67b65e6d26df3(g, w, h):
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return d


def func_dfd479ed33ba441087c2513d9176dcab(g, w, h):
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return i


def func_a2dfdd6769b64a32bca6d215559df14a(g, w, h):
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return r


def func_320db419cb194d989d08541f84dd7b4b(g, w, h):
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return c


def func_e431ecd16a704035b7fa120bc5676535(g, w, h):
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return a


def func_0fe1a08d5c3f4d028578ca5133f72c60(g, a, w, h):
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return hh


def func_f28a47e6eba54570b8598a2f2802f842(g, a, w, h):
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ap


def func_d024ab12fe734cb891a413725bfe834b(g, a, w, h):
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ll


def func_9aaff95799bc4ffa90617a8d5633fae1(g, a, w, h):
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return rr


def func_207e56bfd98d46519a16b9bfc7717679(g, a, w, h):
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return i


def func_e890c4347718435b924d1c729a86a844(g, a, w, h):
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return r


def func_6b8cbafa206e4f70a9fb205cfb3bc0bb(g, a, w, h):
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return d


def func_15594ca359834b079fff66be7fea3c50(g, a, w, h):
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return m


def func_77d67a3218bd496dabcda0be7dabba26(g, a, w, h):
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return eps


def func_9e39f093eba84c03bd528b38caba8e50(g, a, w, h):
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return c


def func_c7f2cdeda8664d86a054d3bae646ee0a(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    return w


def func_225c72866e2745869485ee2448e00f8a(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    return u


def func_e5317200f8a34c26a5de50d091248ecf(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    return g


def func_4cecc3e3730a4318b2a8c1e819e68ccf(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    return L


def func_55daf7310a53450fb79922bcd79cbacf(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    return l


def func_5c65385da0a94f36b6a74a713aa62224(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    return hl


def func_63001b6072bd4efcac1e1e77c8b5d954(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    return U


def func_05924202bf9b4ebb93580aa468ece31f(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    return i


def func_c714349d482f4eb6ab56bf55cb301b3a(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    return h


def func_675532033aea4bb486ab390a9f4f44c5(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return hl


def func_7f27d9c2f5164a3ca2baac180a0074a8(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return d


def func_9a15dedd99c746f9b000e597f4dd2394(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return U


def func_11226e1e015441c5aac033ee1c4d0160(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return h


def func_4c9302573942487da9d6d167e63a46fc(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return L


def func_68d62ea30ffd411cbf6f01201504a1dc(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return x


def func_bb64db1c06794b0c9ecaaf9d40671a3d(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return dx


def func_7876898950e140b393652bda446cfea7(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return w


def func_092894127eb34865895895042778170d(u, l, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return i


def func_41aee303aa6840b196a065367d8f8eb0(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return dx


def func_5d2ed9c20c5646cf8cfc9cd6905602c1(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return hl


def func_b8ccd5d98e284db1b0fe90e744cd99e9(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return U


def func_7717ef15befa4f79806f80927a205bb6(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return w


def func_a9f7c12f6c624daab34230c676294a0b(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return l


def func_5d0d3f5a3ea9444fbed287a0f58dc544(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return i


def func_16cfa09d394a419f923333b1802395b6(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return d


def func_6ae92191fae640bb83446ac0042a3ab6(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return h


def func_f9b0e3f7bc644853a72778cf145f6a1b(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return x


def func_e4a27a7d24244d21a0dbbdb7bd34abc8(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return L


def func_3092a7d9bd264f9fa7a8462b31b328a5(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return h


def func_0c21a5561c4346539a02442acab7093b(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return L


def func_e331d99a20f745ad84a98417291f3804(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return w


def func_54f8dba259394920ae6c06909dfe6603(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return hl


def func_d6d87cf093c84ea8b1239a6feae6a1fc(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return x


def func_b6e0bb8be2bc4c3daa476750cc118d00(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return l


def func_f3b04191248f48cc9927456482b4156d(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return dx


def func_80507bbe20f5459aa94f635fe8144e13(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return i


def func_23572533d75a4ce881d6effc84684be3(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return d


def func_493c8b8e17f240bdb73240d4031ccca6(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return dx


def func_b121b42cbf694d00b4c69d8511122650(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return i


def func_6e7d3fb333254d9f8b328d6ea171a788(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return h


def func_da7fe78e67fd418d87779d33c21dde2d(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return l


def func_2f8d23e835304be2825d1db7e614e29d(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return d


def func_0b8adc5a25864d439f94378c4abb6a8a(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return y


def func_8820c411838945ebbc53e0ba96296163(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return L


def func_bfe5f83101b548f898586911080f61e0(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return x


def func_a3398002e8514f0e84293a76c31847f9(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return hl


def func_ae0b63227ce44811adac1bdb62c501b9(u, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return hl


def func_2ff21a848c444d848f53da6526aba12b(u, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return h


def func_94c2dd982f3e43e8b833e20ee3c66d49(u, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return a


def func_f0f1b453aec8488a8f2feb10fb702f2e(u, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return y


def func_e25c4c55da594b22a6c4ce390cab0728(u, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return L


def func_455fbd3d0f974658b89d94925e38f970(u, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return x


def func_55882a475c7041608d8e781f60c0d7bd(u, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return i


def func_113318699f3b47a6804da1ca0d7e3a23(u, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return l


def func_666c620f2c5c4b7fb5e36a3c8b01f49b(u, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return dx


def func_269106d5130944f59ea5cfd6003ed1bc(u, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return d


def func_2a99ea65447b4f63b6c645e3e571bbd9(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return h


def func_e383e2f4550747bd8faca9e7c1ed6843(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return y


def func_e483473afcdf4acf999118a5afcf458b(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return i


def func_7fa7fa5d8839479c835b97cb93d68814(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return a


def func_184ed635e4084395a8d9c2da2a9b7ac4(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return dx


def func_b56b414aa1024b708bc706ce15d96d17(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return x


def func_1f7e503ead3f430b8827fe850c53c906(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return L


def func_86bb4ecbb9fc4687baa1117a93c2d2b6(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return l


def func_4499559082bf43d18b9fab53a52d62f8(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return d


def func_569b23b941ef415098c39205e1edd1a1(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return d


def func_ba3e2b9cb0414964b3267ad15d32bdb6(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return h


def func_99978d5bda6840d095662f40cf054ce4(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return y


def func_0b97ad1c3c8f4783b6cef1ff479ff41a(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return l


def func_b0682bf742a846469e7d726f5a37c5b3(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return L


def func_08fb11f859694ceeaa951499031c265f(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return x


def func_de48560f809c444396e72f633efca580(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return r


def func_33ab8dc9d1fb48e48dc303c284a65552(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return dx


def func_08d83dcb9860472db6141d3f2c0acc62(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return i


def func_883cdaf54a0d4a3f97973b04d2b7c3a6(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return a


def func_584a39a4b5144c52bb581b217dfdcb1a(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return r


def func_73d6dbb5ffaa4d71967ed04ced44e987(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return d


def func_90aa5e72c4824458a8f6be30bfcfb67a(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return h


def func_4f15651437194ba994803d4e5b9932c5(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return y


def func_a3ad322aaa4449e3ab714f821d3a2502(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return a


def func_5e8145be0dd34e8abbf740760bc2d843(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return i


def func_4144882611e1492baae1ababa695403e(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return x


def func_e7f1155c0ef546e18c641b9b1d24a8e8(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return dx


def func_41cb5c5edda74b5682323646d96be2b8(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return h


def func_443d867a39c745dda058f000f875a06b(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return c


def func_7b43a680dd8f441da9155bbf808d228c(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return a


def func_90553fd1ba114bc180c1842b90b22aa4(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return r


def func_313f0672394d4d069564eff19e0d8742(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return d


def func_d11ee4b823c94c27b7744c9b726c24cc(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return i


def func_8d3fb5a2e2684c379fe7be4ac3bfdad7(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return y


def func_ad242af608e341bf8fa585367235b71e(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return x


def func_5686498ee59c4e6b9f0fc6ab55bf1f59(g, w, h):
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return hh


def func_3d0dffea61f447019ba3e74ebfd245e3(g, w, h):
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return c


def func_b0b3e9c6035f42df9f2d67567e3ce8fe(g, w, h):
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return m


def func_52797012272b409da06f8a28ba22ad79(g, w, h):
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return eps


def func_c225b259c95c4ef7a574b2336f0a208c(g, w, h):
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return rr


def func_bd7634e25f8d418d8cfc5ad366c27d9e(g, w, h):
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return r


def func_56223b1fd0ce4928b2681c8a012ee819(g, w, h):
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return a


def func_6ccd8529bacb407fa69abd6e4418d8b7(g, w, h):
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ll


def func_17d4e6ad0ef549959c7ae223e8aeecc5(g, w, h):
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return d


def func_74fc1043a78449cbab38bfad0d260662(g, w, h):
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return i


def func_d03a457922724bca83d247b8204fe2c9(g, w, h):
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ap


def func_f36573b9971e4b9a8af9235911399569(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return w


def func_e4b8e964f11e41c7a008d0871413d72a(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return dx


def func_f87fcbc18578445ba8c06348ae4297d3(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return hl


def func_4a6df8ceb6324cd89d8944716001fd54(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return u


def func_eb81c1dd7e8547c5a957a566db9352b2(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return L


def func_b890f942ff5144739a73e29dd44510e5(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return g


def func_db11d561f1a94ce4a783826a2c1d73ea(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return i


def func_7c2755a4f4e84969902bd107dc8c66de(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return x


def func_de8d2ff0f3ed4be6b06fe710ebb59c50(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return l


def func_4d453ad832fe4ffdb26f6282034d8097(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return h


def func_463ab5ac9aa74920a1c683887bf93f65(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return U


def func_e95c229b55644009a658faccc81b3855(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return d


def func_83968d4b392b47c1b636e1c122ae4512(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return d


def func_8e02d7bf92e94efb932947b5b0700c80(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return l


def func_155856c541b8447ebd6d907710bb520d(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return x


def func_dd21584038de4984af3ba552d92348d5(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return w


def func_118b939ee6044fe9a0e4cd2828dca4dc(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return dx


def func_6ff4ced569f34b78872d5a2253fd8a40(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return L


def func_a020549d12d5479f974fc22af5d4b93f(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return i


def func_176bf2c4ea344ed0b5ea2aa4b2724012(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return U


def func_ccc117dc296244bda602fe35a9c4bd2f(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return hl


def func_c59b3d84a58243ad9116ba8731c784c2(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return h


def func_78ed7da671e5437dbe459a702af26c2d(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return i


def func_ebfc7ccc6fe4490090a05fdc23016ec0(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return w


def func_2695f66c6a6e4ad9a22b9243b82df2e7(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return l


def func_38e21d2c00e748178a573bb059880046(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return U


def func_2ae249bdacac4b3ab16d53b542f82286(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return dx


def func_1e910a63c1eb41a3bdad66234da4bcf8(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return h


def func_250fcd9b755c4c8f97ed01c5ba767043(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return L


def func_dc9f0683a57e469dad66aa88710eab18(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return d


def func_4f35b4e451d3436e828316eb005bd1a9(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return hl


def func_35515bb240874c738f493c4851dd99e0(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return x


def func_b7ad7161587e45c0846268b60c77038f(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return w


def func_df84d2135a724891a83893927303e500(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return dx


def func_ded0d276345a4fcfaa4bb160b1680f02(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return i


def func_382b1a27340f444daea2fe8c8ffbd6b9(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return x


def func_46c2e68355a4454da58ae0e8fc91d9f1(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return L


def func_e8456a621f9f4496902994ef1b634edf(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return l


def func_9b56960335854dfb93ca66cc2de2026c(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return y


def func_a84553d4be6842d5a61637827aad7580(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return d


def func_40c69da22e544bc8be7757740e506efd(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return hl


def func_d51624d2c3fb40458aab564816268761(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return h


def func_b7ee8010c4fd49f3981b7df5aee3f6cd(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return a


def func_8113b187d4f84748ab2ccb0980dd876b(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return L


def func_db75f194d6a94f3296f5e5d2bc5303fc(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return x


def func_a3590dd7d310453a8d8a4290529c7739(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return hl


def func_0296a608afb84b26a0368729f851481a(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return h


def func_725c994308eb4118ad7d3bbb59267119(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return dx


def func_a782898d7af143129896412e49a1ec2a(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return y


def func_b9d12549bead41a1bbc5d2f4200355f2(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return l


def func_710dacd9a1dd4e54b50af68540fb4814(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return i


def func_144c4908e9ed40f4b4a11b6e2e541306(u, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return d


def func_4568e7d4a6df4440a22c17cd6058a453(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return h


def func_6b3cce3821834a9ca5448ce5311a6f54(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return a


def func_12973b822a414cf7868d3c7b6dd94cab(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return x


def func_faa08be2ae744a4d8539994b8974952e(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return d


def func_456ed042b39445108400b8dea332800d(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return l


def func_eb07ce2b617146bbb7e8d20c1ff47a26(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return i


def func_81d1f6e1894744c59e8314119f1d2a38(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return y


def func_6aa8628e53fb45d6b8ec6a387e448eb7(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return L


def func_f673144017774b2cbcae6b0b114036fd(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return hl


def func_811d2f55a1e14c5a931a54e0f42fb95f(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return dx


def func_76909477223f45afbcadf5d41f172c6a(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return d


def func_5d5e489a728e4ea2876cceebd0155a3b(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return y


def func_bdcaed2dca2448f3a3ade3c2efdac262(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return i


def func_60b16cf5ba7d49c7b3e86217c8b6ef60(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return L


def func_9c0d80e5b85045c99c840239e205e9dc(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return h


def func_56cddcc12c29430788151c443e8b3796(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return dx


def func_fa91a5382e6343cf99b095d8e7eafd39(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return x


def func_2f6d821008ee4abca5884f0d8f931c24(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return r


def func_ec95abdc259b41bf9452e6dd66e8ae1d(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return a


def func_ae1d940ec75a4291b55129318165cc10(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return l


def func_c99eb61790cc4238ab0e29e5d79717e8(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return h


def func_69045a8c916c4a01b6fb2fcb0b1f935f(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return a


def func_08e5a052d7084bc0a70458538ab60f78(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return L


def func_1ab8870fd53640b589b6d4ff88eb97d9(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return l


def func_4484f4eec86b4b0cb2e9b1fcc6065122(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return r


def func_985b58a4b5254e38964c58a0fa94d7e0(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return y


def func_e3160e069d0c4e42a34086f2bfbe1217(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return i


def func_b09fe05a2efc4dde801eb36789c5ff31(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return dx


def func_8fede6dafe4140eabb899ef46bd2d526(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return d


def func_c8839f171d264cd192d9f4ef61cb4687(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return x


def func_dc02e401561f4151a775886e088d7dc7(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return i


def func_55a030753f5840379101fd6250929cf9(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return r


def func_9ffac257c8f3430b99406512ffd7663e(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return h


def func_7f7fde4a5ab84c4ab1443b8c1ccf6906(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return d


def func_63e67a703c2b4adc9865c15d457f0893(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return x


def func_31c57008480f4323b7e1d24128709b6b(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return a


def func_375a4b98d5724d9a839c9268136dc24f(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return dx


def func_7bae3b020f024c4fadbd42a603dd4a03(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return y


def func_892b432b00e046e3bdfc5627840ed178(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return c


def func_eecaef4704b7448a9c7e0f20eeab8aa0(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ll


def func_40b4a77640704d268b24f21ad53937f1(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return c


def func_a2b3712a32794e92a467f418617c2a86(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return r


def func_2a1cc1e6bfda468a9dfe6b6cd0f5cc38(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return d


def func_3f3dd4944e2b4cc3bf424e62ceef7630(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return eps


def func_89ef5d7c4d8f4e0d8fc902f80044e0bf(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return rr


def func_82d1cb5e2d034d7096eb1e0aa2f2975c(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return x


def func_e9de481688f9463aa324f390756d7ce0(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return y


def func_61b0f411332e47f6bdcdbf4870ddba7f(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ap


def func_b6aa5612fe5e481491559d3baab29b58(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return i


def func_7ca3e42e59554af1920b898ab9d8b6a9(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return m


def func_f76fbf4dc6af4ff89f46e277cd9f0721(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return a


def func_ac2e0987187f47569afadb4caab7ed4c(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return hh


def func_c3cfff7643f444b2af9aa48fb17ca611(hl, g, w):
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return h


def func_04050a5e4c0a4802a6a89d572feba90d(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return h


def func_f37f2045c5654f3abcd2b8a26f34d499(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return g


def func_17712178b7d2492193da7547d29aecfd(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return U


def func_27945bd3264a42869fbb17ca308d3794(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return u


def func_6969ca1c7c7c4bea9003d323b6f6513d(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return w


def func_2f3b8b7253e2466bbd1c8fb86e1fada3(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return i


def func_f6819ac52b664407b78f7b2f3710e968(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return hl


def func_4f32d66f37734217894c5817a4b04b79(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return x


def func_8dd0ce312b164a7aa791cddda6c3da66(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return dx


def func_976ee484d9c240cba7aa6d3c76f08a16(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return d


def func_2993a9953a1341bf96bfb1a63e047f15(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return l


def func_989b7f2861ec40efa29c40ec4a431612(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    return L


def func_28d0a95f244a426aa4b429252ca3564b(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return hl


def func_29959dc8f46248fd9b4c523b0de83088(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return dx


def func_e039693346374dcbbbb814ff1c4511cc(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return l


def func_7f3c6c283d094fe3ae9cb5e06e16241f(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return w


def func_dbcf13bdf21540dd8863a97824bd5510(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return L


def func_d0a67447e227422ab44d8de022b02092(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return x


def func_cf976cb0cd3d44998c306bdaff63b566(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return i


def func_1b2bc990db4941bf8b351194ac5b3a7b(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return h


def func_52c9d89fb824463884ab8cfafd1c9a22(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return d


def func_b5deb6a0a6af4bd1a4cd68b55e354969(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return U


def func_cd646813a6c642b1ade440024ec52955(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return dx


def func_b2e5fc2044c84bd3a3f741801e46efa3(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return L


def func_c6c752206ec14fb58f980df4526b8676(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return w


def func_2000ed4afa4e4fbe884d39e4fa7647c2(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return y


def func_ea98ddd624984931879ce1fc2b1b76d4(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return U


def func_f58acdfe04ed4406a8b93cda10e24c9e(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return h


def func_ecbd0fc2e5c847aa8b7bdf829237a31f(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return i


def func_bd01868c8f9a490693f1985b97579357(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return hl


def func_ada113ea8e8241739c2b54627eef2723(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return d


def func_33672d64801b495d9df4ac859a7ea10b(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return x


def func_2ba4c5d3a2a84242b2bc6ffcf628f2b9(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return l


def func_56f208803d3549178fa3b96a69da8178(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return a


def func_ba6e10f2c1bd4b91a12ece58d6aa30f7(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return x


def func_67d220bdd00342219c52ee6d8635756d(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return L


def func_40e54c19e3784e15a0a457be2baaf12b(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return hl


def func_ffde6878cab444bcb408b48eacca5c56(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return h


def func_01a2a0e611704130aa1e73716c9c3e38(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return y


def func_7012a0c4c3034db9809e421a5c215e4b(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return l


def func_905cc81040b54f14bb928b64b0b312b3(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return w


def func_7b110e04ec02412fbb6a4d9e011d977c(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return i


def func_888e60990ad14d79b77994ce48150c41(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return dx


def func_041b37e380304582962a706e2c04047e(u, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return d


def func_6743ed0dd3224c7692a776f561bd264d(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return d


def func_e24e6adff8ad4a86af5992b4bf15481b(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return h


def func_2f8fca0292b9482a9aebbbf35b047a90(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return i


def func_342c80b6cbcb49b79934fc0d06260927(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return dx


def func_e70508b7a26e49d8a745f53395299b39(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return y


def func_9a7d75a116b545e4aba39237b79e6476(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return l


def func_ab41bfaa9ee648cc962610521e1b8a44(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return x


def func_7e2fcae81d4947c8b522d0626a785d18(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return L


def func_8ea64cc315754220bb43776b6c54962e(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return hl


def func_e2f09ad93c7146f4864061fc4d1408cb(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return a


def func_29595f2136864b17b932af207af3013b(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return hl


def func_2d49c9e0fcf345358c7de27bf38b1579(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return d


def func_213f6a529c0e4bb2abb26d732dbbdd61(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return l


def func_b906ae34736d47a3a0c02dfd819fd023(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return a


def func_6f0757bef8ef4db6a48adcb2b2629dc9(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return dx


def func_00af821d43094a3dbfcde040a8814e15(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return x


def func_0c86e2ee7d064719973944966e5e9e35(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return L


def func_3ad5df0b3c594de1a1bf6c546d212c36(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return h


def func_93a8868a7dc84c3a8e1e50e687b505d2(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return r


def func_85e6784305ae499da67c6c1d6fa74ec1(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return y


def func_5bbda99ba7da4dd9984d1d879b3fed6f(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return i


def func_4383ea4c42dc437c82974d80bbbbb737(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return d


def func_c4b65e9d549345849ab8fcd407bf2326(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return a


def func_3c7d290777f841e880e5205a898bd3af(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return x


def func_e73ac05a5874419cb6134f4ed67c5451(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return h


def func_3f809616e502485a854cb966e82aa5c6(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return L


def func_02c00c0f308d4324b1c5e9621ade084e(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return i


def func_c02f6bdb4f5a4aa28161469f52019c80(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return dx


def func_8a254d3e6b39493fb5cdd71d83feb71c(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return y


def func_865a425868a74ae6982065dcefb12328(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return r


def func_bda27396f15846ddafb80b9a95848d7d(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return l


def func_4b93e3505e7c49df920303c5550b727d(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return h


def func_5fdedec2bdf44b1592717baec185056a(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return c


def func_39bcab4563a84f809bd10e1b4f9a0a13(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return d


def func_99276551b6b24a46abb15a22e0e34b56(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return y


def func_8f7b1381f4724c66b214d0d31346f439(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return L


def func_a8230736fed84ea1a8df251cae680603(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return i


def func_d67a8b32ea8d4d7a97faacc4d23b3816(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return l


def func_dca98c3a02794541bd17d7b78505c93b(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return r


def func_0a12838e448f4728bbdf6a554224ee7b(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return a


def func_358ea5ac99a041118891539d4cbe25aa(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return dx


def func_c23c8208576c436bbf391f81c1279f83(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return x


def func_f322d8ebc9644da3931f3273efa45c74(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return a


def func_a7974f8efd28409a8e5ebdcfce71e309(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return m


def func_ed17ac0bfb7244ab93ef6aa93cd19b16(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return r


def func_b8497fdba8b14645b54012fab8753b4c(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return h


def func_2c48b64359d747b383f61ab5ed630480(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return y


def func_090fa844977b48cd87d16112357e2ebb(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ap


def func_1a44daa6e5b34edf85a23140fedd7a8d(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return d


def func_4a3bd0c380244f97ab6ed26d627908fa(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return i


def func_490c03398b5c4ecd96cbb9d9dd0b6851(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return rr


def func_a99ac7d3959b4b6c8f50542cc8730ee1(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return dx


def func_da022643410f4abe839cbf59fa682fc7(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return hh


def func_842ff640f2f14c77b57777aa7eb2993c(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return eps


def func_1fbc667163604a3298cd48172d29032c(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ll


def func_0da3e4d182154f38b5d1176aae5afdc6(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return c


def func_8cf6c2585baf4a3ba1fe711e6a63df23(hl, g, w, l, L):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return x


def func_57a51d3036784f7f9323cf75e97af3bd(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return hl


def func_4143c308f64c492da3fb29f30f5db423(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return w


def func_056c040a98d44cdfa0aad3d6e326862d(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return L


def func_f0f1fd8cb6b241f8bff5e2c6d5e232d8(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return h


def func_8cab791170d84f45a1ff55ec8de930c7(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return x


def func_5f4927c1514844fe8569a47b83f0b5b7(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return i


def func_9e813a3b424245b3a79448e2853cb45b(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return u


def func_314cd82a537d46adb8988d6a99ef8003(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return l


def func_debfdb57371b4cefa557c055c0759f48(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return U


def func_a3a47dfa02e243c0a39700dc76e76271(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return g


def func_da64bc806fcf4e2885d1e2e90d7b6e61(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return d


def func_f237311019cb4545b5884c659f53c48d(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    return dx


def func_1c39c09728784ff7b70c93acdfeec71f(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return d


def func_837e323c382c425db2f76ea0cdd51cdc(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return L


def func_04ed643904b845a8a0b048c4c7d25be4(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return i


def func_7b98ff5609aa4f3cb12b746fccea4b8f(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return U


def func_4a93cfe597114b8bb1b0a488a3ab1660(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return l


def func_a37c3dfd35de4590b7776214301b6701(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return w


def func_14feb998cd964908a14932cffc4d6ca5(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return h


def func_f29dcf82cd114026a1124c8b378e1877(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return dx


def func_cae8fd0233db490aa875935348e3ed5d(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return hl


def func_304da52653ec4d0aab5258bea6e6d04c(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return y


def func_b8145c49ba224e82ba139f175f81623a(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return x


def func_3380324410374f96a434f2b1dc0c7fe6(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return x


def func_bd419859a07e473b90045a8b21f71927(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return L


def func_6c22d2f96c76491f9b54724449565d45(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return dx


def func_2bf2478063c449f5a8323289ff74f3ec(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return d


def func_150c0a1b64084652a02576e239064f20(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return hl


def func_f53a5f79b14f43a3bf6871372a3132b3(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return l


def func_67e3866853214cf087778b3b5275bba1(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return h


def func_b6bcba0a60c44fe7b4298f217235aaa0(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return w


def func_c66d46f2d9794fcca760a801721a2ff6(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return i


def func_67b5b2fd93924cb5afd5af1264bcc01d(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return a


def func_aa7a1bbbdcaf44a5b5c6c9b8d5e3ee93(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return y


def func_12d67b36081545509b21e224f6e12012(u, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return U


def func_eb5d419701d149c89661844adc647a17(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return L


def func_e276636848894ebd8e7ad97baa6304a1(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return l


def func_4280aa02d86d4dc2ac90b6c7741e4201(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return a


def func_9840fa5cb62c4317923d8f1ccbad77f3(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return h


def func_9778090a7aa94de5b0b06b64f9020ed5(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return hl


def func_f28fb29270fb4cee881d03e0e6c029ab(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return dx


def func_6988e8ec720b4da68de58d095ecd19e7(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return i


def func_c80f6ccff5604ac6aef80d627606f291(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return x


def func_25b849413a2f4a0880c5c0f76080b389(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return w


def func_9cb825f9520448ff83fca2e12cbdf454(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return y


def func_22b9022584514435b9639b892740eb50(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return d


def func_ebf03086401f41f59c57c5a0270a9289(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return l


def func_6d6c89b7d93f4567ac9554b2f8eed98b(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return i


def func_8ce6a04b811346589133a8bb9e4bd02b(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return dx


def func_57ea599e29c242f3a323eca1c2443e52(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return h


def func_732be942a9dd4c00acdec765369035c9(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return d


def func_72ddef2ba18b46ebb96e687baf414769(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return hl


def func_22c2103c064d4a1e95d237fe1400b181(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return a


def func_909aa048bab5495ea7234521046afa64(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return x


def func_cc1adccc3a004f66b935a14a55fbc9aa(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return L


def func_05f2bfed2aef4a94a4ab72b15ba5c502(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return r


def func_04baa86c2a074eb4a8972b45dae7d886(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return y


def func_753c6ce2a6a647908da8a3f4c4295c6b(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return d


def func_d15d70308efc46a6afe92ce15f440633(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return h


def func_0df8b4eeb85e44c2bb1f41c8195aa697(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return r


def func_dc75d40bc0524bf2ab47a35999917ecd(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return dx


def func_66e4a523804e4c4f8ef98b2d16516ff5(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return L


def func_58a79eb9210e4d129acf7ba8fbf0eaa4(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return l


def func_761e0bf2d05548a3950fd1987ad29128(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return hl


def func_d4a5efcedd2f4f188e4e73b27416fff8(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return a


def func_f1c1054f01284157be3e1cf7f72c24ba(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return i


def func_f13c1e9efa6a4435994b04a0868e966f(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return x


def func_450de5cb1d17409a9a461e85b531d827(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return y


def func_02004f9a4bdd48949a2f6f41f72bb38e(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return L


def func_0ed1bbaca464446eb998a007221b4e4a(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return r


def func_94df3fae33d940ab81ee81174de90252(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return dx


def func_0b45bd124fa34f4cb2669d9c4df6e290(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return d


def func_086b6188a2a2492480f5860a2bdb7c08(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return a


def func_25ed9df5a50a46dca4adc7ee73084c04(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return c


def func_e130c043b32542479f148ddbbb3456a5(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return l


def func_c34b25f207584c4397940335ea5de999(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return i


def func_79db161d4adb40298ae4a8a9ebf9917e(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return y


def func_acc80fdb914f432d836f8e79840f967a(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return x


def func_bef2a770dd3c4441b4d8e32c27ae64a9(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return h


def func_f24f9821c4cd4a3b907a95623ab45822(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return a


def func_3f3aceca516f43d7964bf05d8eef8a1d(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return i


def func_68635c3ae1e6443a827624f1633539e5(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return L


def func_0499056a4ca5456884dc344b230eb7b1(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return eps


def func_77e08cd95148488d968a03fdc8608f5c(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return l


def func_91e5a065a18c4411a46a924cf1f36214(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return y


def func_4151d55d11f54cb2bbfe2831b2456b99(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ll


def func_afeb5fd3adbb40498c2ea1f7733b3f7b(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return h


def func_dedec99a88cf43918e136d4301aeb4d5(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return hh


def func_4d61f207c1d3437f9fdd1e9e58776440(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return c


def func_c62aed4613f244e2aa2f25090142a2f3(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ap


def func_a85711c5a87d41318b91dad13157aaaf(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return rr


def func_ec64a60effb9415392dacf186eaf8b36(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return d


def func_e1c8e0d0eb154ddc86f017dc0e197d63(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return x


def func_9179e1a834ae41cb8b01ba904d966dc2(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return dx


def func_5d67fd7cabf742c5853f8ff76277aac2(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return m


def func_7de8ff61242a40ee8e761cf7c8ab7d49(hl, u, g, w, U):
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return r


def func_c2c10bfdd0d840168f27f5827ca51539(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return l


def func_c6df25a738c148c89171e501199c7953(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return x


def func_c38e2a90bad94f0e842b78f5ebe8b05c(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return i


def func_285ef590f5f546c78d047e7845a7cc26(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return dx


def func_61098f4a1cee43ce821c64cd06b00a8e(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return g


def func_1d69e26cf15a451692286fafb502452e(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return U


def func_0116e232485b402ca98bac66c2cbfa07(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return h


def func_5b3c781541674a55b0ece5299882f0d4(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return hl


def func_186b1136b1b942d6b70ebe8f424cc447(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return w


def func_7bde56f56c284538ab32811757bc80d0(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return d


def func_2820f939f88f4a91916074413b9865e8(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return L


def func_de429dfb7ad64231a6d45c50ea31a9a8(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return u


def func_008c92dca87c44349c58d415db1b437b(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    return y


def func_1af7b6ba34d546d19756b64887bac5ba(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return L


def func_058971486cbf44a29ca1aa7c48c1febb(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return h


def func_1f565707e29d44b2a99b2f1041d516b0(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return y


def func_52d0bc7fbd2d4bff83df25865582f867(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return d


def func_c0b03a1bb111450a9875857c408aeed0(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return l


def func_d4be9907f560488ebf57f88a8380e1bc(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return a


def func_ee8a6122b50a446f9bde28d2ffadf55e(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return w


def func_78ee67dafd5a4849ac272e5e3fc14e0c(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return U


def func_502cdbe6740647a9be7b7ae538178e52(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return dx


def func_9d3689db112a4bb787c4176bee63b4da(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return x


def func_61ae90ef7afc4da282bc5d6059ba91e2(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return hl


def func_e4816b4c616e4c4094a4e8bb700387ce(u, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return i


def func_0cf6119c36cf4ba880b8883a52c55910(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return dx


def func_27469d9f269246fbbe4605d6914b595f(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return x


def func_5485e585b41f4d8f86892dac7aed712d(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return a


def func_b2787d08024c40668f13157755dce2b8(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return U


def func_7461b49e66124aefa91fde0fde9eab81(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return l


def func_3ceca2cfc8b9496c9e3035422ce43439(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return i


def func_e98f9d8e624543b6a73656a2f61f7e39(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return d


def func_bb5e0773013246478da5fa4737695f8f(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return hl


def func_43f18766d0d64fd3a60f6bc635150ba3(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return y


def func_d00e02f71a994d3d89264dd3564ed352(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return L


def func_6db5b44efb9840858971effc05c45c04(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return w


def func_b2b30f0282b0444c9cd71868a072cfbf(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return h


def func_f8445fc35de84b229fffa36a6e077487(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return x


def func_497d77badffe4ca4a543432e20e9aee0(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return h


def func_f193638bc27c48d89b4139a51bcda2ba(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return L


def func_2accd54793154da5a90144b414d1b314(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return hl


def func_fad400e62998484e9bf6f0f364db53d4(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return l


def func_507bf10577984715964521a03dde72e4(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return w


def func_962a5e119d6a4b1bb608ad148c1e3f44(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return dx


def func_9b4e5c35862e4d4f9dde01da316c95fc(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return d


def func_a796b8135e6c4ae6aa484954fa1f21b6(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return y


def func_541b23ff766542e78fe437a1ee4bc1d2(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return a


def func_a5f9d27dd5e347bc9538ed3172478950(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return r


def func_7759404a1a1444b7bf5b6f6ea03d7911(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return i


def func_0e2cd06319a9496881e4ce92fac59ddd(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return hl


def func_b780f54ead7b42c0b106e245ae087b8c(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return i


def func_526b04419b94478e9af77f6bdadfff52(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return x


def func_5b10ce747b6c485ea5fda8db607a5c5f(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return L


def func_1f5d80bda1224c1b88248e8430ed33cb(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return l


def func_e47b2ee1edb548a9844555ef418f8e5c(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return h


def func_2c128aa7a5804f4aa5ef1f9c4f89db9c(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return r


def func_9dffe316140f4bb8a22a58ef38726d21(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return d


def func_e8e9c8fbd888491dbc7c8250359d55a0(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return dx


def func_1a9fdaab3b494b69b4535baecc6272fe(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return y


def func_1adf1f79f31b4ec3ba116c4a7c196761(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return a


def func_0e0d6b10645443e5b5b743833e5ce914(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return d


def func_a8d26a91297b488dbeb1e5fc5e1a4b48(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return L


def func_fa92295dab594632bb2e07bc11da0008(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return y


def func_76c4b7af6c6042b1a35fd875c61b1c1c(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return i


def func_db0adc8fba3e4e2282df4bb931e2bec4(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return a


def func_fc352c83f61b4191bcdc5859d912154f(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return r


def func_9215f6d2e098489a870980d55df18b81(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return h


def func_fbfa96c146bb4daba179ac3ff59b1c1d(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return hl


def func_694d8ccc4ebf413ca638115bb5ae5ec3(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return c


def func_978f3ab21a5246689119f2ae99dc4a5f(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return l


def func_a779de89c6b24869bc20012dcdbf1fc5(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return dx


def func_162f610c5cdf42368c416de1a6dee0ff(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return x


def func_a3a276c031ea42fba195e8e11e69c9dc(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return dx


def func_d7de544adcfb45f392d0f01a74b34601(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return hh


def func_af9d6a7e1a334fc1b5c6a23b21824528(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return x


def func_b25af7ada58e421f8e9705c288c607f5(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return c


def func_32c0a79ea804445b85916140c413b201(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return eps


def func_fa08ec6f213946e89184c1a656d81e37(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return i


def func_9be9ad3385a642ab8ffaff4e75e965fc(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ap


def func_82097bb2cc7e4436849f57a33797f8e4(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return r


def func_6a594951caff4f3bba0cd7e9efbccb57(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return d


def func_0068a166def2432b9ecdef0655496a4d(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return l


def func_b8982f7e486243409250eca4cba8f2c8(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return m


def func_0ad4987097ba470285fac31e2bdd21a8(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return L


def func_9dde0829617b46e7a9eab750d0ece9d7(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return a


def func_c29feae4267d4175a45667e4f1b59f08(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return rr


def func_fb42d8cd9a2a4cf0a519277ea11868db(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ll


def func_42fb7ca15b784c319c5e7f2562007442(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return h


def func_808daef8d3ea4640bdb0e914f65009f9(hl, u, g, w, U):
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return y


def func_d303da4b0dc14738a9086004fa2f83f3(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return d


def func_7b4fa993a6dd4bf0bda4976111b8c34c(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return u


def func_836bfdd5a4c64f218803a828ebbbe4b0(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return h


def func_c340a97f1cb2425087bd1d1875457ef4(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return U


def func_d490b5bccd664ac29b14a43b7855e036(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return dx


def func_bf1d3e4200b0498ab814d2a157e0ee18(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return w


def func_f32a295e9f0644daa89c955f8409fffa(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return x


def func_6ee2cc4d394848fcbcba6d828fa5d514(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return y


def func_1ca9b540fa71422aa0403ce85ad5e02a(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return g


def func_db472fdef31747d38104dc3d22ef7362(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return l


def func_209806fd73ea42889d7f73b166f5a6a4(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return hl


def func_51cdec0a869a43998231e8f7a5396714(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return a


def func_d6b220110d7b46ba8e4acb16f2e04122(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return i


def func_6cab1d8d59ca4cc8bca55ce90981ef82(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    return L


def func_c58ac429e66b423bbc49bf24866a74f5(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return y


def func_a8508aa729814bc89dd39389c9cac58e(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return i


def func_351dc8a2e8ee48a5ba2d12c9000463e9(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return w


def func_b45b81590bd449859ea2d52a32dd585f(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return hl


def func_fa326523a1204dce98d6e0ba0feb3a5e(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return l


def func_2cf60d03f3cb4439be97f95b27851f0c(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return h


def func_27bfff61ba924bf5bf011cbdeae261b9(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return d


def func_d94a9a8128ef48898e0ade91066bc715(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return L


def func_b29413faa1a94a67a34b88b12448bbca(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return x


def func_616c819810b14880af0666f2b64a423e(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return U


def func_fae9c21b945046de8f68d91244a959a9(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return a


def func_b0a63f1a45664000810c8b2985aec823(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return dx


def func_b0dc52c889fb4deda0fb72fb8371252d(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return r


def func_0fbad5c9500e40b08d52cea4742e836c(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return l


def func_06429ceef24546838dbc318fddf8ad4c(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return L


def func_451acdd8e28e49759537447df8c31eac(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return i


def func_f7899444cbd84d009711894428ed21ac(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return y


def func_456512f061fe4feebcf9d0acd5c2502d(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return h


def func_bddf979387224a57b6f4a9bc7280e14b(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return U


def func_9fa127ba713d4e53b897d397e9882f04(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return x


def func_1ce118066b864a4c86786f265efd91ab(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return a


def func_5cf5957b67e240769a70944ffdcf08fe(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return w


def func_f7a4d02928d045cf88d65bae2e8f5130(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return hl


def func_259d57a0cf5347afa0797685622e35a7(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return d


def func_04acf5534f814daabd297add426c13ad(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return dx


def func_c896c1d27407417c8ef25dc8f09feab1(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return w


def func_8ce5d3faed4b43afbafaf85c1c039d95(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return h


def func_f45d05be251f4dfaa5552927a7678eb3(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return L


def func_7c8925f9b2404791aade103dd7641f56(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return d


def func_f8711692c2ce46f8962a0dbaf93ed901(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return y


def func_62efc1a7f2e84c30be6b918e752743c6(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return i


def func_2b8dfa6211334ae882a94e85bc8582f7(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return hl


def func_e1f2a41b49d74c49bad41c985d9dff75(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return r


def func_61c1be7c684e475d8b2a4f5653681444(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return x


def func_5708f9d9fc724c8093efa5af6b55b6a9(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return dx


def func_755c9e8832274d11ab0d25ff2e9607ac(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return a


def func_f857d7bfab174c1a953bee589eb2b83a(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return l


def func_7473ac7ebc8a4da1a5a938bf371ae1d4(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return dx


def func_59e3395593b74201bcbd8279c972fd36(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return d


def func_e7953978345a4bfbb65c9b8ed09bf221(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return r


def func_789d7e6868ab4fb59bfff1f798dd0c81(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return L


def func_4db018c16ff241568fe019b13214c23a(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return x


def func_4df89fb621fb411cbb8ad4d600f9d302(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return y


def func_8df5959757f6479d96662bfe9cf60647(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return a


def func_7fdfd493e908490c970aa25f39b5fa0e(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return l


def func_72459ed14f014f05926cb4a749143bfe(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return c


def func_ddac8bf2fe454b96af31cbd88ac00b8a(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return h


def func_fa32fb56639c4215b5e289419c3b1f1d(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return hl


def func_d30261c7024149e888a3e7c541c53079(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return i


def func_31f7e08c5a0b4309abfb7f368f812079(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ll


def func_0ed3dca732574a7b8f90e5764bc52c21(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return hh


def func_943013c9a23b42668a2c3dd09b8f18fa(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return l


def func_e3cd2c0ed21a40feab6f0ea16e8471ac(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return c


def func_c5856418122240e8bdf14f26b9fc67ea(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return d


def func_2a2f2b442afb47ffb10d6b4726817934(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return L


def func_e39b041c86964b0987c8ac90ab39fd14(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return x


def func_aed55669c81b48f3b3ab0047903f1082(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return hl


def func_a89685a4a1f346d69a4e6881fcb2a390(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ap


def func_231667ec89734ebc98998c60eca75adb(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return a


def func_f8e54c3897ae4668a546c08f5cc27b44(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return m


def func_6229bd904ae84b2bbd7d49e72be5d362(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return r


def func_a0f82bda4aae4832a4a4c4575947fa9f(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return dx


def func_b0dd94550d2f49d2bff2fb9778b66fd5(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return eps


def func_f87089a6a8dd403c8dad507069e7e7f7(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return h


def func_3a9863564b494c97b1c4a5f5f63f0eab(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return i


def func_f0c6cd5cf2d44320bd28151f40fe8057(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return y


def func_436adaaf41ec47519a4cf70cc99fb9bd(u, g, w, U):
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return rr


def func_7c79d6d735964b4fb350357d7f724140(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return hl


def func_cf2175f9f2614196957d3cad0966d8a9(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return u


def func_b10f6ed70a6549ce922a5cd69529f288(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return L


def func_4c143d7c6aea491c9136f92a3d5e294c(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return U


def func_8d781e7cb34f428e9c76b54cd80cab2d(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return x


def func_b3c398089e3a4f66b59485c014c4e6ca(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return dx


def func_bb02bb719bb64c36ab30bade608f6e1e(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return l


def func_8198f75579a74e24be04a88cf65ce51f(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return g


def func_cd50e0a6387f4b548a6fd120bef56a25(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return h


def func_0be5a4ba6dbc4a7390cbede0efca643b(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return d


def func_977f9937a6784e588a5051e4a5990171(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return a


def func_0be4b5246aa240589d78bc469df5b442(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return w


def func_e1a183304f094b34abea168994270f7f(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return i


def func_4e95d2954e384c6889d8520a50046afe(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    return y


def func_1891d137bcae4a3f9e9a368350611d8b(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return hl


def func_38ab736c89054b55a28e1eeb28b5daad(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return w


def func_d9e8e3729d474479b7eb22a93490b1a3(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return a


def func_823c44e7697b4175987ae0edf8fb676e(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return h


def func_4c044b2322e64ee093d62d3289a5ae91(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return dx


def func_52d454eeca7a434bbca34f29f0614170(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return U


def func_211a745cc6a143b69ecd58468bdad8d2(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return L


def func_3a37a5f9f653492dbe8f2e28123d3ed0(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return l


def func_154487d660554842b59a424c9cde84ea(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return r


def func_31d42b01241849b4a2b60b2f28528537(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return y


def func_fc872d3d7ab440cb809350e353e67124(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return x


def func_c83aea388544427ab14726580cd09714(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return i


def func_f67b479ae30345a39e61cf749b277614(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return d


def func_ae101b4e5c6546ffb065b49d071518a9(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return d


def func_dd2c2eb7b3d3416097ab1196350d0f79(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return r


def func_b23f368074da4c2784effec0a0f7cabb(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return L


def func_564a70c8573040d1a4d0cbed3da22496(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return w


def func_2d375734f6d742dea3c4f204f99c4048(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return y


def func_7e9d7407ffbe4a3583a4218b4b66e337(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return x


def func_83395fea273f4f94a57ef2e303c70b20(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return dx


def func_a7e102a3c5ad46deab1a1ca9f04530e4(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return l


def func_61a9100014f245f3b8cb33e82a5c1f51(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return h


def func_330cd116f1d14867a43a9ab3663891c3(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return i


def func_650a1fbd59f24ba9b1042fb1a1976766(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return a


def func_9e961abdae1f40f682d7059d9a6dac04(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return hl


def func_0dc45ffd2cf247a28e07644c6603ba98(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return U


def func_82dc3235b2cd4c6ab1096208a59b90f7(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return L


def func_97a8bdab9a2b44d89ae9e7c1061f9087(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return w


def func_68f694e485c54b9cb5e61fcbda902d4d(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return h


def func_f46a5a8028cd4253bd266d5048843081(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return dx


def func_3d454bcb1f8e4210bcbe5054b7c9451d(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return x


def func_1d9b20a3dddc4872a03ef34aa147cc89(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return i


def func_0a458ef122ba4ab5aca37d390ff0ac6b(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return y


def func_ca0b4ad396f0428b8388e4eb1de45c65(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return hl


def func_0ec93cf5b7f7486bbee991280bfde89d(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return c


def func_8f8f58ea9ecb4e8aaa0e7f2b32b84869(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return d


def func_103a1f8c948f450984302ec0bb9fdb69(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return r


def func_392c4b6e2b0c4e24842e73d1daf36cf3(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return a


def func_b5e16face55e48d8bbff5f83c84d974a(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return l


def func_d42409d6cc4646769e6b2f3866e4ca31(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return l


def func_beed24d62d114ca988bda7af01fedefb(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return hl


def func_4b95337c96a344bf84def7422be00b32(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return eps


def func_568442ba7e4747c79f0e853a8f05bae6(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return i


def func_dfadf674aff548c6a556837300854511(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return m


def func_2865d688f7de48cd94397bda336b06fe(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return hh


def func_ca530070feeb41bda67bdb7379bf50bb(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return x


def func_1904a07c0cc0413d95ec2fa3d3f95f33(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return a


def func_2981ce3589cc47d29a6eb8ca9287e5d5(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return dx


def func_efa4aba22bbd4c759797f10854c4ea66(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return rr


def func_d286e344e0d54c6697dc95d3fb2cce48(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return r


def func_79fe72015f9040aba0e9d42aceba1704(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return L


def func_470c9bd9f1e748ff82545bf5e1122af6(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return c


def func_41cb968b785940b889d5d74e2aa684fb(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return h


def func_d3a1c916450b414f9abcbb5ddaed926b(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ap


def func_3184ad0dd8574cb297c9509604c2b1fd(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return d


def func_fc523366f65b4f049dbb093d9b76692c(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return y


def func_c39fef135f364450ac1535f07245047c(u, g, w, U):
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ll


def func_4af53fe6acfb41aab7a9a8e664c8ba28(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return r


def func_307b82f57ba64d038e42948c82e3e26f(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return d


def func_33a7f2513b334fe39b37e882a900efe7(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return g


def func_eff82d9adfc7497b9386296a5fbb38c5(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return y


def func_ba1d194d407a404881ac028f7fedfe67(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return L


def func_0a831f9d31d34387bfee232d4aaa87ab(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return dx


def func_54b433e72e314f41b47741939d040333(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return u


def func_f03c43f1a1a749439fac2ef8d42e24fb(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return U


def func_0d87b7995e47416face93b5f8ccff569(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return a


def func_0d15e1f2432f4816b44224f0d2d9200a(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return i


def func_61df6fc10f7c4beaad1c0c7b05dae41b(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return h


def func_26105fe330c24325944b3939ca2aa0c2(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return l


def func_da54865ebf9a45ae8a868f1867c816c2(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return w


def func_79582a8b5cbc4ef3b22b33067154da1d(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return x


def func_387507169d8541c382c440e9bf9fde75(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    return hl


def func_b5d982de6f9045fe8006dc316afdf12d(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return h


def func_6594912c117f46d3a83d5d69fff13287(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return L


def func_86753abb81c54463a38086e63f728222(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return a


def func_82c139f784394257a5752efcad318937(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return d


def func_284302fb06e044fea923ed817947dfdc(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return i


def func_dce354219f054923b3d8a90c4e271892(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return U


def func_e45c74bb79424857b0b2df4be3789612(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return x


def func_4a6d1778402e4e138e45dc171d45f6f5(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return y


def func_6daf392b8c994b6e873e8c8c58064f92(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return r


def func_4ca6db817cd04640ab6f27ab7ec400d6(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return hl


def func_120d8476cc5643098bfbf4c94c61b848(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return w


def func_72bf9d4896544f889e4fe0ee5b47dfb1(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return dx


def func_fbfaafefdefd44ba9845ac67e0c127f9(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return l


def func_7f730c940f4840b1a63924f3e163e8e2(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return x


def func_3b27a98d5f1b4d0cac4296afabf39e00(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return a


def func_7f9614152138493ca97f29591cc97f05(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return i


def func_7be6a1c6c8c64731a3b177c7c56ccd97(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return L


def func_1eca0aac2a0844a9b829320d825193db(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return hl


def func_0607fcaf83be478581e14847720b3b1a(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return h


def func_271022f57cfc4dafb68b6c97d678b17d(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return dx


def func_1f9911ddad50444fa5d344a635d69e75(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return l


def func_6145e37098df4add963395d9650f65e4(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return y


def func_7542273505804c93b720757e47aec29e(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return r


def func_74cba6060ce349919651a30e12e518c6(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return d


def func_5bbd12d15be640fe9614b3895891df30(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return U


def func_2cfe6969a2dd4444b343257366fe95cb(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return c


def func_2c4765b7222743c98552340e9a606568(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return w


def func_ad03d4f10301412b81b60ca6b70d6d62(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return r


def func_aa4fecd08f7343cb9758d836f4baf029(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return l


def func_7835b2c5573c4f13973c85a9d42a6186(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return i


def func_6a47162dbaa34e2f8f7a088665afe449(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return L


def func_05995a70ca094111a69f615226010eb4(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ap


def func_6b765c6f192a4f7aa3b3028b5227e598(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return eps


def func_55a8fbf2dbe049b18b77e00adc6a1252(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return x


def func_19eca0edc88e4aec8847961434ac23c1(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return w


def func_c8348066abd847e9a59bfa5b36202b48(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return h


def func_b3997b9328324818a5c37ebb1381d648(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return a


def func_e9e2e4bea8b14bed9c4742dc063c8098(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return m


def func_f06180ba36bc4d8aa4582ac60ba0b49a(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return y


def func_13e0a0e8870a41d0b9182550865b4496(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return hl


def func_6118990a93ca4c5796e7fab5d28c26ed(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return rr


def func_d2dbe9f91a0f4a1a97c0f1ea6523023c(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return c


def func_3cd968e33fc2416d8a15f8125073efd8(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ll


def func_c609352988084eac9e12faf6f63f0259(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return hh


def func_ab904bd81976427eb60b4fdc8f0f7cb8(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return dx


def func_c58809f3cb2246a5bac970f98aa48622(u, g, U):
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return d


def func_f540f2a894ed4d7da71f0685baa3b88a(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return i


def func_935f2150979143fca48027b6538c7ab1(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return U


def func_cff097e3c40e419aac86aa80a069e4e7(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return w


def func_efaf4354e2fc403f8312781d460637f9(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return a


def func_88a723e3615442e082fbe64939ccbeb2(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return d


def func_cd7890e380e0455695d51ffc552cb72d(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return h


def func_8b4cc3d68ae444de935e669f98d6e69d(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return g


def func_90e4c54e742a4ec0b71a52e620640857(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return r


def func_0f1eb35e15f343b780a98742cafd5cd8(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return dx


def func_42610e9704854a85b1326bb69e887f04(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return u


def func_98401645a7944d70ab4921c1da0dd07d(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return l


def func_86ec84e17bd54743b0d92ebdccf0c60a(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return hl


def func_5267823b8be7453290f63b4bd452ec03(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return L


def func_28a6fd78ae1c4d0288ecd1578dafe512(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return y


def func_f6d3f9e95db8422ba7c0a74291479128(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    return x


def func_d4903c894af3441c829ae9355933f6ce(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return y


def func_a250659a755649d6b9a079712b033523(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return dx


def func_d2860a5091e24a15af11095ea9867a88(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return a


def func_71eed156db2f47c092873d8297682f2a(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return w


def func_5a8a098797cf4dac96a72cd0482f7c21(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return d


def func_08dcc38193054180aa4d81a086fb7b75(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return h


def func_0b196643336747159eba6b80453f8f21(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return L


def func_b5c539bda6974113833ccac35b4d07c7(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return c


def func_8ba6da82d6ab487798428ded9a92a6bb(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return x


def func_e18d603739fa4735a8041bb7f68bbf7c(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return l


def func_44127cb9d7294ec4b83f3e0e7f7fbe6d(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return U


def func_36ae9211173e463686d2b6373ec2f1b5(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return i


def func_c16bfdac7f5447ff8a5215bf56c9c602(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return hl


def func_9eb02c9a91994cdfbe1f4b9a6264004e(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return r


def func_d2341bc8988e4d65953a04ffccbeaf63(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return r


def func_cf55da74c6d54cc28f5b8e597ef5fc74(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return hh


def func_2d5576186d7c4e4fbf833703a47bf1f1(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return L


def func_823e8d79ecc749fcadffd541f033e9ab(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return l


def func_d29c6eedaeeb49f7b34c3d9b7d78626d(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return eps


def func_daaeb9e89987455cb2f26025b9286a6e(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return m


def func_aa33b2f63e0c451aa2b7920bca29d088(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ap


def func_29f5ffda45004863a7fc53c4ebab908f(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return dx


def func_9084e161fd624c698f7194f9efa28019(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return a


def func_05c266c6df52425893c2d372d138d3b5(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return y


def func_61722f067f294b0bb5e519e750608909(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return hl


def func_2c2e761fdb5843fd9a1dda4105129b44(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return U


def func_4beb228a4d5f47a9a29b35eb9c001737(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return i


def func_5d96a1c468fd4b6b8048b3ec19c148ac(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ll


def func_2725b3e1248948feab7d09073424312b(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return d


def func_1bc3d682d65b4ea8a12abb8adc3668be(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return rr


def func_883edae9c33f45da83d3c53fe148c85e(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return c


def func_1e13efd45c3d49ce92358c5c44e746fd(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return w


def func_f2554773dd124b8ea82eddefa6a1193b(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return h


def func_f0245d35b80e4371b24072ead440f251(u, g, infile):
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return x


def func_fa3783682d574ebe9b261d944aba153a(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return r


def func_f22476b5852f455295817a33360b8d63(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return L


def func_24dc4e578fc44e4db534aa8eb4965d19(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return dx


def func_111693a3320145849afd469e3b682ee8(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return i


def func_b139d7cb5b454e1382fe28040f18704c(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return y


def func_f3ab074e206f410dadb5e6a965682e8e(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return d


def func_b10b8bf3c11c4ac6aa78cd19a3d34eb7(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return a


def func_5a536c1c0e2b48308028fd5190e96f5c(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return hl


def func_e74ed737225540038e8f043e91fc6d9a(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return c


def func_75d5aa765c704ee3a026a7b2cdabaca5(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return x


def func_39c5c5ef5a11427ab16da2972279f15c(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return w


def func_6a0321f1b8fd4ab0ba69d285fd8dfbb5(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return h


def func_c1e869a4e9634a31a5576b9175038759(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return U


def func_42adce67435641679fff233594bc5147(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return l


def func_c4ab9d32be2e4113934f001723e323c6(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return u


def func_1c56fcbe9f3447e5b0678c912912917c(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    return g


def func_32a7796be7874600a617ef2e9310af49(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return a


def func_9646dbd001314c22a642e22b14ea9db3(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return U


def func_65f864ddc12e4d64be528d45288bee8c(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return rr


def func_2d09341a275441fc96261664d1303db1(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return dx


def func_2a51912b2898488696c288d4b80f6a24(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return d


def func_c2c6dc19981943eb8673bde2c7200364(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return w


def func_6b97da6512e84eca808ca536bf347d5e(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return h


def func_2e883a08a3944a63a398837f074b4633(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return eps


def func_361af38d6642455e93551f9b3b2dd092(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return r


def func_dbebd308b3be4e2490b097f67731077e(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ap


def func_53978f2fcdd24c70a67704e0b774de31(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return y


def func_d16f71c122444051802d144d0adda095(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return L


def func_c42fccc1016e416eb6784e1fe89b1587(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ll


def func_6fd05bd17d2f4a3090a03b90dc8b47ed(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return l


def func_be8bcf5529bc4a249b4056c09cdbeb15(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return c


def func_61ef6234f37642688cf6ebcf7ad347ad(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return hh


def func_1982e10b018e4e439ea3c9d77cfab201(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return i


def func_52842d81244044338b8ec531f132a3c8(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return m


def func_9afee247004e439391cec15e2e3b7bfb(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return hl


def func_35d16c8a821940c6aed82fb35e741f82(u, g, infile):
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return x


def func_32da583385684c4f8d91f606840d2f4e(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ap


def func_dfddd0d76928404e8ac49d3894a42c45(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return hl


def func_986ee0578f784ac29086b65872d850ea(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return c


def func_27de69054ef842b5be3ef6254aa4c577(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return rr


def func_293eefa8271d4572b1b8218fb6b31d49(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return dx


def func_543172cc287142cfa25ba2ace6055930(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return u


def func_aea7d4fd17b64ac8b0e4c1ee9638a26b(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return hh


def func_cdad835293aa4c428f646d93ceb489af(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return h


def func_7c7aeb05e0814a0e876ff25e6dea6a3b(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return y


def func_972dc383b9a24f749dd50b99092cad7e(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return g


def func_ec322344455e4a429450d72813d2f4ce(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return ll


def func_158e28e157e44065b4b00e1cd136f7c9(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return i


def func_42bb84b696254ab9afc5f19b09628326(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return a


def func_54eef8abf6074494a7ff6a401fa3eff7(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return m


def func_1246df98339349e386245f08466fc9d4(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return r


def func_e4602a6f9c3f48b2bb0390233073ee27(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return w


def func_26f9e2d78764498ab6ccf5ff1cfcc9cb(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return U


def func_7bcb441ed9a54c8098007f0ebecd0284(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return d


def func_0b708bc182b64403b43063a3ae8d138a(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return l


def func_83ea45f156b842c58af68b4ccc8bde8c(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return L


def func_c4dfd13831a54b68978f218439d0be61(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return eps


def func_94cba64e6f9c4a45907dfc663e8df2f6(infile):
    w, l, u, g = map(int, infile.readline().split())
    L = [map(int, infile.readline().split()) for i in xrange(l)]
    U = [map(int, infile.readline().split()) for i in xrange(u)]
    w += 1
    h = [0.0] * w
    hl = [0.0] * w
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            h[x + L[i - 1][0]] = x * d + L[i - 1][1]
    l, L = u, U
    for i in xrange(1, l):
        dx = L[i][0] - L[i - 1][0]
        d = 1.0 * (L[i][1] - L[i - 1][1]) / dx
        for x in xrange(dx + 1):
            hl[x + L[i - 1][0]] = x * d + L[i - 1][1]
    h = [(x - y) for x, y in zip(hl, h)]
    a = sum((h[i] + h[i - 1]) * 0.5 for i in xrange(1, w))
    d = a / g
    r = []
    i = 0
    c = 0
    while len(r) < g - 1:
        if c >= d - eps:
            ll, rr = 0.0, 1.0
            while rr - ll > 1e-08:
                m = (rr + ll) * 0.5
                ap = ((h[i] - h[i - 1]) * (1 - m) + h[i - 1] + h[i]) * m * 0.5
                if c - d > ap:
                    ll = m
                else:
                    rr = m
            r.append(i - ll)
            c -= d
            continue
        i += 1
        if i >= w:
            break
        hh = (h[i] + h[i - 1]) * 0.5
        c += hh
    return x


def func_cdaa5a6e855a4812a45952df050b381c():
    infile = open('codejam/test_files/Y11R5P1/A.in')
    T = int(infile.readline())
    return T


def func_be114bfa77ad4a93803edb5fa95798b5():
    infile = open('codejam/test_files/Y11R5P1/A.in')
    T = int(infile.readline())
    return infile


def func_86880a6e83cf4d2c94995b7ce97ea704(infile):
    T = int(infile.readline())
    for i in xrange(T):
        print 'Case #%d:\n%s' % (i + 1, solve(infile))
    return i


def func_0dd2f00d26b24742834be7d9135ee9b1(infile):
    T = int(infile.readline())
    for i in xrange(T):
        print 'Case #%d:\n%s' % (i + 1, solve(infile))
    return T


def func_e260ff49028e4022ad35f5cb9e4b7e9b(T, infile):
    for i in xrange(T):
        print 'Case #%d:\n%s' % (i + 1, solve(infile))
    infile.close()
    return i


def func_c3b7dac5da4d4556858957da5efcd36b():
    infile = open('codejam/test_files/Y11R5P1/A.in')
    T = int(infile.readline())
    for i in xrange(T):
        print 'Case #%d:\n%s' % (i + 1, solve(infile))
    return i


def func_5c65df76b04a4621a242171c81ece5cf():
    infile = open('codejam/test_files/Y11R5P1/A.in')
    T = int(infile.readline())
    for i in xrange(T):
        print 'Case #%d:\n%s' % (i + 1, solve(infile))
    return T


def func_ae9aab903507450b9c93d63bb85b1494():
    infile = open('codejam/test_files/Y11R5P1/A.in')
    T = int(infile.readline())
    for i in xrange(T):
        print 'Case #%d:\n%s' % (i + 1, solve(infile))
    return infile


def func_2c0b536fee184657bbf33bc973b9510a(infile):
    T = int(infile.readline())
    for i in xrange(T):
        print 'Case #%d:\n%s' % (i + 1, solve(infile))
    infile.close()
    return i


def func_67b2757000c04064a6e51834098798a5(infile):
    T = int(infile.readline())
    for i in xrange(T):
        print 'Case #%d:\n%s' % (i + 1, solve(infile))
    infile.close()
    return T


def func_9b9ecc6cdb9c4b9cb0509c4e1e249712():
    infile = open('codejam/test_files/Y11R5P1/A.in')
    T = int(infile.readline())
    for i in xrange(T):
        print 'Case #%d:\n%s' % (i + 1, solve(infile))
    infile.close()
    return i


def func_9b17aa1e6f4c4aae9e9ba7242db7c1d1():
    infile = open('codejam/test_files/Y11R5P1/A.in')
    T = int(infile.readline())
    for i in xrange(T):
        print 'Case #%d:\n%s' % (i + 1, solve(infile))
    infile.close()
    return T


def func_8e14b1ea189242178166a3f888424fb7():
    infile = open('codejam/test_files/Y11R5P1/A.in')
    T = int(infile.readline())
    for i in xrange(T):
        print 'Case #%d:\n%s' % (i + 1, solve(infile))
    infile.close()
    return infile

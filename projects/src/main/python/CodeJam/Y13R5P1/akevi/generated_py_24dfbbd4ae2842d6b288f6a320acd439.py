import sys
sys.path.append('/home/george2/Raise/ProgramRepair/CodeSeer/projects/src/main/python')
from CodeJam.Y13R5P1.akevi.a import *

def func_f6a957a3059f46c48f01332c34599ecc(x, cx, i, b):
    crem = x[i - 1] * i - sum(x[:i])
    if b >= crem:
        cx.append(x[i - 1] + (b - crem) / i)
    return crem


def func_8e40b989b28248da9bb90e59d2700f7e(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    return x


def func_e683d783e7e549c58a4e77e2867fdd9b(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    return b


def func_2bd5c3da60954419996f15e760c2c4a9(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    return n


def func_62a2ebc4440046d08f693ecf15f203f8(infile, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    return x


def func_d2ddc87a2c0a41acbca869d05edb2b9d(x):
    x.sort()
    cx = list(x)
    return cx


def func_555f3d3ae8a34bb5b184e236dddd8190(x):
    cx = list(x)
    sx = sum(x)
    return cx


def func_1061798b98c646c69ae5ec87be036720(x):
    cx = list(x)
    sx = sum(x)
    return sx


def func_228d60d145a24a3facdc0d44a0bb1497(x):
    sx = sum(x)
    mx = x[-1]
    return mx


def func_fc2e6161d945453185c01d939f5761ae(x):
    sx = sum(x)
    mx = x[-1]
    return sx


def func_c5e7a6dab6e54146a95764ed04f3bbb7(x, cx, b):
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return crem


def func_fdb4fd033c6f475280330d908bbf17d0(x, cx, b):
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return i


def func_a201075948c14689a24a604e142bdbed(x, cx, b):
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return mx


def func_f073ce775cf3494aa602ca2b36f56de1(x, b):
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return crem


def func_85f1715dc4d24edc8bf416fbeb2047de(x, b):
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return cx


def func_aadb3f0239244de5967bc7a45c33ec7f(x, b):
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return i


def func_1099613ddd2a407cad3a3275ed5cf666(x, b):
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return y


def func_5b39802b58cd48a498c550738801d71c():
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return y


def func_0f0a4e19dd8d4a03aeed3572aadfe552():
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return cx


def func_108d7ae2646a4f8b9a9cfafb46f39f4d():
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return y


def func_67ea2d07a4464bd9ac84edcae9565111():
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return cx


def func_e6858552381e4ac1a29ca2875e8eb824():
    cx = sorted(set(cx))
    best = 0
    return best


def func_1a8836986e3c4665af13545e2c60625d():
    cx = sorted(set(cx))
    best = 0
    return cx


def func_933932625b1349368bbb2fb95c175ca1(cas, ocle):
    best = float(best) / ocle('Case #%d: %.15f' % (cas, best))
    return best


def func_54c01c7dc3554b17b7f70d34e200f0da(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    return n


def func_b2d7b088146d4f60bf1705ee4881afa0(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    return x


def func_49629c51a3ff48fc973dd4e845c6726f(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    return b


def func_d11c606ae6ff452c8bbf99957e9e5b04(infile, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    return x


def func_904f6b283a714483ace35fda45627fc8(x, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    return cx


def func_ca1317bd485c4e87a82141180a5265bc(x):
    x.sort()
    cx = list(x)
    sx = sum(x)
    return sx


def func_2875bc7241234311877688a950fe5e7c(x):
    x.sort()
    cx = list(x)
    sx = sum(x)
    return cx


def func_8d78284b9549466b92a0257a1207623e(x):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    return sx


def func_ed56b8cfd6ac4ee7862e4b790e24e948(x):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    return mx


def func_dcd8b40c2f7846f9891ebc1b8fa37b72(x):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    return cx


def func_06f3b52e1fbd4507afe87811bd51badd(x, cx, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return crem


def func_3a0ba184268f46039a285e12aa447c23(x, cx, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return sx


def func_f4a87832c9e34b94a7d942c7f761ee54(x, cx, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return i


def func_68e3e7a2b91d4cb9afd65b631d050528(x, cx, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return mx


def func_671f8606bc914d1bbf8f5ca8628e97e5(x, b):
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return i


def func_88668a507824415c974eca0b93803734(x, b):
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return mx


def func_528412e04cdb44f384a35c673a52b247(x, b):
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return y


def func_49049fd28c37429faecace7660f9486f(x, b):
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return crem


def func_3f173b9a7e734742bdf0e01f9c33b1a4(x, b):
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return cx


def func_81ea8b3bd1b54b8599e4de95873da00a(x, b):
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return y


def func_a06bd8cb31674f9780d47c98adf49f17(x, b):
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return i


def func_d90ff638ec784a45aaf192c54385704f(x, b):
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return cx


def func_a152ea4f692d4c368482517383d86688(x, b):
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return crem


def func_5317f45649d745bc936a22248c0bb858():
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return cx


def func_8ccd32c00e5e482ebd418c6fec8717c7():
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return y


def func_134fa6b6dd414bc6b785e56ecb2495a3():
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return cx


def func_7ecf465c5de145a8aac3c3a87b69d1b6():
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return best


def func_c7195dc8ac714d88b646a11ef8cc3bb7():
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return y


def func_9f35f383981f4842adc52ccc9e9ae02e(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    return n


def func_2da6fe8cee7e4781b6cee19a61ba1d33(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    return x


def func_819ce53f342a4927af4c88d30551c27a(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    return b


def func_73916f53210d47c8bde91d91cbf4c94d(infile, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    return cx


def func_3c7ed34efe264b38a14b337e63a80388(infile, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    return x


def func_e20fbbb51f4647e982bb75c033662527(x, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    return sx


def func_413dd86f71d44142b10cdbf1bdddf4a7(x, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    return cx


def func_f0729025c12341a5b02eb2e1839e8746(x):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    return mx


def func_ba6c6cf85c5c42289b94a45e06d83a74(x):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    return sx


def func_aa8510e7e9404957b6a27324c4795f10(x):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    return cx


def func_dd7c6accd31a4a3dbc5d8c997cf24c6f(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return sx


def func_307e3fe21e5848f69a13f4137ebb5308(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return i


def func_a8f1ef8a25e24b95a157e890f205ad15(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return cx


def func_c268559d10664243baa2dffefda67ba4(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return mx


def func_94115d5f35054a0aad6d16ed04ca0e72(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return crem


def func_6d5c1fe4bb554f999de904f6a9ad38ca(x, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return mx


def func_852e221066374d118a6627440cc1c1b1(x, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return sx


def func_9ff6f7782dbd4168af92c8688cc5e5ff(x, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return cx


def func_b3c805bd646f4e7292f3313e642aa5c8(x, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return i


def func_c12a61d105624907a8271ea8105c6a73(x, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return y


def func_4744082b8d854283b2e355f2bfade806(x, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return crem


def func_8614cdc7d37447f7bb12d7d18b0d6c24(x, b):
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return y


def func_57e69b68dc6b480ab13d0db155ac3f77(x, b):
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return mx


def func_34e21115fbfa481ea54d61751fd20c48(x, b):
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return i


def func_5813f625311544c5a7063c343e39e8d9(x, b):
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return crem


def func_8ca393c7d6664b6abd598d9dc7ad10ca(x, b):
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return cx


def func_e2c6569757e24f0bbf07aebfe71c5a92(x, b):
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return y


def func_05b3868318524063aad5a85f6a7082d3(x, b):
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return cx


def func_86b9ef978359483ebcab675c8535c4e5(x, b):
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return crem


def func_3ddeb633c3d14577bd78e41e537c9495(x, b):
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return i


def func_cef205ceb4a14a4d930ceac41494ae76():
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return best


def func_b46996a21e1b4b90a1d1c11e134fc858():
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return y


def func_d5e3fb896e3542e38526bdce0da010ab():
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return cx


def func_2a18428c345d4b5bb06f7a3b8fc96755(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    return b


def func_83d3eeb5eab04fd89b04a49824c80623(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    return cx


def func_686e90fbcf744b268d6be6b5a07a5c8e(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    return x


def func_eb5f855521924a20a6a77c5a927e7efa(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    return n


def func_452b21e9dff34ea38d949c5f1cd1761e(infile, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    return x


def func_50cba7feb5094df68b830915cf19b137(infile, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    return sx


def func_1241703a7d7b49099cc16feff324f191(infile, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    return cx


def func_eddefd669c904eb5b84c61fb31b15ad6(x, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    return mx


def func_2c65a4249cc740608076eb67687a7c14(x, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    return sx


def func_ec1ec7013e83410491ae538993715ec4(x, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    return cx


def func_1395d1b37ed3425b98b6fd3d9bbf1c6e(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return crem


def func_18bfd0b9ecef4a78bfdb95c72988b98b(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return mx


def func_eb68873725004be1955513a57bebcf49(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return sx


def func_e099a3afca9a4e97a57f85f48c593131(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return i


def func_98123137feea44fe8e1d65ad8a57ea71(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return cx


def func_5290e720b6914336b5e6f544bdd5f608(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return sx


def func_8d772be388c34ac290466bf40e60bb2c(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return y


def func_d28f9c6f5ade4a508e4c5eb8f44b22d2(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return cx


def func_e00bea761bd44cde9cf38c6458c60b26(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return crem


def func_b20feccfd2394bccac91230c605465e6(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return i


def func_8c1032bf6d3f4e11a01e87e0d594bddf(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return mx


def func_b8913fa555ca4ac58ed7bd4a0abd9e9f(x, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return crem


def func_7aa7f20d28704c75985d5da71158c382(x, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return i


def func_dbbeda21cf784dc38da0a4e591325312(x, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return mx


def func_58273de6be7a47c1804d9aafa77b445b(x, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return y


def func_916e6529968d4034959d74587bc5b5f8(x, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return cx


def func_99b0b7264dbf4bff83ad73d9d33d1f2c(x, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return sx


def func_acf70eb0164c4c4ea5ab370933ae0019(x, b):
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return mx


def func_f4924656c0bf4bec868277fa0415d554(x, b):
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return y


def func_06e81511b59b48788468f909044c4279(x, b):
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return cx


def func_bb8160bbdaeb42b4b7f70bf06cf4fafd(x, b):
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return crem


def func_3fe1d30df284460d98d9032ad6203134(x, b):
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return i


def func_5f491746ed78464eb82fb914588b8585(x, b):
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return y


def func_2dbd8551567745c89515050433bb6015(x, b):
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return best


def func_33b9ceef73954d1ba837db382a4b6c26(x, b):
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return crem


def func_cb62311130d3475cb6553f8de159b699(x, b):
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return cx


def func_fc2fd6fb2305400982aed196e7c6115e(x, b):
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return i


def func_e08e8fb0bd0446ad8a62962129e5b985(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    return b


def func_13d224ef1d0d4ace803ae9f22a01ea82(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    return sx


def func_cf2472d20b8f489e88b69d4d73aadfab(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    return n


def func_e954c2adf0154d7c9bc9300ab1b9fb75(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    return cx


def func_738bc3c9bb9541dfb1e4d87b8409c6b6(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    return x


def func_f0696bbfac9e49bbb374623a9a792441(infile, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    return mx


def func_bea8673ef8c342f49af2f04f7e891db7(infile, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    return sx


def func_cdb13d8716b4484fafba9f8728829db9(infile, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    return cx


def func_f7514c7a6dae4d9a94d97c2a2ea489be(infile, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    return x


def func_a4f7dd7513a74d8b820648d71f891e00(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return cx


def func_ddb29484b38e4133aafddced008ca260(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return crem


def func_053a9e1a03fb4d3892d7ab28953a0323(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return mx


def func_2167822f4f6f4e7bb233101678bb1bc7(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return sx


def func_772aad3dba424a64a2a1c09042db71b6(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return i


def func_3a1cbd48d8ec460a8a2234890c061a5a(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return cx


def func_5907b0e0e03f479a82c4dff30d1a71eb(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return sx


def func_c21cdd3a795e47e7b3bae3e14245703b(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return y


def func_59aaba89257543808bc47b8e25ed6bad(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return crem


def func_bd1684a27a5a477bbcf936a74d91ca33(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return i


def func_e4a3f9ff0111432e94d26021b6a71700(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return mx


def func_a732725937d24b598963cd6e4fbe0cd2(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return crem


def func_791c580fe35f4f9b857e0e6c09083196(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return mx


def func_3aef410d4f5f42d8a12019bf4411ed02(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return cx


def func_176a40d92b5b47c380af3fc226c36c61(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return i


def func_dc844604a138442ab2b4b74aacc758ec(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return sx


def func_8de44f7b78ef4353b96cb262a9ed4e44(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return y


def func_8944ae44a4f5491f9cb5c50ece976177(x, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return y


def func_fbb2858c13ab4139b543c09afd7b3a9d(x, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return sx


def func_04f8c2ab08db4fecbde1603140bed168(x, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return crem


def func_ced777e974b54f43ab3bd236faa8e2e8(x, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return cx


def func_e80fb557a67740bbb1634a1f94dbd1ff(x, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return mx


def func_0771e9eb22984d6da6844c274afea3ad(x, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return i


def func_7ff5070a096c47e7ac1c0b342baeb3e8(x, b):
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return crem


def func_626619628f664bcfa70b7ffa7b0292cd(x, b):
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return best


def func_cbf55d8c62cd401fa205363460ace1f8(x, b):
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return y


def func_c196ee873f7640ac81a47df79dcee37a(x, b):
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return cx


def func_04f2f16b81c7463e8a542d6b79eafa32(x, b):
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return mx


def func_de91cec29d134cbbbbee237e86d90613(x, b):
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return i


def func_7164254c656e473db7c3a9d55487ed57(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    return cx


def func_a5d99448256d49099b15fa0e4fb21770(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    return mx


def func_608aba9db10b46b3a333d3ed3a42a2c8(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    return sx


def func_b5dd37f064d64026810eb571cd222ed7(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    return x


def func_8739587816c74298b5d3813cf6870ed4(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    return b


def func_69f1faa88bea4321a5a51b9d027de7c3(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    return n


def func_b6b5065a5dee415693fc2d996d6e8d79(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return crem


def func_95eaef459b1543179e15091b424360b8(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return x


def func_5e6bae7aadfe4dac86adc361ae4541e6(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return cx


def func_d9e787e7934f43c9a0a02ac4540d6239(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return i


def func_97ea4480d4db4b68b5aa087268288504(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return mx


def func_94ba257382d2424ca0986b81faa6a350(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return sx


def func_2952648717d44dc4b1892d3b4224b289(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return cx


def func_3e076ecac0f74a6aa0768e5157d84894(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return sx


def func_94d86a4218814d7ba0e7210049d46136(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return mx


def func_8ea3283e34d641b1a6b7ccd21bcb4e0b(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return y


def func_23bcf0ade954423ea8faf8334234a8eb(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return crem


def func_947d894e1c5e41d9b5cea2afa8f9f734(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return i


def func_72dc87936dbc48da9d28b4925e726ebf(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return sx


def func_d3a08f356cf142ad85ebe4d2d3e36baa(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return crem


def func_11849c249aad47509e0a1064e987adb2(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return i


def func_f71e39ed428a4455af9fbd52a5eb78ed(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return cx


def func_6b0509362da64a74b9712bfee10d409f(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return mx


def func_17fe85c5cd4d4f6088e8e7f8eef96c1d(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return y


def func_cfa7b7355ff3423da23a4761951c1e56(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return sx


def func_f1348d4f6022450c9bfe216225d3671e(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return cx


def func_355ce4f1206141ce812675a1aee5ca8e(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return i


def func_8b580c2ba5b2439f8e0a1a918e2dc030(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return y


def func_207791446184483ea54719256c5dc5f5(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return mx


def func_6da457daa81a4e6babb8be510059d73e(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return crem


def func_79940bfbc784429eb9e9cef8d15b1cf8(x, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return mx


def func_bdaf53a2c86f443b8be0b5ccb319378f(x, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return best


def func_11b738efc3aa4156b39adbb1f12d94d7(x, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return cx


def func_6adbaff1a91147ed978ee343c37ea200(x, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return crem


def func_bbd3648c6fb040c994f94fbcf2e3c41a(x, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return i


def func_548e2a22b5154cdd9f48d7c0caf3e6eb(x, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return sx


def func_eedcf030ad17439daa3f645e4b17b01d(x, b):
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return y


def func_4bf537b9666742cabb66cac179d5dddc(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return crem


def func_a6cc5f6378f547fda21dccb613c193da(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return sx


def func_e233472b1cba4b2d9707bc1d1bba3ad6(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return i


def func_43c70255f4cc4526b022e4c5efa5914a(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return mx


def func_fcfaffdd1c97431fb73f7cb846671f13(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return x


def func_04cd7922c240434ca7098c4462060db2(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return n


def func_1916f4a7ea294568b6a5eecc5fd2f4b5(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return cx


def func_aad84ac5b4b844ef8c2fbf540cfc6663(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    return b


def func_faa575a2687541ac9f34718eb64d46d6(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return crem


def func_2cdd532b066b4c0a8aa23893c887b5d5(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return sx


def func_efca4a4e5ec1425797925a85c69c0748(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return i


def func_bfaec7339c27437ab39736dc46fa9431(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return y


def func_22a4660815254ab39d1b6413392bba6b(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return cx


def func_e40401ae872a485eae665c7457aa3cd1(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return x


def func_afe2ea8263cb453eb263224ba0c09cf4(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return mx


def func_7948b6a0a91a499894a6c474eef4a9c9(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return crem


def func_d1f32725783e4b908b8031f33fae116c(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return cx


def func_23364b70a08945ba932094d14fc62d83(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return sx


def func_86303f309789414ca452558d2a32f079(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return i


def func_dac67865ade047c7bc4bb34611b3447f(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return y


def func_a6e3057018914b5bba137100af3b951b(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return mx


def func_9b35508551044d11b7850effc4cacc89(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return sx


def func_3c4a7d27d5b346a59712071cc4926e79(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return y


def func_7d8e6312c635418f9f5bb861651cac1f(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return i


def func_696b65efc22f4af3be2a9d3eca610789(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return crem


def func_bb37a6d4bbdf4ccd986b8d5afe8b80f1(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return cx


def func_6fb42f03ae1947a7a25c5541551e1c93(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return mx


def func_bed1bb79fcfa466393f89af0bc5a784b(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return i


def func_998103f29d34403aab302fbb9b349767(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return y


def func_9fed3cf9c4724ab693bd7ec93ae1018a(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return sx


def func_b65f204ca12e4d5a9a48c1b7de39e281(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return crem


def func_ac49007e4ed54caeb53ebd892acbb35f(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return best


def func_87cab31a3f50408b98c3a3af89898413(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return cx


def func_cb9dcd78b80e42448d17b59e8c82ffb7(x, b):
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return mx


def func_550b0cbf97034e3487b84d7097eba736(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return sx


def func_f1f24abb72de4b1c8feaf2e29c92ec87(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return x


def func_741efa8ff99f42f9bad6a472863e8c3c(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return n


def func_52c100f62da143c6a697368e434d383b(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return mx


def func_08ee21734cd54997b57ed972f98cba72(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return cx


def func_6a6930c49a4e41a38d285bd92a35f4a5(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return y


def func_fb1204ad907b496097a90db24f5783cc(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return b


def func_dbbe58c1695044d58b0325a255565f53(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return crem


def func_f18c7b95158a451ab52b67328287d5b3(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    return i


def func_2fd699d0d1e445c0b2b599f29377f866(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return x


def func_1230a04c960a403ba97570927163c547(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return sx


def func_7f030d7c674e4637b328c5561f59015e(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return cx


def func_624f8b2f461b4148a00c2b80b9567ce6(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return i


def func_27323f58f64348758bab9ecd350c5c2b(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return crem


def func_a13393d68e5c4f9fb5433108348082c1(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return mx


def func_305c9714d81c47269673244abb321396(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return y


def func_d575c5cdea35471da566db89e878dd8d(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return sx


def func_c3469afa95444c83b1ab66e421878e9c(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return crem


def func_0525fd89c34c45f7997fdd6fa68ab7ea(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return cx


def func_6568615782c04a7b89b0846bef3f9081(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return i


def func_85691a3123a64155ae71f65e2e182532(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return y


def func_1c477286277841ab9ecef01d810be440(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return mx


def func_23d44470472249a186062c7391f88137(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return mx


def func_1b75fd387a8a417fbd9cb88d5c02b772(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return i


def func_737216898ce841969e7674be95456fd4(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return sx


def func_13173ac1918042749e46b56106f696cd(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return y


def func_df47ad957e24486ca9cd05d42041c692(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return cx


def func_27b299ec09e74473a1a1c22414efe0a5(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return crem


def func_9022320e92c54f189b4a1155b14ff2cf(x, b):
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return best


def func_7e027b2eb82d481d913f0c6f40bf5bd5(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return n


def func_f4c04516229648b7a1565ce55b599592(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return sx


def func_0ad86385c10043ed8582dca38fba561e(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return b


def func_f8212a4218f4405bb0f88bfc025760ee(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return i


def func_3f2ac190b133436287509d3edcb92e6e(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return mx


def func_b7c569a8f2234f7f9221a07fb2acbd7c(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return y


def func_11258830c3c44db187dbfdf7fc1f7bca(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return cx


def func_ead6f3b70bc54d6c9161a6ee8f9cecd3(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return x


def func_a6d36dfaad364cc1951b54814c714d78(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    return crem


def func_f5a42e97bde84e09a20c8c9353b1bf6f(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return x


def func_fa14106736f0497fb4da550994d5c089(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return cx


def func_b078de0edfaf4c999ba343de5203ff2b(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return crem


def func_7804497dad074940ae59697b62c7139f(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return i


def func_16113ce562c941cb829cc17563b41805(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return y


def func_f0b13baf8b734e6289d77229b8b76712(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return mx


def func_63229f914c264139bc7f5653b923d0ba(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return sx


def func_dcae4c91ad5e450199f238aa1f197245(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return mx


def func_2e6c2c9b0b1745509145064ffc24116a(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return i


def func_281f9d66a58f4b2aa3c7b9557641454f(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return cx


def func_0b2e1f3a9b454dd0aa46e9a67218e2a9(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return y


def func_e824fe8955ce4dcda2da72a0fd0bd2cc(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return sx


def func_d14be9b592f44c478efac897a08e0f7e(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return best


def func_fe8736014d1a40cf8f9e5d3cb712c3c1(x, b, n):
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return crem


def func_f3527d287ce24795b0628c5148f7d483(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return y


def func_8e6e93ded63447d89c3076d8c4de0b0b(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return mx


def func_ed04e6d88a364933a799532c77ea5ce7(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return b


def func_651ad65e805743aa8b2af40a2215e35e(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return sx


def func_f0d2bfdbf65647bcad3c28b69f72dd9d(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return n


def func_1e6fc7c9950949ab83e84a6d6580463d(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return i


def func_a3fe04998ba44cd491f84311fce3daa2(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return cx


def func_65acbde38bc24052a5be21e40861b319(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return x


def func_fc8ec068a1294147b8c967c5477d06dc(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    return crem


def func_80edee386ffd456dbccbadb0505b6a4a(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return i


def func_66602b35192f4269aef57dd716ce54e9(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return x


def func_db122f889d0544cfb6e4d61da46a42aa(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return sx


def func_c2fb5e0657294833b346f58af87f097c(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return cx


def func_9be9cb15067045a2bc17d20fc75fbf8d(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return mx


def func_dffc22cf335a415d9e850c9134b8eaee(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return crem


def func_a7835684bf3a4b64b02918a2e004f2e2(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return best


def func_5f6ce9f2ebad4a158de1ff167af4a438(infile, b, n):
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return y


def func_4cd3591bbf4d49e1afcd32c8d5028474(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return sx


def func_a012f6c7f7e6448aa4c6148e1e3e2393(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return b


def func_23b02fb9ae5f40baa185dd011e1e5869(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return crem


def func_cf4201e705cc475c9f8d6b9dfcbe5c5d(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return y


def func_716b52aa728145839b26f43f126986fb(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return n


def func_5223b275daf34df8af2c856bd45a1d2e(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return cx


def func_019a3d6b57e740a39dfc2cd13443c288(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return x


def func_27088fa09e4e4ebeb12c4e0dd96104b9(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return best


def func_b4f9d26c24fb41d59217f4266fce6138(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return mx


def func_43a943458312416ca1d42d119ec6e6ae(infile):
    b, n = map(int, infile.readline().strip().split())
    x = map(int, infile.readline().strip().split())
    x += [0] * (37 - n)
    x.sort()
    cx = list(x)
    sx = sum(x)
    mx = x[-1]
    for i in xrange(1, 37):
        crem = x[i - 1] * i - sum(x[:i])
        if b >= crem:
            cx.append(x[i - 1] + (b - crem) / i)
    cx = cx + [(y - 1) for y in cx if y]
    cx = cx + [(y + 1) for y in cx]
    cx = sorted(set(cx))
    best = 0
    return i


def func_036a2553c7d24fc78af294c151e05618(x, ocle, j, v, req, cle):
    bag = ((cle - j) * v - sum(x[:cle - j])) * 36 * ocle / (cle - j) - (req + j
        ) * ocle
    best = max(best, bag)
    return bag


def func_c35be4523fc2453fa71bd7d471d4033c(x, ocle, j, v, req, cle):
    bag = ((cle - j) * v - sum(x[:cle - j])) * 36 * ocle / (cle - j) - (req + j
        ) * ocle
    best = max(best, bag)
    return best


def func_0b883d0d9a984179abb17979da62d6db():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    ocle = fac(37)
    return infile


def func_00145d505dc6469f96b7b859418b4238():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    ocle = fac(37)
    return ocle


def func_b2a7596b74cc4130b30ddf931a506f4b(infile):
    ocle = fac(37)
    z = int(infile.readline())
    return ocle


def func_9fdd9940872940cbae4567b811e5de02(infile):
    ocle = fac(37)
    z = int(infile.readline())
    return z


def func_96c3ec08324a47d3a90eed391caa991c(x, ocle, v, req, cle, b):
    for j in xrange(cle):
        if req + j <= b:
            bag = ((cle - j) * v - sum(x[:cle - j])) * 36 * ocle / (cle - j
                ) - (req + j) * ocle
            best = max(best, bag)
    if req + j <= b:
        bag = ((cle - j) * v - sum(x[:cle - j])) * 36 * ocle / (cle - j) - (req
             + j) * ocle
        best = max(best, bag)
    return bag


def func_d11898b34a4643d5886aaebd6f6467ca(x, ocle, v, req, cle, b):
    for j in xrange(cle):
        if req + j <= b:
            bag = ((cle - j) * v - sum(x[:cle - j])) * 36 * ocle / (cle - j
                ) - (req + j) * ocle
            best = max(best, bag)
    if req + j <= b:
        bag = ((cle - j) * v - sum(x[:cle - j])) * 36 * ocle / (cle - j) - (req
             + j) * ocle
        best = max(best, bag)
    return best


def func_fcf05d157f334890a6a2ffef9c2c443f(x, ocle, v, req, cle, b):
    for j in xrange(cle):
        if req + j <= b:
            bag = ((cle - j) * v - sum(x[:cle - j])) * 36 * ocle / (cle - j
                ) - (req + j) * ocle
            best = max(best, bag)
    if req + j <= b:
        bag = ((cle - j) * v - sum(x[:cle - j])) * 36 * ocle / (cle - j) - (req
             + j) * ocle
        best = max(best, bag)
    return j


def func_1ccdfa2f83724394b9df1e99bb1609e0(x, infile, ocle, j, v, req, cle, b):
    if req + j <= b:
        bag = ((cle - j) * v - sum(x[:cle - j])) * 36 * ocle / (cle - j) - (req
             + j) * ocle
        best = max(best, bag)
    infile.close()
    return bag


def func_ef60a6b3ec0c418c9fa77c4c4237757e(x, infile, ocle, j, v, req, cle, b):
    if req + j <= b:
        bag = ((cle - j) * v - sum(x[:cle - j])) * 36 * ocle / (cle - j) - (req
             + j) * ocle
        best = max(best, bag)
    infile.close()
    return best


def func_35247fe3a64e438096bb7f1b6f5d85b8():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    ocle = fac(37)
    z = int(infile.readline())
    return infile


def func_5b2abd22428444c4a3b3ccf5ec6114cb():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    ocle = fac(37)
    z = int(infile.readline())
    return z


def func_b5af5bc688404184a10e8f91a0d603df():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    ocle = fac(37)
    z = int(infile.readline())
    return ocle


def func_8be0bdb3b580463ead43bb68d81d80ed(x, infile, ocle, v, req, cle, b):
    for j in xrange(cle):
        if req + j <= b:
            bag = ((cle - j) * v - sum(x[:cle - j])) * 36 * ocle / (cle - j
                ) - (req + j) * ocle
            best = max(best, bag)
    if req + j <= b:
        bag = ((cle - j) * v - sum(x[:cle - j])) * 36 * ocle / (cle - j) - (req
             + j) * ocle
        best = max(best, bag)
    infile.close()
    return j


def func_085080efa729432c96e7b3e0b3213d8f(x, infile, ocle, v, req, cle, b):
    for j in xrange(cle):
        if req + j <= b:
            bag = ((cle - j) * v - sum(x[:cle - j])) * 36 * ocle / (cle - j
                ) - (req + j) * ocle
            best = max(best, bag)
    if req + j <= b:
        bag = ((cle - j) * v - sum(x[:cle - j])) * 36 * ocle / (cle - j) - (req
             + j) * ocle
        best = max(best, bag)
    infile.close()
    return best


def func_3b68fbf1b25d447e93f58e34973e9c27(x, infile, ocle, v, req, cle, b):
    for j in xrange(cle):
        if req + j <= b:
            bag = ((cle - j) * v - sum(x[:cle - j])) * 36 * ocle / (cle - j
                ) - (req + j) * ocle
            best = max(best, bag)
    if req + j <= b:
        bag = ((cle - j) * v - sum(x[:cle - j])) * 36 * ocle / (cle - j) - (req
             + j) * ocle
        best = max(best, bag)
    infile.close()
    return bag

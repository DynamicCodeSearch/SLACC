import sys
sys.path.append('/home/george2/Raise/ProgramRepair/CodeSeer/projects/src/main/python')
from CodeJam.Y14R5P1.Nin.a2 import *

def func_717d246c1b9b4310ac153dec98d6567d(cum, ar, al):
    amid = (al + ar) // 2
    left = cum[amid]
    return left


def func_45a8ae82050e4422b36fef97690207cf(cum, ar, al):
    amid = (al + ar) // 2
    left = cum[amid]
    return amid


def func_363fa4131bca4c56a7ac090593e893fc(cum, amid, b):
    left = cum[amid]
    right = cum[b] - cum[amid]
    return right


def func_d5d4c3663d48447494b8a8cdaf4e232d(cum, amid, b):
    left = cum[amid]
    right = cum[b] - cum[amid]
    return left


def func_7d07b68537204d21b89775bd045c274a(cum, left, amid, b):
    right = cum[b] - cum[amid]
    if left > right:
        ar = amid
    else:
        al = amid
    return al


def func_f30e678f9551418faa66237510177c05(cum, left, amid, b):
    right = cum[b] - cum[amid]
    if left > right:
        ar = amid
    else:
        al = amid
    return ar


def func_4fdcfbb1250c4998bc11c407402b095b(cum, left, amid, b):
    right = cum[b] - cum[amid]
    if left > right:
        ar = amid
    else:
        al = amid
    return right


def func_faf04282331749f9be21410277064c49(cum, ar, al, b):
    amid = (al + ar) // 2
    left = cum[amid]
    right = cum[b] - cum[amid]
    return amid


def func_5e90434bef2b45f8915866e2133ffd6a(cum, ar, al, b):
    amid = (al + ar) // 2
    left = cum[amid]
    right = cum[b] - cum[amid]
    return right


def func_acd5e8dd008f49f09ff5962dd582dae6(cum, ar, al, b):
    amid = (al + ar) // 2
    left = cum[amid]
    right = cum[b] - cum[amid]
    return left


def func_17d2f2e187844d84bb9dcc0913caa8f8(cum, amid, b):
    left = cum[amid]
    right = cum[b] - cum[amid]
    if left > right:
        ar = amid
    else:
        al = amid
    return al


def func_97ed03ac8d0c4d27808250ddf19042e5(cum, amid, b):
    left = cum[amid]
    right = cum[b] - cum[amid]
    if left > right:
        ar = amid
    else:
        al = amid
    return right


def func_1ad4fb9a676f4952867d44daa778ddd8(cum, amid, b):
    left = cum[amid]
    right = cum[b] - cum[amid]
    if left > right:
        ar = amid
    else:
        al = amid
    return left


def func_c5d88fa3e4a24aeeabb77ecb458070ed(cum, amid, b):
    left = cum[amid]
    right = cum[b] - cum[amid]
    if left > right:
        ar = amid
    else:
        al = amid
    return ar


def func_2aee8dcf68974fdb989c67b57fae2a07(cum, b):
    amid = (al + ar) // 2
    left = cum[amid]
    right = cum[b] - cum[amid]
    if left > right:
        ar = amid
    else:
        al = amid
    return amid


def func_d5e8344c93b8484ca77f00e9a008672a(cum, b):
    amid = (al + ar) // 2
    left = cum[amid]
    right = cum[b] - cum[amid]
    if left > right:
        ar = amid
    else:
        al = amid
    return left


def func_fc55837e1d3543fba8b9a861f4edf0e6(cum, b):
    amid = (al + ar) // 2
    left = cum[amid]
    right = cum[b] - cum[amid]
    if left > right:
        ar = amid
    else:
        al = amid
    return al


def func_9f255a63a75e407fb8704e1e07f8f7ed(cum, b):
    amid = (al + ar) // 2
    left = cum[amid]
    right = cum[b] - cum[amid]
    if left > right:
        ar = amid
    else:
        al = amid
    return right


def func_fd9dfb08df09463c905f4b6a1296e7d5(cum, b):
    amid = (al + ar) // 2
    left = cum[amid]
    right = cum[b] - cum[amid]
    if left > right:
        ar = amid
    else:
        al = amid
    return ar


def func_15da570d60e344b997a020076cdf82dd(vsota, cum, b, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    return rem


def func_1cd4a7f74acd420494709fcbcfd7b065(vsota, cum, b, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    return al


def func_f2db81a6a6bb4227bffcb9a56a5b2d71(b):
    al = 0
    ar = b
    return al


def func_47501cdae7d34d3a9bfa47a8ce22e9ee(b):
    al = 0
    ar = b
    return ar


def func_a72d96056dd84545a5b903150c3e0ebe(cum, b):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    return al


def func_f5013bbc8df04672b52f47f620d0b9fa(cum, b):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    return left


def func_50013e4f2b484aceaed7ea7385722584(cum, b):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    return amid


def func_f493f3cb37474b128635bbb9f1477314(cum, b):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    return right


def func_6113c133c85443f59af3e5121749ee30(cum, b):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    return ar


def func_62b3513891cc447f88cd44f3e27fc1ee(s, cum, b, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    return right


def func_4b1548a6488249e9ba40dfae3e302bad(s, cum, b, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    return s


def func_5115fdf84d9a4a69b77a81dc349e784b(s, cum, b, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    return al


def func_120bf244f89e41d9ab7493ff05926cbc(s, cum, b, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    return amid


def func_67c1179c8e544f0fb3e140a9869a8b0a(s, cum, b, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    return left


def func_8ff03a8e5077497bbe76bde6b7e82095(s, cum, b, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    return ar


def func_d708a0becec44cd79d52e86ecb718870(s, cum, al, b, n):
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    return s


def func_e599fddf746044b3a708798ee43d15b5(vsota, s, p):
    s.sort()
    p = (s[0] + s[1]) / vsota
    return p


def func_378f057af3c7477eb6074a442ad2f0bb(vsota, s, p):
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return p


def func_22b5edebfed34388b50dc8f795eed272(vsota, s, p):
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return best


def func_c3f21485ff654940a3e153744bd5fefc(s, cum, ar, b, p, n):
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return s


def func_1fc125baeee343e0b82dfb53afb3e6a3(s, cum, ar, b, p, n):
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return best


def func_5610c77d459f46e7906a9deed81b7e9b(s, cum, ar, b, n):
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return s


def func_4ce92cb7d330420d966c06c8f6b5350a(vsota, s, p):
    s.sort()
    p = (s[0] + s[1]) / vsota
    return p


def func_5adbee6badf448c0a087a77aeec7997a(vsota, s, p):
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return p


def func_b4e1bd36610b4eefb7a3e1f2f82b513a(vsota, s, p):
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return best


def func_0a8fcc166bb04210b46db2f73cf70596(vsota, cum, b, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    return rem


def func_2b0c152a009a4655a2da10197fe560ca(vsota, cum, b, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    return ar


def func_62c78243c0704d67be90d4ee6bbbad97(vsota, cum, b, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    return al


def func_416ceb9c18e74625a45d645bfbca37b8(cum, b):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    return ar


def func_b10aa2dc8e164c58939b98d21cb6f6af(cum, b):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    return amid


def func_fa25c79888944ddf920da89f544f8bad(cum, b):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    return left


def func_64bc4a1e98d14a63ba77a4c3b4dcdb98(cum, b):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    return al


def func_3fabea1491ef43f5afb69db1357b3b66(cum, b):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    return right


def func_c584c2bc39d64bacaef4e09f4a94e3bb(s, cum, b, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    return ar


def func_52fa32389756454bbbb63c0614cc1578(s, cum, b, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    return amid


def func_6c9db2e6a8ea432da36b2387b22f5b6b(s, cum, b, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    return left


def func_d9af8ec9b2da476493c9c78c7180b79b(s, cum, b, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    return right


def func_92342efe662940ddbf295031682d7dda(s, cum, b, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    return al


def func_8ff35685ac2c4676bd2bc4544d5c5b53(s, cum, b, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    return s


def func_715658bd0cb549d9a3f2aaf71acd3144(s, cum, b, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    return s


def func_6b138d2a733c484ba8d6324a47ec6797(s, cum, b, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    return left


def func_4af1f2bd458d420999b25940bc0ea69c(s, cum, b, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    return ar


def func_207f5e3017f744819b1e1a2f6c09dc03(s, cum, b, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    return amid


def func_182a8afcec51468c833b6fab79cadb19(s, cum, b, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    return right


def func_cb280208cbe9442b9db42a73f99f5438(s, cum, b, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    return al


def func_55a12b490ae24ddda9518ed612dabee5(vsota, s, cum, al, b, p, n):
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return s


def func_28f9937bc37f48ec9ef630d305a1f46a(vsota, s, cum, al, b, p, n):
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return p


def func_1c3f9c53836a404497fd19deb6e6ade6(vsota, s, p):
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return p


def func_b2b29617f6e54becb6362632613f419e(vsota, s, p):
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return best


def func_4d425522d868448294b6d44de49382e4(vsota, s, cum, ar, b, p, n):
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return p


def func_ea43a5b874244cf9a93b60c0edbbf8f1(vsota, s, cum, ar, b, p, n):
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return s


def func_805de542e7c54250a136f8e8456c5060(vsota, s, cum, ar, b, p, n):
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return best


def func_ca04c13dfaa04acd9c639dfdb7f5db8f(s, cum, ar, b, p, n):
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return s


def func_e483232c797f45d2815e1cb0fda8b88b(s, cum, ar, b, p, n):
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return best


def func_febd6d26cf184f00a5a73b2673710fff(vsota, s, cum, ar, b, p, n):
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return s


def func_307ffbb0ec06465ea2d052c1d5736801(vsota, s, cum, ar, b, p, n):
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return p


def func_58c765c44b804436bf8614cef8b99a7e(vsota, s, p):
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return best


def func_9ce8fbc4d87b42049ae4afbcbb4af04f(vsota, s, p):
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return p


def func_535cf2767e3f443b892d9d2d1fa55389(vsota, cum, b, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    return ar


def func_538477d687f14906a3c785e4dcf7915e(vsota, cum, b, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    return left


def func_262333ff1ffb4f2c816e12d54ec99f0a(vsota, cum, b, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    return right


def func_b9664bbfa0aa49abbe4aa874a609f5e7(vsota, cum, b, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    return amid


def func_e364e1aad6424a89a45b69a8a22ce0c8(vsota, cum, b, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    return al


def func_fb7e3f128fe44aed93ed764974a6d9b6(vsota, cum, b, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    return rem


def func_fcd65948a50c4fa3ab294a9237172cd4(s, cum, b, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    return amid


def func_e2da72ec51d640648f401c4bfcda296e(s, cum, b, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    return left


def func_54ae434b2d2d457ebc2ce310e21a3f12(s, cum, b, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    return ar


def func_d23debd6797e49c4922935ce4d7779a8(s, cum, b, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    return s


def func_fea698bf101d49dd8ff396b2839e5c55(s, cum, b, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    return right


def func_268a5f466f2a4f36ab767412c5fb70ca(s, cum, b, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    return al


def func_d3039af70ed14a359a1738a328ff2c44(s, cum, b, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    return right


def func_61a3e42191734991a454042ca2ffb267(s, cum, b, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    return s


def func_53d580f6fa164617ad985803db21fcfa(s, cum, b, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    return left


def func_812aa4709e4241fbae7b0fcd1c908e88(s, cum, b, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    return al


def func_8dfdba3ab30c48488b08868a061db22e(s, cum, b, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    return ar


def func_01c52dfb08c54fcd9491cd32b5f3f4f6(s, cum, b, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    return amid


def func_59ec8afc6cbc4d4096123f1e3dafd920(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return p


def func_04e569aee58040e38359df688af93409(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return ar


def func_30545de20ce14a409b69782d0f4b6a0b(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return left


def func_db7c1d88b49446e69a0b1d15dba93268(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return s


def func_87839d5537dc4bd5adb2d56166b0a9d5(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return right


def func_59ae3ca45c5340d3948fa43bfea91f83(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return amid


def func_87e27f22265b4acfbf538c5994a2384c(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return al


def func_8beb4563966242aaba3d61051c05550e(vsota, s, cum, al, b, p, n):
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return s


def func_f3ece5c5cd6c461b961fe28e8df711f5(vsota, s, cum, al, b, p, n):
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return best


def func_e11bcbf73ee24c729a3b60f6a9899dc3(vsota, s, cum, al, b, p, n):
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return p


def func_a0b2a79b43124a29be14636d58395fa8(vsota, s, cum, ar, b, p, n):
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return s


def func_8502e54c64714600b7da5b1f5e112be0(vsota, s, cum, ar, b, p, n):
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return p


def func_c1be09dcc051423dad53ee5a483eb54c(vsota, s, cum, ar, b, p, n):
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return best


def func_b1086f2ee0184945a641f2b079a056b7(vsota, s, cum, ar, b, p, n):
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return best


def func_ccc204355bc449a7bc39318afc6e6b75(vsota, s, cum, ar, b, p, n):
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return s


def func_498c3d76911240c5bd3e15ac70b5e9e7(vsota, s, cum, ar, b, p, n):
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return p


def func_61075cef8b6c4f13a0e9177626e48f79(vsota, s, cum, ar, b, p, n):
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return p


def func_3307473703de463ea1d409dd7697fb1b(vsota, s, cum, ar, b, p, n):
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return s


def func_bf541e42e1654c03b84ad3ef3bb0b4f1(vsota, s, cum, ar, b, p, n):
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return best


def func_df789ba0ddd845df806a7badffd8f3e7(vsota, s, cum, ar, b, p, n):
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return best


def func_c4252f21333747a981fd0d7ebbabfe65(vsota, s, cum, ar, b, p, n):
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return s


def func_9386587a6d3a496288d1a2c2ca425b5f(vsota, s, cum, ar, b, p, n):
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return p


def func_6bace7b669f444d1bd3d36bef569aa0a(vsota, s, cum, b, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    return s


def func_cb272c1ef3a94239beeea8fbfa4f7504(vsota, s, cum, b, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    return amid


def func_e3259b6bdac348bb9fbe86204be5ecad(vsota, s, cum, b, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    return rem


def func_bd875015e6224d3b890b731d74bf9e2d(vsota, s, cum, b, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    return right


def func_01b85ffbb17a45c89a2916b5d0512603(vsota, s, cum, b, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    return ar


def func_ede3306e6f2f4458a4ec9f4ac60035e6(vsota, s, cum, b, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    return left


def func_b90cf9bfef10445c9993534c8ff75728(vsota, s, cum, b, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    return al


def func_65a0fbd5131a402a98bcde406342eeab(s, cum, b, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    return s


def func_2a09d4e696d844ebaac1cdffcdfab8a7(s, cum, b, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    return left


def func_a361a7fb84d44a17a45fd8993edf21e0(s, cum, b, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    return right


def func_88bb8d366a674c8983986b4dbc7e025e(s, cum, b, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    return ar


def func_919a45d8558a44ceae99b7c285a4c76f(s, cum, b, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    return amid


def func_a530fb5fa2604b909c83b26a0cadeb75(s, cum, b, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    return al


def func_d77873fd855f48b6a8ea9335e3ce8152(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return al


def func_e0e7aeb3f30043b0bbdf5ba6405e9867(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return right


def func_a3e4e08f0c9545d9a959d96cb3e31cb0(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return s


def func_4ba46be9fb5f4850bc5b4d8bb77ca36c(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return p


def func_93f16441eb7248dc9efc79580331f01e(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return ar


def func_cfb4be0f0ec841c89f0a9bd04333703b(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return amid


def func_ed792c5e5d9144f2a757f47eb5443f4e(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return left


def func_7ecef8634c4443269276e9e8db793e0c(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return al


def func_32a2d8a356624e09b8dcde1d3846776b(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return p


def func_f6655af5d60c404caaeba68eaae9b5ef(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return amid


def func_a311ecb00f7943a1845e7903503fcb1a(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return best


def func_5604a379b5fa4e878d68c078bf8e36cc(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return right


def func_6487b50ad02244b68aa52dca3941131c(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return s


def func_2b7090153f4a4881af01ec60025d75a3(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return left


def func_e1cf39ab5ce54ad583e65ce1c342bc50(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return ar


def func_9a1c1722af3b41b68a11191c922788ff(vsota, s, cum, ar, al, b, p, n):
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return s


def func_14cd7994503647a1b4883671c4fe6400(vsota, s, cum, ar, al, b, p, n):
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return best


def func_97ae317be5cc4428950806848f01efc7(vsota, s, cum, ar, al, b, p, n):
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return p


def func_43bfe0b0a5bf4519a0d8e94223ea6b9d(vsota, s, cum, ar, b, p, n):
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return best


def func_359e9843d3b24f2d879b44989df8609d(vsota, s, cum, ar, b, p, n):
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return p


def func_f94bc630c37e41188da56a6f6d757385(vsota, s, cum, ar, b, p, n):
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return s


def func_9f5fb5caec0a44158f222efd133050ef(vsota, s, cum, ar, b, p, n):
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return p


def func_0993bbad1802456a93f7a4f2a84b215e(vsota, s, cum, ar, b, p, n):
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return best


def func_8da2d74b14fd4697995c0768f4054888(vsota, s, cum, ar, b, p, n):
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return s


def func_e5d00bd19901473fa20db8f2402e924f(vsota, s, cum, ar, b, p, n):
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return s


def func_e4eb3f9599cd4fbcb8c7e6e627bd72a9(vsota, s, cum, ar, b, p, n):
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return best


def func_aec5c083995243acabae57e632a65a97(vsota, s, cum, ar, b, p, n):
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return p


def func_e9482789bf29497a99ddd954df22e0f3(vsota, s, cum, b, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    return s


def func_a2faf4b1f3234edcb40e8c82aab7264b(vsota, s, cum, b, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    return amid


def func_a8acf9f8062c492092cb7f2a10dc3b28(vsota, s, cum, b, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    return right


def func_38697314770b4a37a6a3a939299b792d(vsota, s, cum, b, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    return rem


def func_0652969ba3ef485099447dc180fc9bca(vsota, s, cum, b, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    return ar


def func_aa5946ef2b2d4d5d9c7fb0bba269909a(vsota, s, cum, b, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    return al


def func_d951ebe498814d1c863d6c659bfd6ce2(vsota, s, cum, b, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    return left


def func_9170acc4fa9a48928cfddab5a039ba8c(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return s


def func_362945995a094d98be3e4bdf43ffdbde(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return p


def func_88451ae485ce4ef5ac0eaae0c17c0162(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return al


def func_1b26807116354ec0a9d325da58ecd232(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return left


def func_255f8d43509b419e96a03d0c54dc64de(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return ar


def func_8fb124c2d6a84fb4b6b13a78c92d96e8(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return right


def func_3ea71417667944fd8d3f8345f2eb4641(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return amid


def func_22fbaa42163945639fd71b13d2fe0642(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return al


def func_7d95c9f8ac1a4102bade97182171329b(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return ar


def func_0a0e1b6c927948bcb8d54aa19c30df02(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return s


def func_bf9bff11066a462ebaa5301e03303c86(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return left


def func_6e288e5ef98f47c685ce8db7b0f99f8e(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return p


def func_7a2891bdc6c14519bb771a261c5a7d89(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return right


def func_ecd6ec4c74064c4e9f12c52ec51e392f(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return amid


def func_a1530ef6d01144b7b8988858a83f271b(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return best


def func_9973ee79f4dd403eaf038acb5fbaa3cf(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return amid


def func_8a66d41490504dd2b41ebe7bcf02a90e(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return ar


def func_50ddf89e730644d08b595ff15dc112ef(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return best


def func_b8d959366275418e9d0ce71ac62d75d0(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return al


def func_ad739c7b1f634a068252401b7f022e6f(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return s


def func_1e9d5dafb0d34c5bb61cfbe17bc98470(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return right


def func_5ea77cd61f1f49888137c4cb3f9fe65f(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return left


def func_d218712f029849be800ac3eda3315ad9(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return p


def func_94a7de48fbdc473ab8228aff19337229(vsota, s, cum, ar, al, b, p, n):
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return s


def func_7ca7a6f305124064892897f612689a95(vsota, s, cum, ar, al, b, p, n):
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return p


def func_5716f4f9288d4ef2beac3029fe442df8(vsota, s, cum, ar, al, b, p, n):
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return best


def func_bc45fa924eb247c492416148059179b5(vsota, s, cum, ar, b, p, n):
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return best


def func_9f79ca79a611415ab6d51c45b86d7cd3(vsota, s, cum, ar, b, p, n):
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return p


def func_32d8d595d86a4999a51c189147fa69b1(vsota, s, cum, ar, b, p, n):
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return s


def func_206d4423904045aaa2caf90570ac006c(vsota, s, cum, ar, b, p, n):
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return best


def func_5ded8d05671647b3936d173b8be8c625(vsota, s, cum, ar, b, p, n):
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return p


def func_33031adcaa7c408f9993d8f1d3378b7c(vsota, s, cum, ar, b, p, n):
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return s


def func_8bcf9fa3926647e3be71f656dd84bff4(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return p


def func_8606815b134e468a833e9beff8f025a7(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return right


def func_eabab10945dc48a5aceb212c38ff7990(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return al


def func_5cc7ec9e39a1465e9dc35bc8afa28f04(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return s


def func_2384072ee28a4d5dad31c9f5a121e4b1(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return rem


def func_4cec2538baab49ce867e36b74e6947e5(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return amid


def func_45777745748c40bc968130fa788355d5(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return ar


def func_e2b8041d7c57449ea4d5677291773e4c(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return left


def func_ebaa7d664cc246c1b0ef8ebc7eee97cf(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return right


def func_b20ca598638e4ab78c733240841bde72(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return ar


def func_69883f0c46114095a2243c4f086e5d3b(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return p


def func_002656a3213e4f33800a4af377353824(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return al


def func_f821991fc57d40f6b06a49c551be2ec5(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return amid


def func_de9a3bb50bc141c490bb6213860d6e5a(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return left


def func_620d7c1533af42a49e6c8d6d28095e24(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return s


def func_670d535c08b74cac8c818a06eddc1d62(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return best


def func_929ae02a44be443791d564c65395a889(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return ar


def func_a494fc2203cf4d2aaa9c8dcd071a5fec(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return amid


def func_c9d1d8f728b44c698b4985b1d8c8596a(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return right


def func_471b7adf96374afbbfa9f9ded6754749(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return p


def func_52d08f0d933a4e5385075b8e109234a4(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return best


def func_97d44bd91c2b4e2fa5ebbd076acd8268(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return left


def func_15710aca4c58460e81e9982be7d33171(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return s


def func_1ff48d9bd1bd40d3a22058744776afc4(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return al


def func_bde943996d594e1ea9b914b62e6465c7(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return best


def func_bc1213b333af4e119ae1580980feec86(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return amid


def func_d470d7b7b5024d41a04793742f7d03d3(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return ar


def func_70f56a1842784811877cabbc7c3c97fe(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return s


def func_9e6203d6ed5e47d385ebbd4d2e52f3fd(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return al


def func_90c69f2b76b54784a2892c3708b57a32(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return left


def func_96fe1bbbed034cbf808405ced16488cb(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return p


def func_ed4318dfd2a5494d94ae23a3e86c4548(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return right


def func_21157f7ced314fde9e19b5cd24ecb8f8(vsota, s, cum, ar, al, b, p, n):
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return p


def func_cd364b77c47b4de7a56a396ed135e889(vsota, s, cum, ar, al, b, p, n):
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return s


def func_cadfdf5b6ae446b5aee9c8c85ae88eb3(vsota, s, cum, ar, al, b, p, n):
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return best


def func_6cdf4629da6f4daa81f5ebb37a219b55(vsota, s, cum, ar, b, p, n):
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return s


def func_dc8f8302398f4a33bc29828e70fa09e3(vsota, s, cum, ar, b, p, n):
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return p


def func_1bf3d602b98c48398bb82c563da72336(vsota, s, cum, ar, b, p, n):
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return best


def func_fbb57b90534147309706e0d2573d5000(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return ar


def func_b49190d3b5e144a4901527dd0c722ecf(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return p


def func_8ddee00f37cb4f10bc03dec70349a35c(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return s


def func_4e7746abe28b4733a4743ba4a85df21c(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return amid


def func_18e740de90484d28bdf0102b8dfb6370(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return rem


def func_7c7cf0e09f114ac5b674632cb4d4d49b(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return left


def func_1598d6a2c71a4ecbbdb35693ee2e1321(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return best


def func_2a522c88a886442d88f82fc7b55b8026(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return right


def func_b3ceb9525acc4622a1310f1e6511fa38(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return al


def func_549b3a9c4a594e6f9e6861d1810d34e2(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return right


def func_fa76ee00e42d49bba1fd0027af10a93a(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return best


def func_590db4e7f6e94bd38804cf0bcd89f7b1(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return s


def func_71b53999f1b04f5e8990143091454a08(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return ar


def func_15c0702f96a4464ea68158ac261ea598(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return left


def func_192fbe0ee4224e52b1bdd7fdc021e77b(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return al


def func_7db2acd6cb3a4b5c9a1f8a10b71edd61(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return p


def func_7ec01fca8d9644cf919cf718125213a4(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return amid


def func_13190dcf274444698c65f1060fdb3ff3(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return amid


def func_a8ad2687325c494f96fec92cb32d0693(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return ar


def func_02dc2ea480504557941de572cf347a90(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return p


def func_403e0752609e499a95f16cbafe48222a(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return al


def func_01b1d58e38034dd2a1f619672f0e8f3a(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return s


def func_b4fabecdd569476aba4b209ac5046f1d(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return right


def func_8a4c7dee1ea44dada20c06654bed3578(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return left


def func_a984c0e8852c438bb45c9e65057b4f19(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return best


def func_07830965dcff4e149d091bd210d53b8c(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return left


def func_f4ed73a0321b4c0ba150eb41643f5a08(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return amid


def func_91f9095207394f138b6faa8f8e676620(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return right


def func_172e5b92aa8743f7bfbdae09bbba0471(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return ar


def func_c44a4a427859410fb6e318e4b3b773a5(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return best


def func_4414a74186764538b52014f9a9888a1d(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return p


def func_9ff12aaefcf8430f8af31a16b0bf50b4(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return al


def func_7f1cab31ffe74046879bf4e12319983a(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return s


def func_3c43a6dbd53d4bbdb03c9a1989106d00(vsota, s, cum, ar, al, b, p, n):
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return best


def func_e9b4ddf457334d9b9b97f32d3c554ebd(vsota, s, cum, ar, al, b, p, n):
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return s


def func_38c47e80cf5643749a9ff33ec082c57b(vsota, s, cum, ar, al, b, p, n):
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return p


def func_0320a28792304fe59973fb00f0bb3c9d(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return rem


def func_d3caad791b944f228c46ae4eb5f6ad67(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return best


def func_fb5a9abf51484d3aa566f8bc211f2ba6(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return al


def func_442518fdaf9c40f1b51ae115aeb1b47f(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return amid


def func_7907e6f608ec49589a6310455572b009(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return ar


def func_4393e626191544a1abd2a02377d67aae(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return right


def func_646ce98f9f57433facc2efbcabfdf604(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return p


def func_d8178afb754e41a1aadf97b457546f81(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return s


def func_46beeebf3aa340309f70f9b4365ec5c5(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    return left


def func_77a64ce9cbf3405883373b120d685589(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return amid


def func_42ecfcf2e15f44bab060e135af948513(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return al


def func_fe5254dcbd724f229f36bd8c1b37babe(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return p


def func_77ecd64ee7634c36b0d7acdcb4525a98(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return ar


def func_4b2e793a0dd7403ba9180d7d6a8e5170(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return best


def func_2b472f4a270d4f2387fa5a2cbc8c5eca(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return right


def func_bf5c717dcf9a40eeafe64b80b5c461ef(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return left


def func_8c1eafe080e8444bacef49646c23fd31(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return s


def func_7bdc19c2a48f4bf98272be8d4b3065e0(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return al


def func_5dd2da837d7c43c8b489a5605ff52a26(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return right


def func_3538d1dbd98e4e948a6a734175f963ab(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return p


def func_fceadc1946f446c995f31c10f152dc77(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return left


def func_c8a5372df0a842aca2cac31460bb05e9(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return best


def func_334de7864c1c4c9fb9ae8e3b1da1af81(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return amid


def func_3914b00ebf7a486290577701689c6ae4(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return s


def func_87ef9d3d02d44d1ea8b3b7b07fedbed5(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return ar


def func_399646ccf8824f538e900eab6cda6a91(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return left


def func_c5d544d7991c417599b345e055f186c6(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return p


def func_df4f064f41a745a9826b55445b6b0439(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return ar


def func_6d5c996dfcbe4bb1a5372b9c179f1a19(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return right


def func_7c0ffe22cd1c4849ab2af78fd419d03a(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return al


def func_ca2670d6dd6749f6b8c70f696fd3599b(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return best


def func_afeb9050a570405582242a0c959ee39a(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return s


def func_7b969bfa94104c20926ec9d0159ad005(vsota, s, cum, b, p, n):
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return amid


def func_962bd401c9644c03bde805278fd06a69(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return ar


def func_b3ded44431904aeca4a730534971d74a(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return p


def func_c12ab90f0973414b99d40532338886b4(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return best


def func_6f2968686d2b4ce28ee3bd7abef95b87(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return left


def func_922a71472a0d43a1a8b418410329815b(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return amid


def func_632f0a5308584ec4be693dad11fbb5d5(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return rem


def func_9afa8d8d49184e03a995929cbcd9c975(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return s


def func_ccfbef225c2248d298bf62f80c2ef221(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return right


def func_fb58aded86f648f6b5ddec19be949c42(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    return al


def func_d851d33488364f72a4a04d35bb5a75cc(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return s


def func_14499f27799d439ea6a3bacbcefda211(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return right


def func_07d1c0b7d7b54a48831f5f5c4c67435d(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return best


def func_63a6fe694ea4426db483016b2b4fd21b(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return left


def func_3d09c4e02eaf47ebbef9eeb824efed79(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return al


def func_507da12dc794414fbe6522962dbe0ae1(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return p


def func_38b1302020b84397b85e2ca5cf69bc5c(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return amid


def func_a0f32b2fb77a4e15b9c463c13ea945f1(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return ar


def func_14984d1c66834b6f88dc700598d4049a(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return p


def func_455564920e0d4dab9f87c0737f787479(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return left


def func_9214a53e14c84589b2f4aefa003982fe(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return best


def func_1c7dbff8f3e043deb25506c0a8b3cf59(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return s


def func_931555f1b5fe465a8ef64e66795bcf70(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return amid


def func_b70bd0cee5d94124a567c3191b00b370(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return al


def func_4938cb1854244cb5821117c7b3fec188(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return right


def func_552425580cc64e9582f703363e8a623a(vsota, s, cum, b, p, n):
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return ar


def func_ed281b635cbf40b2a96fef354e2326e8(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return s


def func_d2ec22b1dcd84154bb7fda9379ebbec1(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return left


def func_cddcb6e5a5374e208f1e6ee1c20c6b73(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return best


def func_cea8cd4f314d4dea802e41599d76d297(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return al


def func_24fb9e2842e94d4cbdc900ecb7aa963b(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return p


def func_a87863af67204998bb9482cbdf96c4cc(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return ar


def func_7855a7881bd64d3fa006241f6643d343(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return amid


def func_e3b761f98b154604be075d6e3a010f01(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return right


def func_d0aaa5cc0f7d4d40bb137d3719a71712(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    return rem


def func_9ddce7db0a874af0bebb6d6841235ff9(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return right


def func_3d92191cbc5c4c65a29164726ad73dd4(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return left


def func_44b69e46a6214807a5820443c3dcf316(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return al


def func_646bf0a9ddf9492f949a141cc1163ce7(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return s


def func_3ed52c09080e4b38ac93bc23524582ef(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return amid


def func_3ac03e5be8d94d9e982be540a183e99e(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return ar


def func_96de37e5bfdf4b5bbc704f0c55bd4e60(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return p


def func_ea2d85eb5ed049e0b117502b04da2a69(vsota, s, cum, b, p, n):
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return best


def func_0d72093dc72245b9ab79438e9ed05864(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return p


def func_828504af1f6d4f0b95ad42f3714ff842(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return s


def func_f52a824d8d7d4044aac67ee3c1ff3b4c(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return ar


def func_8f91055ab55b42619cde2daefa724df0(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return amid


def func_1d0af9e4f8d9479fbf94b07b882fa7a5(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return al


def func_09ecabe1fa5b4858a42d495c5822c921(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return best


def func_d27c24d16f194c1a8b98d0d9b3ea84c9(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return rem


def func_d1bd49c27aff497985958be69c16e396(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return right


def func_39a4f8fc4af143e389b61ba2cb6daf61(vsota, s, cum, b, p, n):
    rem = vsota - (cum[n] - cum[b])
    al = 0
    ar = b
    while al + 1 < ar:
        amid = (al + ar) // 2
        left = cum[amid]
        right = cum[b] - cum[amid]
        if left > right:
            ar = amid
        else:
            al = amid
    s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
    s.sort()
    p = (s[0] + s[1]) / vsota
    best = max(best, p)
    return left


def func_5a1d7d9e50594971b43b0d1613f75ab2(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    return l


def func_3ff90242573f42f7961a7171e7ff90fc(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    return i


def func_29cd2d7e7b874493984c77518a44467e(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    return vsota


def func_0624f3dd50434e2cb497ca1382445c24(l):
    vsota = sum(l)
    cum = [0]
    return cum


def func_bd0ddcb706654b92a5ea8f4e5bc047fc(l):
    vsota = sum(l)
    cum = [0]
    return vsota


def func_4a321c77087c4f28ba611330523d875b(l):
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    return cum


def func_66487c945fa14da3989a2fd33276a580(l):
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    return x


def func_560be556345f4c1f95e0d49b38de689c(cum, l):
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    return best


def func_6beeb6279a5b4bba931a9ce945d37685(cum, l):
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    return x


def func_752d606d26234a30baef351aa49c1600(vsota, s, cum, p, n):
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return best


def func_46309d3bdcd9470ba98995fca301be00(vsota, s, cum, p, n):
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return amid


def func_5ed8723e583345258856782fd7da1978(vsota, s, cum, p, n):
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return rem


def func_5d63b4fb7d664cc49142e0998f170afd(vsota, s, cum, p, n):
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return ar


def func_f8f0e6cb0d6b4bbfaea9cedad7d1bda7(vsota, s, cum, p, n):
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return al


def func_f7e4d5602b3741998613ede464f28ab5(vsota, s, cum, p, n):
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return p


def func_613581661f2d4340b8de4437d31481ea(vsota, s, cum, p, n):
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return right


def func_d0915ef86c984e4090bf793b45f9acd1(vsota, s, cum, p, n):
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return left


def func_75c4851d6ef24739927f324392d652ec(vsota, s, cum, p, n):
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return b


def func_1e2d6a871baf4c2ea6ced5cdc248666b(vsota, s, cum, p, n):
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return s


def func_ae0914f069f142c7b2b03298c239f783(vsota, s, cum, p, n):
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return best


def func_563511baef8548b2bc009687b233dab0(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    return l


def func_887746103a7e4ed7a31065bacb287a6b(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    return cum


def func_5bf961990e2641ada95df6e3c3623b07(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    return i


def func_a96fb315bf2541e5b21f16714c5ee556(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    return vsota


def func_684b933c52eb404b88eee1fdf8486a71(l):
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    return x


def func_64dbb86ea41b48c890fd0574ae1446f1(l):
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    return vsota


def func_4e27dddb3cca4a19b8eb49332bf6eeb9(l):
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    return cum


def func_98844474a18b485fb6e4fd1189ae0848(l):
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    return cum


def func_8e0b1bd0a70949ffb3cdb6d3804a49bc(l):
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    return best


def func_1533683bfba64c4ebdb3a89f9b818002(l):
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    return x


def func_f45f6912fe8844d28bb958444abd4adb(vsota, s, cum, p, l, n):
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return amid


def func_f524a4b3ef904760b9f5c51ffca9bd2d(vsota, s, cum, p, l, n):
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return right


def func_e3820101c8a3435a8844966b4c6d15af(vsota, s, cum, p, l, n):
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return b


def func_87284661e92546ea8778a91e60dda22f(vsota, s, cum, p, l, n):
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return x


def func_5e483f554af94a01a4fd3c7596764f86(vsota, s, cum, p, l, n):
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return s


def func_6b1d929c1d4c49428cc72c07f3c0805c(vsota, s, cum, p, l, n):
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return best


def func_9dc70f1eca4e4d16a0f246b5238b88ee(vsota, s, cum, p, l, n):
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return left


def func_7fb33953af6c4b16833eaa83d3e31d93(vsota, s, cum, p, l, n):
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return p


def func_04a10d693a68472fb689bac29aa7d5b8(vsota, s, cum, p, l, n):
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return rem


def func_32341e35154c4a1a9e47afa69eb296c4(vsota, s, cum, p, l, n):
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return al


def func_e1053851cd564eba965630e6aaddd864(vsota, s, cum, p, l, n):
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return ar


def func_b61f3ddd91754bb7b2f81ab401b5bcc8(vsota, s, cum, p, n):
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return best


def func_1c9ff699e56540f09d1f8b14f0f5b2fe(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    return l


def func_6380437294e14950867c975ec1bd65e8(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    return cum


def func_b59996bcec58446a8422bd281b371f95(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    return x


def func_07357508ba4a48528d852927f71e3857(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    return vsota


def func_df0c7d54f81a4e4bac81bd5d279339c5(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    return i


def func_6ca246f5f6c64f9a810c87cd47efe514(l):
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    return cum


def func_21f77a2097554e7a89f21e47cf37f796(l):
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    return vsota


def func_501c9d54cd14420481de1285888dd06d(l):
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    return x


def func_36c99378eb3046cab95f323bbd0b0d9f(l):
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    return best


def func_5fe6ec58c9a3457aa32d8bcc596e2caf(vsota, s, p, l, n):
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return al


def func_4f0f9f40aa9f4e209e9655de05a5a0ac(vsota, s, p, l, n):
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return s


def func_858315ae603b461fa80eac973e88ea4a(vsota, s, p, l, n):
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return ar


def func_2d009adb4f7c42f6ab0fc58226ebf8d4(vsota, s, p, l, n):
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return x


def func_edc7d6e9a50a4ac0ad03073b4a988617(vsota, s, p, l, n):
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return b


def func_8234eb8cdcc44e4c83a06d4bd0bb55db(vsota, s, p, l, n):
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return left


def func_2ff4926043114d9ea0f523c1090d3d47(vsota, s, p, l, n):
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return right


def func_eb26f37d503e4d908bd621b1725ba2a8(vsota, s, p, l, n):
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return amid


def func_17ae2312ec66476eb36abb126f7be05e(vsota, s, p, l, n):
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return best


def func_1da24c71949d44589b711a1f19f63d21(vsota, s, p, l, n):
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return p


def func_4c47c580d15d4c4997907ea46c029232(vsota, s, p, l, n):
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return rem


def func_a860946e9a67458ab47cbcda217a175d(vsota, s, p, l, n):
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return cum


def func_2bb384990d66440ab353ce1a0071c44b(vsota, s, cum, p, l, n):
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return best


def func_6e9b8ca81b7a46ef8b4885f229934f65(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    return cum


def func_0cf66f4d89354bbe8913856332912b42(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    return x


def func_f06ad2fcd44946cb88861e6387f71d62(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    return best


def func_684b93d1375a465f8a1213977c72f315(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    return vsota


def func_dc81d0657a7d46a683f062b677154e3b(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    return l


def func_0d037852158f4795b544cde8c7056985(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    return i


def func_84d225a5b42449a5a80ff935d36ffdd6(s, p, l, n):
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return amid


def func_9397bec11f1341f38eb269ad1da335e5(s, p, l, n):
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return b


def func_c96f57307551439da21c26a1683fe198(s, p, l, n):
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return right


def func_1d3b1342d13f42d6b9b901abdd0a7530(s, p, l, n):
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return vsota


def func_26575656ebf14862aa1839e9dda37c82(s, p, l, n):
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return ar


def func_1266ab18c1db474990deb208ed7f9a9c(s, p, l, n):
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return x


def func_02202c35bb6b40538d4bb960bc782654(s, p, l, n):
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return p


def func_aaa8d029cc3242f1b0409937dffc4896(s, p, l, n):
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return s


def func_792cf28b171a4726bf058f483d97a142(s, p, l, n):
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return rem


def func_737593e0dc0b40f78082cc9c9015d346(s, p, l, n):
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return left


def func_c9c455c7a5974a90be0871c8ccb83ae6(s, p, l, n):
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return al


def func_f85911c133084020b6586df2b835ef50(s, p, l, n):
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return cum


def func_3a89b16e862544a4841161072a1e0170(s, p, l, n):
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return best


def func_2c580d2b330e43ec8541e4bfaaab8be0(vsota, s, p, l, n):
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return best


def func_f337d088cd454430b6c8999e23b4b594(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return ar


def func_ac146c24394445eb9c0aa6864b9eda60(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return b


def func_8df637b61aad482d935f9900d42736da(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return right


def func_f3d3034e7ad040cf990b672b4cc9daf2(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return cum


def func_0aab367d05ef46b390e35c8884accce0(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return x


def func_211a1aaca4cc464a948e7eb4e80baa9a(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return rem


def func_756fd32fd67d444e8e2612ac70c7d8fa(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return al


def func_a055967bb6b4433db847ced1069154e3(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return best


def func_5a9c0c9ed38744f183f344262b3432a3(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return amid


def func_dc58a11994434084b00a1ee96606a8ac(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return s


def func_511de39f78054dca83eea08e84433180(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return i


def func_ce020307352b48219d259a4b96a7545f(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return p


def func_b2f81494903341e58d7c1006e6833bda(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return left


def func_f896245351e64ee69b87c46ea56272f1(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return vsota


def func_43933f774c194a439eeb302f07298b77(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return l


def func_e00277bf12a44fa5a8c73dce8346a802(s, p, l, n):
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return best


def func_e5c313ffdfcd45c89fb28993b5373cd0(q, s, r, p, n):
    l = [((i * p + q) % r + s) for i in range(n)]
    vsota = sum(l)
    cum = [0]
    for x in l:
        cum.append(cum[-1] + x)
    best = 0.0
    for b in range(n - 1, -1, -1):
        rem = vsota - (cum[n] - cum[b])
        al = 0
        ar = b
        while al + 1 < ar:
            amid = (al + ar) // 2
            left = cum[amid]
            right = cum[b] - cum[amid]
            if left > right:
                ar = amid
            else:
                al = amid
        s = [cum[al], cum[b] - cum[al], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
        s = [cum[ar], cum[b] - cum[ar], cum[n] - cum[b]]
        s.sort()
        p = (s[0] + s[1]) / vsota
        best = max(best, p)
    return best


def func_2754417876f34e4888131d1e4de4ab0f():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    t = int(infile.readline())
    return infile


def func_feeae1e307cf4d48844505f667b8e4f4():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    t = int(infile.readline())
    return t


def func_77b540ea10214a669af5607c8f3ed026(infile):
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    return q


def func_f8aaa9e4d3f34eff8f9a263dd8ebcf42(infile):
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    return s


def func_ad89a1d8f4ee48b48cf1e3be5f055b43(infile):
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    return n


def func_e684277e6bb4403197442599baf48644(infile):
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    return p


def func_432bfa5e35124dbe81e72a8bde323ad3(infile):
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    return r


def func_b9e64e96758649399a5fccbd8a17f12d(infile):
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    return t


def func_a90b8dfc7842451dbad28fba02ae7bef(infile):
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    return test_case


def func_8cfeb1066b6a4197ab79a36ef168ed4a(t, infile):
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    infile.close()
    return p


def func_b622543ba1bb4f919edd3f5fe922ab64(t, infile):
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    infile.close()
    return r


def func_695108182dab45ba905b344e2f5d57d4(t, infile):
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    infile.close()
    return s


def func_b322de7e33bc4db29f3a471ffd916521(t, infile):
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    infile.close()
    return n


def func_0598737997e84fae9046f073daac82cf(t, infile):
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    infile.close()
    return q


def func_5e014fa9c24f4ae8b4b05abeb90c2341(t, infile):
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    infile.close()
    return test_case


def func_cf71ee69a9b64638a6691741ed6ebd24():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    return p


def func_70dc737b8b5145b3b01154a6dfa3aa07():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    return test_case


def func_190fdd4ecbdd47baafd23722f95a5fe6():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    return infile


def func_34e3a905d6d04c769e8cf0ac707111e4():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    return r


def func_c290727c71df43a2a0ce026de3b58beb():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    return t


def func_564eef9ebdb04b159222d90e1012e5dd():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    return q


def func_8c3a0eec9e0e4b479fc6382277275a09():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    return s


def func_0b01a635b02246898a2423067da936ca():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    return n


def func_13e80f6d868e436fae5eec0f94b6434f(infile):
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    infile.close()
    return n


def func_77f5fd74c4ed45ad81f6faf26ae32ff9(infile):
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    infile.close()
    return r


def func_3c981cdf7cd5445d9158a49eaa8d463e(infile):
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    infile.close()
    return q


def func_c83f575793f044d583a314f1231997e2(infile):
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    infile.close()
    return test_case


def func_4d5e6cd9e6e04672b445eaf373b22132(infile):
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    infile.close()
    return s


def func_9d0a6484cf6d4fe09d0d42e352c0cd2f(infile):
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    infile.close()
    return p


def func_11b4851670a14ef5a1a33c042d64d0e7(infile):
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    infile.close()
    return t


def func_d479679646d2428491995dc5a62be8f6():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    infile.close()
    return r


def func_a42a0f84b50943fcb23b7df2318193bb():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    infile.close()
    return s


def func_25fc652dcd9642dea4e56e1d1e970b4f():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    infile.close()
    return q


def func_c5390140321c45c99bebce638377cde4():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    infile.close()
    return p


def func_3ec859608fda4033853cc5fd967ae4b1():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    infile.close()
    return test_case


def func_0972881919434aadb563e88cc2ccd898():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    infile.close()
    return n


def func_f39848f4299a42988543fc2dac21efd3():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    infile.close()
    return infile


def func_d169ce73cd164cd08dd3f68f80735eb6():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    t = int(infile.readline())
    for test_case in range(1, t + 1):
        n, p, q, r, s = map(int, infile.readline().strip().split())
        print 'Case #{0}: {1}'.format(test_case, solve(n, p, q, r, s))
    infile.close()
    return t

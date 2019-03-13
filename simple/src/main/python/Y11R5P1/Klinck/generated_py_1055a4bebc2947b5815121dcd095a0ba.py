import sys
sys.path.append('/home/george2/Raise/ProgramRepair/CodeSeer/projects/src/main/python')
from Y11R5P1.Klinck.A import *

def func_05167192b425404daf13a2969a0f20a4(s, w, part, a):
    dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
    x += dx
    return dx


def func_e6fe3f1f1a194be2ab06530f5e7fd4e4(s, w, part, a):
    dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
    x += dx
    return x


def func_8ab37f20c2a746b2a93814495087544a(dx, s, w):
    x += dx
    a += 2 * w * dx + s * dx * dx
    return x


def func_e743baf5d41f4b689e69fd72b16ca203(dx, s, w):
    x += dx
    a += 2 * w * dx + s * dx * dx
    return a


def func_e16a2df3eca043df828472b511aeab64(dx, cuts, s, x, w):
    a += 2 * w * dx + s * dx * dx
    cuts.append(x)
    return a


def func_f292f47e37da46cea88c2515d299ec8e(dx, cuts, s, x):
    cuts.append(x)
    w += s * dx
    return w


def func_22f6258ad91c4f61b68f73cfdbeb6fdf(dx, s):
    w += s * dx
    a = 0
    return w


def func_ab3d2f18cfae48bb95cd0fbfc84af354(dx, s):
    w += s * dx
    a = 0
    return a


def func_d6dc00a887f74cc1a49139413187e788(s, w, part):
    dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
    x += dx
    a += 2 * w * dx + s * dx * dx
    return x


def func_da243e796c5a45b4ab1445d03438691e(s, w, part):
    dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
    x += dx
    a += 2 * w * dx + s * dx * dx
    return dx


def func_0d44189c6e664beeb543aac32e44cfa1(s, w, part):
    dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
    x += dx
    a += 2 * w * dx + s * dx * dx
    return a


def func_ec6f253a40614abb9aabbd5b42c40fbf(dx, cuts, s, w):
    x += dx
    a += 2 * w * dx + s * dx * dx
    cuts.append(x)
    return a


def func_d43ab91ed81d474c9cb241c27eb8a13f(dx, cuts, s, w):
    x += dx
    a += 2 * w * dx + s * dx * dx
    cuts.append(x)
    return x


def func_fa49417346cf4fc6bf3feca3d5f4858b(dx, cuts, s, x):
    a += 2 * w * dx + s * dx * dx
    cuts.append(x)
    w += s * dx
    return a


def func_81b47f009e8d4375910625a83346e01e(dx, cuts, s, x):
    a += 2 * w * dx + s * dx * dx
    cuts.append(x)
    w += s * dx
    return w


def func_655e58ad68da4e90878917abfd9bf5dc(dx, cuts, s, x):
    cuts.append(x)
    w += s * dx
    a = 0
    return w


def func_bc80e77d815c401a899554650498a1a2(dx, cuts, s, x):
    cuts.append(x)
    w += s * dx
    a = 0
    return a


def func_55451917f2ca42d29a8f99a709e5c179(cuts, s, w, part):
    dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
    x += dx
    a += 2 * w * dx + s * dx * dx
    cuts.append(x)
    return x


def func_7fede071f0984ddb8cdbb8c3d570c2dc(cuts, s, w, part):
    dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
    x += dx
    a += 2 * w * dx + s * dx * dx
    cuts.append(x)
    return dx


def func_6a79c12408e64a9092a5f8f11db3098b(cuts, s, w, part):
    dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
    x += dx
    a += 2 * w * dx + s * dx * dx
    cuts.append(x)
    return a


def func_30bf576b55c14654b9768c0e9a88f71f(dx, cuts, s):
    x += dx
    a += 2 * w * dx + s * dx * dx
    cuts.append(x)
    w += s * dx
    return x


def func_0482116fe29f4ed99912e3066274e334(dx, cuts, s):
    x += dx
    a += 2 * w * dx + s * dx * dx
    cuts.append(x)
    w += s * dx
    return w


def func_904e7796de4a4c76aef285abee45b1ae(dx, cuts, s):
    x += dx
    a += 2 * w * dx + s * dx * dx
    cuts.append(x)
    w += s * dx
    return a


def func_291d7bf6636046e3a550cba649736786(dx, cuts, s, x):
    a += 2 * w * dx + s * dx * dx
    cuts.append(x)
    w += s * dx
    a = 0
    return w


def func_36e2ee250f83446dad7db64a55fd96fb(dx, cuts, s, x):
    a += 2 * w * dx + s * dx * dx
    cuts.append(x)
    w += s * dx
    a = 0
    return a


def func_d86c2f881fdf4507b4fee011d7f9a8c6(cuts, s, part):
    dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
    x += dx
    a += 2 * w * dx + s * dx * dx
    cuts.append(x)
    w += s * dx
    return x


def func_22e1ee092d1345249083bad7b46e2894(cuts, s, part):
    dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
    x += dx
    a += 2 * w * dx + s * dx * dx
    cuts.append(x)
    w += s * dx
    return w


def func_ec4486820d274bacaa2bf14f300877d4(cuts, s, part):
    dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
    x += dx
    a += 2 * w * dx + s * dx * dx
    cuts.append(x)
    w += s * dx
    return dx


def func_322398a527494e79bfedcc869b18e619(cuts, s, part):
    dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
    x += dx
    a += 2 * w * dx + s * dx * dx
    cuts.append(x)
    w += s * dx
    return a


def func_7da841aba03e456f8532f6c51981e477(dx, cuts, s):
    x += dx
    a += 2 * w * dx + s * dx * dx
    cuts.append(x)
    w += s * dx
    a = 0
    return a


def func_0a7879bb81a8417499530f2aa27d6b4d(dx, cuts, s):
    x += dx
    a += 2 * w * dx + s * dx * dx
    cuts.append(x)
    w += s * dx
    a = 0
    return w


def func_91435e03925b45d7a4f740905a09850e(dx, cuts, s):
    x += dx
    a += 2 * w * dx + s * dx * dx
    cuts.append(x)
    w += s * dx
    a = 0
    return x


def func_6fea6d8b201845908632459561694f1a(cuts, s, part):
    dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
    x += dx
    a += 2 * w * dx + s * dx * dx
    cuts.append(x)
    w += s * dx
    a = 0
    return a


def func_880c3b37e2034bd2a40f62f9c8ea0d51(cuts, s, part):
    dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
    x += dx
    a += 2 * w * dx + s * dx * dx
    cuts.append(x)
    w += s * dx
    a = 0
    return w


def func_ef1d0822d0dd4b8ba46fd3907927c4c4(cuts, s, part):
    dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
    x += dx
    a += 2 * w * dx + s * dx * dx
    cuts.append(x)
    w += s * dx
    a = 0
    return x


def func_9b0b02f0e320497eb80f7dc18e7a5880(cuts, s, part):
    dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
    x += dx
    a += 2 * w * dx + s * dx * dx
    cuts.append(x)
    w += s * dx
    a = 0
    return dx


def func_831cd25dc0ea4f44afc5880ba8390065(s, x, w, nx):
    dx = nx - x
    a += 2 * w * dx + s * dx * dx
    return a


def func_862d9a80e17743218bc1596d6e99350a(s, x, w, nx):
    dx = nx - x
    a += 2 * w * dx + s * dx * dx
    return dx


def func_509820c8c40745fc978667613ef3cbf3(dx, s, w, nx):
    a += 2 * w * dx + s * dx * dx
    x = nx
    return x


def func_245e37d9201b4438bcd3fcdb8d14a414(dx, s, w, nx):
    a += 2 * w * dx + s * dx * dx
    x = nx
    return a


def func_1a6d6fdc979f4c498002eeb4b5c1c158(dx, s, nx):
    x = nx
    w += s * dx
    return w


def func_651100218ba6403b82e34b76c90eaa78(dx, s, nx):
    x = nx
    w += s * dx
    return x


def func_9291c202541c456398c52f614c8c6c5d(dx, s, nx, nxL):
    w += s * dx
    if nx == nxL:
        iL += 1
    return w


def func_d3691a9ff0d5419489b03f1382fd6002(dx, s, nx, nxL):
    w += s * dx
    if nx == nxL:
        iL += 1
    return iL


def func_001b15acc807450c90cda8803e3be4d6(nx, nxU, nxL):
    if nx == nxL:
        iL += 1
    if nx == nxU:
        iU += 1
    return iU


def func_149e53146763406c98f7ec2894c4f17b(nx, nxU, nxL):
    if nx == nxL:
        iL += 1
    if nx == nxU:
        iU += 1
    return iL


def func_a6a9c6e6681d40079297ea0784389a3a(s, w, nx):
    dx = nx - x
    a += 2 * w * dx + s * dx * dx
    x = nx
    return dx


def func_e087955e3cb1427f925f59e75935116a(s, w, nx):
    dx = nx - x
    a += 2 * w * dx + s * dx * dx
    x = nx
    return x


def func_facd685633274e8f886c574a2fb26f02(s, w, nx):
    dx = nx - x
    a += 2 * w * dx + s * dx * dx
    x = nx
    return a


def func_23cf03d331954170beab89f9388b922a(dx, s, nx):
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    return x


def func_60b73c787d4742f4badf9e0b01692bf0(dx, s, nx):
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    return a


def func_6b648157b67745bab64d0f2288188186(dx, s, nx):
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    return w


def func_1bdcbbd08369422bacbf768433cd2494(dx, s, nx, nxL):
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    return iL


def func_8b78240618d24b8080d790c2c724408d(dx, s, nx, nxL):
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    return w


def func_ac941b4b8d0a475abea414e92628e7eb(dx, s, nx, nxL):
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    return x


def func_83730b8a0b644eec9a69cd2d4488ddce(dx, s, nx, nxU, nxL):
    w += s * dx
    if nx == nxL:
        iL += 1
    if nx == nxU:
        iU += 1
    return iU


def func_86f722bf9a4a49b1b9b73ecff0faee74(dx, s, nx, nxU, nxL):
    w += s * dx
    if nx == nxL:
        iL += 1
    if nx == nxU:
        iU += 1
    return iL


def func_08e1237d21d5438e9646a54610d315db(dx, s, nx, nxU, nxL):
    w += s * dx
    if nx == nxL:
        iL += 1
    if nx == nxU:
        iU += 1
    return w


def func_3db720c419ba4d309bbae8ca5d7cde87(s, nx):
    dx = nx - x
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    return dx


def func_07f202c6e4764f4f8356700a9a3fa551(s, nx):
    dx = nx - x
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    return a


def func_ee459e91a0814cb5b514b9a2fdaf7637(s, nx):
    dx = nx - x
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    return x


def func_a75f3df798ce4911928cceb34fd2d225(s, nx):
    dx = nx - x
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    return w


def func_b9138d3a6376461fac83865987068f5f(dx, s, nx, nxL):
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    return a


def func_481910dba3b44bf3a37c594e466b198b(dx, s, nx, nxL):
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    return w


def func_ad1e3a41c23d49f1b26c1f0d9c2fa268(dx, s, nx, nxL):
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    return x


def func_b976871a854f4ee2b9832ed2e75997df(dx, s, nx, nxL):
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    return iL


def func_1db14cde499a4849b576f4e1904f74d1(dx, s, nx, nxU, nxL):
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    if nx == nxU:
        iU += 1
    return iL


def func_b8d2f116271644a78369a0d34f9163f3(dx, s, nx, nxU, nxL):
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    if nx == nxU:
        iU += 1
    return iU


def func_16a5441b74354b74bbdc193a1445759f(dx, s, nx, nxU, nxL):
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    if nx == nxU:
        iU += 1
    return w


def func_ba2fc1b6fa774294b3de4129be80767b(dx, s, nx, nxU, nxL):
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    if nx == nxU:
        iU += 1
    return x


def func_097b25d4a9604f63b59f257925b16786(s, nx, nxL):
    dx = nx - x
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    return x


def func_edc38b0b9b4745eeb035757b491f4b02(s, nx, nxL):
    dx = nx - x
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    return iL


def func_9c2b20b06f2e490da49a92673318fff3(s, nx, nxL):
    dx = nx - x
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    return w


def func_38ff479074614bab85c99bb8dc07403c(s, nx, nxL):
    dx = nx - x
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    return a


def func_390f5f0c78d14e68adf182c354da9823(s, nx, nxL):
    dx = nx - x
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    return dx


def func_da5eb4d1d2874397a92c51db9201e52d(dx, s, nx, nxU, nxL):
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    if nx == nxU:
        iU += 1
    return a


def func_936ba88f593f49e1a1d9bc987a57c260(dx, s, nx, nxU, nxL):
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    if nx == nxU:
        iU += 1
    return w


def func_945b62ddb3934150ac5aefc32b9e7f63(dx, s, nx, nxU, nxL):
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    if nx == nxU:
        iU += 1
    return iU


def func_e51b6ad5c3a34a7694ec2c15d41d8775(dx, s, nx, nxU, nxL):
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    if nx == nxU:
        iU += 1
    return x


def func_f3b035d02711483fbf54fef405e42099(dx, s, nx, nxU, nxL):
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    if nx == nxU:
        iU += 1
    return iL


def func_a600b523889049aba2519a3f7e8d189e(s, nx, nxU, nxL):
    dx = nx - x
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    if nx == nxU:
        iU += 1
    return dx


def func_1c035c9f413140329959f5107ce9547f(s, nx, nxU, nxL):
    dx = nx - x
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    if nx == nxU:
        iU += 1
    return a


def func_cbdfc4dec6c34e868d00cc48ffc862c9(s, nx, nxU, nxL):
    dx = nx - x
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    if nx == nxU:
        iU += 1
    return iU


def func_81f76ffc8298404fb4a4267009bfd9d9(s, nx, nxU, nxL):
    dx = nx - x
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    if nx == nxU:
        iU += 1
    return w


def func_522d77885fa3490bafc254c37ca35dd6(s, nx, nxU, nxL):
    dx = nx - x
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    if nx == nxU:
        iU += 1
    return iL


def func_5f15200d51fb448ca2205c09dbe71af0(s, nx, nxU, nxL):
    dx = nx - x
    a += 2 * w * dx + s * dx * dx
    x = nx
    w += s * dx
    if nx == nxL:
        iL += 1
    if nx == nxU:
        iU += 1
    return x


def func_67dad84487bb4e3c8215bc0cb6886790(U, iL, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    return sU


def func_01726ad9e6ec4d1187f953634fc973b0(U, iL, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    return sL


def func_bde4874531c04f97ab994fc034ad01ad(U, sL, iU):
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    return sU


def func_6188b368e3d8457da7a7dd8c2302360e(U, sL, iU):
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    return s


def func_67c7da13b02f4b3592a2a891d027b303(sL, iL, sU, L):
    s = sU - sL
    nxL = L[iL + 1][0]
    return s


def func_013a0658cc674b42abd3c8be8ddeed9e(sL, iL, sU, L):
    s = sU - sL
    nxL = L[iL + 1][0]
    return nxL


def func_972a7412dc7847c3bcaabfdbd492801e(U, iL, iU, L):
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    return nxU


def func_0fbeddc71dfd45caaa879d0bd9aa3173(U, iL, iU, L):
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    return nxL


def func_e6c07da745244c3faf7f3a4e5b12c23f(U, iU, nxL):
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    return nx


def func_f4c3445d1cba440a9c3c0a4323e4c9b4(U, iU, nxL):
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    return nxU


def func_273076cadf4c44a3b3f581f163970cde(s, x, w, nxU, nxL):
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return na


def func_fe54d21b69f546cbbbdb63362f8f1664(s, x, w, nxU, nxL):
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return nx


def func_1ee301f6dd614979a5a930a80ee44a00(U, iL, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    return sU


def func_02d5e5f195d24fea821a3ac4547aab1d(U, iL, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    return sL


def func_cc459734be424c8089ca8b585cd1d45e(U, iL, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    return s


def func_0f163445b8d94bbaacce0d038233cb3d(U, sL, iL, iU, L):
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    return s


def func_cbfa9dfa339d4450ad798bceaa23d02c(U, sL, iL, iU, L):
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    return nxL


def func_98aa48510e9d4729a0660e8b3e2508e6(U, sL, iL, iU, L):
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    return sU


def func_619c01a594b043beba766e1a5a151832(U, sL, iL, sU, iU, L):
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    return s


def func_fa9e2ecf34b94dcea054974cf0657d67(U, sL, iL, sU, iU, L):
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    return nxU


def func_3a586103aeb84c0d8e2879f0cfe42e00(U, sL, iL, sU, iU, L):
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    return nxL


def func_23e8dcaf6a9d47d99fef36bacf4c490e(U, iL, iU, L):
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    return nx


def func_619bd51feaf641628b48eed44a0337d8(U, iL, iU, L):
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    return nxL


def func_305bfaedef3e441883b28f540d6da64e(U, iL, iU, L):
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    return nxU


def func_320af4cf455a4bc59fef584078fbb158(U, s, x, w, iU, nxL):
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return nx


def func_da67bca5b459443789fd315a4b6e1e55(U, s, x, w, iU, nxL):
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return na


def func_6fa344c72fa348e7badf3cc8cb978fd7(U, s, x, w, iU, nxL):
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return nxU


def func_48ea743ffa474dd68799c4fbf77d8364(U, iL, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    return s


def func_39eb16478b7a41d48e31846285820aaf(U, iL, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    return sU


def func_02e09436fdd7431284f4bfbd0ebef4c1(U, iL, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    return sL


def func_5bdcbf45ff5f485eaed8945d3aaa188d(U, iL, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    return nxL


def func_40bcdcb8aab34d578b6eaa4ba402f874(U, sL, iL, iU, L):
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    return sU


def func_848ed6147f8848a29daf47a9d08da52e(U, sL, iL, iU, L):
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    return nxL


def func_44a24c45707846ed9511ecc6ad4d6731(U, sL, iL, iU, L):
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    return s


def func_a46b9d079aea4a29978f3ca336e9887a(U, sL, iL, iU, L):
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    return nxU


def func_abf0d36bc23a4284823a4b744dbff54c(U, sL, iL, sU, iU, L):
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    return nxU


def func_97ab7f49d3ec456b9242d09cc920fbd7(U, sL, iL, sU, iU, L):
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    return s


def func_9b0247cdd7264178926618a5e8f4614d(U, sL, iL, sU, iU, L):
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    return nx


def func_bd90faabc9a94052ac80017f141ce5f8(U, sL, iL, sU, iU, L):
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    return nxL


def func_87c68b0366f74834b6b63923b0382094(U, iL, s, x, w, iU, L):
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return nx


def func_a2359673d7d74e16a2124cd3e484113a(U, iL, s, x, w, iU, L):
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return na


def func_f778230c8c834f37a2899ece9c101fe3(U, iL, s, x, w, iU, L):
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return nxL


def func_d68e3654e0fa4da98bbab153a7e86a0a(U, iL, s, x, w, iU, L):
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return nxU


def func_9fa26f46d08b471bb442a94e21831bbb(U, iL, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    return sL


def func_cb048b4653094b97b4679b7e3011e4cc(U, iL, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    return nxL


def func_48d647362ede40b2adf218b390d421aa(U, iL, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    return sU


def func_6f19fecae14c4bb9b6de2048274f097e(U, iL, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    return s


def func_1ba6d015134a479f86821bfdd195fb3b(U, iL, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    return nxU


def func_e6b2e6506f274ca089dee6ec61789a8b(U, sL, iL, iU, L):
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    return nxU


def func_9aa88d3a1d0840cbadc875590edb6103(U, sL, iL, iU, L):
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    return nx


def func_d3834a940fdf486197cdac0c9846e8cc(U, sL, iL, iU, L):
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    return sU


def func_7d3dfeaf5cab46bdb41530422c92abd2(U, sL, iL, iU, L):
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    return nxL


def func_c4a3847728794f45ac23d760d75f1d04(U, sL, iL, iU, L):
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    return s


def func_ff850f6eab3f4f858e5e9fb1b3d97286(U, sL, iL, x, w, sU, iU, L):
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return na


def func_f6b09fa80aca4e83a2882312c191c08c(U, sL, iL, x, w, sU, iU, L):
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return nxU


def func_cf876bc960784e918c691b542d44f0c3(U, sL, iL, x, w, sU, iU, L):
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return s


def func_c674361f2776473ba43375e5c952e4a2(U, sL, iL, x, w, sU, iU, L):
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return nxL


def func_59fe8bca6c02440c9def6d9d2ee4fe1c(U, sL, iL, x, w, sU, iU, L):
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return nx


def func_1ed0c64432754318b463b4f899b9cca6(U, iL, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    return sL


def func_5f05d26200e843789fa33b018cbbfcd7(U, iL, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    return nx


def func_15025bc7864c4075b45727751e88f9ac(U, iL, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    return s


def func_7e78439037194e3ba155e1644da75394(U, iL, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    return nxU


def func_2f4c6ea534ed446e82efa729f296bab8(U, iL, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    return nxL


def func_93009363d8cb4d24b2cda9b3c4b2cf45(U, iL, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    return sU


def func_f38378e17a604823b9c97b379eba0b52(U, sL, iL, x, w, iU, L):
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return nxL


def func_7c65f092dd6148c19db2a93e445c2b0a(U, sL, iL, x, w, iU, L):
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return s


def func_6f7663fc78ae4b71949119f540cccb5f(U, sL, iL, x, w, iU, L):
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return nx


def func_08555286c5294fec9963248b2eaac2f0(U, sL, iL, x, w, iU, L):
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return sU


def func_2378176d53b644f393b8b3faba9b0b6d(U, sL, iL, x, w, iU, L):
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return nxU


def func_abf20acfaffd4ba2b8eeecc989fdadf4(U, sL, iL, x, w, iU, L):
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return na


def func_e1304300b764415db9fc3ac51f0619cb(U, iL, x, w, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return na


def func_f86ac92d652448a39f4c252163b55cb6(U, iL, x, w, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return s


def func_1576ea1bdbf04b4ea770d558b0de3962(U, iL, x, w, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return sL


def func_1dcc5538508e4071a7a994d3e7f57778(U, iL, x, w, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return nxU


def func_514c6cb842f644669b60b93c2cff8fcf(U, iL, x, w, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return nxL


def func_69d7ba8f4fb443e9bd7263c0a1e5c441(U, iL, x, w, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return nx


def func_b14587f7a1a34edebb681fd889ad167d(U, iL, x, w, iU, L):
    sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
    sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
    s = sU - sL
    nxL = L[iL + 1][0]
    nxU = U[iU + 1][0]
    nx = min(nxL, nxU)
    na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
    return sU


def func_8098d03276c242c3a3e3c093670df31f(L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    return i


def func_7d7d611113db48b7b5137ec79fe0ee5e(L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    return area


def func_724f3b60faa840ad82b4441149b71c86(U, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    return i


def func_9d36cd529a7e4474853154a8645e070d(U, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    return area


def func_98f1e3268cd147309809c84c60729990(U, G):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    return area


def func_307932031e8148b2a6af5e062e852498(U, G):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    return part


def func_bcb6b85be29b41b4b8ae9bc919edcb34(U, G):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    return i


def func_d5d166e5ca4a400d9797f489d83623f1(area, G):
    part = area * 1.0 / G
    cuts = []
    return cuts


def func_c4aed95ffa324ecbb25b7c724f507630(area, G):
    part = area * 1.0 / G
    cuts = []
    return part


def func_170a2501e02d490a87dd0aa7a68fb573():
    cuts = []
    iL = 0
    return iL


def func_26101337dd2e4fe1b5f404b0f0fe4061():
    cuts = []
    iL = 0
    return cuts


def func_8713745972c5456792f5f402af5b00b5():
    iL = 0
    iU = 0
    return iL


def func_8a510dc3eb5c4480af0eb9c4045658e0():
    iL = 0
    iU = 0
    return iU


def func_cfd4c2ba7f774f1b988d278b615593b2(U, L):
    iU = 0
    w = U[0][1] - L[0][1]
    return iU


def func_9b955340ac02402d9108b8e0674c0e5c(U, L):
    iU = 0
    w = U[0][1] - L[0][1]
    return w


def func_edfa552206c34f77b7e317c470331b16(U, L):
    w = U[0][1] - L[0][1]
    a = 0
    return a


def func_0bb5956886d9428ca5b3d17695057b5e(U, L):
    w = U[0][1] - L[0][1]
    a = 0
    return w


def func_6218e5290e1147ebaa8a00fd23a2ef2f():
    a = 0
    x = 0
    return x


def func_99ab55135f134deaa171b86ee8eb4b22():
    a = 0
    x = 0
    return a


def func_585cb4ab920148708f8f28a6b9f235f2(U, cuts, part, L):
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return w


def func_59ff2411202c4e71bc7fa20b6f3053f9(U, cuts, part, L):
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return a


def func_01e8fb107ea846bf8a43e6faece93d47(U, cuts, part, L):
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return x


def func_2f7d2c27a6c94b1b96cd6d84499c4db4(U, cuts, part, L):
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return sL


def func_36dbf0656a0542208508590edbd58e2d(U, cuts, part, L):
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return na


def func_0d52a0c770374ec1a0593cf0188f8e44(U, cuts, part, L):
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nxU


def func_ae4212519b1c4cdf869452f01fc2364b(U, cuts, part, L):
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return sU


def func_9a7e242f8d0f436fb83953f04affba94(U, cuts, part, L):
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nx


def func_dd460fde3abe4f7db08612baaf0137ff(U, cuts, part, L):
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return dx


def func_dd11f1fc331f44b6beaeee089ed2a7d6(U, cuts, part, L):
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return iL


def func_01233905030f4ed8ab46a409c90f1c92(U, cuts, part, L):
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return s


def func_ae06a77960e54942a3d269d4727c5da6(U, cuts, part, L):
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return iU


def func_b4c91fd9c6d445828b70692a4a6b86f2(U, cuts, part, L):
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nxL


def func_2fb916ecbcda4864836d5e478855f597(U, cuts, G, part, L):
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return cuts[:G - 1]


def func_ef3ee55e2bfc4c9b90daaef395f58c80(U, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    return area


def func_36654ab36c5e42f086229a6e15c8e669(U, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    return i


def func_b976c397239d4b0c93fe3ece26d216d2(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    return area


def func_e7154132744a4f9688f772fbe51f7487(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    return part


def func_370a116425164f94aee8cf4540071efc(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    return i


def func_582e561ac4fd4d509c33ad11091b68f2(U, G):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    return part


def func_19cb971e85e54e5b91ab53c623c4954a(U, G):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    return area


def func_2ed3199e84e646c9b9f0478e3adfa5aa(U, G):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    return i


def func_08c918f931e340b1a3d88f4c0346ec3d(U, G):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    return cuts


def func_adc8c54bfe3e4dee88f09bd272853976(area, G):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    return cuts


def func_d2efe7edc7b24ab8853a8fc8e95e72c3(area, G):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    return part


def func_240fd9b17bf242ab8a242e842a54c641(area, G):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    return iL


def func_3dd07bd3ade9453eaf9bbe807794b466():
    cuts = []
    iL = 0
    iU = 0
    return iL


def func_0825bcc47c284dcb814f75ff53ef7b79():
    cuts = []
    iL = 0
    iU = 0
    return cuts


def func_501750c65c8f4bf1952c44f0dbdd0967():
    cuts = []
    iL = 0
    iU = 0
    return iU


def func_5f75e410aba84dfda5a90445bbbbde34(U, L):
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return w


def func_434db584b8ef4c2b8d631aa664d5b6e1(U, L):
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return iU


def func_8a171240eba94481aa48c3891b47df17(U, L):
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return iL


def func_18db47e99d404add9b5cdcfe1e1bfd71(U, L):
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return iU


def func_af6097b15fb04d8494e53701b7664fa7(U, L):
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return w


def func_58dab3f0939b4679bf3087a896a09af6(U, L):
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return a


def func_b7bd8afdeddf4971acb4dfa0c8b12d76(U, L):
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return x


def func_a38b4abc2e0c43419b9ebeed1444d45b(U, L):
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return w


def func_b8782e9b1c37491d9c7f91bbfc94ce81(U, L):
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return a


def func_992ed194a6ed482181ef5cb17f1e1051(U, cuts, part, L):
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return iU


def func_2590a5230aa8447dbdbe65faa73108a9(U, cuts, part, L):
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return s


def func_81a8c3e327d949aa8d50c72c8b29edfc(U, cuts, part, L):
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return x


def func_da9f1df26ad3450582547fa07bab81c8(U, cuts, part, L):
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nxU


def func_b279eef9c06b46fcb24d1c9c1f6f92b1(U, cuts, part, L):
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return na


def func_662e61648abd434889c612fb3d96a548(U, cuts, part, L):
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nx


def func_7be8cd1c4fa3472fa781884bd1682697(U, cuts, part, L):
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nxL


def func_e514a7b9c1c143ab98415e51bed9ad42(U, cuts, part, L):
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return w


def func_d747709da1b14693b3e93f304d1dc34f(U, cuts, part, L):
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return a


def func_bb2d02a5c8174cab9c6507fe60140fb7(U, cuts, part, L):
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return dx


def func_10163f166fc04cd4bee048c79544b33b(U, cuts, part, L):
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return sU


def func_05c10860f8004136aeb5ed955569081c(U, cuts, part, L):
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return sL


def func_ed2e55a3bf7f4e069da46aeb8b3a572b(U, cuts, part, L):
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return iL


def func_dd9b986c4505429da79550672a955a1a(U, cuts, G, part, L):
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return cuts[:G - 1]


def func_08510c1e054f47fba03eb87223ed377a(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    return part


def func_b52ace99a7464c69a2d27d5c7cf4a788(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    return area


def func_3074a3e1e2b048eca26e8d809ce71e6a(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    return i


def func_371b3b0416a64c189392f701481fa57c(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    return area


def func_44748ced7c6b4456a76dd24102f5a5cb(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    return i


def func_7fd8a97c37b347ca91d1f629d6ba57fd(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    return cuts


def func_408e08946a2147988d3ed75fa4a30e1c(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    return part


def func_90df394fba0d4d4394e4ff643e27bebe(U, G):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    return i


def func_a7f07afcafa545f89e76cfd0e9aa0b92(U, G):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    return iL


def func_75cff0dbcff845869da72d084164dbae(U, G):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    return cuts


def func_e09abd1a833144c0bd18a5544820dce7(U, G):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    return part


def func_f0cff4f1c2294373802ca0036e023f39(U, G):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    return area


def func_45bc842637be4922bc402931f9afa4e0(area, G):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    return cuts


def func_8c0fe194924842278096e55a02443957(area, G):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    return iU


def func_1ad630ccbafd485abbbb734417a33bf5(area, G):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    return iL


def func_7aa108c55a064628afbb367e9e7a206e(area, G):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    return part


def func_d6196f2a84b9495e9b2f3752f05efe37(U, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return cuts


def func_6353770e8add498daa01dc5298f7fe77(U, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return iU


def func_6adadabad36e4bb9a220b417ccfffcf5(U, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return iL


def func_7a69c780adab424db4216e4b9340d0bd(U, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return w


def func_b1102c1dc0c6494c9a74acc2f022af45(U, L):
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return a


def func_c10113162be348d8859c6dd4a7ef97e3(U, L):
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return w


def func_bb90bf8b63e947f197b5a7a891b56340(U, L):
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return iL


def func_6452c4d6e5be4f5eb13fceda42dcb7f9(U, L):
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return iU


def func_20ba3fb2867246978b03fb0ab88258fd(U, L):
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return w


def func_c1d61e00434e46b282e90559c0c80c2c(U, L):
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return x


def func_385c3e7081a84551b7c36c5141659b3f(U, L):
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return a


def func_5d02b9736e044dc5bcc89b5a12f7050e(U, L):
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return iU


def func_ac8dc8b7307b4aa3a05a0866fe18c5aa(U, cuts, part, L):
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return dx


def func_6fc699da181b4ed2ba807ceefbae37fc(U, cuts, part, L):
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return a


def func_3be34b3c6ca6426db811c8f7ee43ed4e(U, cuts, part, L):
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return sL


def func_281d7869b60a448faee570ba788ce170(U, cuts, part, L):
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return sU


def func_65e7bfbd3f2649dcbef2f93e796e01e4(U, cuts, part, L):
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return w


def func_4109c13465ea4396bfc93955ee61b71a(U, cuts, part, L):
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nxL


def func_70c65637e8804cd1a76d3a2d706d7f96(U, cuts, part, L):
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nxU


def func_f5e50c9e10064c98a9818c024c156dc2(U, cuts, part, L):
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return na


def func_63100391eda748a89c83c4c347914348(U, cuts, part, L):
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nx


def func_d801b166dff349b382965597ca6bae45(U, cuts, part, L):
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return iL


def func_b0ddf6fc358140c693518e0be8c5d2af(U, cuts, part, L):
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return x


def func_810c311f63a047599fae7dab7b80fc39(U, cuts, part, L):
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return s


def func_08cbe703f9f04d479a55e5513b9e53c3(U, cuts, part, L):
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return iU


def func_51317ac105834fbcb0f9be16c8584aab(U, cuts, G, part, L):
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return cuts[:G - 1]


def func_310f02cba8c3406aa0e8c0311df732c0(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    return cuts


def func_74f9aba41fe24244b95e548a06ffbabe(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    return part


def func_9b6bb42a6fa04eabb734cce069ad8119(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    return area


def func_208cb0c9c5ae45c1a6b82374ea2c55e2(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    return i


def func_db124ded567d42bd9bf8209a3c809839(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    return i


def func_ad77b8ff4f814fe498e8daeea4998e43(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    return area


def func_8181e743cc0947c2ab5c2386441f2050(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    return cuts


def func_e19f2f93ccd5450a98547aa06d31275d(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    return part


def func_aaa1f4a5485c410ebe47188d90e3cf92(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    return iL


def func_b1c42481128940479a7fea3102b381f4(U, G):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    return iL


def func_c90554d7d24b4c2480d1f2590fdcb7a1(U, G):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    return area


def func_061cba7d980c410eb1a622995f850e71(U, G):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    return iU


def func_9f38205af3b24e189f5b72c5995f1dc0(U, G):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    return part


def func_2ae951e7c3054b908a690b2f776b6b5d(U, G):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    return cuts


def func_6fe556e5e5cd4ee9985133d63991b7bb(U, G):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    return i


def func_17d75e38589244d3848be7fc1f57d361(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return part


def func_2189c504997f44ab8e76e70131865884(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return iU


def func_388b583702be4f3e80ce530f282fa080(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return cuts


def func_6ee387782a02435e9b633601797719d8(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return w


def func_60f2e819db2a40809736c7cf7bca0207(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return iL


def func_51ecfb05289640808b64d6a256b78752(U, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return w


def func_127f4ccea85345a9832d9b106ab80a79(U, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return cuts


def func_38d5abf53a1d4d78beb051ee48524e2d(U, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return iL


def func_761be1a3fd3546f88d19e662407643f4(U, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return a


def func_df9fca82f45b4c0e8cff949a767b20e2(U, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return iU


def func_068f203d39a14e57bfa0a6445da40046(U, L):
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return iU


def func_fc87580d2bb94ad0af15a09d03f485dc(U, L):
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return x


def func_744539b6d4a148e1902c68df67acfdcc(U, L):
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return a


def func_0cf46bdb91044895ab8b5535e5df7ba8(U, L):
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return iL


def func_32bb7c3927424d6887895d233f2ac176(U, L):
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return w


def func_2823ba26ef40455c95b85e8969cd147c(U, cuts, part, L):
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return sL


def func_eaf3df5039d5482393beb01b8cd34397(U, cuts, part, L):
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return x


def func_34e21acc27fb4cfba31e239b259e0fdd(U, cuts, part, L):
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return sU


def func_fd51d2cddec04c209957a06b228e01d7(U, cuts, part, L):
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nxL


def func_357f734463b6421ebea1978616ed7705(U, cuts, part, L):
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nxU


def func_d1e1d912f6d14886ac994088f25f6b17(U, cuts, part, L):
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return a


def func_4a25938b4c3f482e9df8a85c5e286e1a(U, cuts, part, L):
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return w


def func_1885d1838ec14f8886fa62a2bac0abb4(U, cuts, part, L):
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return iU


def func_f09cbe561c9c4d448646f3858b72e9f8(U, cuts, part, L):
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return iL


def func_8f3237ce341448d8bf8aeb33088ac038(U, cuts, part, L):
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nx


def func_9a935920ad3649079cf17a8a9f186f0f(U, cuts, part, L):
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return s


def func_b2230ae6a9b1446fa7be4d19ea6bb11f(U, cuts, part, L):
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return dx


def func_b5cb2049e1af4394b33b711299b6592c(U, cuts, part, L):
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return na


def func_f407b7da6ff34d83b31a2d34af60a647(U, cuts, G, part, L):
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return cuts[:G - 1]


def func_7798a99b1d304c0990dddc58b2d2d71f(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    return iL


def func_adf883fbe0f046da83a4ffb31e0624a6(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    return part


def func_c5e363e31ef2458f990361e4b5a8d13e(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    return cuts


def func_13a5cfad57c34eef86d8bf2b18497c5d(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    return area


def func_e8f537425d1b4adab2e94f28094e05bb(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    return i


def func_a9898413b0f44b0f88c55d5e5045e6bd(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    return part


def func_26cbea671a79461f833f5c98977edd90(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    return iL


def func_32b20e3845354332a25a63c72136f125(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    return iU


def func_0a4b03284696468292755f0e96501686(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    return area


def func_fec3ac37780549c08b5bf7af3bf3ac48(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    return i


def func_a32838c066694bbca29c8a40849f58ce(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    return cuts


def func_e30d3f089b2d4fb5b802563327a16a87(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return iU


def func_a3809f8721a2470288dbdf8c17bdfe44(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return iL


def func_1e0a8bdda05e41c18ace45f7407674d5(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return part


def func_9b76fd68a38548ebba8cb99bde146869(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return i


def func_f6388289613d48ebb76fd7d6587883f1(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return w


def func_6f83482e27ce45529a43073c4342d4f6(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return area


def func_8e1a827d353f499087287f603b516b69(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return cuts


def func_f8250d806f304b95b9588695dc6b4f0b(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return w


def func_87fb9285e6044ffbbab636889ba08709(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return iL


def func_62af612fe0aa40698062ba467dfe231d(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return part


def func_601fe58d1a6b427893c5eb15befd44d4(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return a


def func_35d9a2c478b94ffb814c1a666559966f(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return cuts


def func_a08ad8ab8bfe40b5bbff089131eb4bb4(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return iU


def func_0fa454fb548e4c1ea5fe64cf4cebfa22(U, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return x


def func_b652cd887be2428b8824502d2d5b5c84(U, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return iL


def func_12afcb015d6945f59377a9d63b0fe047(U, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return a


def func_b8c997bb233e4a948fac3e6fc249baf8(U, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return w


def func_fa175f678bfe4395b6f3ae4e822b2203(U, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return cuts


def func_a1fa09edf2d2461e98185f4acc62df6b(U, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return iU


def func_57f1f75acdc342068b6143971ff83a30(U, cuts, part, L):
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return a


def func_f17f69533eba44af81607fa3cb66f116(U, cuts, part, L):
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return na


def func_9dcd645f3351404f8b6c6d2208defaf8(U, cuts, part, L):
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return sL


def func_1e297c6a66434af8a324ac6c541772ec(U, cuts, part, L):
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return sU


def func_46d7c6fe48da4aadbfa4e8a3745376cb(U, cuts, part, L):
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nx


def func_a62591580ea046a588f6a9f8e7ecd68c(U, cuts, part, L):
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return s


def func_e8df3f4ac7084c118301e3a17c5adfb4(U, cuts, part, L):
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return x


def func_fb1cfe2a342945e4ad460011853a4397(U, cuts, part, L):
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nxU


def func_8f936ece22744d36993370e1d4d19d22(U, cuts, part, L):
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return iU


def func_d0000979198c40ad8a853ba6739250bd(U, cuts, part, L):
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return w


def func_9c1402316f7b4847a35e248eb5c932c5(U, cuts, part, L):
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return dx


def func_cf465014941242259cc5352d7379bdc9(U, cuts, part, L):
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return iL


def func_f268864b0af145299895fe3d987b0d0b(U, cuts, part, L):
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nxL


def func_8eed91d063ee4ffc95fa98501def6d07(U, cuts, G, part, L):
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return cuts[:G - 1]


def func_688c99428b444116bafee0c874f453fa(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    return iU


def func_e253717e537149dba4a21fb9874066d3(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    return cuts


def func_781aa9a4e874415e81fd3c95efeaaa2f(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    return iL


def func_2405e689cb3148f78572d6d1dd57904a(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    return i


def func_691f152a5828475e808e05beb5abc4ac(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    return area


def func_78973c361b7b4516b214cd112bcc96f1(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    return part


def func_50f282766eff49a1ab6ff19a515d8d9a(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return w


def func_910aa814a36f4cdd8a0e7f21f421d37d(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return area


def func_9770df6cb5ca46d98382851c7ceae264(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return i


def func_32b0052233a8498fb8ead258f1b72ba6(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return part


def func_b2b3c4b6d78d47568d07cd2df7dc6112(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return iU


def func_969e3708c75945f1a83e75102cc3961e(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return iL


def func_9c76bed32e764b0a851066624f98fcf7(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return cuts


def func_251401e0e76844d5836daacf8eb73c07(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return cuts


def func_845fd3d315d84ec1a089aba57a7df9de(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return a


def func_a7cf64d8b8234c7fbf2989bd2e46082f(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return i


def func_2964406a78304ec6956b66fe162c27eb(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return area


def func_bcf41b20339145d1b612b61b85e020b0(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return iU


def func_a2610eccacb14075b09e71bfe1e5d869(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return iL


def func_214216e0ace5488d9dc1402935c61518(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return part


def func_653177098d4c4b6baffd02c2a23867d9(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return w


def func_d2a78c9c121b436fa848672b75832eac(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return iL


def func_503e8f0c3c60418fbba7855bc7038332(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return w


def func_dca0bf793a8645e2955e229d4af7faa1(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return cuts


def func_a104e87559f845a0917034644287c9a4(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return a


def func_7d8d253922204f658368f018eecbf0ca(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return part


def func_df087a8908644067a3962322184711c7(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return x


def func_515a46e864dd4feeb19f09ab82f28dc5(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return iU


def func_eb856bd9cbb1460c973837505c11b0ff(U, part, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nx


def func_81369f0341024a4cab4d9d6598d4228d(U, part, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nxL


def func_9e59887caf6d4b65b8e4b64fd3854397(U, part, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return w


def func_8c820020ff334cfc81d1a4717a86d3b3(U, part, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nxU


def func_34afb4357c0d43bab92e3c5818e63614(U, part, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return x


def func_9b32d292577e438daeb6d52b63c7dcf9(U, part, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return na


def func_fe13b0ec1f704f97b60f711128d519fd(U, part, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return a


def func_315df0b33f944cfeb3d4f24cf21a5b47(U, part, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return cuts


def func_bc488b92692c46fc89b1ee7cb688111a(U, part, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return dx


def func_1b939b70ba0044e9ba1a1961515c93e1(U, part, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return sL


def func_495f3a5607a846a2b0955f5c849a114b(U, part, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return iU


def func_d4541f90cbce4e1ab7d03be5819e039c(U, part, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return sU


def func_9ae5cb22b11348588e64ebb02e7e4ceb(U, part, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return s


def func_9a8414723985424c8e44560b56c27e1b(U, part, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return iL


def func_a69490c5e16d449d91a0082feb964957(U, cuts, G, part, L):
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return cuts[:G - 1]


def func_cbd334cdd238492ebac7219753d59278(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return w


def func_bae2edfbca7e466caffeccf926011e35(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return iU


def func_83095b1a4a4e470fa1d0ccb4692f0555(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return cuts


def func_44b231d1942d4e28ba422edfcdd50132(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return part


def func_6f50b8b5816e42ed9f51e328cb17dcc5(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return i


def func_5c293511b56845c8a04cefbc1b18a72f(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return iL


def func_2f0fa45493fe4c4692e1d4ee6f0f98a7(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    return area


def func_ff1ff27d56284b9cae861456b0d54950(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return iU


def func_7196f62bb1474613a44156f2489581fb(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return cuts


def func_985fc012775d4d88a9d635fe5ea5f252(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return iL


def func_05b4a34e79f645dfb7dd646eb5e50146(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return a


def func_d0a0a63098a44cd99df80a435663742e(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return area


def func_474a6425776146ada9946987d05e316a(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return i


def func_84256870ed4647a8944188b8bb700be1(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return part


def func_d1ae0e70192d4a32998ea689020b78e9(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return w


def func_cdd18c9a48364841bb9c2dac06b067d0(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return w


def func_bd178459b6494418b4c8466a33ad410c(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return x


def func_d9651e0c40eb42c89930c30f6a9f21d2(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return area


def func_772a8405562d4ba89fd838392603a569(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return cuts


def func_b74280b7f1064662bc4c472582d94056(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return a


def func_555db1941df74c0e97ded95c3a2f3d49(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return part


def func_9adc3b30378d4735b1f8ec73a226d231(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return iL


def func_b6101acdd6f94b70970b0254fe2fe665(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return i


def func_a09a6e4f5bbc4f4e8400b3455f9e9ad2(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return iU


def func_c6fccb668e64482098ab41a7dad5ce24(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return s


def func_55c026d1fafb413eb31c9a0e5f0f2063(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return iU


def func_8416291f7456495db78f14df3bbd40da(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return na


def func_d7c71b90dd6b451bb8be405cc8fe2901(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return cuts


def func_3d1f230de1fd49fc9055cd6f9b9b2d9f(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return iL


def func_25603fb371dd45c2bcc3a1b96757389c(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nxU


def func_aac466f09e484f65bac0dee42a089dc7(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nxL


def func_3b580ce2ffb04208b860b3c34228e230(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return sU


def func_c298698a2a024fc58885d53f84c1dd1d(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return a


def func_e84f96856c6a4116aef3778a2edabb01(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return sL


def func_0fe3a7ec6d3340fca8144d6f1ad11ecc(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nx


def func_2ce52cc93859401995c4ad0d433ab422(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return w


def func_afec5fde0398410b90b70867d518ac1f(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return x


def func_6d275b7e34fc424eadf3e1bae96a55c6(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return dx


def func_ce1c77e5822240df943d617884cfa478(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return part


def func_a4b3a3bfd1c347f8a1d9fbba39a59346(U, G, part, L):
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return cuts[:G - 1]


def func_add00ab1fc714955a8329bffd59a5705(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return area


def func_3379029ec7e94b06a381738df39cba2d(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return w


def func_af731d4e6d90404a8ca822e99e819621(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return part


def func_b72f23406b574768b86b970353b1f8c6(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return a


def func_334c3d1ff852432088fee062cb66aa07(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return cuts


def func_0e70f765563f49b38b0b8e7450500932(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return iL


def func_a50a61d935d54ead877b007c9c85bc30(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return iU


def func_5ac09755b2a84340b2a55f618fd43753(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    return i


def func_badb8dfaff5043dfa5ecbeaad7e48d33(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return w


def func_63949d009f634cc9b27a04766b475d10(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return x


def func_411a896678d040c593e4cf9c842c7c0f(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return cuts


def func_029d683300554fbdb863aaf436793867(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return iU


def func_b551156296d348b9942db45d25761505(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return part


def func_09e8864adb564413ae955a5233a1fee6(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return a


def func_d12690792af543dfba2c871eae37b9b5(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return iL


def func_5e063018afcd4caea44b8d4f77954d69(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return i


def func_3daf6663cafb45f5b51ab05cd40eab19(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return area


def func_4857f1834f8643a18feb2b3d2c3adfd4(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return iU


def func_9fc3005a9af049b28a9d7f07ea241878(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nxU


def func_13071893c570466a99ccb020b9adf6c9(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return cuts


def func_d2f6e08898eb41e1b4641f2096baaf37(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return w


def func_dd500f0519264ced975ea8aad0069a65(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return part


def func_961b8018e32140b791a734c15d36a1f3(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return a


def func_879f50effbe44979bd51e4086a8ffc50(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return iL


def func_0be4e10edac742a685e5070660bfc5e2(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return s


def func_8bbee53a1c484230970d69ef7378bef4(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return sU


def func_ca387d2f368c46eca31058de9a0ed990(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nxL


def func_0f09fb15740f431b99882aae99e2f306(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nx


def func_c775fc439a364f35947c113ed1e6a1c1(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return i


def func_feaf78a441614754a8f1035351d7f737(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return sL


def func_a3797197e25a4a3abadf26f6e2f640b6(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return area


def func_ae1107d17df542b988be11d97acaeec4(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return x


def func_422b1411029e4d0faedbfc2012976f4a(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return dx


def func_824dbfdb97554d8b9c3176f8235e38ca(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return na


def func_b9a7da6dc22846db851b69a419982b27(U, area, G, L):
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return cuts[:G - 1]


def func_efacef43370e47c5b9e890905ef8507e(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return cuts


def func_971789a299584dec8045d6b606f05c0f(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return a


def func_3ac42e559aab413488729694d66db24f(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return iL


def func_602d292a2aa9479bb85a433b135dc49b(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return w


def func_bbd28699a5314d54a78d7ad7b69947cb(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return i


def func_49a11cf7da4a487f92e6116bdee6ad57(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return part


def func_d0eadd4ad8c04c86aa0d999a2972282a(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return iU


def func_9039880572034d708ed165b8bb35e8cb(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return x


def func_ec76b389c81a43d5928bf27b782b4bfc(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    return area


def func_bd7cfeccc8af460cb583fd3a9ff4f469(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return i


def func_3e90e5f140af41b88ba7fa5863931b9c(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nx


def func_b2ecdc2d22d7448b9dfc3d7dcca85d83(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return sL


def func_70504912281545d0b644851fe501af9e(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return a


def func_ee1604c45fd549e28952d07802606962(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nxU


def func_a0a0b7dd30b345b7ae8c06536332a153(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return cuts


def func_4a255a8e0ebe46e3a6b57bbd9f785490(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return na


def func_a3f62b8443744481b6429d6955a7f197(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return s


def func_4a8adf6404994836bb4873f269a72bc0(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nxL


def func_ea39aa07f9764330b8dc0c6bbd03890a(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return dx


def func_997c3e5acf6f4919a043fec68060d9df(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return sU


def func_8c1a138374c9469fbab93c6c89e63b56(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return part


def func_6aa385c5d21942e685e3874e1af4f45d(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return w


def func_03a8912e61d34064a44458ba8e2fc035(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return iL


def func_84cf5c989863469086f826dbadcf8e32(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return area


def func_9e2fd52d93724ce1a45a968274bd00c7(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return x


def func_28a3f603b2984fe2a99a4bd231ebc0ec(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return iU


def func_cb480ee0686744e4857d24caf225e427(U, G, L):
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return cuts[:G - 1]


def func_99db1937cd0147eaab2f93c709fa13ac(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nxU


def func_b016106b42724b1aa9f37710765ca9c8(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nxL


def func_b5e22db2addf4779a0f7f580813b5894(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return dx


def func_0c6dec6f64b94fd78c77be39486785bc(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return na


def func_721b5dc13bf346c3995590b47850ab7d(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return iU


def func_b367d3c3aa9747b99b6d13daa2266697(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return iL


def func_5014325920f0491e99011f492c9ff69f(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return a


def func_0c3ed49bb6b7428588603c808e2990a0(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return sU


def func_c447a73cf0394f5aad1f8c08cf7aeca0(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return sL


def func_c9d72c8449794feb832306b03614decd(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return i


def func_bfaf93f5400d4add8f2b09690b01ad5e(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return s


def func_081c5dfd22e14a939e2ad6e19524c7cf(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return x


def func_e21e42ad93324a5390e645638dfc69ba(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return part


def func_bc3661f76a6b47ca963ab5b1c76f0829(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return cuts


def func_945b17627e8d472c81648cc0b9c5703d(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return area


def func_995cc4c33ed14683b1f895b4964c2e8f(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return w


def func_adab218c23b748578c3e39d30bbd0c1b(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return nx


def func_d036bb56dbe54a69870065ebded74304(U, G, L):
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return cuts[:G - 1]


def func_eac337ad2a584aec82969051156e1e41(U, G, L):
    area = 0
    for i in range(len(L) - 1):
        area -= (L[i + 1][0] - L[i][0]) * (L[i + 1][1] + L[i][1])
    for i in range(len(U) - 1):
        area += (U[i + 1][0] - U[i][0]) * (U[i + 1][1] + U[i][1])
    part = area * 1.0 / G
    cuts = []
    iL = 0
    iU = 0
    w = U[0][1] - L[0][1]
    a = 0
    x = 0
    while True:
        sL = (L[iL + 1][1] - L[iL][1]) * 1.0 / (L[iL + 1][0] - L[iL][0])
        sU = (U[iU + 1][1] - U[iU][1]) * 1.0 / (U[iU + 1][0] - U[iU][0])
        s = sU - sL
        nxL = L[iL + 1][0]
        nxU = U[iU + 1][0]
        nx = min(nxL, nxU)
        na = 2 * w * (nx - x) + s * (nx - x) * (nx - x)
        if a + na >= part:
            dx = (part - a) * 1.0 / (w + math.sqrt(w * w + (part - a) * s))
            x += dx
            a += 2 * w * dx + s * dx * dx
            cuts.append(x)
            w += s * dx
            a = 0
        else:
            dx = nx - x
            a += 2 * w * dx + s * dx * dx
            x = nx
            w += s * dx
            if nx == nxL:
                iL += 1
            if nx == nxU:
                iU += 1
            if iL >= len(L) - 1:
                break
            if iU >= len(U) - 1:
                break
    return cuts[:G - 1]


def func_44b9f16aaf9e4309a7fdd1906a10720a(input):
    line = input.readline().split()
    x = int(line[0])
    return line


def func_d56b9d05ca974a87be974adf1ab4cfa2(input):
    line = input.readline().split()
    x = int(line[0])
    return x


def func_e32cd0efa8274f73a08830d400b416f2(line):
    x = int(line[0])
    y = int(line[1])
    return x


def func_c4b4bd6f78494897a23005a7985f2c4c(line):
    x = int(line[0])
    y = int(line[1])
    return y


def func_01ef9604b88b43e29f34c14f5f3ac2d1(L, line, x):
    y = int(line[1])
    L.append((x, y))
    return y


def func_f07dcf52b0bd4ab58736cca41ae9076f(input):
    line = input.readline().split()
    x = int(line[0])
    y = int(line[1])
    return line


def func_1b41188234954473a28a564a64578a28(input):
    line = input.readline().split()
    x = int(line[0])
    y = int(line[1])
    return x


def func_d96928d81269454bbb49a663e19a7886(input):
    line = input.readline().split()
    x = int(line[0])
    y = int(line[1])
    return y


def func_6847cedb32bd4b8581ff299b8bdb2eba(L, line):
    x = int(line[0])
    y = int(line[1])
    L.append((x, y))
    return y


def func_e2f2e48857e34114a8445794b53acb90(L, line):
    x = int(line[0])
    y = int(line[1])
    L.append((x, y))
    return x


def func_de228a26a5774e89a7991ad0a3320ebd(L, input):
    line = input.readline().split()
    x = int(line[0])
    y = int(line[1])
    L.append((x, y))
    return x


def func_42d10cd466e2446689fd9fdaf69020bd(L, input):
    line = input.readline().split()
    x = int(line[0])
    y = int(line[1])
    L.append((x, y))
    return y


def func_289bd38ede054cc5ac1a945fbf35280b(L, input):
    line = input.readline().split()
    x = int(line[0])
    y = int(line[1])
    L.append((x, y))
    return line


def func_a71cb14239be43f7820844785581dcb9(input):
    line = input.readline().split()
    x = int(line[0])
    return line


def func_610a39602fd947a08a3668acd182b322(input):
    line = input.readline().split()
    x = int(line[0])
    return x


def func_46672874e00744fe8154a704c71bc638(line):
    x = int(line[0])
    y = int(line[1])
    return x


def func_80a0700322224e3ab235c8be4a82c50a(line):
    x = int(line[0])
    y = int(line[1])
    return y


def func_23dd093c1de240e18d76c77c9b9a25f7(U, line, x):
    y = int(line[1])
    U.append((x, y))
    return y


def func_937c1ebc30a146ec888bb69843143320(input):
    line = input.readline().split()
    x = int(line[0])
    y = int(line[1])
    return x


def func_d30b4be169664215a61e8bfeacd5f8ea(input):
    line = input.readline().split()
    x = int(line[0])
    y = int(line[1])
    return line


def func_eff01fcdedc446f591feb1938759aaea(input):
    line = input.readline().split()
    x = int(line[0])
    y = int(line[1])
    return y


def func_ec42c79de0234842bdba6e516ffab1df(U, line):
    x = int(line[0])
    y = int(line[1])
    U.append((x, y))
    return y


def func_328e4d52b3ed4fd4a3e688062086c8a5(U, line):
    x = int(line[0])
    y = int(line[1])
    U.append((x, y))
    return x


def func_a964025d790841c59ed24e749dc1d4b8(U, input):
    line = input.readline().split()
    x = int(line[0])
    y = int(line[1])
    U.append((x, y))
    return line


def func_e9a94b394600416e9d21315f35785f0f(U, input):
    line = input.readline().split()
    x = int(line[0])
    y = int(line[1])
    U.append((x, y))
    return x


def func_2b4019b8e4a44462b99f4b0f0bc39978(U, input):
    line = input.readline().split()
    x = int(line[0])
    y = int(line[1])
    U.append((x, y))
    return y


def func_40e0289ca7eb426d841f809d70a09fa6(input):
    line = input.readline().split()
    W = int(line[0])
    return line


def func_336bf70105ec4daf934089668a1c8078(input):
    line = input.readline().split()
    W = int(line[0])
    return W


def func_348f5cb994dd42e39737fbb12f442729(line):
    W = int(line[0])
    Ln = int(line[1])
    return Ln


def func_88f7ba26c08542348c78c9f54095d3d2(line):
    W = int(line[0])
    Ln = int(line[1])
    return W


def func_04001943109d4449a288e7540e90c315(line):
    Ln = int(line[1])
    Un = int(line[2])
    return Ln


def func_477b58c4cf9b4daa908a532711431b88(line):
    Ln = int(line[1])
    Un = int(line[2])
    return Un


def func_cab4fb53e15547e2a848e85de415ddfa(line):
    Un = int(line[2])
    G = int(line[3])
    return Un


def func_c76fc1a2d01646bc8ce65f0a139b868f(line):
    Un = int(line[2])
    G = int(line[3])
    return G


def func_ce1afd0d40864313b42d572d7be7d827(line):
    G = int(line[3])
    L = []
    return L


def func_f52701ca81854e61a9b42e43fea70bea(line):
    G = int(line[3])
    L = []
    return G


def func_a838dffe2029415aa44132f65bdc74fa(Ln, input):
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return i


def func_5fe62fcd85654736a7a9007c65cc568e(Ln, input):
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return line


def func_fa839ced05274921bb1df6c9688414a8(Ln, input):
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return L


def func_2492d99f0a7b4b53bf7ebb323888b1ca(Ln, input):
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return y


def func_9b8baff513a24f4db38e1506c78879a2(Ln, input):
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return x


def func_ae503ec1285148059e798b9f282a768b(L, Ln, input):
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return x


def func_c5839e08ec1e429da023096066e99896(L, Ln, input):
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return i


def func_45a40519c18442938544de248f535dbf(L, Ln, input):
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return U


def func_60f86d889ab14d86816720500db3e7c5(L, Ln, input):
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return line


def func_82d0cdf8de0640fc9d96845f1bd54ae3(L, Ln, input):
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return y


def func_3b8e6ab46c804f40ba8d87967cb71f2e(Un, input):
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return U


def func_0e6309dc63da4120851b58ce10a4b892(Un, input):
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return i


def func_0c8e8148bc82463a820ec9cf85d72f66(Un, input):
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return line


def func_2da81b17ec7b43af8b282f78b5e59e76(Un, input):
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return x


def func_25f620b58b1f4edabc8875935eba3fab(Un, input):
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return y


def func_dd56bb4feefa4f10967cc1b529a8c8c2(Un, U, L, G, W, input):
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return res


def func_c11e8119ab6f42ecbff3c7df794843e7(Un, U, L, G, W, input):
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return x


def func_651ffd7c78ec4e658a2d10bd51bb20b5(Un, U, L, G, W, input):
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return y


def func_41a05e89cd1e4199b4a23f66b4a1592d(Un, U, L, G, W, input):
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return line


def func_82a7b25bdb5c4e0182d820e18394b855(Un, U, L, G, W, input):
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return i


def func_82499f28c66e4a0e8a42678141fd7bfa(U, L, G, W):
    res = solve(W, L, U, G)
    return res


def func_e8f5a72216d14639ac84190f214524d8(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    return W


def func_e59e3b214b714834a2493b8b598107f5(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    return line


def func_3baf6749d2cc4c2286d09ae39fda04e1(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    return Ln


def func_aa3c563550cb43fd871ccd9b4421c13e(line):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    return Un


def func_d6d097b5d2574358befe36e235d7214a(line):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    return W


def func_403109ab73c442b7959f17894d1c090b(line):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    return Ln


def func_e1ed3d53c3b9430a9db92171361236bb(line):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    return Ln


def func_3e45ff94cb4c4519bfccd410555287c7(line):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    return Un


def func_a7945af4c8ca41d297d3a5fd10b3ce29(line):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    return G


def func_1f3e98fafead4c2bbf9e721bac96d5a1(line):
    Un = int(line[2])
    G = int(line[3])
    L = []
    return L


def func_e0c9f33e6f704a8db00e5f3039b7d8a2(line):
    Un = int(line[2])
    G = int(line[3])
    L = []
    return G


def func_01de4c4411dc476cbcc8afc244edea89(line):
    Un = int(line[2])
    G = int(line[3])
    L = []
    return Un


def func_31d4f74e030740c29c561c44f2861f25(Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return i


def func_d06b754f8d664f369190cddab3760cd0(Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return G


def func_722c4b93d7a04aa489eaead68152dda4(Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return y


def func_e824bdd90d074d7788836e5ceb22ebc7(Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return L


def func_b3388629b8c6413582013e4e800be3f1(Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return line


def func_02688e3ae2674c459f60fe462b9e2d69(Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return x


def func_ee7d8fef27fb4450a16618ea87bd65e5(Ln, input):
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return i


def func_7d79c3f433a1492cb1e7e4547995e3fe(Ln, input):
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return U


def func_000a91f7a5a74a8a9b1d448b8ec0c086(Ln, input):
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return L


def func_3bdde1b73f0849a5b0c87a36348c2149(Ln, input):
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return line


def func_d8ebc7024a0043429eab57cfc997ab16(Ln, input):
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return x


def func_2b08fcf5eee145f8b90bcd11c4dff618(Ln, input):
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return y


def func_0998f80353774220a64925af8fc82b6b(Un, L, Ln, input):
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return i


def func_452ccff0a9d64658a263e048958dd669(Un, L, Ln, input):
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return x


def func_36f7950f75e64a14b9cd1f01fc83c708(Un, L, Ln, input):
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return U


def func_16f838b3bab949c1a2259b9de1499f3f(Un, L, Ln, input):
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return y


def func_5337e3c6fca0438394823be2459cba27(Un, L, Ln, input):
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return line


def func_db9cdef03617493fb8c8a07b0ba19dc1(Un, L, G, W, input):
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return i


def func_880ac35bf506454fb563c0076f115813(Un, L, G, W, input):
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return y


def func_3ea93f34d6a64811aefd9aad853144d0(Un, L, G, W, input):
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return U


def func_adbc88835466406cb436947796609b18(Un, L, G, W, input):
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return x


def func_59a61cd30a7b4c948193409ffa19371f(Un, L, G, W, input):
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return res


def func_bf04b97274ca427aa267a33d2ef325f4(Un, L, G, W, input):
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return line


def func_eb425d1af520427fabcc455b388094ca(Un, U, L, G, W, input):
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return res


def func_4eedf41f2bc54097b5e002e06600a4de(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    return W


def func_0a04871730b7481ba74e6f587913a8cc(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    return line


def func_e394f349d7c3401aa1f94f676a5e4d45(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    return Un


def func_f290d17fbc344fb08f0448d3662a68e9(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    return Ln


def func_25320480ce0a468d98cda472f0782efc(line):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    return W


def func_ecd91b3f34b94283a16b37d392e7ba80(line):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    return Ln


def func_4f4053b375ed462eaeb21f8c6bf17f28(line):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    return G


def func_df3a759b0aa540cab7e8c0b44b1b8bc4(line):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    return Un


def func_355add9c25ef48859befbf1860374525(line):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    return Ln


def func_58ab23659ba44a88b726ddecda4bff6c(line):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    return Un


def func_4352ff6cbbcb4f748454b32517d41ad5(line):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    return G


def func_2a5676e8ac0f45c2bb0cd7e75d35f272(line):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    return L


def func_c2fb5e9d86544b8d97e9e9a4d8d56ddd(Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return Un


def func_d15e752f2f0146a898075201f2690af0(Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return i


def func_5170b9d4984a465ea7f0143f1240e0c8(Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return y


def func_ddc200c9f313474fa00e5b83375f05b1(Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return G


def func_139d0c9028514314845bfe08783d0949(Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return L


def func_47f2587f7711420799d175ab8838a94e(Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return x


def func_137bdc4e20ea4ddfbcf01408310f8ec6(Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return line


def func_80b102bd2ba347a5834a25b2bda6971e(Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return x


def func_4d22390f48b34ef0b977d81d53296d51(Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return L


def func_51bbede9293049f8a0646a4971aa36aa(Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return U


def func_7086160e4d13483ba2b5d7c8f42e604d(Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return line


def func_26991f41683548c6bd5f0a786c1b96da(Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return G


def func_6c711a60d64844fdb72823b1884682a4(Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return y


def func_5f63bd39cb0342748f2cdea04a8c935b(Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return i


def func_7149d9f295d74c51bde92024831f0cee(Un, Ln, input):
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return L


def func_8608f68e75eb469e8a988c474002389a(Un, Ln, input):
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return line


def func_8ac4d7103234491791fb53bc63a33f69(Un, Ln, input):
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return U


def func_6c1b02c02b0d42b684a7b2df9d03d75d(Un, Ln, input):
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return y


def func_8de73e889a6d46a491b18a5429d668ab(Un, Ln, input):
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return i


def func_f49275c92d8c4ffdb4b37686f3d012e0(Un, Ln, input):
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return x


def func_a76dd9ec36ac46c0876f33ccb9ab678c(Un, L, G, W, Ln, input):
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return i


def func_e67dc2858d5442309637a74315fbb792(Un, L, G, W, Ln, input):
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return res


def func_a341879312a849e38dbb32101c83313e(Un, L, G, W, Ln, input):
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return x


def func_c6f48c78fe7349449b85263987e50e90(Un, L, G, W, Ln, input):
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return line


def func_2a2c5b0d3e7a4e73a06323c4aa56c3db(Un, L, G, W, Ln, input):
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return y


def func_a951cc4468814bb49ca1385fc48f94cb(Un, L, G, W, Ln, input):
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return U


def func_29d8038897f2446eae2a8412e79552d5(Un, L, G, W, input):
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return res


def func_dfa76206dc884fe4bca9f982a0c55085(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    return W


def func_1747b2af2e5e4205bc8f05e5ec0d589a(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    return Ln


def func_be7d61fbacfc43549f1a4b3bc4378ccf(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    return Un


def func_54de44beb8a54c91b8daae7868b56768(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    return line


def func_4c492ee72abc49fa927c30014c7279bc(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    return G


def func_10fb86feff80419cb1b009ba7033a31d(line):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    return Ln


def func_00a19c5f68b649cfb06e0f8dbe09498b(line):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    return Un


def func_520d0f875e8648ef8eacd4592a740fc1(line):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    return G


def func_0fe1e5423e8142f4a3083c60c3921628(line):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    return L


def func_8810c23f8e5d40c2a3efc7c5ade3b051(line):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    return W


def func_3c3ffa013d544da1b72608556e3321a1(input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return y


def func_e347c5f0c06146619427e085cbcb8650(input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return line


def func_32b8e2725bee4590aa2e0b55d5390fab(input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return i


def func_6e3a9d6182824b61bceca194113d16ad(input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return x


def func_a81f3aad01ac4ca7a1b33b4a33a5db4d(input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return L


def func_1579594d6c8b45149209bfc841a68555(input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return Un


def func_4be9bde85b4a46f9b7114ddd6248e165(input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return Ln


def func_5384de55393f4cc5a3ae2170d9c84515(input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return G


def func_eec5ebe603a64af6956be4038f9e9097(Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return U


def func_65b0893033464d9482af2af16e1720fa(Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return G


def func_99b382b7cdce4d13bda2077b5ac3e72a(Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return y


def func_8d4800522f124109b06264829936afb5(Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return L


def func_7fd772f7a7964204a45a5c44546b6d67(Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return line


def func_ac9d530b505644ec87e5e93196adc7aa(Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return Un


def func_ba64407588d840e498b2bd3c97f3238c(Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return x


def func_6d8d567545fb48d7950134dfa112d638(Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return i


def func_fc8b7a225ede4f7c98dcd410929f39f0(Un, Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return U


def func_e85529ef321240c9afcca69fcb2d9c5e(Un, Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return x


def func_87050cdb8607439d9f3d935a66464dc7(Un, Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return line


def func_e1e713ef13694326844d64cdac74741a(Un, Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return i


def func_0cb0e83041ea41f49f8295f2cf4638ce(Un, Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return y


def func_9499a5faacc04791a29f5e3fee75646d(Un, Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return G


def func_18fc7d9282ad44e791a0058ab5333dbe(Un, Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return L


def func_7bc8337191b4449c90ddf31207e87ea9(Un, G, W, Ln, input):
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return y


def func_9fe3584561c5405da11e1a066179efcd(Un, G, W, Ln, input):
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return line


def func_d877d4e44daa40699358b78d3efe777d(Un, G, W, Ln, input):
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return x


def func_67214fb92d5b4d2da7375e6a4320b42a(Un, G, W, Ln, input):
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return L


def func_3991fe830c364b38879381dfc2e3de82(Un, G, W, Ln, input):
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return res


def func_475e4f6fcd7347ee9b3071136648852c(Un, G, W, Ln, input):
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return U


def func_21c6916ab62643a0a0558869f367cdbb(Un, G, W, Ln, input):
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return i


def func_e90c9b46392348f8ad179e1ad168b6c5(Un, L, G, W, Ln, input):
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return res


def func_b0380b4133ea4ae4a68aefcff139b45e(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    return G


def func_a05e8dff6777452ca17909089229470e(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    return Un


def func_5f73f103a32b49bf952e23ab13630673(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    return W


def func_8eed08d7427b44fa8b03ae60259272ff(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    return L


def func_745e97d8065e4437a2ab564ef11d801d(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    return line


def func_726fc0a53ae542718f18045a54a8cea3(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    return Ln


def func_6ff77fe57f5e4a47890f0d01069804e3(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return W


def func_ef80265d979b42979e584d44592bdbfc(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return Ln


def func_701fe4f612224e27817a283667109807(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return line


def func_0e74a9733154408780e458ab157ece47(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return y


def func_afcb5c9dda304cdcb14314e9f814fe77(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return Un


def func_0c0ec6f2732749d2964e67a6629252a6(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return i


def func_5f7c62cd0f484926b6a79f6dea1a7c31(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return L


def func_94aec3574713417a9fd1fcd7e49dd500(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return x


def func_c72d1c8955c74c1891dbad21c6534ecd(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return G


def func_17081acf36bd491d93676e5952f804d9(input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return Un


def func_4edc498d551b43cb87af148d0f9e8d4e(input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return L


def func_7def63cd1abd4571abb25522a85731f7(input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return y


def func_09a475df0833405fb8f19d642f6b43f7(input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return Ln


def func_b8ff44d76f794bdda2ee945a6305b9dd(input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return line


def func_395e4271ca134c71ae8eab6d3f2e3111(input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return i


def func_7656621a59cf4bd8b81b240234ea4779(input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return x


def func_4958ac5824694f3d8a1937387f0fe9f2(input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return G


def func_f65ea19fc4344e81aa565d3ccaa78ee5(input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return U


def func_e667567fc90943aa837ed71391faa6d4(Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return G


def func_a4f8c9a98e7c40389d262babd11ee7c4(Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return x


def func_2df27e9ba9254424af1bb5443b3f33a5(Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return y


def func_cb9ddc4eb50b4f52ba892b18e9221bc8(Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return line


def func_14c341cb0d1f4b3dbabde214cc483748(Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return Un


def func_767d549bea794cb3abc87c7d31d57e53(Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return U


def func_f995579384894558aa9a8fd4a256f031(Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return i


def func_52a8b2f91c4b4f8b840ede0412787721(Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return L


def func_08811cf9d3454ae3a8b8810cebda29f5(Un, W, Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return line


def func_edca8bfea0ff451ca448bc4cd80cdfa8(Un, W, Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return res


def func_d70ba3d7c60e4dc4910ca24912c1befd(Un, W, Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return i


def func_9fc1da4e84cf4bcc8e82a6eb20d23c93(Un, W, Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return L


def func_814a5c95c08c4f3aaf706378a0eb50ba(Un, W, Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return y


def func_aaec1d41f16d41639fbe4001333f600a(Un, W, Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return x


def func_87b7507a791e45649ff67cc9d72d0e32(Un, W, Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return U


def func_7761a2fc721b42979b9e8e300097e0a5(Un, W, Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return G


def func_53e46d0240ff45e3b48e57b480a4ac88(Un, G, W, Ln, input):
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return res


def func_0c291a448c8643a081df629b9dd3920b(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return Un


def func_8ff168152f124008b52444156c183f0e(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return L


def func_aaead9d89dff4996a2e222e1b58ea8da(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return W


def func_5b5674701cba458d904aa8b19918c795(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return G


def func_7840a56381934978a9e403dd81075c7f(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return x


def func_f1f1bc0421ae40538830be90a11b9e63(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return line


def func_ecb35af1e9f94c49805d513c42c4b756(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return y


def func_4ce8c87f24de46bbb68f4c6830db1933(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return Ln


def func_274c29e3e1244da3b1b5d8eb82909935(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    return i


def func_8b249f43a02344e3937a53df149f940e(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return i


def func_91cf33ea3dcc4f24b8b9406a5f2101b1(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return line


def func_73e3bbc45d89414e8d03cbb496a9cea1(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return y


def func_961541194efa4e82b4401054eb12f225(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return x


def func_cae936e9e42e426eb0c0fc38c2e313d9(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return Ln


def func_dd086ff8e08a4c7fbdc7c5716a167710(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return G


def func_1034ce88e7a746db9ee2f27bc9b38cb6(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return W


def func_2eb22b3eaa944ea697f9ab683a313a9b(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return L


def func_c0094d0f670d42b38962d9e06ab25adc(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return U


def func_fef22b20348a4fb7b37e0cbb71e50707(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return Un


def func_4f612b42db234ed498b71b4f3791c68c(input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return x


def func_00b9dc9bd80345eea12b41e1a103ae5c(input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return Un


def func_6d2fd5cfa7be471d8b68d3c15333c5b7(input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return i


def func_bf383be0c4154071965497e0ca0e6452(input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return y


def func_bbc2b84f4c8e42a4bc1df5ae3f7c4a81(input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return G


def func_72e21e059ad249a5a4629442c6e41cb0(input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return line


def func_e895bc49a26943d5a0d8f717bbab0de4(input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return U


def func_cc04bbd70fa6463783f918db4859e1ba(input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return L


def func_abed7c8e17804f16b45d3b10e4191f6d(input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return Ln


def func_7d38160a11d14357bbfeeba721ee1e02(W, Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return i


def func_81563792259d46ebb3f1e683c28e3198(W, Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return line


def func_2bc4ca6dd1d844a8af484ce721c1b8fc(W, Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return G


def func_a241ca65bec8415ba481bb4483510f98(W, Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return res


def func_0a950d3e16694eb3ad9dc1d5f9833345(W, Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return y


def func_74e6642c1cb84eccb5bfcfce673cae00(W, Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return Un


def func_993cbab5a8ba45a0a16db87f66306f82(W, Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return x


def func_896778f8096a4cb7bef6ab941e445e00(W, Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return U


def func_539a134fd8bc407bb419d520b946c25a(W, Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return L


def func_55290d6c9c394087b7b3c56d3cfbc080(Un, W, Ln, input):
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return res


def func_7dd8a34c0ee14abfa8f10aae6f16f0dd(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return U


def func_fc66b4484a84489084474f440c6ce556(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return Un


def func_c254d0250514416189e4a7885b708610(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return y


def func_67366f31fd72438984d6b0a24e7921ed(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return i


def func_dd3f5458444b447594a7bfaa29fb85c9(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return L


def func_8d20ed8cef9e48be9dc7da17f739cbc2(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return W


def func_5718f4a197a944beb35c1cd8d03f462b(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return G


def func_9420cb37818949faa39572475df263f2(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return line


def func_e788327d52d94146b4829e7276856490(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return x


def func_ebb4f150007e48b18ff9d58441f59c9a(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    return Ln


def func_1e2426182b1e4094ab7c37ee4b29c4c8(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return G


def func_7003544133d74421ad034af577f491b3(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return L


def func_259b02e84f714162b3ff6c21c36b3439(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return line


def func_b5c76355b2bb4f8f817b6dcb93e36368(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return x


def func_25eff4c7c18443668715c5e60182c1d8(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return W


def func_c4807925ed4647c384a5054c5e5dd8bb(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return y


def func_7ce2921aeba34378a4e61f7fe30ec167(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return Un


def func_455411b861aa40c7957e3856165b5e77(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return i


def func_1e9c64d214ed4cb895ad1c723d2438ed(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return Ln


def func_a6a8a0f44c584a7189e7e98c24e1f189(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return U


def func_0dea3f178a024d9e8a91c52afe6d3cd4(W, input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return L


def func_7ee1d90da0664d18a0823df5755d1228(W, input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return U


def func_4e53eb07ca1b47a7b8a55e00f167ff61(W, input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return res


def func_71ae69fc71c64555b263a67363ea363b(W, input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return line


def func_f6fe25c98a9146a5ab3ec3bf46ea8aae(W, input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return x


def func_0d1b974d04ce4d939b84884a6814ca38(W, input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return y


def func_00bcbb790547449cbb482c765d2ca1cc(W, input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return Ln


def func_bed90db4270a47a680974045813ed96c(W, input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return Un


def func_b04fd5e684c54452a5f2c914eea16ea6(W, input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return G


def func_39233f8032d04038a86a84d3dfe8cf42(W, input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return i


def func_c30d4656fa194eb488992991c3ddad5c(W, Ln, input):
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return res


def func_a9182e627ed84fc091bb7ac5b617d822(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return Un


def func_3145944526ed4473b0e633ed5638615f(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return G


def func_06576485cd1040a690e47b374a3c6a2e(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return x


def func_a876d98e02084d3daadb2bfcb64c38ad(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return y


def func_49315becc94d49c99c862e192f4396f9(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return Ln


def func_a55741f070cc422dbc4d162dfd67a14e(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return i


def func_e06084b9b1d64249ac7a0786210130ab(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return W


def func_aeba6b324ddb4c4386d93cba5c3300bc(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return L


def func_9987175cb61e4aab96de6de041d5bb8a(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return U


def func_831496497c12427b834d4414b3f01621(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    return line


def func_b60128b40bd94a61a079457e245bd77c(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return L


def func_de990fecc5414ab5bfc25f2d0625accf(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return y


def func_4f545e0a4dc24b6c8487255c3a080e4e(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return Un


def func_fd694bbb186240848235a008001c134b(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return x


def func_3a86037428ee4da09ce6dd1ddb68d88f(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return line


def func_1578aa5f8d4d4df99e6bb55b7b4eab84(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return W


def func_c7a56953f66f4364901dcaaad00eaf92(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return res


def func_115f92f8e2f443289f7ca56f9d496f2d(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return G


def func_c47333d6722346a48e4c44dbb6f8aef7(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return U


def func_081f68165c1b43d0b529011e62c20e4c(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return i


def func_256e15e8329f45ee940208a997d2ce58(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return Ln


def func_22cb4bdd57ec484fb9652f08d9ea7354(W, input):
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return res


def func_3779f005fdcf434cafeb9722e0782875(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return y


def func_fe40d69c7a79414ab9b905d0c071e563(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return W


def func_94dca51d56b445da8362ca8bace6b92f(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return res


def func_ab3da2e76d314403a68737a338ef2fc3(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return U


def func_d87f640fa86e4d069344cd0f5a1d1bba(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return x


def func_fd12bf75414e4083a29bdce3997193d9(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return i


def func_dbb2389ff8a0483faab0789d802d3242(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return G


def func_98896768d2a5426881952af7ab32f614(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return Un


def func_29e8fed4b7654644bef4a565517ae8d0(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return L


def func_edb1c10038374cc1923998cdc96f36a5(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return Ln


def func_5c6501397f0f432784ccd082f63b4812(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return line


def func_00945088e28d46009efc32b692d44914(input):
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return res


def func_7168bbbcf6e44fb99691a406b3b7df49(input):
    line = input.readline().split()
    W = int(line[0])
    Ln = int(line[1])
    Un = int(line[2])
    G = int(line[3])
    L = []
    for i in range(Ln):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        L.append((x, y))
    U = []
    for i in range(Un):
        line = input.readline().split()
        x = int(line[0])
        y = int(line[1])
        U.append((x, y))
    res = solve(W, L, U, G)
    return res


def func_9193f9b0517d45abb373712c83f1ecaa(test, input):
    answer = do_test(input)('Case #%d:' % (test + 1,))
    return answer


def func_f0721f05951b40dbb0e4d52fdc356f7d(answer):
    for x in answer:
        print x
    sys.stdout.flush()
    return x


def func_a1ec747b699642ec9c05ceb60ea51573(test, input):
    answer = do_test(input)('Case #%d:' % (test + 1,))
    for x in answer:
        print x
    return answer


def func_8cbbf9f951664dad86ca26e52dc35e09(test, input):
    answer = do_test(input)('Case #%d:' % (test + 1,))
    for x in answer:
        print x
    return x


def func_f5adae8430b14015b6bdc25d8992130e(test, input):
    answer = do_test(input)('Case #%d:' % (test + 1,))
    for x in answer:
        print x
    sys.stdout.flush()
    return x


def func_7807e939148743689ffdd05d285048d3(test, input):
    answer = do_test(input)('Case #%d:' % (test + 1,))
    for x in answer:
        print x
    sys.stdout.flush()
    return answer


def func_4ecd40f710084c89b3530ea476cc8625():
    input = open('test_files/Y11R5P1/A.in')
    N = int(input.readline())
    return input


def func_28d3999253574769abf282b2ac823d8a():
    input = open('test_files/Y11R5P1/A.in')
    N = int(input.readline())
    return N


def func_c5bbfe1dc9824ae0b6e5d10f8750260e(input):
    N = int(input.readline())
    for test in range(N):
        answer = do_test(input)
        print 'Case #%d:' % (test + 1,)
        for x in answer:
            print x
        sys.stdout.flush()
    return test


def func_d038889772db42348d77b64b4ede44aa(input):
    N = int(input.readline())
    for test in range(N):
        answer = do_test(input)
        print 'Case #%d:' % (test + 1,)
        for x in answer:
            print x
        sys.stdout.flush()
    return answer


def func_29fe9ef318854d109896ff312d57ac59(input):
    N = int(input.readline())
    for test in range(N):
        answer = do_test(input)
        print 'Case #%d:' % (test + 1,)
        for x in answer:
            print x
        sys.stdout.flush()
    return x


def func_fc371c906f82476c970de2d77bea3722(input):
    N = int(input.readline())
    for test in range(N):
        answer = do_test(input)
        print 'Case #%d:' % (test + 1,)
        for x in answer:
            print x
        sys.stdout.flush()
    return N


def func_8530d6f1879f43a78fae90045190b111(N, input):
    for test in range(N):
        answer = do_test(input)
        print 'Case #%d:' % (test + 1,)
        for x in answer:
            print x
        sys.stdout.flush()
    input.close()
    return x


def func_e9e6c9e05bda4448a8942467d17ff899(N, input):
    for test in range(N):
        answer = do_test(input)
        print 'Case #%d:' % (test + 1,)
        for x in answer:
            print x
        sys.stdout.flush()
    input.close()
    return answer


def func_db95f9d7ce9d4cc799cc8ad15a506d48(N, input):
    for test in range(N):
        answer = do_test(input)
        print 'Case #%d:' % (test + 1,)
        for x in answer:
            print x
        sys.stdout.flush()
    input.close()
    return test


def func_e65102553c29421383d3371f71b6112c():
    input = open('test_files/Y11R5P1/A.in')
    N = int(input.readline())
    for test in range(N):
        answer = do_test(input)
        print 'Case #%d:' % (test + 1,)
        for x in answer:
            print x
        sys.stdout.flush()
    return test


def func_fc731d2a9ee043f0ac5a55d1198f1b96():
    input = open('test_files/Y11R5P1/A.in')
    N = int(input.readline())
    for test in range(N):
        answer = do_test(input)
        print 'Case #%d:' % (test + 1,)
        for x in answer:
            print x
        sys.stdout.flush()
    return N


def func_2568369f12e545d3b485462540efef64():
    input = open('test_files/Y11R5P1/A.in')
    N = int(input.readline())
    for test in range(N):
        answer = do_test(input)
        print 'Case #%d:' % (test + 1,)
        for x in answer:
            print x
        sys.stdout.flush()
    return input


def func_68163f108ddc4274b5991af7b0113dd2():
    input = open('test_files/Y11R5P1/A.in')
    N = int(input.readline())
    for test in range(N):
        answer = do_test(input)
        print 'Case #%d:' % (test + 1,)
        for x in answer:
            print x
        sys.stdout.flush()
    return answer


def func_b6e4db9e0b3348b1bf784744a28f81f1():
    input = open('test_files/Y11R5P1/A.in')
    N = int(input.readline())
    for test in range(N):
        answer = do_test(input)
        print 'Case #%d:' % (test + 1,)
        for x in answer:
            print x
        sys.stdout.flush()
    return x


def func_26b27a6d391848c7bbd24cac4be83bd8(input):
    N = int(input.readline())
    for test in range(N):
        answer = do_test(input)
        print 'Case #%d:' % (test + 1,)
        for x in answer:
            print x
        sys.stdout.flush()
    input.close()
    return x


def func_0138888116cc4566bf4e2d1a87b28206(input):
    N = int(input.readline())
    for test in range(N):
        answer = do_test(input)
        print 'Case #%d:' % (test + 1,)
        for x in answer:
            print x
        sys.stdout.flush()
    input.close()
    return test


def func_71ea7ae4ffb34b4c874fa85d6e12fdcb(input):
    N = int(input.readline())
    for test in range(N):
        answer = do_test(input)
        print 'Case #%d:' % (test + 1,)
        for x in answer:
            print x
        sys.stdout.flush()
    input.close()
    return answer


def func_05a0a6ceb30a4db6879b55038b360527(input):
    N = int(input.readline())
    for test in range(N):
        answer = do_test(input)
        print 'Case #%d:' % (test + 1,)
        for x in answer:
            print x
        sys.stdout.flush()
    input.close()
    return N


def func_3fe5b0f4bbb14f0b81b2d74b6736a3dd():
    input = open('test_files/Y11R5P1/A.in')
    N = int(input.readline())
    for test in range(N):
        answer = do_test(input)
        print 'Case #%d:' % (test + 1,)
        for x in answer:
            print x
        sys.stdout.flush()
    input.close()
    return test


def func_a5001f182c0148499728b0b020ef7d3a():
    input = open('test_files/Y11R5P1/A.in')
    N = int(input.readline())
    for test in range(N):
        answer = do_test(input)
        print 'Case #%d:' % (test + 1,)
        for x in answer:
            print x
        sys.stdout.flush()
    input.close()
    return answer


def func_3a877b8b3f7c4d5dbdfae58ff1f8cf93():
    input = open('test_files/Y11R5P1/A.in')
    N = int(input.readline())
    for test in range(N):
        answer = do_test(input)
        print 'Case #%d:' % (test + 1,)
        for x in answer:
            print x
        sys.stdout.flush()
    input.close()
    return input


def func_d6e60efaebd74dd790b0fb93291906a4():
    input = open('test_files/Y11R5P1/A.in')
    N = int(input.readline())
    for test in range(N):
        answer = do_test(input)
        print 'Case #%d:' % (test + 1,)
        for x in answer:
            print x
        sys.stdout.flush()
    input.close()
    return x


def func_1bd6dbd50cec4590bfd8cf49c86d4cc1():
    input = open('test_files/Y11R5P1/A.in')
    N = int(input.readline())
    for test in range(N):
        answer = do_test(input)
        print 'Case #%d:' % (test + 1,)
        for x in answer:
            print x
        sys.stdout.flush()
    input.close()
    return N

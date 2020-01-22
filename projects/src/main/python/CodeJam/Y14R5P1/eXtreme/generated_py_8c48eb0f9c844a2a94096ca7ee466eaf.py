import sys
sys.path.append('/home/george2/Raise/ProgramRepair/CodeSeer/projects/src/main/python')
from CodeJam.Y14R5P1.eXtreme.golden import *

def func_f5b8307516df4619a6dec15146a599fd(seq, i):
    lsum += seq[i]
    lend = i + 1
    return lsum


def func_8246c5d76cce460faa881e4077367742(seq, i):
    lsum += seq[i]
    lend = i + 1
    return lend


def func_a47fe98904ed4dd5aa830f5dbd413a6b(seq, i):
    rsum += seq[i]
    rbegin = i
    return rsum


def func_5d6f0fa04216401dbb355f7bc2f8ce35(seq, i):
    rsum += seq[i]
    rbegin = i
    return rbegin


def func_e25ed701a1b741a5826837dacf00d2cc():
    lsum = 0
    lend = 0
    return lsum


def func_15f11a5df5214aba8cab0ba2e2601a0c():
    lsum = 0
    lend = 0
    return lend


def func_6b88f3ee73634929a032745a09fa1dd9(seq, bound):
    lend = 0
    for i in range(len(seq)):
        if lsum + seq[i] <= bound and i < len(seq) - 1:
            lsum += seq[i]
            lend = i + 1
        else:
            break
    return lend


def func_85ced86fd2384e658c9455ff8cbc556d(seq, bound):
    lend = 0
    for i in range(len(seq)):
        if lsum + seq[i] <= bound and i < len(seq) - 1:
            lsum += seq[i]
            lend = i + 1
        else:
            break
    return i


def func_46ec2884213b45879f0b3ec8b78862ba(seq, bound):
    lend = 0
    for i in range(len(seq)):
        if lsum + seq[i] <= bound and i < len(seq) - 1:
            lsum += seq[i]
            lend = i + 1
        else:
            break
    return lsum


def func_40f170b11c494c5ca05133eda4cee7de(seq):
    rsum = 0
    rbegin = len(seq)
    return rbegin


def func_d48e268bdfb34290997726ef07035da7(seq):
    rsum = 0
    rbegin = len(seq)
    return rsum


def func_f3ef7c9ef0a64eccb2d1f931d9447612(seq, bound, lend):
    rbegin = len(seq)
    for i in range(len(seq) - 1, -1, -1):
        if rsum + seq[i] <= bound and i > lend:
            rsum += seq[i]
            rbegin = i
        else:
            break
    return i


def func_dc73e054cf724fd0b0e1f8f664dcaafd(seq, bound, lend):
    rbegin = len(seq)
    for i in range(len(seq) - 1, -1, -1):
        if rsum + seq[i] <= bound and i > lend:
            rsum += seq[i]
            rbegin = i
        else:
            break
    return rsum


def func_fea481f72ae04bd7b11223d6bd3b5cb6(seq, bound, lend):
    rbegin = len(seq)
    for i in range(len(seq) - 1, -1, -1):
        if rsum + seq[i] <= bound and i > lend:
            rsum += seq[i]
            rbegin = i
        else:
            break
    return rbegin


def func_6aaf01fd911147098b9ec38548c18555(seq, rsum, lsum, bound, rbegin, lend
    ):
    msum = sum(seq[lend:rbegin])
    return msum <= bound, lsum + rsum + msum, max(lsum, rsum, msum)


def func_6f089706201f47f4a06fc8afb2d6dc0b(seq, bound):
    lsum = 0
    lend = 0
    for i in range(len(seq)):
        if lsum + seq[i] <= bound and i < len(seq) - 1:
            lsum += seq[i]
            lend = i + 1
        else:
            break
    return lsum


def func_cb286d57c650443d9647a007ce1d2a3d(seq, bound):
    lsum = 0
    lend = 0
    for i in range(len(seq)):
        if lsum + seq[i] <= bound and i < len(seq) - 1:
            lsum += seq[i]
            lend = i + 1
        else:
            break
    return i


def func_a9b125358c0d4f9cb5b377fd0fcd0eb9(seq, bound):
    lsum = 0
    lend = 0
    for i in range(len(seq)):
        if lsum + seq[i] <= bound and i < len(seq) - 1:
            lsum += seq[i]
            lend = i + 1
        else:
            break
    return lend


def func_a7275c9a11ce45dd940563815939e485(seq, bound, lend):
    rsum = 0
    rbegin = len(seq)
    for i in range(len(seq) - 1, -1, -1):
        if rsum + seq[i] <= bound and i > lend:
            rsum += seq[i]
            rbegin = i
        else:
            break
    return rbegin


def func_fb828bc7cb2c419a81f6d9fb27f64eea(seq, bound, lend):
    rsum = 0
    rbegin = len(seq)
    for i in range(len(seq) - 1, -1, -1):
        if rsum + seq[i] <= bound and i > lend:
            rsum += seq[i]
            rbegin = i
        else:
            break
    return rsum


def func_ba05a54dbc9e413a815083f72189329e(seq, bound, lend):
    rsum = 0
    rbegin = len(seq)
    for i in range(len(seq) - 1, -1, -1):
        if rsum + seq[i] <= bound and i > lend:
            rsum += seq[i]
            rbegin = i
        else:
            break
    return i


def func_75ef0c8247e9473faaf5d8de75d9dc83(U, sm, seq, L):
    M = (L + U) / 2
    hs, sm, mx = has_bound_3_split(seq, M)
    return hs


def func_c6e757ecd5b8408cb6907bca31f474b8(U, sm, seq, L):
    M = (L + U) / 2
    hs, sm, mx = has_bound_3_split(seq, M)
    return mx


def func_058e8057b1b8461f9a6a0f158dfedf9f(U, sm, seq, L):
    M = (L + U) / 2
    hs, sm, mx = has_bound_3_split(seq, M)
    return M


def func_61dbb22e9dd34819b0c0c4937a9bc617(sm, seq, M):
    hs, sm, mx = has_bound_3_split(seq, M)
    if hs:
        U = M
    else:
        L = M
    return L


def func_3cea5b939b974831ab00c279efdc7825(sm, seq, M):
    hs, sm, mx = has_bound_3_split(seq, M)
    if hs:
        U = M
    else:
        L = M
    return mx


def func_724cbed8cce0433283bb4683fef3d33c(sm, seq, M):
    hs, sm, mx = has_bound_3_split(seq, M)
    if hs:
        U = M
    else:
        L = M
    return U


def func_cee5bd8917254b0aad05639b1dbb04fd(sm, seq, M):
    hs, sm, mx = has_bound_3_split(seq, M)
    if hs:
        U = M
    else:
        L = M
    return hs


def func_c7b1049be1114aa4ac77bec7b42c51f2(sm, seq):
    M = (L + U) / 2
    hs, sm, mx = has_bound_3_split(seq, M)
    if hs:
        U = M
    else:
        L = M
    return hs


def func_6c849c2839624e229e0b3e0a8b56d166(sm, seq):
    M = (L + U) / 2
    hs, sm, mx = has_bound_3_split(seq, M)
    if hs:
        U = M
    else:
        L = M
    return U


def func_6eb07cb57e964fbb921d8b9962ba781f(sm, seq):
    M = (L + U) / 2
    hs, sm, mx = has_bound_3_split(seq, M)
    if hs:
        U = M
    else:
        L = M
    return M


def func_683f4eaeb3b04ba081f8bdfc37711fea(sm, seq):
    M = (L + U) / 2
    hs, sm, mx = has_bound_3_split(seq, M)
    if hs:
        U = M
    else:
        L = M
    return mx


def func_4bb95937aefc41aa8847e3f5eb2b4125(sm, seq):
    M = (L + U) / 2
    hs, sm, mx = has_bound_3_split(seq, M)
    if hs:
        U = M
    else:
        L = M
    return L


def func_edd6508b40944f0aa7955a2642788700(seq):
    hs, sm, mx = has_bound_3_split(seq, 1)
    if hs:
        return float(sm - mx) / sm
    return hs


def func_a37251439488432aab05dee63e3b5f84(seq):
    hs, sm, mx = has_bound_3_split(seq, 1)
    if hs:
        return float(sm - mx) / sm
    return mx


def func_2051dc906766408b867c1cb240f99552(seq):
    hs, sm, mx = has_bound_3_split(seq, 1)
    if hs:
        return float(sm - mx) / sm
    return sm


def func_a2984d65408749fe9dbfab7b9f62073b(mx, hs, sm):
    if hs:
        return float(sm - mx) / sm
    L = 1
    return L


def func_e5fedfe51c5f4c5da5db0d11c083daab():
    L = 1
    U = 10 ** 15
    return U


def func_7f7b26849c774ce7ae0e1b803f1b79d1():
    L = 1
    U = 10 ** 15
    return L


def func_f57d7944fab848b38b8490c73bf59de9(sm, seq):
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    return hs


def func_b12ef238189945a5913015a7dc019ba1(sm, seq):
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    return L


def func_ac55179980dc4122871aebfdc6f1a814(sm, seq):
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    return mx


def func_4bae5028cbb248c2a8738dbac15cb464(sm, seq):
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    return M


def func_b59ae360c86544bc86c9ef9180fa413a(sm, seq):
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    return U


def func_626c2ff6be6a468ebda55bd66d029110(sm, seq):
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return U


def func_ff78c191ffd84f9e85f4a4db18996e7f(sm, seq):
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return mx


def func_b510edda7ac04db8b0f8a45aa299b8f9(sm, seq):
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return hs


def func_ba70768b9fe1431086dea0caa1bff0b7(sm, seq):
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return L


def func_1aad9871a0cf495a9883b13be8fa235d(sm, seq):
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return M


def func_28b2f0ad58a34a46b0d32af3030fce59(U, mx, hs, sm, seq):
    hs, sm, mx = has_bound_3_split(seq, U)
    return float(sm - mx) / sm


def func_3fe79e7eca4448a9b7237ce01f316f4f(seq):
    hs, sm, mx = has_bound_3_split(seq, 1)
    if hs:
        return float(sm - mx) / sm
    L = 1
    return sm


def func_6a242cc8d31040ffad38871e46141c4a(seq):
    hs, sm, mx = has_bound_3_split(seq, 1)
    if hs:
        return float(sm - mx) / sm
    L = 1
    return L


def func_9f2ef24dd70b4665ba68db0c35534d65(seq):
    hs, sm, mx = has_bound_3_split(seq, 1)
    if hs:
        return float(sm - mx) / sm
    L = 1
    return mx


def func_18f4193f2aa7413babc658d3568fbf55(seq):
    hs, sm, mx = has_bound_3_split(seq, 1)
    if hs:
        return float(sm - mx) / sm
    L = 1
    return hs


def func_67bd34367700480dba114e31dec9e9b2(mx, hs, sm):
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    return L


def func_d02453ee6af14e4eaed616ef577ab6be(mx, hs, sm):
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    return U


def func_60308a2af217420584f9f7cd34d8c51b(sm, seq):
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    return M


def func_760cc0ffa94e4e79a9e8b21f5db63c38(sm, seq):
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    return mx


def func_78e9c9cc53a04753a317d0a160ac7c07(sm, seq):
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    return hs


def func_71ac23ff1da04fe58bf0ac8dff24f065(sm, seq):
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    return L


def func_6d6762536dbc43488e306657d2cac0a1(sm, seq):
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    return U


def func_25412d0c6ebd40029914726d333424e6(sm, seq):
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return L


def func_530376e05a3e46d993577dd81500de4f(sm, seq):
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return M


def func_2b591972871e4cfe850500cd952c8a2d(sm, seq):
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return mx


def func_89c751f242c84515a0184000b6105cca(sm, seq):
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return U


def func_d6570e9cfe6d4534bf523f97cf9f32db(sm, seq):
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return hs


def func_020963ac70474a9398d9b4cd0759acdf(sm, seq):
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return float(sm - mx) / sm


def func_8b5546b144ce42a0a3b57828b97bcf67(seq):
    hs, sm, mx = has_bound_3_split(seq, 1)
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    return L


def func_bb4347bd4c7e4af3a3a047671efc381f(seq):
    hs, sm, mx = has_bound_3_split(seq, 1)
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    return hs


def func_d55856e0fa70497fba89d83d32275ae0(seq):
    hs, sm, mx = has_bound_3_split(seq, 1)
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    return U


def func_3372a697df484321aa10f1242147d25f(seq):
    hs, sm, mx = has_bound_3_split(seq, 1)
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    return mx


def func_5b6578a93da34850bd9c728d130e620b(seq):
    hs, sm, mx = has_bound_3_split(seq, 1)
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    return sm


def func_8a8f9120b8994e8f9335429dc3f04480(sm, seq):
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    return mx


def func_d170427b82744c0386aba5a2fd87d4a3(sm, seq):
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    return U


def func_a1e13627a89d42a5ab6d8d15ee2cf2c5(sm, seq):
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    return M


def func_ed1ebfa8a7304106830da5931a95430d(sm, seq):
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    return L


def func_587bb44e5c584a9d91ac027e27b8aeac(sm, seq):
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    return hs


def func_13682d4d3af048109cfcf66b2c0918cf(sm, seq):
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return hs


def func_a8a526f94d604fa29bae69fd92522859(sm, seq):
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return U


def func_ca605fe1f2cc404ba26d21dc35cc2835(sm, seq):
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return L


def func_02a958eacf334d04bd5c02a58b9f6c8d(sm, seq):
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return mx


def func_31fd12bbd453429d8be5ad94ad4d0a45(sm, seq):
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return M


def func_a6c3288f797f4a6b94a7858a702239ba(sm, seq):
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return float(sm - mx) / sm


def func_d7c239d79324446bbc2210d2666ffddd(seq):
    hs, sm, mx = has_bound_3_split(seq, 1)
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    return U


def func_73e3bdb9e609419baa2390f288bf154c(seq):
    hs, sm, mx = has_bound_3_split(seq, 1)
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    return L


def func_3f35e46305df400a929a6f26090ba3bc(seq):
    hs, sm, mx = has_bound_3_split(seq, 1)
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    return mx


def func_9ca631b4e8194a7a9f82f75246b53c93(seq):
    hs, sm, mx = has_bound_3_split(seq, 1)
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    return sm


def func_60a3e0b26b844e37bcc6ae43dc56a11e(seq):
    hs, sm, mx = has_bound_3_split(seq, 1)
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    return M


def func_4a31c272c0274b1e831381c9292cd513(seq):
    hs, sm, mx = has_bound_3_split(seq, 1)
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    return hs


def func_7db0bb275d0e458888537c425b06c1bd(sm, seq):
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return mx


def func_83adadf5d20041a6980603b1c03962bb(sm, seq):
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return hs


def func_aa673741ca24436a9914ce712cc20ac1(sm, seq):
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return U


def func_093b20847a194f83a98b54cc7a7ce85e(sm, seq):
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return L


def func_8b040a6882e9432fb12ab466907c3314(sm, seq):
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return M


def func_9ff2d06e643c41368902b7989ea92f25(sm, seq):
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return float(sm - mx) / sm


def func_72034a75318e44169339d01f71fe1911(seq):
    hs, sm, mx = has_bound_3_split(seq, 1)
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return U


def func_198663561eb84e1ea0519a20089add0d(seq):
    hs, sm, mx = has_bound_3_split(seq, 1)
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return L


def func_deae9e002cc74229b6561c55140104d4(seq):
    hs, sm, mx = has_bound_3_split(seq, 1)
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return sm


def func_cce20f7966ef4d27b3c1bda09708a195(seq):
    hs, sm, mx = has_bound_3_split(seq, 1)
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return M


def func_8e68e081a55d4c37869b3c4e2f416b2f(seq):
    hs, sm, mx = has_bound_3_split(seq, 1)
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return mx


def func_1ac00bbf78dc452c97535907f0145211(seq):
    hs, sm, mx = has_bound_3_split(seq, 1)
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return hs


def func_9d02077108c840ec91cbb75c22f95cc8(sm, seq):
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return float(sm - mx) / sm


def func_8052ac896faf4185a5572455b85ae21b(seq):
    hs, sm, mx = has_bound_3_split(seq, 1)
    if hs:
        return float(sm - mx) / sm
    L = 1
    U = 10 ** 15
    while L + 1 < U:
        M = (L + U) / 2
        hs, sm, mx = has_bound_3_split(seq, M)
        if hs:
            U = M
        else:
            L = M
    hs, sm, mx = has_bound_3_split(seq, U)
    return float(sm - mx) / sm


def func_2a240caae8fb42a7989209823733ada8(inf):
    N, p, q, r, s = map(int, inf.readline().split())
    seq = mkseq(p, q, r, s, N)
    return N


def func_3f1a9b69fd4e4f1cbd1694e212b87440(inf):
    N, p, q, r, s = map(int, inf.readline().split())
    seq = mkseq(p, q, r, s, N)
    return q


def func_a582c6d0781046c880df92bbb5265cd3(inf):
    N, p, q, r, s = map(int, inf.readline().split())
    seq = mkseq(p, q, r, s, N)
    return r


def func_81ca5f0a23314c3d95ff1e6193aef632(inf):
    N, p, q, r, s = map(int, inf.readline().split())
    seq = mkseq(p, q, r, s, N)
    return p


def func_ce03eced1ea84c75adbdce979d13d4bb(inf):
    N, p, q, r, s = map(int, inf.readline().split())
    seq = mkseq(p, q, r, s, N)
    return seq


def func_d0aee7f80a7d4a7485d1c4356add69d1(inf):
    N, p, q, r, s = map(int, inf.readline().split())
    seq = mkseq(p, q, r, s, N)
    return s


def func_d1f1b7a3572a4f5abc092763fbc5250f(N, s, t, p, outf, q, r):
    seq = mkseq(p, q, r, s, N)
    outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return seq


def func_0abcbfeb554e43f8b1a2a0122c6b0910(inf, t, outf):
    N, p, q, r, s = map(int, inf.readline().split())
    seq = mkseq(p, q, r, s, N)
    outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return p


def func_90ffbc38d5b14eb6b6427a91eb5842ee(inf, t, outf):
    N, p, q, r, s = map(int, inf.readline().split())
    seq = mkseq(p, q, r, s, N)
    outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return s


def func_60d33c2f0c9b45d5a4b3d3eade36881b(inf, t, outf):
    N, p, q, r, s = map(int, inf.readline().split())
    seq = mkseq(p, q, r, s, N)
    outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return q


def func_ea9ffc63163047d1836a85a2eb7451ac(inf, t, outf):
    N, p, q, r, s = map(int, inf.readline().split())
    seq = mkseq(p, q, r, s, N)
    outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return N


def func_46efafa8b6394c28b91821a77241f753(inf, t, outf):
    N, p, q, r, s = map(int, inf.readline().split())
    seq = mkseq(p, q, r, s, N)
    outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return r


def func_cc15d3cbf6f14a4abe209bb7d2d0b3c9(inf, t, outf):
    N, p, q, r, s = map(int, inf.readline().split())
    seq = mkseq(p, q, r, s, N)
    outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return seq


def func_8adc3753837641cabfc530529aee6b68(inf, outf):
    T = int(inf.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = map(int, inf.readline().split())
        seq = mkseq(p, q, r, s, N)
        outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return q


def func_5239d50b9ba148849052327388891ab9(inf, outf):
    T = int(inf.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = map(int, inf.readline().split())
        seq = mkseq(p, q, r, s, N)
        outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return p


def func_f4390a0c39d04de6a79996e0466c0c5a(inf, outf):
    T = int(inf.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = map(int, inf.readline().split())
        seq = mkseq(p, q, r, s, N)
        outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return T


def func_2c77aa23110a4fc5b8879821e2ab6d7f(inf, outf):
    T = int(inf.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = map(int, inf.readline().split())
        seq = mkseq(p, q, r, s, N)
        outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return t


def func_4194c182aaf64f859a84a9ff802dbe9a(inf, outf):
    T = int(inf.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = map(int, inf.readline().split())
        seq = mkseq(p, q, r, s, N)
        outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return seq


def func_32dd721a8de04818ac25d70737c3f740(inf, outf):
    T = int(inf.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = map(int, inf.readline().split())
        seq = mkseq(p, q, r, s, N)
        outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return r


def func_4f34860dd38f444290d7cccf4aab5119(inf, outf):
    T = int(inf.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = map(int, inf.readline().split())
        seq = mkseq(p, q, r, s, N)
        outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return s


def func_45f2c4adf9854acf8097b2f72d65766e(inf, outf):
    T = int(inf.readline())
    for t in range(1, T + 1):
        N, p, q, r, s = map(int, inf.readline().split())
        seq = mkseq(p, q, r, s, N)
        outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return N


def func_db98afb6527347e09f1b0917ae6fc4ec():
    infname = 'codejam/test_files/Y14R5P1/A.in'
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return seq


def func_d5a1e537e6654675958ce75e1ba64837():
    infname = 'codejam/test_files/Y14R5P1/A.in'
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return inf


def func_b0c9560166624a61b87e3b5c5a7f0d48():
    infname = 'codejam/test_files/Y14R5P1/A.in'
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return T


def func_80be2c2fb75a4170b56a3e2a9ac1309f():
    infname = 'codejam/test_files/Y14R5P1/A.in'
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return infname


def func_0dcad2708b144981aea6a42c41e43c33():
    infname = 'codejam/test_files/Y14R5P1/A.in'
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return t


def func_e0037959cc944e5f86afbfbb743ffbaf():
    infname = 'codejam/test_files/Y14R5P1/A.in'
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return s


def func_13d71db46cdc4ae4902797d88213f5b7():
    infname = 'codejam/test_files/Y14R5P1/A.in'
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return r


def func_3fd547b67504480a86f9893a40665150():
    infname = 'codejam/test_files/Y14R5P1/A.in'
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return outf


def func_44fca66c96eb425fa167bbc65b5db3c4():
    infname = 'codejam/test_files/Y14R5P1/A.in'
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return q


def func_913cb821b0204d019a9eb1f95f1ad429():
    infname = 'codejam/test_files/Y14R5P1/A.in'
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return N


def func_bb594e0109c244f3bfa068b12d396cf9():
    infname = 'codejam/test_files/Y14R5P1/A.in'
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return p


def func_933b73e91cce464787c93c0021b449f3(infname):
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    with open(infname.replace('.in', '.out'), 'w') as outf:
        T = int(inf.readline())
        for t in range(1, T + 1):
            N, p, q, r, s = map(int, inf.readline().split())
            seq = mkseq(p, q, r, s, N)
            outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return t


def func_babee6d0430c460e97f92693c428917f(infname):
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    with open(infname.replace('.in', '.out'), 'w') as outf:
        T = int(inf.readline())
        for t in range(1, T + 1):
            N, p, q, r, s = map(int, inf.readline().split())
            seq = mkseq(p, q, r, s, N)
            outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return N


def func_8e3516e9f5e64cd88e9e0a664ae5e2da(infname):
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    with open(infname.replace('.in', '.out'), 'w') as outf:
        T = int(inf.readline())
        for t in range(1, T + 1):
            N, p, q, r, s = map(int, inf.readline().split())
            seq = mkseq(p, q, r, s, N)
            outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return seq


def func_295e1ff72f8a4c9c9801c4ebf9d0151b(infname):
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    with open(infname.replace('.in', '.out'), 'w') as outf:
        T = int(inf.readline())
        for t in range(1, T + 1):
            N, p, q, r, s = map(int, inf.readline().split())
            seq = mkseq(p, q, r, s, N)
            outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return p


def func_51b9173711e74481b9ce53b7f4c9d2a2(infname):
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    with open(infname.replace('.in', '.out'), 'w') as outf:
        T = int(inf.readline())
        for t in range(1, T + 1):
            N, p, q, r, s = map(int, inf.readline().split())
            seq = mkseq(p, q, r, s, N)
            outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return r


def func_ea5d1ad4f84f4105a7783d899980ecc0(infname):
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    with open(infname.replace('.in', '.out'), 'w') as outf:
        T = int(inf.readline())
        for t in range(1, T + 1):
            N, p, q, r, s = map(int, inf.readline().split())
            seq = mkseq(p, q, r, s, N)
            outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return s


def func_4d9932d9f8a74f538f7bda1cb5574632(infname):
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    with open(infname.replace('.in', '.out'), 'w') as outf:
        T = int(inf.readline())
        for t in range(1, T + 1):
            N, p, q, r, s = map(int, inf.readline().split())
            seq = mkseq(p, q, r, s, N)
            outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return T


def func_5075bb6a34694eae9747728334915d7f(infname):
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    with open(infname.replace('.in', '.out'), 'w') as outf:
        T = int(inf.readline())
        for t in range(1, T + 1):
            N, p, q, r, s = map(int, inf.readline().split())
            seq = mkseq(p, q, r, s, N)
            outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return outf


def func_ccf37c7ffd27470ca5178774d099c1a9(infname):
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    with open(infname.replace('.in', '.out'), 'w') as outf:
        T = int(inf.readline())
        for t in range(1, T + 1):
            N, p, q, r, s = map(int, inf.readline().split())
            seq = mkseq(p, q, r, s, N)
            outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return q


def func_bf7313bca06d4543a6c3e0dfe962c82f(infname):
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    with open(infname.replace('.in', '.out'), 'w') as outf:
        T = int(inf.readline())
        for t in range(1, T + 1):
            N, p, q, r, s = map(int, inf.readline().split())
            seq = mkseq(p, q, r, s, N)
            outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return inf


def func_ce4bd6ed09e24562838141d61e22a7ae():
    infname = 'codejam/test_files/Y14R5P1/A.in'
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    with open(infname.replace('.in', '.out'), 'w') as outf:
        T = int(inf.readline())
        for t in range(1, T + 1):
            N, p, q, r, s = map(int, inf.readline().split())
            seq = mkseq(p, q, r, s, N)
            outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return inf


def func_0e2c9832a2aa4e5397de8c1b8c494a0b():
    infname = 'codejam/test_files/Y14R5P1/A.in'
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    with open(infname.replace('.in', '.out'), 'w') as outf:
        T = int(inf.readline())
        for t in range(1, T + 1):
            N, p, q, r, s = map(int, inf.readline().split())
            seq = mkseq(p, q, r, s, N)
            outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return p


def func_b61ed77be6234afa9623d62ebb35ac20():
    infname = 'codejam/test_files/Y14R5P1/A.in'
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    with open(infname.replace('.in', '.out'), 'w') as outf:
        T = int(inf.readline())
        for t in range(1, T + 1):
            N, p, q, r, s = map(int, inf.readline().split())
            seq = mkseq(p, q, r, s, N)
            outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return N


def func_87133ddcdb774a17be0d8f0b18d5abf7():
    infname = 'codejam/test_files/Y14R5P1/A.in'
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    with open(infname.replace('.in', '.out'), 'w') as outf:
        T = int(inf.readline())
        for t in range(1, T + 1):
            N, p, q, r, s = map(int, inf.readline().split())
            seq = mkseq(p, q, r, s, N)
            outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return t


def func_f65069db409746748ec8c8c33c0f6663():
    infname = 'codejam/test_files/Y14R5P1/A.in'
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    with open(infname.replace('.in', '.out'), 'w') as outf:
        T = int(inf.readline())
        for t in range(1, T + 1):
            N, p, q, r, s = map(int, inf.readline().split())
            seq = mkseq(p, q, r, s, N)
            outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return seq


def func_83c3c69c6d22441ea7c16c452c844977():
    infname = 'codejam/test_files/Y14R5P1/A.in'
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    with open(infname.replace('.in', '.out'), 'w') as outf:
        T = int(inf.readline())
        for t in range(1, T + 1):
            N, p, q, r, s = map(int, inf.readline().split())
            seq = mkseq(p, q, r, s, N)
            outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return T


def func_4d6df5e4c9a24ef6828a6d0f5dc82d2f():
    infname = 'codejam/test_files/Y14R5P1/A.in'
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    with open(infname.replace('.in', '.out'), 'w') as outf:
        T = int(inf.readline())
        for t in range(1, T + 1):
            N, p, q, r, s = map(int, inf.readline().split())
            seq = mkseq(p, q, r, s, N)
            outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return q


def func_8a2cfd93057948cbb77bcd298f44b507():
    infname = 'codejam/test_files/Y14R5P1/A.in'
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    with open(infname.replace('.in', '.out'), 'w') as outf:
        T = int(inf.readline())
        for t in range(1, T + 1):
            N, p, q, r, s = map(int, inf.readline().split())
            seq = mkseq(p, q, r, s, N)
            outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return outf


def func_e9900af0319e4c95a59ee124692b3471():
    infname = 'codejam/test_files/Y14R5P1/A.in'
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    with open(infname.replace('.in', '.out'), 'w') as outf:
        T = int(inf.readline())
        for t in range(1, T + 1):
            N, p, q, r, s = map(int, inf.readline().split())
            seq = mkseq(p, q, r, s, N)
            outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return r


def func_b6293ae1c50f4c47b26e9a5a7a121767():
    infname = 'codejam/test_files/Y14R5P1/A.in'
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    with open(infname.replace('.in', '.out'), 'w') as outf:
        T = int(inf.readline())
        for t in range(1, T + 1):
            N, p, q, r, s = map(int, inf.readline().split())
            seq = mkseq(p, q, r, s, N)
            outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return s


def func_7aba9394384b4ce1b372425deb7fc3eb():
    infname = 'codejam/test_files/Y14R5P1/A.in'
    with open(infname) as inf:
        with open(infname.replace('.in', '.out'), 'w') as outf:
            T = int(inf.readline())
            for t in range(1, T + 1):
                N, p, q, r, s = map(int, inf.readline().split())
                seq = mkseq(p, q, r, s, N)
                outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    with open(infname.replace('.in', '.out'), 'w') as outf:
        T = int(inf.readline())
        for t in range(1, T + 1):
            N, p, q, r, s = map(int, inf.readline().split())
            seq = mkseq(p, q, r, s, N)
            outf.write('Case #{}: {}\n'.format(t, search_max_bnd(seq)))
    return infname

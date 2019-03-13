import sys
sys.path.append('/home/george2/Raise/ProgramRepair/CodeSeer/projects/src/main/python')
from Y14R5P1.foxwlog.A import *

def func_a929b64f5a164141b7eff814496152ce(b_hi, a_try, S, b_lo):
    b_try = (b_lo + b_hi) // 2
    mid_range = S[b_try + 1] - S[a_try]
    return b_try


def func_5fa5f316cd294f9dbf75b1f8402cb156(b_hi, a_try, S, b_lo):
    b_try = (b_lo + b_hi) // 2
    mid_range = S[b_try + 1] - S[a_try]
    return mid_range


def func_a28d1d23da654cac8109d67b7b2ebcf8(a_try, S, b_try, N):
    mid_range = S[b_try + 1] - S[a_try]
    hi_range = S[N] - S[b_try + 1]
    return mid_range


def func_bf672db1516c427ca86a9200179e4c67(a_try, S, b_try, N):
    mid_range = S[b_try + 1] - S[a_try]
    hi_range = S[N] - S[b_try + 1]
    return hi_range


def func_3e4debf00e1b425a99d793913f0810fb(S, b_try, N, mid_range):
    hi_range = S[N] - S[b_try + 1]
    min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
    return hi_range


def func_2bc3588ccef34f62bff29e459cdfcd99(S, b_try, N, mid_range):
    hi_range = S[N] - S[b_try + 1]
    min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
    return min_max_mid_hi


def func_56d9e474f5fe407cbbb83cc9606d5edf(b_hi, a_try, S, N, b_lo):
    b_try = (b_lo + b_hi) // 2
    mid_range = S[b_try + 1] - S[a_try]
    hi_range = S[N] - S[b_try + 1]
    return b_try


def func_e386206e9cb44059ba4b413f99c506c3(b_hi, a_try, S, N, b_lo):
    b_try = (b_lo + b_hi) // 2
    mid_range = S[b_try + 1] - S[a_try]
    hi_range = S[N] - S[b_try + 1]
    return hi_range


def func_bb2258c21efb412085989c05c9e3ebc1(b_hi, a_try, S, N, b_lo):
    b_try = (b_lo + b_hi) // 2
    mid_range = S[b_try + 1] - S[a_try]
    hi_range = S[N] - S[b_try + 1]
    return mid_range


def func_6a9ac1a7e3da44f28439e3fbcc6d228f(a_try, S, b_try, N):
    mid_range = S[b_try + 1] - S[a_try]
    hi_range = S[N] - S[b_try + 1]
    min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
    return hi_range


def func_12ad554a819647fd9ec72c70f197022c(a_try, S, b_try, N):
    mid_range = S[b_try + 1] - S[a_try]
    hi_range = S[N] - S[b_try + 1]
    min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
    return mid_range


def func_cdab5d5c4f6d4795b37b2a22ea1f00bd(a_try, S, b_try, N):
    mid_range = S[b_try + 1] - S[a_try]
    hi_range = S[N] - S[b_try + 1]
    min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
    return min_max_mid_hi


def func_ebc700b58cc2414ba1edd73a6732b7a9(b_hi, a_try, S, N, b_lo):
    b_try = (b_lo + b_hi) // 2
    mid_range = S[b_try + 1] - S[a_try]
    hi_range = S[N] - S[b_try + 1]
    min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
    return mid_range


def func_90ad6a4f7190427487a40908aae774c9(b_hi, a_try, S, N, b_lo):
    b_try = (b_lo + b_hi) // 2
    mid_range = S[b_try + 1] - S[a_try]
    hi_range = S[N] - S[b_try + 1]
    min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
    return hi_range


def func_d32b6f03001b432bb1ae132f15393119(b_hi, a_try, S, N, b_lo):
    b_try = (b_lo + b_hi) // 2
    mid_range = S[b_try + 1] - S[a_try]
    hi_range = S[N] - S[b_try + 1]
    min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
    return b_try


def func_5257bb0f743f42a7aaf2f039087ae2b0(b_hi, a_try, S, N, b_lo):
    b_try = (b_lo + b_hi) // 2
    mid_range = S[b_try + 1] - S[a_try]
    hi_range = S[N] - S[b_try + 1]
    min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
    return min_max_mid_hi


def func_fb107cba36d74414909c5f2d92df10b7(S, a_hi, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    return a_try


def func_2df4239740db4729860e2d5efff82cf0(S, a_hi, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    return lo_range


def func_fd335c1d46fa4ce59090cbe0e35b9f1c(a_try, S):
    lo_range = S[a_try]
    b_lo = a_try
    return lo_range


def func_35378086c702453f8d76813dd90a2a38(a_try, S):
    lo_range = S[a_try]
    b_lo = a_try
    return b_lo


def func_91c088b065a64defa4723edb0f819d66(a_try, N):
    b_lo = a_try
    b_hi = N - 1
    return b_hi


def func_5efff94f187f4f36bf4d5315ce9a6ea7(a_try, N):
    b_lo = a_try
    b_hi = N - 1
    return b_lo


def func_3a0847c1b82b4ed886159c22d4671679(S, N):
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    return min_max_mid_hi


def func_23d74cd510cf43778b866513aa0537d7(S, N):
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    return b_hi


def func_564afe926ba14dc6b7e3b2aa3bc7b0f8(a_try, S, N):
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return min_max_mid_hi


def func_ab495c296e61499c8f90e2cfed919057(a_try, S, N):
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return b_lo


def func_26f74259b4aa44748e45bae7044e3b62(a_try, S, N):
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return hi_range


def func_18989b41dfbd47d38be07d7a3c6b9518(a_try, S, N):
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return mid_range


def func_0288a87c40c84565b087df5b5d307edf(a_try, S, N):
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return b_hi


def func_286d46fb544f4992beb61eadfdb8ef4d(a_try, S, N):
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return b_try


def func_f08222c9f25547bcbb6852a032eb9f41(lo_range, a_try, S, N):
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return min_solveig_score


def func_fdcbb987e34d4a619828096c2c94047b(lo_range, a_try, S, N):
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return b_try


def func_3808d452d2604616ba72cdc1ea0f81c9(lo_range, a_try, S, N):
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return hi_range


def func_0c6117232d174a2db96d1989962eaea0(lo_range, a_try, S, N):
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return mid_range


def func_632f2addd3ae414da075fded4aa9c5cd(lo_range, a_try, S, N):
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return b_hi


def func_e074ff65652f4f3585b6e3b461fb3dba(lo_range, a_try, S, N):
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return b_lo


def func_49d6b24b3065461bbefe9efbefb097ac(lo_range, a_try, S, N):
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return min_max_mid_hi


def func_7bf13712c6c447409a792cb51cd119e7(S, a_hi, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    return b_lo


def func_f13c38ca5e234fa5a5fcd9fbbd5eaf6d(S, a_hi, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    return lo_range


def func_cb1b419eb0644ad1a46d11ef7bbd589a(S, a_hi, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    return a_try


def func_99ca66e76bc045c88f53155dc16fcc12(a_try, S, N):
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    return b_hi


def func_040e346823bd4223a7e74e6a65253a84(a_try, S, N):
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    return b_lo


def func_692516aea4d246788d64b4c1517905b3(a_try, S, N):
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    return lo_range


def func_0ac249c466f0471899e468dad1e5be64(a_try, S, N):
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    return min_max_mid_hi


def func_3d783b624b3945f1b768e7177a89a426(a_try, S, N):
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    return b_lo


def func_72bbd447c99a48dab876746729aff477(a_try, S, N):
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    return b_hi


def func_77d90af9798f4420b10751660699ad07(a_try, S, N):
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return mid_range


def func_dfbb55e24c3349f19051c3ae7689ab54(a_try, S, N):
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return min_max_mid_hi


def func_6c11d4a270a44c1a8d49b23d42af094b(a_try, S, N):
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return b_hi


def func_85f3576627f84c46853f8d4e13d018fc(a_try, S, N):
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return b_lo


def func_354e0d59dbf04f5ebe9935c2b4bb0b6b(a_try, S, N):
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return b_try


def func_c3d626c9138249a781ce9d752e9b4116(a_try, S, N):
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return hi_range


def func_7b0a634ec1c74bbfac580dee4d7eee4e(lo_range, a_try, S, N):
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return b_hi


def func_c30f74b561994fd481569c51b311239a(lo_range, a_try, S, N):
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return b_try


def func_27b1aed2d9454784915be124c7ce4b51(lo_range, a_try, S, N):
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return b_lo


def func_043e308589434a93b962b9c2be185c4f(lo_range, a_try, S, N):
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return hi_range


def func_21865cfb4722403bba1767d429158203(lo_range, a_try, S, N):
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return min_solveig_score


def func_6b15ca126c994266857803843f91a907(lo_range, a_try, S, N):
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return mid_range


def func_e84f4dc4bdf44a328469ee72a4ab61b1(lo_range, a_try, S, N):
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return min_max_mid_hi


def func_e2bf26cb08514b808a4e0f269140bd29(S, a_hi, N, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    return b_lo


def func_624fbfbe5d6e4e679bc56f3b69292bb2(S, a_hi, N, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    return b_hi


def func_e5a6aa58c69a457283c68865604369d2(S, a_hi, N, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    return a_try


def func_bf6e1abd5660488ea1f6a61d8665c32c(S, a_hi, N, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    return lo_range


def func_bbf0c3b39f134b4f8106c7bf9d8b8e16(a_try, S, N):
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    return b_lo


def func_fbb54a438c7047b691684d1bf2b6a9c8(a_try, S, N):
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    return lo_range


def func_c5c5c8d5b4be41cc8855bf50fa7b78a3(a_try, S, N):
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    return min_max_mid_hi


def func_6f795c988cf241389021a4c13e3fbfdf(a_try, S, N):
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    return b_hi


def func_0debde0978e644fd81b882a69288a01d(a_try, S, N):
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return mid_range


def func_97fb2d4f258c4bd6a615572b4a7e9dd6(a_try, S, N):
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return b_try


def func_b8749f7b6ba04de0a5e73b4c8afb27b0(a_try, S, N):
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return min_max_mid_hi


def func_8ae7873c909444b68250a1029ce763f3(a_try, S, N):
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return b_hi


def func_79624231f62f4c20b978a7b02af0adcd(a_try, S, N):
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return b_lo


def func_57ff3245767a4506ae240ba5c6bc7534(a_try, S, N):
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return hi_range


def func_356ed57e81e744ab9a1570c8d8b12539(lo_range, a_try, S, N):
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return b_hi


def func_63c5c299fadd4a779d6db9930b7f80c3(lo_range, a_try, S, N):
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return b_try


def func_6436ca98e0914be9b2df320c4e110c4c(lo_range, a_try, S, N):
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return mid_range


def func_b7660950a16445ab8298a83c45fa48e3(lo_range, a_try, S, N):
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return min_solveig_score


def func_1ca42bf4a8cb46d38deeb92cd7aea1c1(lo_range, a_try, S, N):
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return min_max_mid_hi


def func_e6fa30cb5ec34ad48e4ac09986c1cd69(lo_range, a_try, S, N):
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return hi_range


def func_efa374cb91a9421ab1744fa3316df141(lo_range, a_try, S, N):
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return b_lo


def func_301e56287fb245bd8e0268280bc5f910(S, a_hi, N, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    return lo_range


def func_7bf04fbf30e64148bd5e878051f7803a(S, a_hi, N, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    return b_lo


def func_e6ffd8c67cdc467485323c741b02d124(S, a_hi, N, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    return b_hi


def func_ac2b2b0b13aa4a38abf4d5c5cc421628(S, a_hi, N, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    return a_try


def func_07e2845e58c84478bcb46b2c9fb53164(S, a_hi, N, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    return min_max_mid_hi


def func_589a4b8e09914ba1a16568f22afbf132(a_try, S, N):
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return lo_range


def func_e2cc5ac035b14e3e9b3bb1b53bc14833(a_try, S, N):
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return hi_range


def func_66132682661a44a299f59609fa383f1d(a_try, S, N):
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return b_try


def func_1affa17eb0e14e94a1989780c72646be(a_try, S, N):
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return b_lo


def func_4146bfc444b542b68f92baa0555bda23(a_try, S, N):
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return min_max_mid_hi


def func_625370c783fc494494aaed4b3d43bafa(a_try, S, N):
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return mid_range


def func_6bb1c1c7c0074f4293c147710eb46f55(a_try, S, N):
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return b_hi


def func_28c16ee2a5e040de8eaa44333397ec60(lo_range, a_try, S, N):
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return hi_range


def func_aa05ba233f8340f7a3da98c68e2c28a7(lo_range, a_try, S, N):
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return b_lo


def func_e412c7f590614db6b58801d3531b4979(lo_range, a_try, S, N):
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return b_hi


def func_4fa68471f37942f496c65a337d6d7ad6(lo_range, a_try, S, N):
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return b_try


def func_1a0f5852a30f483d9f31d79d1e917793(lo_range, a_try, S, N):
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return min_max_mid_hi


def func_0661fd7545c44fdf9fa0f2d541db8cb6(lo_range, a_try, S, N):
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return min_solveig_score


def func_e60bec2733ba4bfb95bcfdfc876f6d95(lo_range, a_try, S, N):
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return mid_range


def func_ad913b20d3d54d01b05a0389497e9376(S, a_hi, N, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return hi_range


def func_8fde7227a6cb46549fdf543119fee28a(S, a_hi, N, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return b_lo


def func_be094c9e49ed428bb181244fc48d6075(S, a_hi, N, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return min_max_mid_hi


def func_823178e5208b416b88802c7d8442d3d7(S, a_hi, N, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return lo_range


def func_fb283a89539a4ab7bea6d1285b927d01(S, a_hi, N, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return b_hi


def func_2c645609b32346ee8cd39868c7edb004(S, a_hi, N, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return mid_range


def func_25380010f62746bea30efd768fad48c2(S, a_hi, N, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return b_try


def func_f0e2e034ebb044ea933ea7b2f1621e56(S, a_hi, N, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    return a_try


def func_aa7377acd5574f82844032d2b963a003(a_try, S, N):
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return b_hi


def func_41fc3730e63a4de0bd780a2a0af8a3b8(a_try, S, N):
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return hi_range


def func_69c887213375457685b15f97a75d5b6e(a_try, S, N):
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return min_max_mid_hi


def func_ee2c09da20464b59b9f796cf4c27e8ed(a_try, S, N):
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return mid_range


def func_3594a097ee3a48c4843b2f5d51cd8420(a_try, S, N):
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return lo_range


def func_ad871ea3211d4d8a8cce8d84d0d12f78(a_try, S, N):
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return min_solveig_score


def func_0f39a187ec344695aca36caf226f0c13(a_try, S, N):
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return b_lo


def func_6a51ca6e443e44a59e4e2240fae87b60(a_try, S, N):
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return b_try


def func_30d591285b6e4a36ac6942a1d40fdfcd(S, a_hi, N, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return b_hi


def func_184559930bbc4daf9c1d465084ad66b6(S, a_hi, N, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return mid_range


def func_4f1f960d8ec14357b4d4829ea326b084(S, a_hi, N, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return b_try


def func_ea4b04d469254ac49178c552c558b311(S, a_hi, N, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return min_solveig_score


def func_d1d833874c784f18b909f2f0311d745d(S, a_hi, N, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return min_max_mid_hi


def func_fec7be3261ac4118abeb70e40083a104(S, a_hi, N, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return a_try


def func_d787af2622894e7aba0da1ae5caecfd6(S, a_hi, N, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return hi_range


def func_d6081a0eba884413adc1d3635cf65a5b(S, a_hi, N, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return b_lo


def func_8a47147185274fc7b6afa3af7057f19e(S, a_hi, N, a_lo):
    a_try = (a_lo + a_hi) // 2
    lo_range = S[a_try]
    b_lo = a_try
    b_hi = N - 1
    min_max_mid_hi = S[N] + 1
    while b_lo <= b_hi:
        b_try = (b_lo + b_hi) // 2
        mid_range = S[b_try + 1] - S[a_try]
        hi_range = S[N] - S[b_try + 1]
        min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
        if mid_range > hi_range:
            b_hi = b_try - 1
        elif mid_range < hi_range:
            b_lo = b_try + 1
        else:
            break
    min_solveig_score = min(min_solveig_score, max(lo_range, min_max_mid_hi))
    return lo_range


def func_aa7439feb8dd489897993f1f30e97544(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    return S


def func_e8fe871761f74ce4a0504095d2e922b5(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    return p


def func_44c3633ba6e440f399f3ab082d181f77(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    return q


def func_c824b52f9785469c807c8dcaecb01964(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    return s


def func_6a63ed5f0e894f30a6763aed9f45e875(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    return r


def func_6b256a7d16364f80ba860fb7d8c4e5fc(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    return N


def func_bf529cbee23a4a41910956f144160cb9(N):
    S = [0] * (N + 1)
    S[0] = 0
    return S


def func_7ace25aab5a14b5bbb528d5fe3e33121(q, p, s, S, r, N):
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    return i


def func_e792d5a2b86942aea82fb1ccfe2ed927(q, p, s, S, r, N):
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    return a_lo


def func_aefc6f0513524baa946a9dcece18e824(q, p, s, S, r, N):
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    return i


def func_2d826c08780d44b584d04be8e5553a2a(N):
    a_lo = 0
    a_hi = N - 1
    return a_lo


def func_f63cca139311488eb5f4bbdc9c087b9d(N):
    a_lo = 0
    a_hi = N - 1
    return a_hi


def func_aa53e1b496ab4e32bb6e242bb8abd9fc(S, N):
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return min_solveig_score


def func_7d6cc8c5e60b4796a6885fee822ccfab(S, N):
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return a_hi


def func_9d31a2c0426847d6ae04fe9553ad4824(S, N):
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return min_solveig_score


def func_a822e0a890f149279db1e2326c8c47a5(S, N):
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return b_lo


def func_64835d65757945318c66309e704767b5(S, N):
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return a_lo


def func_d254c9ad1b21428b9153d004adf96419(S, N):
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return a_try


def func_fa4430d0243647caa50fe2643958a09c(S, N):
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return b_try


def func_f8694226a69a4877aefe09deb928bb5b(S, N):
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return b_hi


def func_c3090cb656ce413a99331918ebe29cde(S, N):
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return mid_range


def func_e83866e2078245f3842311e3cca6a21f(S, N):
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return a_hi


def func_377377b5c6b8452f983a93cd21ed6fe9(S, N):
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return lo_range


def func_d1092ea6e9694aba9a43406b4505df57(S, N):
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return hi_range


def func_54e89594e4154c3bb0473afe7603d5c8(S, N):
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return min_max_mid_hi


def func_7485e40138f842cea6632ae29a65498b(S, N):
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return '%1.10f' % (1 - min_solveig_score / S[N])


def func_7d30c31942e54e28a0691ca21baea833(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    return p


def func_e15ce5d4bdb9434f9703b09a44ab6afd(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    return s


def func_0072dcbd31a34ae99d15147ba031dbd7(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    return r


def func_ddc797a3c59f4423b32cb5b81a52a23d(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    return S


def func_3c8b5e5787224548af07f83c1832e062(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    return N


def func_f16d2018233a450d963fc12472ba911f(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    return q


def func_6013880d778d4cdfb15365a3c254159c(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    return i


def func_bf4f7b0ba1b942d4b5a171c35c25d3ad(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    return S


def func_f831ab17560c469992cf4abeb8afa4ab(q, p, s, S, r, N):
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    return i


def func_52b2b1acab61472db23a2f0db6e7ed0b(q, p, s, S, r, N):
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    return a_lo


def func_f402004d2dba442887a1ebd83d085b1d(q, p, s, S, r, N):
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    return a_lo


def func_b8783b623cd646d18561946ec10add2f(q, p, s, S, r, N):
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    return i


def func_718def6211cf47368883f23ea3a86715(q, p, s, S, r, N):
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    return a_hi


def func_b4dc8f19bd2845689ab8b02ec4a1ab20(S, N):
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return min_solveig_score


def func_e64ad58b862e4f2cafde14d66a22f705(S, N):
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return a_lo


def func_59ac52388024424093bb036ce42dad05(S, N):
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return a_hi


def func_9c00d845445c41b0924e14f36bc2a041(S, N):
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return min_solveig_score


def func_d35c48a2976d4827af2a7829ae707a78(S, N):
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return b_hi


def func_d8898e9568a248b793eb4a6511b77eb6(S, N):
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return mid_range


def func_26a63ef634d34ee8af6f1715d6338229(S, N):
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return lo_range


def func_343e7556a0c840fc818efac189f43fda(S, N):
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return min_max_mid_hi


def func_48e5dcf426a44a8e85d3aa68706e0a1d(S, N):
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return a_try


def func_bf18439771bd42b1a3a72e3ec213cf12(S, N):
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return b_lo


def func_173e6cf9bca14df68c6f3ffe9de5cba9(S, N):
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return b_try


def func_38058678b12344438b148ca477a0a3ee(S, N):
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return a_hi


def func_e1237d87ab8046b28efaeb44b281ab6b(S, N):
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return a_lo


def func_d258bf3496d6466c9cb4f6056b142e3a(S, N):
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return hi_range


def func_3e7b6117963e4078aee9c3c9eac94fe0(S, N):
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return '%1.10f' % (1 - min_solveig_score / S[N])


def func_c00f6c740dac4b5e9a33f94ac2c148bc(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    return r


def func_57cbe4dd03f845c093cfefff1a6fdfa0(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    return s


def func_6d21825c07bf44c3bba3b7a89f5dfae5(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    return i


def func_f881e1bdbdd1420da3d3c63c186538eb(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    return p


def func_509097a015044699ae68557d8ad06eb9(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    return N


def func_cfafd7969d2f456a8efcc7cd3a0f230d(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    return S


def func_8c72696695e5421ab49857c94a758e44(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    return q


def func_9ebff96c28d549a4b441cf40bcc02fcd(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    return i


def func_7b4e87013ec84bfab25ad2922b56f339(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    return S


def func_c7f4fd4a74134427901ce4b79079fac5(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    return a_lo


def func_4e3020b2761d45859d9be25ea99a9a5c(q, p, s, S, r, N):
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    return a_hi


def func_20e75bbb3031410583bb5df43273bcfa(q, p, s, S, r, N):
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    return i


def func_d289748279f14ad2a5fca83a02a8e5c9(q, p, s, S, r, N):
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    return a_lo


def func_ab102a4e7eb941a199a6e6e89494624b(q, p, s, S, r, N):
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return a_hi


def func_43a2279fe93e4ca092291f54df04f06c(q, p, s, S, r, N):
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return min_solveig_score


def func_29d3d79186414c34b6c2bf4352b7a05c(q, p, s, S, r, N):
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return a_lo


def func_4a77226f5c9f4bd6b314c60638a915fe(q, p, s, S, r, N):
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return i


def func_816cd99f64114977a51b8c64e37a75e5(S, N):
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return hi_range


def func_d79cf115b15c461ba1b4d26fde52e447(S, N):
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return a_hi


def func_f6fa005c3b20422d8d0972ccb8b69fb8(S, N):
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return min_max_mid_hi


def func_6c0d978311c24ba39bd3fbe3c9d48e24(S, N):
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return mid_range


def func_9e9b24c0a48c40f29356cc7ce5ed15a7(S, N):
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return b_try


def func_6b5f7795151d49c880154a3626740bb3(S, N):
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return min_solveig_score


def func_b07cdede1091412f890d38e61fa96182(S, N):
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return lo_range


def func_c18b1596ecb5468996f55b7060141f0f(S, N):
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return b_hi


def func_7d90da6e127c4709a3fe23e0f876dbb1(S, N):
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return b_lo


def func_9364dbd1265f4a95bd9810189e7833cb(S, N):
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return a_lo


def func_8f7ffb459be54fe9ab0eda69f3783ed6(S, N):
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return a_try


def func_3169f66a9fcd43e4988ec79dec1fb326(S, N):
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return '%1.10f' % (1 - min_solveig_score / S[N])


def func_29fcb12d87eb4166814d33a14548eb6e(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    return q


def func_453a62a63b8c453dacb793e5d5af0fef(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    return s


def func_6db5de2c7bab44d49335d90b6019462e(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    return a_lo


def func_d7bcf13b57c5471bbc12c1d404c1af7b(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    return N


def func_69565211a30a4fb58583c056bff54006(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    return p


def func_249685f6b92540258f6eb16be95465d7(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    return r


def func_27641967e78940888a6a2469473bef4e(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    return S


def func_7aaf34fee5094294b5d87bef86a611f4(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    return i


def func_080aa1ec159a42c099fc0a89758fc5e4(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    return i


def func_307f12d2b8714d15966532c5de6cf0ff(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    return a_lo


def func_21ed0f6361524fa3a3d5adacfe72450f(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    return a_hi


def func_d73464ce5fb34b1a8bd4d900480eb533(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    return S


def func_af09121e63234db6829b1d46f7462394(q, p, s, S, r, N):
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return i


def func_6becdee1d6f1466793fa8ad884134b9d(q, p, s, S, r, N):
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return min_solveig_score


def func_a59568c6333a432fbe0954864f6672e1(q, p, s, S, r, N):
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return a_lo


def func_69f8d91035494b7b9b6d67f734d31685(q, p, s, S, r, N):
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return a_hi


def func_3cd3c2bc9d034ab1b8643cdb324c7462(q, p, s, S, r, N):
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return b_try


def func_42794c26588a4db9bd1638cfbe935483(q, p, s, S, r, N):
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return lo_range


def func_41364de8811548ad97e82895796f72bc(q, p, s, S, r, N):
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return a_hi


def func_59e3aee2ee8941309180593a843fe77f(q, p, s, S, r, N):
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return a_lo


def func_c0ad36c4bb554279ab23447252ac32dc(q, p, s, S, r, N):
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return min_solveig_score


def func_9fe237c112954f0ba8d6ee384a133a00(q, p, s, S, r, N):
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return b_hi


def func_837a5f1977144a76bf953650d52806ff(q, p, s, S, r, N):
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return i


def func_a18dfeac491641d7b95f8fe511e13b89(q, p, s, S, r, N):
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return min_max_mid_hi


def func_451284c7b0604760949372bc3df2283a(q, p, s, S, r, N):
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return mid_range


def func_4c79d85b90ec4041adbddad557d7aca6(q, p, s, S, r, N):
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return hi_range


def func_a92adb82e4aa4b06a1192f38b84f60a5(q, p, s, S, r, N):
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return a_try


def func_a98a06b8732e41aa900ac468bd4b27ae(q, p, s, S, r, N):
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return b_lo


def func_dee3b458a696461ba314bee288a7effb(S, N):
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return '%1.10f' % (1 - min_solveig_score / S[N])


def func_10e2af57b46b433798fe01d65474ba9e(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    return a_lo


def func_f4252376ff884ea9beb3e450e2e145a1(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    return i


def func_9972e601d15a4bd79ea53fb404d6570a(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    return q


def func_d7d16187d4794ce8ae734a3e2a049eaa(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    return s


def func_e7e7673b4daa46a68c6361251d21bc11(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    return S


def func_bf04605d0b7f4894bca2b9bc8dc032ec(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    return p


def func_62a97feb55bb4dfb93632851997e1ae4(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    return r


def func_7e3f7148b6334ab388d98a40f65d689f(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    return N


def func_d6b588e2b8da45e8b7321c2cd528cdd3(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    return a_hi


def func_aee415cb57b2442283f1b850b84c60dd(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return a_lo


def func_4864ee7e27264f2da4e48b557c095da9(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return i


def func_fc609bdd35934603bf0988f924a19b81(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return S


def func_814f5831fcd04e9ab0c063fc890632be(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return min_solveig_score


def func_ec0be1694a56424abcc16cebcb039f4e(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return a_hi


def func_75ec0cfb932e400e9684c9d6f25f5b1a(q, p, s, S, r, N):
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return b_lo


def func_c5042e3487094a30b8ede09f9f34d2c9(q, p, s, S, r, N):
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return i


def func_1ad708bf665341f1a2a6ff14c1b1f299(q, p, s, S, r, N):
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return a_lo


def func_c271bac0a5534ec9877ece7d7c88704c(q, p, s, S, r, N):
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return min_solveig_score


def func_7a2321ea990143158c853d0876b58a32(q, p, s, S, r, N):
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return min_max_mid_hi


def func_ef103847806843e89d79ebd846cf1201(q, p, s, S, r, N):
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return a_hi


def func_e2ff827797264cb2bacd3db09dffc91e(q, p, s, S, r, N):
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return mid_range


def func_1824da60cd914b268d3425020612ae74(q, p, s, S, r, N):
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return b_hi


def func_a43470e6dea242b2bb941b3d74fdb191(q, p, s, S, r, N):
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return lo_range


def func_e3f35d4ae5f24c779d90a6a019471c66(q, p, s, S, r, N):
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return b_try


def func_61c34787af994c9f9a19db14df6db676(q, p, s, S, r, N):
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return a_try


def func_45a41154796c4467997590f56c7add3b(q, p, s, S, r, N):
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return hi_range


def func_c97f9b5a156c4db1b2c16b177736f865(q, p, s, S, r, N):
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return '%1.10f' % (1 - min_solveig_score / S[N])


def func_09e3b3047eb44ca48c71d07773f582bb(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return N


def func_415cdc120c3c41b3a6377ce15d0fd1ee(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return a_lo


def func_873ba470e1634bf485bb5a6d06e5bf87(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return min_solveig_score


def func_46762cc4aa424715bb48b282fe97d0af(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return r


def func_bef7ee7252c442d5805ee48349cd3117(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return a_hi


def func_36986491b4e24cfb9ce656bc92b4a434(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return q


def func_c99df8e510464f2198f719a0ea66bb43(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return S


def func_c56047b518d94584b5a0bf0122759218(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return p


def func_8e6d5a724e13408b9e94e208057afe9c(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return s


def func_94d0c66d99124774aeabb689857efb29(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    return i


def func_54f246a5afff4390b08b480893aa54f9(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return S


def func_342299cbfb42494bb8b76faabbc97f06(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return a_hi


def func_33caca6170814033b878637792b629a4(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return b_lo


def func_5ae7b76e0746411b8c9787f707a05a85(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return a_lo


def func_aeeaa23c5a3e4c86842a3993fd86510b(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return i


def func_a6465c02135d4e2b9d1206a49ec23e80(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return lo_range


def func_bbd1d7a462a2468b9c3cd1b295089e4e(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return min_solveig_score


def func_1387c9445c7042a2acf4d992801d15e2(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return b_try


def func_6bf038f152554d398cb896f3e29b9931(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return mid_range


def func_c2bf88ccb2e9435cb9bc91435dcff41b(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return hi_range


def func_56963062c5fa46b5a7cb18fcfb8ae565(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return a_try


def func_ad7f1e3821be4b65ad9e1b55f584cf6b(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return min_max_mid_hi


def func_0ee2983fb96b40238e5043bf21720fcb(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return b_hi


def func_2c219ccf4b864a8ba0bc324bc8465cd9(q, p, s, S, r, N):
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return '%1.10f' % (1 - min_solveig_score / S[N])


def func_029970d0bb1f4b728c9051a5bec901b5(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return lo_range


def func_fad33aa749864ac4b2bb5b37f3a76633(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return hi_range


def func_4952890eb5d04569b37e5c8e646cdbc4(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return S


def func_54bdc1d071864f7094cf7a17a66b0e3c(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return p


def func_f86d58d9a9174b489e17ab185a8417d4(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return min_max_mid_hi


def func_97983a784d6f40efa9e47a002ee32b79(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return b_try


def func_381518f2e30e407cb3a662f7ecd8665d(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return a_hi


def func_4c3925fc8a724ceb9cac84b166be0645(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return mid_range


def func_ea535b560582468f8ed38f9816156d22(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return q


def func_0620b118460d481a92dd785087e6e6c9(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return min_solveig_score


def func_c5f94364ba2544c98af32393ff28af45(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return b_lo


def func_97fbb6b249224e6ba83367d66cfcc34a(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return i


def func_5246f2f7adfe40168e662fbc6e102840(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return s


def func_7640c7c2027f42d2925307cf4f66cf4a(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return a_try


def func_d2dcfb1b9cd9403fbeafb041a8619e8f(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return a_lo


def func_a99cacec330d41d7b5531ade1d95b11a(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return N


def func_c75ebb571a4e4f0eb77dc622d3e04176(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return b_hi


def func_852d12de97e94fbaa8bd3e21a7da1c13(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return r


def func_c969a43995de4a44b36879c7fb4e68db(q, p, s, r, N):
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return '%1.10f' % (1 - min_solveig_score / S[N])


def func_4f0a114da425456993e7fd3c98c40500(infile):
    N, p, q, r, s = map(int, infile.readline().split())
    S = [0] * (N + 1)
    S[0] = 0
    for i in range(0, N):
        S[i + 1] = (p * i + q) % r + s + S[i]
    a_lo = 0
    a_hi = N - 1
    min_solveig_score = S[N] + 1
    while a_lo <= a_hi:
        a_try = (a_lo + a_hi) // 2
        lo_range = S[a_try]
        b_lo = a_try
        b_hi = N - 1
        min_max_mid_hi = S[N] + 1
        while b_lo <= b_hi:
            b_try = (b_lo + b_hi) // 2
            mid_range = S[b_try + 1] - S[a_try]
            hi_range = S[N] - S[b_try + 1]
            min_max_mid_hi = min(min_max_mid_hi, max(mid_range, hi_range))
            if mid_range > hi_range:
                b_hi = b_try - 1
            elif mid_range < hi_range:
                b_lo = b_try + 1
            else:
                break
        min_solveig_score = min(min_solveig_score, max(lo_range,
            min_max_mid_hi))
        if lo_range > min_max_mid_hi:
            a_hi = a_try - 1
        elif lo_range < min_max_mid_hi:
            a_lo = a_try + 1
        else:
            break
    return '%1.10f' % (1 - min_solveig_score / S[N])


def func_86049574033e4921bb8caf02e6d84d45():
    infile = open('test_files/Y14R5P1/A.in')
    num_trials = int(infile.readline())
    return infile


def func_03e2ddcb21d04488b80e499dc730ccac():
    infile = open('test_files/Y14R5P1/A.in')
    num_trials = int(infile.readline())
    return num_trials


def func_edf9f0ea5a6141c0a67ccbe3ce4ad8d8(infile):
    num_trials = int(infile.readline())
    for i in range(0, num_trials):
        print 'Case #' + str(i + 1) + ': ' + str(compute(infile))
    return i


def func_e1608241a27f428daaa59562161620b5(infile):
    num_trials = int(infile.readline())
    for i in range(0, num_trials):
        print 'Case #' + str(i + 1) + ': ' + str(compute(infile))
    return num_trials


def func_5d361ac601c649b495e4ae358afbfe75(num_trials, infile):
    for i in range(0, num_trials):
        print 'Case #' + str(i + 1) + ': ' + str(compute(infile))
    infile.close()
    return i


def func_5c49a8013fc8481f8da6cf6885917b81():
    infile = open('test_files/Y14R5P1/A.in')
    num_trials = int(infile.readline())
    for i in range(0, num_trials):
        print 'Case #' + str(i + 1) + ': ' + str(compute(infile))
    return infile


def func_83209f48fb7f4d8cbbb13ad60d066487():
    infile = open('test_files/Y14R5P1/A.in')
    num_trials = int(infile.readline())
    for i in range(0, num_trials):
        print 'Case #' + str(i + 1) + ': ' + str(compute(infile))
    return num_trials


def func_0ad1c99208574c6fae89382f0dd2ad46():
    infile = open('test_files/Y14R5P1/A.in')
    num_trials = int(infile.readline())
    for i in range(0, num_trials):
        print 'Case #' + str(i + 1) + ': ' + str(compute(infile))
    return i


def func_4d761e5a9ca741fc8a80caaa5bcc6519(infile):
    num_trials = int(infile.readline())
    for i in range(0, num_trials):
        print 'Case #' + str(i + 1) + ': ' + str(compute(infile))
    infile.close()
    return i


def func_f7ff0309b2e747daaaef480e7c0f401b(infile):
    num_trials = int(infile.readline())
    for i in range(0, num_trials):
        print 'Case #' + str(i + 1) + ': ' + str(compute(infile))
    infile.close()
    return num_trials


def func_fdf75bd6305e4c83b36667065fb0b502():
    infile = open('test_files/Y14R5P1/A.in')
    num_trials = int(infile.readline())
    for i in range(0, num_trials):
        print 'Case #' + str(i + 1) + ': ' + str(compute(infile))
    infile.close()
    return infile


def func_08ce530f195e4242813fca03d0cad88d():
    infile = open('test_files/Y14R5P1/A.in')
    num_trials = int(infile.readline())
    for i in range(0, num_trials):
        print 'Case #' + str(i + 1) + ': ' + str(compute(infile))
    infile.close()
    return num_trials


def func_c85dc8e6b5fc4002bfca3f8116616ad6():
    infile = open('test_files/Y14R5P1/A.in')
    num_trials = int(infile.readline())
    for i in range(0, num_trials):
        print 'Case #' + str(i + 1) + ': ' + str(compute(infile))
    infile.close()
    return i

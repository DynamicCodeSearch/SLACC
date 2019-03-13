import sys
sys.path.append('/home/george2/Raise/ProgramRepair/CodeSeer/projects/src/main/python')
from Y14R5P1.smapson.A import *

def func_975f2f69d9be431185c939abecb8443e(transistors):
    firstsum += transistors[first]
    first += 1
    return firstsum


def func_0406ef77134f4588ae52c6a86733dac1(transistors):
    firstsum += transistors[first]
    first += 1
    return first


def func_a65101ff32e44729a8ed6dec498a8b7b(transistors):
    last -= 1
    lastsum += transistors[last]
    return last


def func_a4f427727ad64af2a5ddcb97f1995bed(transistors):
    last -= 1
    lastsum += transistors[last]
    return lastsum


def func_394d43e3f4444269bbc4dc89407807a9(lastsum, first, transistors, last,
    firstsum):
    nextfirstsum = firstsum + transistors[first]
    nextlastsum = lastsum + transistors[last - 1]
    return nextfirstsum


def func_c2cb1538e64a43288e9c35458236c050(lastsum, first, transistors, last,
    firstsum):
    nextfirstsum = firstsum + transistors[first]
    nextlastsum = lastsum + transistors[last - 1]
    return nextlastsum


def func_70baa1957ffb4b4fad40e997fd1c87c6(nextfirstsum, transistors):
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    return last


def func_3832962b90ce461a844875a542115165(nextfirstsum, transistors):
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    return firstsum


def func_dc2eaeb46467434884aa069316cac49c(nextfirstsum, transistors):
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    return nextlastsum


def func_62f25bf96f2a44dd9844d10e226693ff(nextfirstsum, transistors):
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    return first


def func_6d0b1cf931ce47459da58f1400af3bf3(nextfirstsum, transistors):
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    return lastsum


def func_95645cfdb62c4b8fa49a0c9b83841399(nextfirstsum, transistors,
    transistorsum, nextlastsum):
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    return first


def func_e2d394dd3150444ab965b31839d08a46(nextfirstsum, transistors,
    transistorsum, nextlastsum):
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    return lastsum


def func_e46a3cc7be4e4460957b2ab857e8532f(nextfirstsum, transistors,
    transistorsum, nextlastsum):
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    return last


def func_932554b2174747d5bbb8a32879e21c31(nextfirstsum, transistors,
    transistorsum, nextlastsum):
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    return currentmax


def func_2905ceeddc524db98d85295d56ca0855(nextfirstsum, transistors,
    transistorsum, nextlastsum):
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    return firstsum


def func_604e247e7abc40a8b094bcf888bd8a08(lastsum, transistorsum, firstsum):
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    minimax = min(currentmax, minimax)
    return minimax


def func_db0315d0b09846d8aab468cfdbede918(lastsum, transistorsum, firstsum):
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    minimax = min(currentmax, minimax)
    return currentmax


def func_fa601000b0694ba2949c38c9c50a307f(transistors):
    nextfirstsum = firstsum + transistors[first]
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    return lastsum


def func_45c856d60293423e948518fc879a77eb(transistors):
    nextfirstsum = firstsum + transistors[first]
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    return first


def func_6c52d1ec139a4a78ac8af8428439c92e(transistors):
    nextfirstsum = firstsum + transistors[first]
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    return nextfirstsum


def func_d555187c80d841e7859f74b9e2c7e4b0(transistors):
    nextfirstsum = firstsum + transistors[first]
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    return last


def func_0d629ee1b3694760a1383baf60070e85(transistors):
    nextfirstsum = firstsum + transistors[first]
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    return nextlastsum


def func_6d63594e3dcd401a91382fae652404bc(transistors):
    nextfirstsum = firstsum + transistors[first]
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    return firstsum


def func_d099e9561b524985b0ad96fff92f1dbc(nextfirstsum, transistors,
    transistorsum):
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    return nextlastsum


def func_e0ec41b2d6264546aefc480695ac0ff7(nextfirstsum, transistors,
    transistorsum):
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    return first


def func_e053625d93ab4825846ba8ac103112ec(nextfirstsum, transistors,
    transistorsum):
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    return firstsum


def func_e7d2236a6a254fa59a413e3461794d32(nextfirstsum, transistors,
    transistorsum):
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    return currentmax


def func_78951733f3424975a3772f76eab1b0c8(nextfirstsum, transistors,
    transistorsum):
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    return lastsum


def func_77c540d601ee45ad81594fb9f24b8e58(nextfirstsum, transistors,
    transistorsum):
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    return last


def func_d182ed7e765448a6bed3ae97edee8ea7(nextfirstsum, transistors,
    transistorsum, nextlastsum):
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    minimax = min(currentmax, minimax)
    return currentmax


def func_9f9660714b3b4d02bc988266b66633a9(nextfirstsum, transistors,
    transistorsum, nextlastsum):
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    minimax = min(currentmax, minimax)
    return minimax


def func_8cf605e891d049e48f96793487c93d36(nextfirstsum, transistors,
    transistorsum, nextlastsum):
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    minimax = min(currentmax, minimax)
    return firstsum


def func_e9c105436f104758b0811f70b2100026(nextfirstsum, transistors,
    transistorsum, nextlastsum):
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    minimax = min(currentmax, minimax)
    return last


def func_a6330ac86cea4758b68939f467eaf9d0(nextfirstsum, transistors,
    transistorsum, nextlastsum):
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    minimax = min(currentmax, minimax)
    return lastsum


def func_7f34e6cc572a496aaa9e899b09f8f266(nextfirstsum, transistors,
    transistorsum, nextlastsum):
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    minimax = min(currentmax, minimax)
    return first


def func_f2293184932342a69c7506a56ccb8285(transistors, transistorsum):
    nextfirstsum = firstsum + transistors[first]
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    return currentmax


def func_6ef8edb74d93404883dcda272ce96b83(transistors, transistorsum):
    nextfirstsum = firstsum + transistors[first]
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    return nextfirstsum


def func_8e4f0352e67c4f70a0902e6d5f1f44b0(transistors, transistorsum):
    nextfirstsum = firstsum + transistors[first]
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    return lastsum


def func_50a81ce6818142caaec71f6a26fe2fa0(transistors, transistorsum):
    nextfirstsum = firstsum + transistors[first]
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    return nextlastsum


def func_b47c43f0d6ca4dd487aa61f196b2598a(transistors, transistorsum):
    nextfirstsum = firstsum + transistors[first]
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    return last


def func_fa8b3ed0a1d848a39e8a0c9f7caa5706(transistors, transistorsum):
    nextfirstsum = firstsum + transistors[first]
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    return first


def func_33a9fbca80a8419e8147beeebc1bd04c(transistors, transistorsum):
    nextfirstsum = firstsum + transistors[first]
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    return firstsum


def func_0f62693a32a04b6fa0c718c2260d1085(nextfirstsum, transistors,
    transistorsum):
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    minimax = min(currentmax, minimax)
    return currentmax


def func_a5738a2b29884c95af213f561f9c5be4(nextfirstsum, transistors,
    transistorsum):
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    minimax = min(currentmax, minimax)
    return nextlastsum


def func_14f22361f24c4aae8dbe20d27bb95412(nextfirstsum, transistors,
    transistorsum):
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    minimax = min(currentmax, minimax)
    return firstsum


def func_81b2bd30d0834149a5a5833fb7e30532(nextfirstsum, transistors,
    transistorsum):
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    minimax = min(currentmax, minimax)
    return minimax


def func_96d36ee2d95848e0a4c91f7e868ee824(nextfirstsum, transistors,
    transistorsum):
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    minimax = min(currentmax, minimax)
    return first


def func_56cb9801f05c475681ec8c491f2bff14(nextfirstsum, transistors,
    transistorsum):
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    minimax = min(currentmax, minimax)
    return last


def func_f11ff8546d0a436a83ddf508bdb16c68(nextfirstsum, transistors,
    transistorsum):
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    minimax = min(currentmax, minimax)
    return lastsum


def func_730e88351dd74162a7e612379972acab(transistors, transistorsum):
    nextfirstsum = firstsum + transistors[first]
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    minimax = min(currentmax, minimax)
    return currentmax


def func_b0e2d7d108e542a79530c5694dfccc0d(transistors, transistorsum):
    nextfirstsum = firstsum + transistors[first]
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    minimax = min(currentmax, minimax)
    return firstsum


def func_a0d9ee6ff81d4330baca4c700b49a456(transistors, transistorsum):
    nextfirstsum = firstsum + transistors[first]
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    minimax = min(currentmax, minimax)
    return minimax


def func_77cc6005adbf430e88bbcf3b6e6b32b3(transistors, transistorsum):
    nextfirstsum = firstsum + transistors[first]
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    minimax = min(currentmax, minimax)
    return first


def func_a8ed0c19014642e69029bd166e6af563(transistors, transistorsum):
    nextfirstsum = firstsum + transistors[first]
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    minimax = min(currentmax, minimax)
    return nextfirstsum


def func_b722854ba7e14fefb845115609fad431(transistors, transistorsum):
    nextfirstsum = firstsum + transistors[first]
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    minimax = min(currentmax, minimax)
    return nextlastsum


def func_771028eb77904428921cb4cd2b2f6b19(transistors, transistorsum):
    nextfirstsum = firstsum + transistors[first]
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    minimax = min(currentmax, minimax)
    return last


def func_5df90bb53e324c83a5f52f63026b5306(transistors, transistorsum):
    nextfirstsum = firstsum + transistors[first]
    nextlastsum = lastsum + transistors[last - 1]
    if nextfirstsum < nextlastsum:
        firstsum += transistors[first]
        first += 1
    else:
        last -= 1
        lastsum += transistors[last]
    currentmax = max([firstsum, lastsum, transistorsum - firstsum - lastsum])
    minimax = min(currentmax, minimax)
    return lastsum


def func_2bef54e30da9437f93eb3a275fa44039(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    return i


def func_4d374a08a2ab46e8b587038ec3471f62(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    return r


def func_7a4d4a6d80a4456cbbbcd499edd9b98d(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    return p


def func_24b9fb657bc44d7a87b3e7c609ecc519(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    return transistors


def func_7c2f3b767bf0460b8af24a8b3f82024d(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    return q


def func_7a0e6ff660944c8a8cbef530be6738ba(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    return s


def func_832532a581e04093b22af49e6c9f3251(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    return x


def func_4a08a1acb729484db07f07389bc64d3d(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    return N


def func_fe462b250e3b4878b264345263390eb3(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    return transistors


def func_61d3671003534e56903158aba2074282(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    return i


def func_cfaa4fa06f6b411a9a0bbd5079a38ebf(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    return transistorsum


def func_c080f973c26143d197f04158b1bd248d(transistors):
    transistorsum = sum(transistors)
    first = 0
    return transistorsum


def func_a0a226f3b84a45a3843974f71b9271d8(transistors):
    transistorsum = sum(transistors)
    first = 0
    return first


def func_daef88a4ef2c4f149242b921435b5112(N):
    first = 0
    last = N
    return last


def func_09f98dd3c37e41b080e6b695693fa7d0(N):
    first = 0
    last = N
    return first


def func_78ebe6e378744de3b56f69a52b68c31e(N):
    last = N
    firstsum = 0
    return firstsum


def func_e7d89f62d7584c488262f8e17119f7ff(N):
    last = N
    firstsum = 0
    return last


def func_7b896c8c8dbb40258991f429547f44e2():
    firstsum = 0
    lastsum = 0
    return lastsum


def func_0d57a547a8a647519b9c9e481d0c44ec():
    firstsum = 0
    lastsum = 0
    return firstsum


def func_6b2fc224f43d4f6c98d66686f88070b5(transistorsum):
    lastsum = 0
    minimax = transistorsum
    return lastsum


def func_cf637f5c33a544d19e1019d0abbb41eb(transistorsum):
    lastsum = 0
    minimax = transistorsum
    return minimax


def func_7d14a20d80c84c829954e36f67051b6e(transistors, transistorsum):
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return last


def func_47a9773b53964788ae14abb41c198514(transistors, transistorsum):
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return nextlastsum


def func_bb31ec36472b4182bd790f15d9b23f8d(transistors, transistorsum):
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return nextfirstsum


def func_df9dbcb65dcf442a903a503df13f46b3(transistors, transistorsum):
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return minimax


def func_329731e718c44a40bc21b5f16845ac0a(transistors, transistorsum):
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return firstsum


def func_a7ee2f87b7a6444a8863f96c25662b22(transistors, transistorsum):
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return currentmax


def func_b62469b168274eb1b59e90728c0608c1(transistors, transistorsum):
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return first


def func_c6f2f483b5df4dc0b647e371c31932b9(transistors, transistorsum):
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return lastsum


def func_9927e96149a8408797e6bbe7946a67ed(transistors, transistorsum):
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return currentmax


def func_c141f1be557a464ba19dbffe78b1aace(transistors, transistorsum):
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return minimax


def func_cde5c6a7e5394c1292467c3eaa1eaee2(transistors, transistorsum):
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return nextfirstsum


def func_aec0cca72fbb4395b02c84d1a29eccab(transistors, transistorsum):
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return nextlastsum


def func_94f3bc53e63a4c7da7d837754549ff46(transistors, transistorsum):
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return answer


def func_6762b86986c54a60817926a2575bafaf(transistors, transistorsum):
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return lastsum


def func_aa25eb2d76304c36abb21d443ab061cd(transistors, transistorsum):
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return last


def func_a09b6eee847f4df6bf218713f306446c(transistors, transistorsum):
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return firstsum


def func_f6f4cf15a58f455bac8d6cad4fc2289f(transistors, transistorsum):
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return first


def func_25f4d56c88f44359b82a49c061ace05c(minimax, transistorsum, testcase):
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return answer


def func_c6aa2693082c41ec8faf44768c5d2043(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    return transistors


def func_29f1084c70d54ca9b57dedf39dd84e15(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    return s


def func_91dd9554baac420c8611de6fa4b0427c(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    return N


def func_1d53cc4f72d84d0e9674663c0132d5b1(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    return p


def func_1f777bdcd2744c97a2b2196b9b585625(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    return r


def func_943d66cfce904232a4a3643ad2257ca2(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    return x


def func_c02fe4c744af432391ab5274c0290c31(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    return i


def func_913bfdc1c28a429c9c2b8130d724ec53(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    return transistorsum


def func_6ede1741e135442c8560eedf02f2c19b(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    return q


def func_5a59bb82667f4850936289f8d2f5ad37(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    return transistors


def func_b25f2c22870744a09f2ca75ac633d73e(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    return transistorsum


def func_7063f45f0078448588d7a6d34923afc4(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    return first


def func_9b9be35c92b14e9da0d2db0ad55f4ebd(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    return i


def func_0bcc8010454c4a77b62b061fd238b179(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    return first


def func_e18153ab8dec41508aa3778028616108(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    return transistorsum


def func_8606ab3b22b24a2f8b61e586d8d72ca0(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    return last


def func_88d88ba845ac40538a9333bec8fb108b(N):
    first = 0
    last = N
    firstsum = 0
    return firstsum


def func_40b21a40e6744272bd108958567dae53(N):
    first = 0
    last = N
    firstsum = 0
    return first


def func_2e99ae7edaa54b97b2df84cb67e2a77e(N):
    first = 0
    last = N
    firstsum = 0
    return last


def func_fd63678bedf64733bf05c60b1a2e1494(N):
    last = N
    firstsum = 0
    lastsum = 0
    return firstsum


def func_51a74cc291ae4bb9ab53fa5acee354db(N):
    last = N
    firstsum = 0
    lastsum = 0
    return lastsum


def func_bea012f625864e7a9786e048b59afd75(N):
    last = N
    firstsum = 0
    lastsum = 0
    return last


def func_bdd299be495b4af0932287d680acdd63(transistorsum):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return lastsum


def func_7daca5ad88fc499ca0c9d96874767d76(transistorsum):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return minimax


def func_7f91705e09644d33aa6acce40071498d(transistorsum):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return firstsum


def func_ac231012a2aa410bb65471575dbb52c6(transistors, transistorsum):
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return first


def func_15841c390962450590300773f6ceecc5(transistors, transistorsum):
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return last


def func_de60a326ab48448e9074435c413dc97b(transistors, transistorsum):
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return currentmax


def func_b9f719a3890a477fb54770a8e1370e1c(transistors, transistorsum):
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return lastsum


def func_403fb615f5744c329d3e5b835b736898(transistors, transistorsum):
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return minimax


def func_9c3a5f109f4b4bab93f2ff2cb1761801(transistors, transistorsum):
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return firstsum


def func_abf20741b7784dfcad875628513cec34(transistors, transistorsum):
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return nextfirstsum


def func_740926a0b48842ddaffe6fe446fd2dac(transistors, transistorsum):
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return nextlastsum


def func_66a4345465244fbc92b79f3a76e861ec(transistors, transistorsum):
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return last


def func_0c570960ab03444eb9eab2ad89f5b462(transistors, transistorsum):
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return nextfirstsum


def func_1ba0906fe88d47fe9be41fe04a6dd160(transistors, transistorsum):
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return firstsum


def func_6f4218059a774f76a30ad448c589bd91(transistors, transistorsum):
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return first


def func_ad1d4e3119c74ea8bffe2418ff12fe6c(transistors, transistorsum):
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return minimax


def func_08872f6a0b104b1a8b4f29ea2b124de5(transistors, transistorsum):
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return answer


def func_997581678fab419cacd08db279c0687d(transistors, transistorsum):
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return currentmax


def func_7607f866ed8c4cff95bc3d1e02071996(transistors, transistorsum):
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return lastsum


def func_8121810de75047129de5eb200d579200(transistors, transistorsum):
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return nextlastsum


def func_79ec2744408a44c69523a73986020ae1(transistors, transistorsum, testcase
    ):
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return nextfirstsum


def func_292f33df24c94870957c50a495123337(transistors, transistorsum, testcase
    ):
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return lastsum


def func_62a325f7b23b428abd3f5476ad23bedc(transistors, transistorsum, testcase
    ):
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return firstsum


def func_73819d75568c4d3ebf2071d0bb52b0c3(transistors, transistorsum, testcase
    ):
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return currentmax


def func_33a139792a1c4aac862f19aa2775ca5e(transistors, transistorsum, testcase
    ):
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return nextlastsum


def func_1aa223e444754ac7a1cb2d4f29909e7d(transistors, transistorsum, testcase
    ):
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return minimax


def func_9f1f5a99dc9641dfb19e717b13341a25(transistors, transistorsum, testcase
    ):
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return first


def func_255040ffee8e49eab3d4adbac03b4a8e(transistors, transistorsum, testcase
    ):
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return last


def func_2b003946f71848d98389959686e3d180(transistors, transistorsum, testcase
    ):
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return answer


def func_9c3852a4588544d894b2247ac0e42234(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    return first


def func_ad2b38465907454eb8ec7c3f16ccd87d(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    return p


def func_304b9853f470455ab4680fefe4742c89(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    return transistors


def func_d3852ee508be490cbe740a967cc72d3c(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    return i


def func_9738a361723242d3ad19bc57c1196489(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    return transistorsum


def func_eafe11006b5a48dd95a69a8e76893d08(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    return r


def func_24b296b8efef417a9fd56827129e227c(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    return x


def func_e0ac100d07b64e45aa8c97623a8cddc8(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    return q


def func_3406c283f4d84fa0a5959668851946d9(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    return N


def func_a5f90d788a91434fa5391f56afc6b05e(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    return s


def func_48b4a6b983e74443830a11c72016f84f(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    return transistors


def func_2d293e19051d402ab75b090785adb7b6(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    return i


def func_8a663759203b4f179152ef13b000f0b7(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    return last


def func_abfa506c305740b29c71739788d908ec(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    return transistorsum


def func_62f7f3e413534cf685bd83ba38d929f5(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    return first


def func_e5eb70488a4f489b81c972551bdaf2ac(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    return firstsum


def func_0463d41ccda64e11bfcdb5fb1e75b948(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    return last


def func_c2adae8227884782a206bc99ec04009a(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    return first


def func_8fc2ce8c320b44749f9674704a2fd943(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    return transistorsum


def func_ab2d59ff7dfe440c89c4e5f4b37f0a5d(N):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return firstsum


def func_128198aad8ab40c39c5442f6980834d1(N):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return last


def func_6165f4ceb581467dada10c3c633736b4(N):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return lastsum


def func_4168596e8b54497894aafdb9d1ad9c7b(N):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return first


def func_85efa7de3bd74e488ed9ae36b08e51ff(transistorsum, N):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return last


def func_d48b95e22ec943db8e84779d197c93b8(transistorsum, N):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return minimax


def func_e917c0b36bcc4841a553604578d87ccb(transistorsum, N):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return lastsum


def func_3e52a977146141a0b711e349b19799c8(transistorsum, N):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return firstsum


def func_ba701dbb151a4612b97b4e7f115ebf0c(transistors, transistorsum):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return lastsum


def func_f937e41837b44ba8a9e732f93e7aa712(transistors, transistorsum):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return minimax


def func_78625c58b1d54b8f8838e47e59c8afe3(transistors, transistorsum):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return last


def func_37aeb431da064272ae1a857b845d4f5e(transistors, transistorsum):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return firstsum


def func_feb7187bc4ec450eb30a3e54c7117e3b(transistors, transistorsum):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return currentmax


def func_d6ec7b3bbbe4498ca68b1ecfd9c62532(transistors, transistorsum):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return first


def func_20e8d87296014041b82551852cdf61c8(transistors, transistorsum):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return nextlastsum


def func_0f758fec6a50424c8c79c8e367bc7b80(transistors, transistorsum):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return nextfirstsum


def func_b9098cec551844b79045f1ae826d3c39(transistors, transistorsum):
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return lastsum


def func_ec0ce47f5f7a4587a9e4a5c1d6166712(transistors, transistorsum):
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return minimax


def func_4a4b5fcd5f4d4d3391068e80e1a85dbf(transistors, transistorsum):
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return nextlastsum


def func_5548a3643bfb43e3a231b9c836e557f1(transistors, transistorsum):
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return nextfirstsum


def func_db3e1e17aa6d4eab851c62efa3bb89de(transistors, transistorsum):
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return first


def func_bdf44447a21f4bf2955fe6c94d68130a(transistors, transistorsum):
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return last


def func_29bb7ce2bc374c15a0fbb0f9dfefabda(transistors, transistorsum):
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return firstsum


def func_b37995ca83f34b40b51d89a53bb3e14f(transistors, transistorsum):
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return currentmax


def func_d30a5cd684e3406f8e85b79098b28226(transistors, transistorsum):
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return answer


def func_4abb069996bf406ab2649372bdf499ef(transistors, transistorsum, testcase
    ):
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return firstsum


def func_d199b6c4d77d47c09429373efcd2b6e7(transistors, transistorsum, testcase
    ):
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return last


def func_320e001c959443038d690cd0465beee5(transistors, transistorsum, testcase
    ):
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return lastsum


def func_06411a3e23694bc38eadda0bb0742aaf(transistors, transistorsum, testcase
    ):
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return answer


def func_858ed0628f824a729c4f90b5877302e0(transistors, transistorsum, testcase
    ):
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return nextlastsum


def func_d05f09dfc2044dd6af6d0cdf5a8b76de(transistors, transistorsum, testcase
    ):
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return currentmax


def func_eed161c0e0f44f72aea1bd2a1983e07f(transistors, transistorsum, testcase
    ):
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return minimax


def func_49f76355674544cda167a64d920b0248(transistors, transistorsum, testcase
    ):
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return nextfirstsum


def func_4040185d097b4746a59e9eceb60a6bb2(transistors, transistorsum, testcase
    ):
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return first


def func_713cea3d1c8443ac98565a1457f0558a(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    return s


def func_af0756b3b2fb48d695df0faa6741a2a3(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    return r


def func_2254eded6e1a41e1834a19a71f35f8d1(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    return p


def func_5775ea219153400196ebbbe706c1ea23(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    return x


def func_9f4c4c30f417436c98a511ff4bb377e2(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    return q


def func_60cf629ec0bb403cae1a137dcaa3250c(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    return N


def func_9579cee7f8924b3a90bf0ec5857ac3c5(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    return transistors


def func_47d4af1c90224202b350546d3b0e3eaf(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    return i


def func_2a49b9efbf0b485ab5dabd5714080a14(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    return last


def func_2f6e09e6f5234c6b87e5473d21ed277f(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    return transistorsum


def func_3b647c4e7f3a40ffaf3ef28a20bb8080(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    return first


def func_3e89f5863b6c4ade918278afcce212c1(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    return transistors


def func_dbe198c9a9944b5383579e14e43d7353(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    return firstsum


def func_813c92d3a15b4f6d803740c84ce2c247(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    return first


def func_1303250ed0d742e3ab2d9105331455d9(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    return i


def func_adfc08e034c14d5cb9b6943eed5f02e5(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    return last


def func_9216eb769a454f47a0ce6101415b5bdd(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    return transistorsum


def func_6a26ede5a4ce4ef6afc8be0583d127be(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return lastsum


def func_fad41b6a91bf473ba643d0152304ceeb(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return last


def func_abe4256194694467a0993bc69809a784(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return firstsum


def func_80eee299c0b44c5eb3237eecdbc9b650(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return transistorsum


def func_c4f4695664c14b869de3b574c172dbe6(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return first


def func_26f8bca8155041dba88f4effff3112a8(transistorsum, N):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return firstsum


def func_08959f6251844855b1c88511848c6417(transistorsum, N):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return last


def func_6dee6d898270436d93f7606160507e24(transistorsum, N):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return minimax


def func_7fdc514e47fe4b45b28a1bae415c56a6(transistorsum, N):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return first


def func_cf39f0606bfa439bad5eaf5635fdc3d4(transistorsum, N):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return lastsum


def func_829e91e154464c39b293cd96dda86182(transistors, transistorsum, N):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return first


def func_901d12aa77864e57893274fc46b81a69(transistors, transistorsum, N):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return minimax


def func_bedaa4a412a44863814ae3d38cea42ef(transistors, transistorsum, N):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return last


def func_37ef516fe389460f9c8c6fbfa80727ba(transistors, transistorsum, N):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return nextfirstsum


def func_8db7497d1f8043528d54f27dc926036a(transistors, transistorsum, N):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return lastsum


def func_db2ecc3a71db4af1b67181ee070f8ba9(transistors, transistorsum, N):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return currentmax


def func_ed3dff0146a140258a49bd07525ead20(transistors, transistorsum, N):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return firstsum


def func_5faacae29e06442c86b9cb7cdf43d610(transistors, transistorsum, N):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return nextlastsum


def func_e84fb6de21e644f280c1761d61c0e386(transistors, transistorsum):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return nextlastsum


def func_956d8346f494440380a7068537966b07(transistors, transistorsum):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return lastsum


def func_d7f256328b7447dd83323e5a36124898(transistors, transistorsum):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return minimax


def func_369e26419c48490990b4ee2ba44efb60(transistors, transistorsum):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return nextfirstsum


def func_a8b53a35946a479cb050d246d398fa32(transistors, transistorsum):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return currentmax


def func_01f946f6084d4e179eb7c228e6f8b936(transistors, transistorsum):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return answer


def func_a9ec13a3de6340ebb3506b427e973e2d(transistors, transistorsum):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return firstsum


def func_c798733f0f344361b85b4b63217ed973(transistors, transistorsum):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return first


def func_526a49a12d4b4104b2afccd253cf3562(transistors, transistorsum):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return last


def func_1d3af85717ab4996a7f612ba30169f2a(transistors, transistorsum, testcase
    ):
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return answer


def func_75791cd49d8042e9a0c79e21a30068f8(transistors, transistorsum, testcase
    ):
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return minimax


def func_9048e60939f746efae1766ba9a8a4f6f(transistors, transistorsum, testcase
    ):
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return lastsum


def func_a52bae6fb496402ca302477a00065ebd(transistors, transistorsum, testcase
    ):
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return first


def func_416f650acba74ea4ac54ad72935c11f8(transistors, transistorsum, testcase
    ):
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return firstsum


def func_8baf4771b7204721a24bd8af06737d0d(transistors, transistorsum, testcase
    ):
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return nextfirstsum


def func_f95a378625d0432283bc4c711f00145d(transistors, transistorsum, testcase
    ):
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return nextlastsum


def func_f76463cf9001452fab02260c53fd9593(transistors, transistorsum, testcase
    ):
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return currentmax


def func_40abf5846816441094603297735bbd79(transistors, transistorsum, testcase
    ):
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return last


def func_c945a455c2fe49e5a3a2c51b5a6cf874(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    return s


def func_863ddc8114fd48e3b671e771d8657de4(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    return transistors


def func_3fda373528ed4e319de7fa6675a1958c(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    return N


def func_a4ff2d69811a460c92f9790f8d755748(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    return transistorsum


def func_a90177d7ded142429aabea9dea2923fc(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    return first


def func_88c56105e95a43f6ae1b93fcb013b317(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    return i


def func_ccd3aec8e2d84675ae486c7c505846c4(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    return q


def func_e8a0e0c3dd17453b91c5574d2078f1bb(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    return firstsum


def func_c59fac76cdac44b482cbe26a906712c1(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    return r


def func_1d09785053024d13a2c6ce26640c6434(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    return x


def func_091f70fbab084d6595c783f546353b85(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    return last


def func_a89653737b7f4e569c2121cee02a5079(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    return p


def func_f663383ec64c4bec867a3b037ae10be2(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return first


def func_4b11a7f6821243be8831a7fd58280fe6(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return lastsum


def func_0708dedf4a904750bd27b30da05cd0b6(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return transistorsum


def func_f6839618800f4d2985392903792d71bc(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return i


def func_42c9830ed5e74ee1977384abd1c05f1a(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return transistors


def func_001dde38f91e42feae9f4563bc7c8917(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return firstsum


def func_505f06252e34418fa773b4b4c7fc4ac0(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return last


def func_d556afce83824abab897eedf34bd5fa1(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return lastsum


def func_145b4221c9f04d2481a1399e6acc9e06(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return firstsum


def func_867df46333b24d9abafd2de57661f8ba(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return minimax


def func_2201689a6d794442b0b0da4d520ad728(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return transistorsum


def func_08ac3ce8c43442b9812597b1f20725a9(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return last


def func_f269311a5d724548a0c7455e3cdb0f65(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return first


def func_2c423fbde4ab4e689421c40864f79630(transistors, transistorsum, N):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return first


def func_dcc527219629417e9c994e84cb2bd811(transistors, transistorsum, N):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return firstsum


def func_6de74de42eb144b4b8291ebb0a3ca157(transistors, transistorsum, N):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return lastsum


def func_fd65cb7f587a4cceae454b9bdd5d8363(transistors, transistorsum, N):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return nextfirstsum


def func_3cebe53dce314d208e988611bb2cfbfa(transistors, transistorsum, N):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return nextlastsum


def func_76e4279924b44de29e4d8483a24ae030(transistors, transistorsum, N):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return minimax


def func_27d6e74dc742451b918adca81cb0a1f0(transistors, transistorsum, N):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return last


def func_ed0635e005f049b19b1f100d7556319d(transistors, transistorsum, N):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return currentmax


def func_5b3d090c5c5647ffb3efb96b7acda33c(transistors, transistorsum, N):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return nextfirstsum


def func_199844f9dbf14771a18b7586819064f0(transistors, transistorsum, N):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return first


def func_e7267b3d727146cfa68e7263aedffa6b(transistors, transistorsum, N):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return currentmax


def func_986be6a54b7b4f9998d8003991b09fdc(transistors, transistorsum, N):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return minimax


def func_47cd7e0c230148c4917da6fd701a0ecb(transistors, transistorsum, N):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return lastsum


def func_28944a76e008460ba8012d09454009b4(transistors, transistorsum, N):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return firstsum


def func_017e7cd16d1248b79a6d2380bcb6ee20(transistors, transistorsum, N):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return nextlastsum


def func_6ea8e128611a4406a40ced7724176aaa(transistors, transistorsum, N):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return last


def func_603ef9488a0b48558a531046665fa6b6(transistors, transistorsum, N):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return answer


def func_f3a9173ea4414396bf3d7dcb57f97e83(transistors, transistorsum, testcase
    ):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return nextfirstsum


def func_3f96cc7092b348c0bb00ef0bc05558fa(transistors, transistorsum, testcase
    ):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return firstsum


def func_f2aa3b93705042da9a53f624855991e1(transistors, transistorsum, testcase
    ):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return answer


def func_f2c55cabd63d40b4a4237ad6a493b8a3(transistors, transistorsum, testcase
    ):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return minimax


def func_5ae490d6243d4cb6819f0fa52f43cfda(transistors, transistorsum, testcase
    ):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return currentmax


def func_48f0274ca6c24113981320237cb5287b(transistors, transistorsum, testcase
    ):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return lastsum


def func_0adac693daca4a01b7014f8f5e7da3a1(transistors, transistorsum, testcase
    ):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return first


def func_79a58764bf704fecb5e1dc09387fa672(transistors, transistorsum, testcase
    ):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return last


def func_7a8fb30618d9402f95703293346ae861(transistors, transistorsum, testcase
    ):
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return nextlastsum


def func_02cd0047eab34176bfd4653ce31ad02e(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return firstsum


def func_34a751b722a94c138006b1ff2bbc09ac(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return last


def func_0b9625c003c04a8eb4ce0b6811fb01fb(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return s


def func_a016f70cdeee47af94ea40a92656e6f7(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return transistorsum


def func_53e718a55d7546c495034b30fef014e7(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return i


def func_b76559e02fd346008462e8c4c147dc08(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return p


def func_91c0826e7b524a878fa708a4adcaf652(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return first


def func_ec43513ae6544a08b5b3353f9c267f15(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return transistors


def func_4bc9b8b9ba2d4dd88cf071d8cab06ae4(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return x


def func_f53abc645aaa48b8a5bd28bc7044277d(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return r


def func_a7967fd5a6ec4f008f9cb048238df782(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return lastsum


def func_5aeebc437d8d48ea8286e6e3597d8f19(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return N


def func_8bd82d9f08e54877af32c9cd50bd2e5a(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    return q


def func_5712da9d59aa4be7bef9b247c52329df(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return transistors


def func_81c6540f09114f0996d78e50fc86edfc(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return i


def func_8054cb4d5f41412db70067a9e7f4e118(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return first


def func_7282d8715fa4440a9af4c74d2b9429ba(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return lastsum


def func_7797c73eb5194341860ee7884913273f(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return last


def func_83b4145d393e4061834679466d175ad3(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return transistorsum


def func_053de5e1a1b447dd8908ed0588b0d15f(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return firstsum


def func_a77996279abc4bffae107eb011e34fa2(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return minimax


def func_64b5fa7d8b834974905ad77ead0fca36(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return nextlastsum


def func_3db1b7bd9ccf43ee838ab30cfb60fc33(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return transistorsum


def func_3fce5bdec431465db9f4bfb831cfe81e(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return last


def func_ca6001b21b4d427dade15672dbd33f5f(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return nextfirstsum


def func_c038ff38dcd44f6d9261d8a28cc02245(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return firstsum


def func_edfaf2280fe44923996860d9561e5904(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return minimax


def func_8924210257114b38b9870330046fea5a(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return currentmax


def func_8927b81f19374bf88d400b3f04d57cf7(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return lastsum


def func_273139ff11084a54b9a4b6ee102458a2(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return first


def func_a99a8f25cf6744e19363a105df48f095(transistors, transistorsum, N):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return currentmax


def func_1dee943d48424ffc98db83c86ecfcf0a(transistors, transistorsum, N):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return firstsum


def func_1632eb5ebf1c4f2682820d9a0c77992b(transistors, transistorsum, N):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return nextlastsum


def func_6c18ece8233246bab68542bcfe8a81f7(transistors, transistorsum, N):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return lastsum


def func_43746edb56584cb3a4459747e64e17e3(transistors, transistorsum, N):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return nextfirstsum


def func_83747f1ac778494087062aa2ee29fe7c(transistors, transistorsum, N):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return minimax


def func_d35d7add277b4ed09a1667375d8fea3e(transistors, transistorsum, N):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return first


def func_6c5177bb4a554478894070d3f77c1bfa(transistors, transistorsum, N):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return last


def func_fce4b77cc91644338eabf29756905805(transistors, transistorsum, N):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return answer


def func_8dc2f737faf74853aee1987d69bc6525(transistors, transistorsum, N,
    testcase):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return first


def func_b77f7569253140ada78b8d80563f48f7(transistors, transistorsum, N,
    testcase):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return lastsum


def func_c60dbc7155ca4b8f8af7731dbe351e9e(transistors, transistorsum, N,
    testcase):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return minimax


def func_856187231f824851b1bb88e4ec95ddd4(transistors, transistorsum, N,
    testcase):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return nextlastsum


def func_d4af2429311941d9be0acf636acebc04(transistors, transistorsum, N,
    testcase):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return firstsum


def func_c41c2fdea08b446a998362a35879f5a6(transistors, transistorsum, N,
    testcase):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return nextfirstsum


def func_15944102569e40a7966efcf42b08fccd(transistors, transistorsum, N,
    testcase):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return answer


def func_9d3980a48f1042da8e6301dd771485f9(transistors, transistorsum, N,
    testcase):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return last


def func_c36c0e9891c04575bfe17ad599c14a4c(transistors, transistorsum, N,
    testcase):
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return currentmax


def func_a0d539dc54824e0ca159e65170105303(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return r


def func_35862e01e6f844b986580c0e1fe4cd4e(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return p


def func_63562bd30c9245bfaab3a19a5f10915b(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return s


def func_74231335596849a1a15a4a58c7a5c227(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return q


def func_b49728d22efd4a63913deedb7567c683(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return firstsum


def func_483ca297d1dd4ea08b43b8884cea4e88(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return minimax


def func_e8492140e86948fb9ae1016be052d436(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return i


def func_5b2369e247684130ab087e6c5d3866b9(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return transistors


def func_27002c8ae0f14388b6c698b30085b16d(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return lastsum


def func_110f6faf01a44c1da411a57077c05373(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return last


def func_3b777ef0d32049cca2056e051c9e64a9(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return transistorsum


def func_9585a6708c604d7f9fe7a22af03f477c(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return N


def func_d74b6d2e7d8846a4a41545a835d706de(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return first


def func_bab7a40a2c7a4cb589d9e1c136e35c47(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    return x


def func_5eeaf264944a4c98bebac0c95748f73b(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return nextlastsum


def func_7fbb397fefb746068778184061bf30b1(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return first


def func_f32b183e207047b094c45de830942481(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return firstsum


def func_a2a41d8a273d4675aea5c3c7db8f415d(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return minimax


def func_77394f7e114246978b61acd927f1f33b(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return nextfirstsum


def func_c70fd6956ae8475fab037fc5c616969c(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return last


def func_1f3e75fabecc4e988efff6ecec1684c0(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return i


def func_e77961c93d7b487ea604b849ed47a2b9(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return lastsum


def func_66c081e8d7b64e2fbaa56fb9443b4156(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return transistorsum


def func_cce0749682594f85a8ecb9903064edd8(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return transistors


def func_5953016e9f984774b4c530d24529d3d5(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return currentmax


def func_b1b64750ae68437486903edcec5e205e(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return nextlastsum


def func_167accf58c40442284e3a382085a8a82(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return firstsum


def func_2dab683c89974af0bcbf31c439275849(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return currentmax


def func_f11e30f20ccd4703b1f46890d3b5bad2(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return nextfirstsum


def func_8b7476934cf5446d9a7865594ffaf28e(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return minimax


def func_dcacc3e348ef4c6fb0a378c6d9797b66(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return first


def func_10f88c8b4605459ab181dfd9a206062d(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return lastsum


def func_ea6faecd7db74656bc27981437b7e2e0(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return last


def func_ece17c63372b407e8b48625bc1dd0cab(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return transistorsum


def func_3cfe2625bb174df980b4649bc9cccbc5(transistors, N):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return answer


def func_dd349c6a0d8f4c7a89bf5e2d20f94022(transistors, transistorsum, N,
    testcase):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return answer


def func_8063497b0f8b4be6b38897142f9bf7c1(transistors, transistorsum, N,
    testcase):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return nextlastsum


def func_ecbfb6b0ef554e2f867ca26b2544a669(transistors, transistorsum, N,
    testcase):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return lastsum


def func_3399878d1fa94c66a2ecfa11064ce91a(transistors, transistorsum, N,
    testcase):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return firstsum


def func_1405716d74f344cb94faef3554ffa269(transistors, transistorsum, N,
    testcase):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return currentmax


def func_4cd4b9ece3504678b5e7369e1113dbaa(transistors, transistorsum, N,
    testcase):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return last


def func_1e9fa66ce59d4886964e8ae6f8ae9a01(transistors, transistorsum, N,
    testcase):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return first


def func_c87c237fb91b436082d57bb97045acd1(transistors, transistorsum, N,
    testcase):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return nextfirstsum


def func_48abfe1c5e064811a9bad423cdb14f05(transistors, transistorsum, N,
    testcase):
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return minimax


def func_49374c5359e140a7abe2a9babca6521c(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return firstsum


def func_3de1806fff744ecb9b38292d51cf0071(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return nextlastsum


def func_ecf77b76ff0f460fac40b28f78b3b8cc(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return N


def func_2dea108deba14d58b09a29bec0584740(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return q


def func_5e4b814e9edd4c2f92c001eea17a0ff7(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return last


def func_9d81a316f92d4bc0b73714a152cfb619(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return first


def func_b7a8210408c3450280146639b81360ea(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return p


def func_c097bbf385b1493cbc28d7d4b64079db(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return lastsum


def func_76a487249fa14ead952abbe0ffa55681(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return transistorsum


def func_cb6a1e2ea4fe4fd29a52f1a1b95cc09e(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return x


def func_26f2ecf0593242a6a6c8be94b27fda92(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return r


def func_bc2e938b7f5444568c6b97ae2fa5a6da(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return transistors


def func_0766b236354444dd8d2838390f29120d(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return minimax


def func_140b6bcb968c4f0bad671d1733282313(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return s


def func_06afd365d3d0456a860aac82bcfe5429(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return currentmax


def func_505de5f8d5904a50ae6b3de06b79a8b6(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return i


def func_8d9e2865a64c40528d3d2a29fcdc5af4(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    return nextfirstsum


def func_c203887a50e7487aa6107f6dd555252b(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return answer


def func_b9cdf189cdc64d32bd7df6a6f02bd231(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return nextlastsum


def func_1dbca95474be419392403b7d1f0997a1(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return first


def func_3983636710444f88a09808601f21d6ec(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return nextfirstsum


def func_70f12371a3884bf0b9629a4a3791a40b(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return firstsum


def func_51f4f6cc8d5a4186aa10a0bef3406bc9(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return last


def func_552b906686a4455594551419c05440e5(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return lastsum


def func_14bcfe285b1d4aaeb944704be7ef5216(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return transistors


def func_4479bc58930848009429850853e907b6(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return currentmax


def func_1d1b5187edd5444dbc127023abbe4b3a(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return i


def func_b08f5108882746628d53b7e953a8ee79(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return minimax


def func_bf856959b7a44cf09c8af39cfbd9ddb2(s, q, N, p, r):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return transistorsum


def func_9e56c7ba35bc4d69ae6b8f93bbca8ef2(transistors, N, testcase):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return last


def func_6d5ede81e3a64787b4de950437ebfebf(transistors, N, testcase):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return nextfirstsum


def func_bc58fac4d0d1460692957376f4a1b510(transistors, N, testcase):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return transistorsum


def func_bee38bf28a8c44ac803ecb227d8e3ee1(transistors, N, testcase):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return answer


def func_25167578630248d78521dc986c14c852(transistors, N, testcase):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return first


def func_d6a26126495b4f5ea36de0d8bb7b3f16(transistors, N, testcase):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return firstsum


def func_26204c43db03457d92cfa9fc4f35f298(transistors, N, testcase):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return minimax


def func_cc6ec53222234b51b1c696f10f5d07cd(transistors, N, testcase):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return nextlastsum


def func_c1e13c23336e4851bed45a75e30645d2(transistors, N, testcase):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return currentmax


def func_463f946f42ee4808a85d9d6b5c33de2c(transistors, N, testcase):
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return lastsum


def func_cd32e8698e554715b5ffbf84ac158f56(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return lastsum


def func_4370c5ddaf2b427b9a3fd0ca273c96e5(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return answer


def func_2ca4230e82284667a7252fe65d8e13de(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return p


def func_12fbb646fc2f43059a11ded519aa2779(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return first


def func_dfc2c657a7294a31ab752faa3f0433e6(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return s


def func_ee272bc2224a40c9b067125673e1e523(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return transistors


def func_cad01d0871c3490b9dabc0a838523703(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return x


def func_9e185b744f3b4c41908ed0494fb11bc4(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return i


def func_8c79dee95ca9430ab254152e569caabe(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return q


def func_1903fad0d7bd4c2cb597157584b035cd(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return nextlastsum


def func_01c75a5449e848c0a8b9ce11b7d9865c(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return firstsum


def func_dc61e40f812645f888693ee007a02d79(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return currentmax


def func_21dd541f7b9f4fc087f47743d91ea216(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return transistorsum


def func_e977ec1da7cf4b068d84b34ab4a66e44(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return N


def func_d498bc07111044bcbb333993aacbaa41(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return r


def func_15bc3fcf27864906aae30da3586e82c1(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return minimax


def func_a04d1992589d44e08b442300791011e4(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return nextfirstsum


def func_bf967fe582cc4bdfbc4bd9c32de6228b(infile):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)
    return last


def func_3736a1d31fb9402a8eee4aa8ea0c3848(s, q, N, p, r, testcase):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return minimax


def func_812dd6921a064cd4a6df7ab882c3e39c(s, q, N, p, r, testcase):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return first


def func_f9151b441de64f9a885b559e65a85d4b(s, q, N, p, r, testcase):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return last


def func_a11988a81d424f0f905b0706fbbceda3(s, q, N, p, r, testcase):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return i


def func_ce9a56952fb4421fbfe841a79b565372(s, q, N, p, r, testcase):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return firstsum


def func_75eef0fd90a44fb2b57836a80f3087bf(s, q, N, p, r, testcase):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return nextfirstsum


def func_94008ca8f79445879da366062d32d794(s, q, N, p, r, testcase):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return answer


def func_e6dba71110994b43965a19a7a1ec4ce1(s, q, N, p, r, testcase):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return currentmax


def func_2b5f1caa4510403597190fa5bc1e6bff(s, q, N, p, r, testcase):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return transistorsum


def func_f19b8f72a2d24849b4c47103f7f636bd(s, q, N, p, r, testcase):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return nextlastsum


def func_6b7ad8e56aca4af5bf68c1885ecbcf5d(s, q, N, p, r, testcase):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return lastsum


def func_eb6cf2d0760a4494960ab7900371794f(s, q, N, p, r, testcase):
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return transistors


def func_dcd1192fe3c848d49b024c06c5246613(infile, testcase):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return q


def func_358daa42ae434b69a0253e543120315d(infile, testcase):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return transistors


def func_188a21ccd04e4116aba27e4d0901715c(infile, testcase):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return lastsum


def func_e33d41358c084efd8db756c67418fe73(infile, testcase):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return s


def func_7f04290b89b347f0a6b7d97e7f6a96d2(infile, testcase):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return p


def func_259fec91a7b04983b380819342d9039e(infile, testcase):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return i


def func_239648a9ce834812a8645f0c3d5eabb8(infile, testcase):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return firstsum


def func_d0a66048f5b74043aed64c5a34035262(infile, testcase):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return nextlastsum


def func_30a1264d38844f21aa0aecd28e2f8e8e(infile, testcase):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return nextfirstsum


def func_48a74235069347d3897b00cbfa774f28(infile, testcase):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return minimax


def func_865a7a7adaf34ed7a5100b34cdbda078(infile, testcase):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return answer


def func_c449f98f68e1401096c5d024acf4d37c(infile, testcase):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return first


def func_0e8aafcbfaf74d20b89379909464dc51(infile, testcase):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return x


def func_0e49e426fa984abdb8cd169b3d69b7f6(infile, testcase):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return currentmax


def func_91ff7cd32d014deab2175700ac1ceb9a(infile, testcase):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return N


def func_018c18d40e384754b39dcec4ace135dc(infile, testcase):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return transistorsum


def func_489fe72b9489483fb11b14375aa96ef6(infile, testcase):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return r


def func_9f7ef5cec31a4bd7980211b389c08223(infile, testcase):
    [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
    transistors = [((i * p + q) % r + s) for i in range(N)]
    transistorsum = sum(transistors)
    first = 0
    last = N
    firstsum = 0
    lastsum = 0
    minimax = transistorsum
    while last - first != 1:
        nextfirstsum = firstsum + transistors[first]
        nextlastsum = lastsum + transistors[last - 1]
        if nextfirstsum < nextlastsum:
            firstsum += transistors[first]
            first += 1
        else:
            last -= 1
            lastsum += transistors[last]
        currentmax = max([firstsum, lastsum, transistorsum - firstsum -
            lastsum])
        minimax = min(currentmax, minimax)
    answer = float(transistorsum - minimax) / float(transistorsum)(
        'Case #%d: %.10f' % (testcase + 1, answer))
    return last


def func_f8165cadaadd4f218b976da22cec8811():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    return infile


def func_0afbef775b7f43299026bbf879c99888():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    return n


def func_afdb32fdb2d6423e83cebdccd550cf89(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return currentmax


def func_f8f1916000dc418cb59a3b354a9e1179(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return first


def func_ac4c2bfe031f48c6b075177715b69d84(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return r


def func_b9b1285a356b40c38421575b27336b85(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return minimax


def func_f37ca45ca8ce4416a3b0661ffe344ba1(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return q


def func_08496745e9d6439cbbb1f30ec1a19ec5(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return nextfirstsum


def func_4c2a32d385ce4ee8b2686a13dd187ec9(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return transistorsum


def func_89ae2fcd459c4077875431684f9527f8(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return n


def func_239b3e8323bd48bc9359ec5479747edf(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return answer


def func_1a3c7d0fadef4587b221be32678ef540(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return p


def func_ff229c9884a945f0a0ff25909bd87d84(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return firstsum


def func_4dc824ab74bd420ea7f84f34ac759107(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return transistors


def func_38cc125a3bf3423d89d5f354cac7ffc1(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return testcase


def func_15ed5e36345f40a18102353e8aaadff2(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return s


def func_5020afdd258f459887a30e735586e09f(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return N


def func_d417d6b134c34f46941eedc17349739a(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return nextlastsum


def func_6aa52f65eb8f4107a4716bcb0bb9eb6a(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return last


def func_ea0547dc221b44dab0afe9dbfabba6bf(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return lastsum


def func_d0966f048e87411b92596d5ebfc000e8(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return x


def func_5f350182588f424cb2c897face501e33(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return i


def func_8878d012af3c48dc8fe138eb78db38c3(infile, n):
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return s


def func_904c4336da9a44109215f8bbd45228b8(infile, n):
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return q


def func_af5cae604fd749e8a3daaf54004e08ae(infile, n):
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return p


def func_1c375d24d2fa4edd8bfe150451ef8704(infile, n):
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return transistorsum


def func_e6f17c656b7d48859bf01258140fd0c8(infile, n):
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return transistors


def func_e3beb717938948d3861fb899558032ea(infile, n):
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return currentmax


def func_2e355342e7e6423984f200a78d143cea(infile, n):
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return lastsum


def func_e7094e748602428c9e44778333bb6c35(infile, n):
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return firstsum


def func_fe2fd165728242ee98ccc826b8943f77(infile, n):
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return testcase


def func_34411b1232c9414fae23b894fac1d12d(infile, n):
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return nextfirstsum


def func_5152f1a155044cc0b5005c5e8c138844(infile, n):
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return i


def func_d91ca4ea8cb341f7993ee73e7531f71b(infile, n):
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return r


def func_c03b1fcf807a4bc6a99e765595ed9dda(infile, n):
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return x


def func_12eb54ee2d19469ba0e89265d55e9dd4(infile, n):
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return minimax


def func_02a7e4ea0e9f417184ef49918f507352(infile, n):
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return first


def func_cd5c915a9d124d629bb92941f7d14c6f(infile, n):
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return N


def func_eab2fe7a596141a2a5c08ad4ddc258d0(infile, n):
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return last


def func_cfcfde25d4cd47cfb6d530b570b5501f(infile, n):
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return answer


def func_69c690eb529e412dbd8eba654db55be4(infile, n):
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return nextlastsum


def func_df56b23392e84437893b27e9277a1a14():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return transistorsum


def func_13984dc66f8c4800ad5619eba10b7907():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return nextfirstsum


def func_e1f927eab46f46dfbdae3cf73e4a6be6():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return transistors


def func_e134330a196f4971a5a6251026799a82():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return lastsum


def func_77724e9207e94389903583a1caf2d0b1():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return answer


def func_cd8c41ffe74642deba6c1f4f5e6ace59():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return nextlastsum


def func_5faa6d23d22849e8af1867176a6a6762():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return q


def func_c804e7519493479baa785d21a568eafd():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return p


def func_83dfcfa99a134593ad74dd6aa58cf201():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return minimax


def func_1f97aab9e7964d60bc870c5a096ae2bb():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return firstsum


def func_8b4274cb4d494c5793be77de896f7b98():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return x


def func_1ee25c94e66f4c91b256318828821904():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return first


def func_2f792e315c2242d790c575e85e052f9f():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return s


def func_cb2ac85c835d4928b3b33989ac19cd26():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return testcase


def func_60c34c5139c342268c6f18d88f623de0():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return r


def func_0f5cefe047304da896c29ce03e38b44b():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return last


def func_59bdf0123fbf45ee91cec8f97b0eb93d():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return i


def func_3246aea1bbc64fde80d32511c14bff67():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return currentmax


def func_29acdbc547fd46e2ac0fdb6580e62d86():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return n


def func_114d96ddb544409a8218202960a631e4():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return infile


def func_701deba2d03e4410b8192118d338f31b():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    return N


def func_a9cde84f2436472a9a6366fb4e7d9304(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return firstsum


def func_dc542e35e908439cb77e77d0ae9ef970(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return transistors


def func_6ec90b39b2f24a188321e8f44b753509(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return n


def func_8056a95a4f8e4b3aaefefd800f03978a(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return N


def func_5fcaf2fe8f5a4e6fb48b0f723d8aba89(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return i


def func_e0f4da6a84d2488bbd971cc5c4ba6764(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return testcase


def func_957ca3d9ac0641b193a24a105d386ae1(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return lastsum


def func_d77fb607ba214fad883615abfce56743(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return first


def func_4b764851d92544b7862ebca499fc1aa9(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return last


def func_a84dad28ad4a43b49188f5146cf52699(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return nextlastsum


def func_ed856f604246412998c180be4d406dcb(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return minimax


def func_eeef299ed21b4057b08ddd9734484f75(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return currentmax


def func_7dd4143af2df4fba9693a889aa78c276(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return transistorsum


def func_c3c2cf3cf0a544bcab9e5d11ef0ccfa1(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return r


def func_e2f0a16e1d1c4bf38ec665ec6d0f8c45(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return s


def func_3de8c0e0964a403fac96f0b5064caf2c(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return answer


def func_6211c282a99e42c0b7459badc5a6c43d(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return q


def func_b645b7ad5ee245ff9f895c897603306c(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return x


def func_cbe42a561d984922aec7d371a250eec0(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return p


def func_a5eb24417b1346a1b29faf662cd6ff5a(infile):
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return nextfirstsum


def func_e3ae76d276bf48bca22708a974becb15():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return last


def func_27679d1f5e334086a22ac6ae0d19baa5():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return answer


def func_0e68ca24d82c45b1a6b7668a8c17994e():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return transistors


def func_c18690e9720f493e96215e3ea190583a():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return x


def func_8b18343854f24bc9b1db3e481d437127():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return nextlastsum


def func_c6f0b33aac664172b2cafb4fae5ebef2():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return N


def func_20710c5689b94cad826347285215ffe5():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return firstsum


def func_54461b0ebcc3481f8ce5ea28116b0e61():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return nextfirstsum


def func_b4ce79b33d294602b87ef93404d08086():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return n


def func_bc2c8f274a0944aba8d1bceeb65600f0():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return transistorsum


def func_47a6f159d3984c69b01cbc0741f9d106():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return minimax


def func_be62f6fd6f1e47148eec3d1caa09e229():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return first


def func_b5e5aeebc00b42cb80d925e7a13b2def():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return testcase


def func_cddb1d790bc64166995c382a3acdfa90():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return q


def func_3d86a56f969a4b09a62747df021057f5():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return lastsum


def func_271836332c3e46d68b33a9a5b85192bb():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return currentmax


def func_9921be307f3441778aef9e7c70ec8bb7():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return infile


def func_37963050fdb64aa9bb12653698387550():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return i


def func_e355d7a4ad3e418aa15fb90a32977166():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return r


def func_457805ca79b1405bb0e8ac1dfe30b547():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return p


def func_4cf0d61c216244e096756d67eb1c33c3():
    infile = open('test_files/Y14R5P1/A.in')
    n = int(infile.readline())
    for testcase in range(n):
        [N, p, q, r, s] = [int(x) for x in infile.readline().split()]
        transistors = [((i * p + q) % r + s) for i in range(N)]
        transistorsum = sum(transistors)
        first = 0
        last = N
        firstsum = 0
        lastsum = 0
        minimax = transistorsum
        while last - first != 1:
            nextfirstsum = firstsum + transistors[first]
            nextlastsum = lastsum + transistors[last - 1]
            if nextfirstsum < nextlastsum:
                firstsum += transistors[first]
                first += 1
            else:
                last -= 1
                lastsum += transistors[last]
            currentmax = max([firstsum, lastsum, transistorsum - firstsum -
                lastsum])
            minimax = min(currentmax, minimax)
        answer = float(transistorsum - minimax) / float(transistorsum)
        print 'Case #%d: %.10f' % (testcase + 1, answer)
    infile.close()
    return s

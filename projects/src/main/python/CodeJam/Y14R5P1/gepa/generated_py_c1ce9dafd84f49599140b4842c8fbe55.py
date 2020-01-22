import sys
sys.path.append('/home/george2/Raise/ProgramRepair/CodeSeer/projects/src/main/python')
from CodeJam.Y14R5P1.gepa.A import *

def func_4043abbfd15a4df59cbd85885c4e6fa7(a, x):
    last += 2 * x
    a.append(last)
    return last


def func_6401b05c1e45462f932b8a7f27bb7b66(a, pos, first):
    second = a[pos - 1] - first
    third = a[-1] - first - second
    return third


def func_9f74e2b1b8d34d1194fc2780c0c084c4(a, pos, first):
    second = a[pos - 1] - first
    third = a[-1] - first - second
    return second


def func_73a107f37fbe4447bef40be5fe7e69dc(a, second, first):
    third = a[-1] - first - second
    m = a[-1] - max(first, second, third)
    return third


def func_ec8fe65f3ec543dabdf180ca3c799533(a, second, first):
    third = a[-1] - first - second
    m = a[-1] - max(first, second, third)
    return m


def func_370340d91ff64e0d8c8571135814eb61(a, pos, first):
    second = a[pos - 1] - first
    third = a[-1] - first - second
    m = a[-1] - max(first, second, third)
    return second


def func_48bf1803c3cd4882a769dd2496595648(a, pos, first):
    second = a[pos - 1] - first
    third = a[-1] - first - second
    m = a[-1] - max(first, second, third)
    return third


def func_94c9a6d8b4f34f518653298361602afd(a, pos, first):
    second = a[pos - 1] - first
    third = a[-1] - first - second
    m = a[-1] - max(first, second, third)
    return m


def func_6e3c8d725cb743e0adf8518fe98c8982(a, i):
    first = a[i]
    need = first + (a[-1] - first) / 2
    return first


def func_d02aa5f53559411ea151605a51f8d086(a, i):
    first = a[i]
    need = first + (a[-1] - first) / 2
    return need


def func_a8347cd0b5dd4f45939235b3ebe4adf7(a, first):
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    return pos


def func_614c0a51a00f4c93bd9453104b3d022b(a, first):
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    return need


def func_43ad47970a664d2ba9bdee2d1e2882b7(a, first, need):
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    return second


def func_38dc0162a5d744e1b09c86ce70ecb39d(a, first, need):
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    return pos


def func_383425f92b1845df96b45a1b7904a354(a, pos, first):
    second = a[pos] - first
    third = a[-1] - first - second
    return second


def func_0685c913678a4c058f2920ceaefa0c91(a, pos, first):
    second = a[pos] - first
    third = a[-1] - first - second
    return third


def func_7164cf512b4842b5bc6164d54faf40ca(a, second, first):
    third = a[-1] - first - second
    m = a[-1] - max(first, second, third)
    return third


def func_232a2809790841bc9168806665259515(a, second, first):
    third = a[-1] - first - second
    m = a[-1] - max(first, second, third)
    return m


def func_264a7bef2995420b80673545ba7b4330(a, i):
    first = a[i]
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    return first


def func_1965e00f01d64bc0ae2c6aec66fa3608(a, i):
    first = a[i]
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    return need


def func_437843322ab24fcfae6cb9108b68f632(a, i):
    first = a[i]
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    return pos


def func_05df5b2b28604dc9aa50ec6258505e78(a, first):
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    return pos


def func_29af3a023e1a45609773967ba539e71c(a, first):
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    return second


def func_4d7a9421db64408eb654d16a709937c6(a, first):
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    return need


def func_3cdd8328370546c9abf8969761bd274d(a, first, need):
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    return second


def func_fcf513854ee5418493ab71a6fc3db72d(a, first, need):
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    return pos


def func_4b7d6645cebf4e84ad621c2412465456(a, first, need):
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    return third


def func_bf7f6ddb61c24661aa1470ae82b95c10(a, pos, first):
    second = a[pos] - first
    third = a[-1] - first - second
    m = a[-1] - max(first, second, third)
    return second


def func_3f7b6efa76cf4728a8844f218d17e6b4(a, pos, first):
    second = a[pos] - first
    third = a[-1] - first - second
    m = a[-1] - max(first, second, third)
    return third


def func_0b2816903dfa45a391558ad931f93e67(a, pos, first):
    second = a[pos] - first
    third = a[-1] - first - second
    m = a[-1] - max(first, second, third)
    return m


def func_b682c591176d4dec981df30c02e66306(a, i):
    first = a[i]
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    return need


def func_e542b75e165c44799879dd237ee11679(a, i):
    first = a[i]
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    return first


def func_52a474b2d65c419bbe003ca73684c424(a, i):
    first = a[i]
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    return pos


def func_a3780a838ae04842822b901c80a60da5(a, i):
    first = a[i]
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    return second


def func_d6991fcce4a549959ffbfb5ea7659f5a(a, first):
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    return need


def func_10ce5e8b644e42498fcb167ee2b1b482(a, first):
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    return pos


def func_798d906039b7417e992c93d2b7059daf(a, first):
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    return second


def func_ee86a5dcc0e040f9a93dee01f51dae98(a, first):
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    return third


def func_3a7a1d1975284475a6a0f11631b61f52(a, first, need):
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    m = a[-1] - max(first, second, third)
    return second


def func_d62afabaeed34761b18d6ff1882b421a(a, first, need):
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    m = a[-1] - max(first, second, third)
    return pos


def func_1794084277e9466d8471f11ca8006d13(a, first, need):
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    m = a[-1] - max(first, second, third)
    return m


def func_d289dea0830345e2b90b2a78957bac04(a, first, need):
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    m = a[-1] - max(first, second, third)
    return third


def func_7bc778ce1fe04bb49e4dbde609620936(a, i):
    first = a[i]
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    return second


def func_a5ed8de62b5948ff9e76fd88cbee680c(a, i):
    first = a[i]
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    return pos


def func_87f276d82eae4259b1c0ad572868efb9(a, i):
    first = a[i]
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    return need


def func_84a72f9e46804c158bd093c3c4341f2d(a, i):
    first = a[i]
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    return third


def func_027844ad49f447beadcc3c3ca1f2aed1(a, i):
    first = a[i]
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    return first


def func_225afd1e2ba44b6796c7c545969ee0b6(a, first):
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    m = a[-1] - max(first, second, third)
    return third


def func_3d0c03156ff14bfeb39bebb35d6cc0b2(a, first):
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    m = a[-1] - max(first, second, third)
    return pos


def func_62622408c4a148ba98f11f325fcece4f(a, first):
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    m = a[-1] - max(first, second, third)
    return m


def func_3b280529f33b48fe9cf5f26e6ebaddae(a, first):
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    m = a[-1] - max(first, second, third)
    return need


def func_22f8ea15cd774c79ab19739b67601805(a, first):
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    m = a[-1] - max(first, second, third)
    return second


def func_a1df311c237744e9a9ff65677a8e4335(a, i):
    first = a[i]
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    m = a[-1] - max(first, second, third)
    return pos


def func_ba9f846a700c400482ac62eb0b904681(a, i):
    first = a[i]
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    m = a[-1] - max(first, second, third)
    return third


def func_e991c4d7f8b944d8adacbc72382bb327(a, i):
    first = a[i]
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    m = a[-1] - max(first, second, third)
    return second


def func_d61b4646a19c4502ada225ce0cdc5efd(a, i):
    first = a[i]
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    m = a[-1] - max(first, second, third)
    return m


def func_a31b3b2f84e1406d97af8bf413ba90dc(a, i):
    first = a[i]
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    m = a[-1] - max(first, second, third)
    return first


def func_fe6f14456550415cba432b706d45c86e(a, i):
    first = a[i]
    need = first + (a[-1] - first) / 2
    pos = bisect.bisect_left(a, need)
    second = a[pos] - first
    third = a[-1] - first - second
    m = a[-1] - max(first, second, third)
    return need


def func_9b3548b484614899b785d93118b729b1():
    a = [0]
    last = 0
    return a


def func_aabf58f22bb647ab8ebab97850ab591b():
    a = [0]
    last = 0
    return last


def func_332f9bc8ce694d78be41496d55444c7d(a):
    best = 0.0
    if a[-1] == 0:
        return 0.0
    return best


def func_ed597ccafd2346c18e5e375c52dea5ba(infile):
    N, p, q, r, s = map(int, infile.readline().strip().split())
    return N, p, q, r, s


def func_2c0985fd533c47498217ce9a6b8c0496():
    sys.setrecursionlimit(100000)
    infile = open('codejam/test_files/Y14R5P1/A.in')
    return infile


def func_2cb682831c9140a3a506dc97671ac899():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    T = int(infile.readline().strip())
    return infile


def func_24ca3f81533744cc822f15c45c8fff9d():
    infile = open('codejam/test_files/Y14R5P1/A.in')
    T = int(infile.readline().strip())
    return T


def func_502966ee17ea49eebcf802dac8a7a720():
    sys.setrecursionlimit(100000)
    infile = open('codejam/test_files/Y14R5P1/A.in')
    T = int(infile.readline().strip())
    return infile


def func_f88f8eec0cfe49178e7175da41b1cea8():
    sys.setrecursionlimit(100000)
    infile = open('codejam/test_files/Y14R5P1/A.in')
    T = int(infile.readline().strip())
    return T

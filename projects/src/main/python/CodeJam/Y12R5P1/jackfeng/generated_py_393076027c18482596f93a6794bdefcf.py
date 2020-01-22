import sys
sys.path.append('/home/george2/Raise/ProgramRepair/CodeSeer/projects/src/main/python')
from CodeJam.Y12R5P1.jackfeng.A import *

def func_f6e4d1b02d7c47c780aac27dc16e3a6e(input):

    def split(func, sep=' '):
        return map(func, input.readline().strip().split(sep))

    def cmp_fun(i1, i2):
        if i1[2] != i2[2]:
            return -1 if i1[2] > i2[2] else 1
        elif i1[1] != i2[1]:
            return -1 if i1[1] > i2[1] else 1
        return -1 if i1[0] < i2[0] else 1
    split(int)
    L = split(int)
    return L


def func_95f78294c7b5494aaad753079daaa891(input):

    def split(func, sep=' '):
        return map(func, input.readline().strip().split(sep))

    def cmp_fun(i1, i2):
        if i1[2] != i2[2]:
            return -1 if i1[2] > i2[2] else 1
        elif i1[1] != i2[1]:
            return -1 if i1[1] > i2[1] else 1
        return -1 if i1[0] < i2[0] else 1
    L = split(int)
    P = split(int)
    return L


def func_63d5d1c5a3154c47861f41b444aa4f40(input):

    def split(func, sep=' '):
        return map(func, input.readline().strip().split(sep))

    def cmp_fun(i1, i2):
        if i1[2] != i2[2]:
            return -1 if i1[2] > i2[2] else 1
        elif i1[1] != i2[1]:
            return -1 if i1[1] > i2[1] else 1
        return -1 if i1[0] < i2[0] else 1
    L = split(int)
    P = split(int)
    return P


def func_a12a40dfdbdf4835965472439cf93e6a(input, L):

    def split(func, sep=' '):
        return map(func, input.readline().strip().split(sep))

    def cmp_fun(i1, i2):
        if i1[2] != i2[2]:
            return -1 if i1[2] > i2[2] else 1
        elif i1[1] != i2[1]:
            return -1 if i1[1] > i2[1] else 1
        return -1 if i1[0] < i2[0] else 1
    P = split(int)
    items = sorted(zip(range(len(L)), L, P), cmp=cmp_fun)
    return items


def func_3e1a84e3a90446eb8bd6b2f312b01efe(input, L):

    def split(func, sep=' '):
        return map(func, input.readline().strip().split(sep))

    def cmp_fun(i1, i2):
        if i1[2] != i2[2]:
            return -1 if i1[2] > i2[2] else 1
        elif i1[1] != i2[1]:
            return -1 if i1[1] > i2[1] else 1
        return -1 if i1[0] < i2[0] else 1
    P = split(int)
    items = sorted(zip(range(len(L)), L, P), cmp=cmp_fun)
    return L


def func_5d2fb13e0ad2464f89ba007771146ab1(input, L):

    def split(func, sep=' '):
        return map(func, input.readline().strip().split(sep))

    def cmp_fun(i1, i2):
        if i1[2] != i2[2]:
            return -1 if i1[2] > i2[2] else 1
        elif i1[1] != i2[1]:
            return -1 if i1[1] > i2[1] else 1
        return -1 if i1[0] < i2[0] else 1
    P = split(int)
    items = sorted(zip(range(len(L)), L, P), cmp=cmp_fun)
    return P


def func_d6b3d9052348485d81e5f51775f626f2(input, L, P):

    def split(func, sep=' '):
        return map(func, input.readline().strip().split(sep))

    def cmp_fun(i1, i2):
        if i1[2] != i2[2]:
            return -1 if i1[2] > i2[2] else 1
        elif i1[1] != i2[1]:
            return -1 if i1[1] > i2[1] else 1
        return -1 if i1[0] < i2[0] else 1
    items = sorted(zip(range(len(L)), L, P), cmp=cmp_fun)
    return ' '.join(map(lambda i: str(i[0]), items))


def func_c55e4b2dd18f4a5585425efd47840739(input):

    def split(func, sep=' '):
        return map(func, input.readline().strip().split(sep))

    def cmp_fun(i1, i2):
        if i1[2] != i2[2]:
            return -1 if i1[2] > i2[2] else 1
        elif i1[1] != i2[1]:
            return -1 if i1[1] > i2[1] else 1
        return -1 if i1[0] < i2[0] else 1
    split(int)
    L = split(int)
    P = split(int)
    return L


def func_4c2c6cc71ea94eb2af27eabba5172768(input):

    def split(func, sep=' '):
        return map(func, input.readline().strip().split(sep))

    def cmp_fun(i1, i2):
        if i1[2] != i2[2]:
            return -1 if i1[2] > i2[2] else 1
        elif i1[1] != i2[1]:
            return -1 if i1[1] > i2[1] else 1
        return -1 if i1[0] < i2[0] else 1
    split(int)
    L = split(int)
    P = split(int)
    return P


def func_81fcef5a086141608d45ff73bdf8e38d(input):

    def split(func, sep=' '):
        return map(func, input.readline().strip().split(sep))

    def cmp_fun(i1, i2):
        if i1[2] != i2[2]:
            return -1 if i1[2] > i2[2] else 1
        elif i1[1] != i2[1]:
            return -1 if i1[1] > i2[1] else 1
        return -1 if i1[0] < i2[0] else 1
    L = split(int)
    P = split(int)
    items = sorted(zip(range(len(L)), L, P), cmp=cmp_fun)
    return items


def func_8d7af1461a1f45b29990dbb1e85677b4(input):

    def split(func, sep=' '):
        return map(func, input.readline().strip().split(sep))

    def cmp_fun(i1, i2):
        if i1[2] != i2[2]:
            return -1 if i1[2] > i2[2] else 1
        elif i1[1] != i2[1]:
            return -1 if i1[1] > i2[1] else 1
        return -1 if i1[0] < i2[0] else 1
    L = split(int)
    P = split(int)
    items = sorted(zip(range(len(L)), L, P), cmp=cmp_fun)
    return L


def func_ceaef1cc4c14489e9725dfa0f6e6a80a(input):

    def split(func, sep=' '):
        return map(func, input.readline().strip().split(sep))

    def cmp_fun(i1, i2):
        if i1[2] != i2[2]:
            return -1 if i1[2] > i2[2] else 1
        elif i1[1] != i2[1]:
            return -1 if i1[1] > i2[1] else 1
        return -1 if i1[0] < i2[0] else 1
    L = split(int)
    P = split(int)
    items = sorted(zip(range(len(L)), L, P), cmp=cmp_fun)
    return P


def func_3e1dcf4ca0184f139d397a7e01a3ab4a(input, L):

    def split(func, sep=' '):
        return map(func, input.readline().strip().split(sep))

    def cmp_fun(i1, i2):
        if i1[2] != i2[2]:
            return -1 if i1[2] > i2[2] else 1
        elif i1[1] != i2[1]:
            return -1 if i1[1] > i2[1] else 1
        return -1 if i1[0] < i2[0] else 1
    P = split(int)
    items = sorted(zip(range(len(L)), L, P), cmp=cmp_fun)
    return ' '.join(map(lambda i: str(i[0]), items))


def func_d271938d052a4b29a3ff29aace4cdcd0(input):

    def split(func, sep=' '):
        return map(func, input.readline().strip().split(sep))

    def cmp_fun(i1, i2):
        if i1[2] != i2[2]:
            return -1 if i1[2] > i2[2] else 1
        elif i1[1] != i2[1]:
            return -1 if i1[1] > i2[1] else 1
        return -1 if i1[0] < i2[0] else 1
    split(int)
    L = split(int)
    P = split(int)
    items = sorted(zip(range(len(L)), L, P), cmp=cmp_fun)
    return items


def func_a43ffc934506484284a905a247a7aac7(input):

    def split(func, sep=' '):
        return map(func, input.readline().strip().split(sep))

    def cmp_fun(i1, i2):
        if i1[2] != i2[2]:
            return -1 if i1[2] > i2[2] else 1
        elif i1[1] != i2[1]:
            return -1 if i1[1] > i2[1] else 1
        return -1 if i1[0] < i2[0] else 1
    split(int)
    L = split(int)
    P = split(int)
    items = sorted(zip(range(len(L)), L, P), cmp=cmp_fun)
    return P


def func_255bd62ad7974baeb2bfba42a25c528c(input):

    def split(func, sep=' '):
        return map(func, input.readline().strip().split(sep))

    def cmp_fun(i1, i2):
        if i1[2] != i2[2]:
            return -1 if i1[2] > i2[2] else 1
        elif i1[1] != i2[1]:
            return -1 if i1[1] > i2[1] else 1
        return -1 if i1[0] < i2[0] else 1
    split(int)
    L = split(int)
    P = split(int)
    items = sorted(zip(range(len(L)), L, P), cmp=cmp_fun)
    return L


def func_813afe0c56054753b087c2e44889eebb(input):

    def split(func, sep=' '):
        return map(func, input.readline().strip().split(sep))

    def cmp_fun(i1, i2):
        if i1[2] != i2[2]:
            return -1 if i1[2] > i2[2] else 1
        elif i1[1] != i2[1]:
            return -1 if i1[1] > i2[1] else 1
        return -1 if i1[0] < i2[0] else 1
    L = split(int)
    P = split(int)
    items = sorted(zip(range(len(L)), L, P), cmp=cmp_fun)
    return ' '.join(map(lambda i: str(i[0]), items))


def func_6c5e02b282194328bbcde764ba664a50(input):

    def split(func, sep=' '):
        return map(func, input.readline().strip().split(sep))

    def cmp_fun(i1, i2):
        if i1[2] != i2[2]:
            return -1 if i1[2] > i2[2] else 1
        elif i1[1] != i2[1]:
            return -1 if i1[1] > i2[1] else 1
        return -1 if i1[0] < i2[0] else 1
    split(int)
    L = split(int)
    P = split(int)
    items = sorted(zip(range(len(L)), L, P), cmp=cmp_fun)
    return ' '.join(map(lambda i: str(i[0]), items))


def func_461b1fd3be1d4c3f833bfe3490faf02e(input):
    T = int(input.readline().strip())
    for t in range(1, T + 1):
        print 'Case #%d: %s' % (t, solve(input))
    return t


def func_04f8080703ec48508469173fb3d5fa8a(input):
    T = int(input.readline().strip())
    for t in range(1, T + 1):
        print 'Case #%d: %s' % (t, solve(input))
    return T

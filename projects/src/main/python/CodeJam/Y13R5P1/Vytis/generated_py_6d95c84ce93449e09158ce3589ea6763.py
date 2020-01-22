import sys
sys.path.append('/home/george2/Raise/ProgramRepair/CodeSeer/projects/src/main/python')
from CodeJam.Y13R5P1.Vytis.A import *

def func_43934b24cc7948e4b2ff4a53fd6b87f4():
    m = [0] * 37
    best = 0.0
    return best


def func_0bf9d56ca78f41ef9be3fac34a49f13b():
    m = [0] * 37
    best = 0.0
    return m


def func_2d1d9c9c7410411889e327ce4ce1c706(lines, lineno):
    b, n = map(int, lines[lineno].split())
    x = map(int, lines[lineno + 1].split())
    return n


def func_588654aef6a6410e94f262750734b11e(lines, lineno):
    b, n = map(int, lines[lineno].split())
    x = map(int, lines[lineno + 1].split())
    return x


def func_ff1a6fb646dc4146adab5b901af5abdf(lines, lineno):
    b, n = map(int, lines[lineno].split())
    x = map(int, lines[lineno + 1].split())
    return b


def func_0fed36a723dc4665b1092fac84d62fa0(b, lines, lineno, n):
    x = map(int, lines[lineno + 1].split())
    r = solve(b, x[:n])
    return r


def func_24080ef5285846789b80f63052d1c370(b, lines, lineno, n):
    x = map(int, lines[lineno + 1].split())
    r = solve(b, x[:n])
    return x


def func_b5c5379c96a84499a7fe6c06e1e81fc4(b, n, x):
    r = solve(b, x[:n])
    lineno += 2
    return lineno


def func_1af7ebefe4494283b45d81aca4c61434(b, n, x):
    r = solve(b, x[:n])
    lineno += 2
    return r


def func_43ff5ec3ce5e4dd9b00910d46249d5ff(r, i):
    lineno += 2
    msg = 'Case #{}: {:.9f}'.format(i, r)
    return msg


def func_3ce8ac0d668c457bbf1370765e4d5190(r, i):
    lineno += 2
    msg = 'Case #{}: {:.9f}'.format(i, r)
    return lineno


def func_1f0e0d0641d14f10a60cc5e15813efaa(lines, lineno):
    b, n = map(int, lines[lineno].split())
    x = map(int, lines[lineno + 1].split())
    r = solve(b, x[:n])
    return x


def func_74ea4be41e114abeb5386efd0084b9ff(lines, lineno):
    b, n = map(int, lines[lineno].split())
    x = map(int, lines[lineno + 1].split())
    r = solve(b, x[:n])
    return n


def func_2e0c7f52579d4a6f9b2ef292a3c7882f(lines, lineno):
    b, n = map(int, lines[lineno].split())
    x = map(int, lines[lineno + 1].split())
    r = solve(b, x[:n])
    return r


def func_c083c85660c04fc49622c0b56d7ca09b(lines, lineno):
    b, n = map(int, lines[lineno].split())
    x = map(int, lines[lineno + 1].split())
    r = solve(b, x[:n])
    return b


def func_8f48c2ad78e14933897e7861474b4089(b, lines, n):
    x = map(int, lines[lineno + 1].split())
    r = solve(b, x[:n])
    lineno += 2
    return r


def func_f5455ed39fff4d6b8d7ab0f57d41382f(b, lines, n):
    x = map(int, lines[lineno + 1].split())
    r = solve(b, x[:n])
    lineno += 2
    return lineno


def func_00fe097c7bc643dab61ddb97741a6106(b, lines, n):
    x = map(int, lines[lineno + 1].split())
    r = solve(b, x[:n])
    lineno += 2
    return x


def func_339cf4b2e6d74b0dbda777fe9a5a9bb4(b, i, n, x):
    r = solve(b, x[:n])
    lineno += 2
    msg = 'Case #{}: {:.9f}'.format(i, r)
    return msg


def func_df28acc2f2834228b5dcbd12550e6ec2(b, i, n, x):
    r = solve(b, x[:n])
    lineno += 2
    msg = 'Case #{}: {:.9f}'.format(i, r)
    return lineno


def func_98d522c950774610bdf5d7bedd121baf(b, i, n, x):
    r = solve(b, x[:n])
    lineno += 2
    msg = 'Case #{}: {:.9f}'.format(i, r)
    return r


def func_cd99ead5a76c45dd99ebcb862e779e2a(lines):
    b, n = map(int, lines[lineno].split())
    x = map(int, lines[lineno + 1].split())
    r = solve(b, x[:n])
    lineno += 2
    return n


def func_d0209c7855964ef0b8c539a10f05ffb1(lines):
    b, n = map(int, lines[lineno].split())
    x = map(int, lines[lineno + 1].split())
    r = solve(b, x[:n])
    lineno += 2
    return x


def func_dbfd8310ec1a451ab4bdfd1492a2b1ad(lines):
    b, n = map(int, lines[lineno].split())
    x = map(int, lines[lineno + 1].split())
    r = solve(b, x[:n])
    lineno += 2
    return lineno


def func_211433e0eb364bf6af956ff8edbd5ae5(lines):
    b, n = map(int, lines[lineno].split())
    x = map(int, lines[lineno + 1].split())
    r = solve(b, x[:n])
    lineno += 2
    return r


def func_f2fb199f8787457baf1b3d3505e96234(lines):
    b, n = map(int, lines[lineno].split())
    x = map(int, lines[lineno + 1].split())
    r = solve(b, x[:n])
    lineno += 2
    return b


def func_95d772bf04344f61a9674331a9c5942b(b, lines, i, n):
    x = map(int, lines[lineno + 1].split())
    r = solve(b, x[:n])
    lineno += 2
    msg = 'Case #{}: {:.9f}'.format(i, r)
    return msg


def func_a2b32cd8da44408a9b4d9e92de8d6c17(b, lines, i, n):
    x = map(int, lines[lineno + 1].split())
    r = solve(b, x[:n])
    lineno += 2
    msg = 'Case #{}: {:.9f}'.format(i, r)
    return lineno


def func_975054264e5e43e18b752a1a1a236d8f(b, lines, i, n):
    x = map(int, lines[lineno + 1].split())
    r = solve(b, x[:n])
    lineno += 2
    msg = 'Case #{}: {:.9f}'.format(i, r)
    return r


def func_5920530629024d4f8e94724b5f4e6c00(b, lines, i, n):
    x = map(int, lines[lineno + 1].split())
    r = solve(b, x[:n])
    lineno += 2
    msg = 'Case #{}: {:.9f}'.format(i, r)
    return x


def func_d4b882b30d5d4741b6c748fa94f3d754(lines, i):
    b, n = map(int, lines[lineno].split())
    x = map(int, lines[lineno + 1].split())
    r = solve(b, x[:n])
    lineno += 2
    msg = 'Case #{}: {:.9f}'.format(i, r)
    return n


def func_28e7f22202344e89b1f6988be06f875b(lines, i):
    b, n = map(int, lines[lineno].split())
    x = map(int, lines[lineno + 1].split())
    r = solve(b, x[:n])
    lineno += 2
    msg = 'Case #{}: {:.9f}'.format(i, r)
    return r


def func_d43731f4efec4533b6bea060051f159f(lines, i):
    b, n = map(int, lines[lineno].split())
    x = map(int, lines[lineno + 1].split())
    r = solve(b, x[:n])
    lineno += 2
    msg = 'Case #{}: {:.9f}'.format(i, r)
    return lineno


def func_5f0ec4a2f226414293e2f00086787703(lines, i):
    b, n = map(int, lines[lineno].split())
    x = map(int, lines[lineno + 1].split())
    r = solve(b, x[:n])
    lineno += 2
    msg = 'Case #{}: {:.9f}'.format(i, r)
    return x


def func_439ecb91373a4b828c40fc68e1e99f8d(lines, i):
    b, n = map(int, lines[lineno].split())
    x = map(int, lines[lineno + 1].split())
    r = solve(b, x[:n])
    lineno += 2
    msg = 'Case #{}: {:.9f}'.format(i, r)
    return msg


def func_ef15dd37c65a4254996472d5e16e71c4(lines, i):
    b, n = map(int, lines[lineno].split())
    x = map(int, lines[lineno + 1].split())
    r = solve(b, x[:n])
    lineno += 2
    msg = 'Case #{}: {:.9f}'.format(i, r)
    return b


def func_6171bd0dce1e4080b3e9c820f6883466():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    return lines


def func_e5adf451338f4970916b0755e97b1165():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    return infile


def func_3b4d10ad5124442bbfe3955f6787c9ab():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    return s


def func_82a614ca7ec6444bab566e31593b1841(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    return s


def func_891ad90c6af74d0e890e310c82a8939a(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    return lines


def func_ddb66daeba6046f9b8ddbb114833116e(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    return c


def func_4c7bccf15bdf46a1a67535c4b423cf91(lines):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    return c


def func_6d954ada386b450294d3f5ba8b1fdc31(lines):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    return f


def func_57d03b8ff55d41b38fe70101debad13b():
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    return f


def func_5cf1006ad04a4217afdd690cd2065fbb():
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    return lineno


def func_ed028aed4eb44e208e0630239fc3707b(c, lines, f):
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return lineno


def func_9d4e728eff24479e83a614c67aa353bc(c, lines, f):
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return r


def func_15b32acea07d45809c4750d04689cd71(c, lines, f):
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return x


def func_87f4c7110c4a4d44a36f6fb5d995b504(c, lines, f):
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return b


def func_f89aa35fdbcd4d0b94ccb41294fd0765(c, lines, f):
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return i


def func_dc4e95e0158f4ed183a92a12f1264aad(c, lines, f):
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return msg


def func_1be21e6ede24456cac2301840428c9f6(c, lines, f):
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return n


def func_d021e6f5fde04c53b7f6ae8475c5e7e2(c, lines, f):
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return msg


def func_9ad15b91507046d7b3d29d3bcbec3352(c, lines, f):
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return r


def func_c989be4c38ca42d19076d13c1d05e616(c, lines, f):
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return n


def func_85fe64ae2a2e4ee584b2a9f87f23c461(c, lines, f):
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return lineno


def func_236ff00f54584e0dbc73f93aed7a6f52(c, lines, f):
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return x


def func_6ad17a9ebf2a4e4dbbee7320de9e483a(c, lines, f):
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return b


def func_e9be3e6b4abd48d9990e65c9c54283c6(c, lines, f):
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return i


def func_ccb8f4765e8b456cb3ac9239126f0bb2():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    return c


def func_81bbc0b3815e47679fb14cbbb504411c():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    return infile


def func_60db2b0b1e784ccba7310d1f29475ba6():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    return lines


def func_861e2c1eef6e454d97fdec2e74f57e74():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    return s


def func_29a54ad6eb324795a186fcf5bc93dacb(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    return lines


def func_87e0a5feadb34db7a7e0ff938d511f89(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    return f


def func_53a0aef29d6d47e88fff0e89e6ab614d(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    return c


def func_bc89bf3996294c1d9ef382131dbaa911(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    return s


def func_96b76bb18bea409383ffe5e71001107d(lines):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    return c


def func_4d7914a2bd7b4b2ca25a21e4a60a4d93(lines):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    return lineno


def func_86abf30ced0c44f381d10405d06e0746(lines):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    return f


def func_89e8479237394880b0ee2a29bc3c6454(c, lines):
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return x


def func_6d0f84ddf99b4bceb0c875f354bdce57(c, lines):
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return i


def func_e31d3db40fc74803825323a3f42595f1(c, lines):
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return lineno


def func_36989cd4ad6f45cd91cb4532396e2781(c, lines):
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return msg


def func_b89e62573942462a927b2930cc41d59c(c, lines):
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return r


def func_c844161897364d33a2c9d7237b6107c0(c, lines):
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return n


def func_3b03e6ed16c748759786e22202e2c879(c, lines):
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return b


def func_8156979645d442158fd2e758c6bd5772(c, lines):
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return f


def func_9b0bf7fa8ebd435bb276312fab50b26b(c, lines, f):
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return x


def func_c4e56265044f4fa480f9b22bb9f2f463(c, lines, f):
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return lineno


def func_6b40224ebf9042beadca0e1f409c735d(c, lines, f):
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return msg


def func_dc00c05f829c463db618d263915581b5(c, lines, f):
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return n


def func_8e96ccde8ad34aefbab97ac403283428(c, lines, f):
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return i


def func_48e733ea071b4d96bdb3e33f79d65290(c, lines, f):
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return b


def func_f042dba20d9b4a34b2e78c933aa3f31c(c, lines, f):
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return r


def func_ee8070353d29460cab1995ec1b976287(c, lines, infile, f):
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return r


def func_502101d5cdba452f87ccf2f4a8f7394f(c, lines, infile, f):
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return x


def func_1df5f71f6c044e7bb15aa46fd75c3252(c, lines, infile, f):
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return n


def func_2ef8cf97c0f14a26b8b906de437220e4(c, lines, infile, f):
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return b


def func_8f4d78341ab04c69b662ef690ace316c(c, lines, infile, f):
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return i


def func_fa20cddc385a4892836cc0bf2ad4718c(c, lines, infile, f):
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return msg


def func_bcf504260e99443a8aed43171f9a6eb7(c, lines, infile, f):
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return lineno


def func_36b48abaf4914255817cd92dcf4210e7():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    return s


def func_be89bcc16f684c6e8c83a441f7a708c9():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    return c


def func_01e4daeaa4064edca0e98aa9449189bb():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    return f


def func_7b34326cfd2a40bc9169b10447a8ab9b():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    return lines


def func_eb598c8109984c648d28b0f62dc379d9():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    return infile


def func_383cace9c59140b3b79caaf56c61f648(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    return lineno


def func_722689295ca0463eb435ca60fb815884(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    return s


def func_00d362e5e15d4722b0264177f8b76010(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    return lines


def func_260a1a728efb4ff8b54efdf62082c654(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    return f


def func_6d83d6e32c624fdaa31f1f6c348164d1(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    return c


def func_31d19549518748d8b0e909e588c3cd6a(lines):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return r


def func_7e3abb6b0e064cd290b1415eb09bfb1e(lines):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return f


def func_8deb49b0ea3945c88516be4c99490daa(lines):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return b


def func_f95c35e8dd8348ff932c09b24329c3e2(lines):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return msg


def func_6080eacd0915403199d2d5628b009bbb(lines):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return lineno


def func_a40bfd9302e8407aa598b6bf6fd07b63(lines):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return x


def func_833b94e9c6ad49c6acd91c8fe9a555df(lines):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return c


def func_5536e3f28aa24297943fef779e6a3dcd(lines):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return i


def func_fd6cfdadc7444009a95c49e3d5108c3a(lines):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return n


def func_fabcfe15e8ae4b5385b7c4c1df702104(c, lines):
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return lineno


def func_1200fb3891c7434fa3f232287f08b4f7(c, lines):
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return x


def func_583403d3122344dd9f444fd480abb3f6(c, lines):
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return msg


def func_6a7864a6fdbb4c4fb27a372404f02e66(c, lines):
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return f


def func_357d140668544adab332eee1985854d0(c, lines):
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return i


def func_9b6a7e4381bb49149ee4def9e52792e2(c, lines):
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return n


def func_0fbda86800244a588e5b057aae929e96(c, lines):
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return r


def func_c30494a7db984a3c8eec419d5d15d268(c, lines):
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return b


def func_19e0cf9a04f94f939347f21b105c6dfd(c, lines, infile, f):
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return msg


def func_190590ef782c418fae16513207edc341(c, lines, infile, f):
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return x


def func_3aee9c113dc842d8bd2ce878dade4410(c, lines, infile, f):
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return b


def func_47d82bf3414441a8ab3f56bf24c51c32(c, lines, infile, f):
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return lineno


def func_361ebe66c0a842198c4117832d6d3cae(c, lines, infile, f):
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return n


def func_b2f71ea730b04c8facf9c06205f29a59(c, lines, infile, f):
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return i


def func_5ad3b07a36384a4d8c3d2a90ece5551f(c, lines, infile, f):
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return r


def func_83e922cf5e6c4dde9fcdac8290c1b2e9():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    return infile


def func_b93ca116c9254bae9489bb2f467a93ec():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    return c


def func_05cc1fbaf057437d8f84d0240dd32b8d():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    return f


def func_d992a1a3b97d4c04a2fb5ecf6bbbd781():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    return s


def func_1b05010368894fbc899fce25db489fdf():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    return lines


def func_daea0e686b2a438aa5d69041d9c86cf7():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    return lineno


def func_6cacb99baa7e48ff83d1077e70683e30(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return i


def func_45a3b7dfca244409b1ff6a3b9156b393(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return n


def func_4e76ac4bbede4f1cb96012b6c557e445(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return r


def func_d88e98a215dd43d2b233bde39ea8630b(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return x


def func_0d27a2d03eb5446b8793802cc216931b(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return c


def func_d371af6ad9bc405b8717c5d10fc399fb(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return lineno


def func_da228275d19a4c619bbd29d68219fd06(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return s


def func_9b79758e212b4969a93028a6961372bf(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return b


def func_a7cbd1167eee44bd8f752c887ae1884d(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return f


def func_62f2e54cbadf4857983882c25403189d(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return lines


def func_9bb6a7b7f1a54c96b25c7910bddfbc92(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return msg


def func_af44d7895b8c4c839416286cb8bcd737(lines):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return c


def func_dfca5bd0f0554b2595483df31fb747c5(lines):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return r


def func_8dddd53b9bbb4d9d8d66ac4975952bbb(lines):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return lineno


def func_51fd2025eb4c46e6a63a15b6a32a65c2(lines):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return f


def func_e838f5dcac11425e8b73bc8f66fa3d77(lines):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return b


def func_d5664fe9bf3f40a8b8ba56831bd990b3(lines):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return n


def func_e86920794f7a472bb8c795a12bbd1e1e(lines):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return x


def func_834f83423bd9446dbc4ebcb1c05dde4b(lines):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return i


def func_d8ebb52e38ac4747bc06eb0266479c94(lines):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return msg


def func_f98a0d91d62849cfa97beea8e6fd0718(c, lines, infile):
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return msg


def func_ef60dcf3f914452dbf62054935a6db2a(c, lines, infile):
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return x


def func_1cc7905b7b2740a1bdf512d6e8ee954d(c, lines, infile):
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return b


def func_707869425acb46b48d99989e23303117(c, lines, infile):
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return r


def func_2e8feca2650b439dac46b0d41537268d(c, lines, infile):
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return lineno


def func_599f1bd8f79c416dae72c361296b23c5(c, lines, infile):
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return f


def func_02d8fbf709034112ab01cee886eb99f4(c, lines, infile):
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return n


def func_d8ad45a57dba465e99c0916389241134(c, lines, infile):
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return i


def func_b6a09ae1f33045488ca426ddb0eb9353():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return msg


def func_37602b7a252447d49fa781e059a1e822():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return r


def func_3faa31ec202f4557a46d382e70f6d743():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return f


def func_cdbf48d9d6b64eb99447fe8868609af5():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return n


def func_3592e75bdda74ac19675d5d1f863e499():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return s


def func_b4b345277a80439da1fb89a394317c02():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return x


def func_7f2ca49961fb406c88e79f76e4c7646b():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return i


def func_440643013c824741895b7ef740950df5():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return lines


def func_136a074d14d5415b8f8ed286dfead4d5():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return c


def func_e7505a162dc44334b0ef81ac547cda38():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return lineno


def func_133377a200344828a0e17e3ac12ccf9c():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return infile


def func_fb757d4e08fa4c29be44709ee1d0413f():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    return b


def func_66bb3cd5bf7d4a81986d1db9c1597809(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return c


def func_2c7ac7f0d64d42879af72015852e2c35(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return b


def func_e7a399c4367b4fda9190d3777cdcb3f9(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return r


def func_9be28c882d224997af9527444b84c2f4(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return f


def func_2719078d7d5d4d9f959f594ee7ddf9d7(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return s


def func_75476bd955bf4c91b8bf02af8c00ce9b(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return n


def func_bfaa9dc7c1b044289e1cd91ad7285d7c(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return msg


def func_ba40fa5b4a0649b1a5bad0d6e3e0f6ac(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return x


def func_19bb3dbdf965418c97d40b710690b834(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return lineno


def func_0f85611e7ddc41cd9799a5fba133be61(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return lines


def func_c161118d774b48c0b5d622258903599d(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return i


def func_94fd0e606969409abacc30bbb3a3d34f(lines, infile):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return c


def func_1778424788634599af396d1d5501a7c7(lines, infile):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return f


def func_2dfe8b6f1a9a4a34987b6224bcf04574(lines, infile):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return x


def func_f39fd079d15743ee800930d2b365365e(lines, infile):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return b


def func_b456fb48a1a64bafb6e1eaf1b178797d(lines, infile):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return i


def func_750424cea3fb48c2bf2a8188203176cd(lines, infile):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return lineno


def func_0a6eab03cb61471aba787d325bf4520f(lines, infile):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return r


def func_52a540f058cc4aabbd2a6a6d75831b96(lines, infile):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return msg


def func_df0c7758da2743768034c47edbc3f1a6(lines, infile):
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return n


def func_203adba9d8d74acd92ed242b000717d5():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return x


def func_0c6f21f197724b0daca3f8ac97ad891c():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return b


def func_7f0e9f2fd7154a22a1f219abbfb3cc86():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return i


def func_5c51494d8a20475b95cf14467bdb4b32():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return msg


def func_5e9428e5abe64d84a760adc008943dfc():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return lineno


def func_71c887c65fe24560a8081769daefbe5a():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return n


def func_a984200eab4e4f5aafcfd9c362c79a1e():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return r


def func_143096a3901b40f69f8ea61fb81a2579():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return f


def func_02c05b7bff3c48e98b1ea8232e1a95f1():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return c


def func_c2661055931c45c8a7708a2896b9f8c1():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return lines


def func_0a03d484880044c889150cbb65e3dff6():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return s


def func_7b4d9fa3472e448a9cbbe90562a4def3():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    return infile


def func_919900ec6b9340ff89449a21f94c761a(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return r


def func_794f2d940a6e46b88b7f61dd1cf41c4d(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return i


def func_7f224b3796d44d5ea4943478f7c3a1b0(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return lines


def func_3fabd8b0b0e841caa5219c5f7fcabbf4(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return b


def func_5cf25e714aec4014ad298fe3f57daac4(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return f


def func_e5dee86745194dc383fbb1a9fda3e573(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return n


def func_ac8707cd08ad42e3bd7f064e7c801578(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return c


def func_a6d8f778bfc8464e905f0e2c981de920(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return s


def func_0e2600c6804448f6a6d961403ef5a261(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return msg


def func_9793809ccf1949f18b1b82ee4a78f7f4(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return x


def func_d3d351b858614119ae59b3608ca942ca(infile):
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return lineno


def func_f53fe731f16a4777b3675e0febf66f12():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return i


def func_e5a9f1fb1be34d279566370fc5d2d755():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return lines


def func_6c9cd67fbc7e4fc9937e0f32d5fab5d6():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return msg


def func_d007697f971341f4bc82bba38d5d4631():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return x


def func_f872d3afed2c473fb3e048237ff61a71():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return lineno


def func_12453a65754e4678aaa493df8d3a20dd():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return b


def func_b0a5a0f11631438a890617b80a88175c():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return n


def func_78e025520f584950937cb41484313b4c():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return c


def func_50b219e3c6664249b844d234777b3bca():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return f


def func_16861d8d17dc4a55b2bb684bd8682371():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return r


def func_3e36c6e0fee14a73931f9ea576958a91():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return s


def func_ac9f7c80a71044579d9ee8937b44af38():
    infile = open('codejam/test_files/Y13R5P1/A.in')
    lines = [s.strip() for s in infile.readlines()]
    c = int(lines[0])
    f = open('codejam/test_files/Y13R5P1/A.out', 'w')
    lineno = 1
    for i in range(1, c + 1):
        b, n = map(int, lines[lineno].split())
        x = map(int, lines[lineno + 1].split())
        r = solve(b, x[:n])
        lineno += 2
        msg = 'Case #{}: {:.9f}'.format(i, r)
        print msg
        print  >> f, msg
    f.close()
    infile.close()
    return infile

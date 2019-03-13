import sys
sys.path.append('/home/george2/Raise/ProgramRepair/CodeSeer/projects/src/main/python')
from Y13R5P1.alantian.p import *

def func_6d15997fb380463299757fb8f1e25752(s, y, x, b):
    need = f1(x[:s], y) + f1(x[s:], y + 1)
    return need <= b


def func_464ce883e7a94d65a1bc6b62ce3e43f6(n, s, b, x):
    mid = (lo + hi + 1) / 2
    if ok(b, n, x, s, mid):
        lo = mid
    else:
        hi = mid - 1
    return hi


def func_8d28153262d948c3bfba4ee0607c2fa8(n, s, b, x):
    mid = (lo + hi + 1) / 2
    if ok(b, n, x, s, mid):
        lo = mid
    else:
        hi = mid - 1
    return lo


def func_8a28c09434594f268bc2dec64a0e8091(n, s, b, x):
    mid = (lo + hi + 1) / 2
    if ok(b, n, x, s, mid):
        lo = mid
    else:
        hi = mid - 1
    return mid


def func_30b667c55439447db33e192b65dccc55(x):
    if len(x) < 37:
        x = x + [0] * (37 - len(x))
    x = sorted(x)
    return x


def func_7828b96ed9024ef28fa4c953139672e4(x):
    x = sorted(x)
    lo = min(x)
    return lo


def func_27e8b9ab54c249af9796db4e19aa35e7(x):
    x = sorted(x)
    lo = min(x)
    return x


def func_fc1df07e5f3644499d33685ea449984b(x):
    lo = min(x)
    hi = max(x)
    return hi


def func_7e72a51a0427499ab4bba0a107c24e4e(x):
    lo = min(x)
    hi = max(x)
    return lo


def func_46617c68ff684ba2a688fd3ae4c3db19(n, s, b, x):
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    return mid


def func_110e1ed109084b47a9fba59fef52e347(n, s, b, x):
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    return lo


def func_a948e164b7f24873b86af5277b26b655(n, s, b, x):
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    return hi


def func_6342366797f94d1aab4a6790de7e26a0(n, s, b, x):
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return y


def func_568bd50a95a344f1be0eb5b075eb9a67(n, s, b, x):
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return hi


def func_a3ebed2e4edd4287a7750b2d903674e7(n, s, b, x):
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return mid


def func_af09105c4fe043d38a36e86cc251c5f8(n, s, b, x):
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return lo


def func_5ad43800f6a24493a8934442a8d78c5c(s, lo, x):
    y = lo
    return f1(x[:s], y) * 36.0 / s - (f1(x[:s], y) + f1(x[s:], y + 1))


def func_7af80095a25446d99fe14f8430e753ac(x):
    if len(x) < 37:
        x = x + [0] * (37 - len(x))
    x = sorted(x)
    lo = min(x)
    return x


def func_8554b3480b7c49bf8d6510648af5974e(x):
    if len(x) < 37:
        x = x + [0] * (37 - len(x))
    x = sorted(x)
    lo = min(x)
    return lo


def func_273c2be545644bd8900777837a2318d3(x):
    x = sorted(x)
    lo = min(x)
    hi = max(x)
    return x


def func_eedeeab5dfea4907b2e517e7f98617e2(x):
    x = sorted(x)
    lo = min(x)
    hi = max(x)
    return hi


def func_6ba6a21b2a2d43148d994bac1df78e7a(x):
    x = sorted(x)
    lo = min(x)
    hi = max(x)
    return lo


def func_5f6c9a4aaaf048c48c727976d1a0d472(n, s, b, x):
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    return lo


def func_dac7c11dfca64bc3bf7f2a1e3a55dece(n, s, b, x):
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    return hi


def func_ff408e9842be4e998c22f89149b41e25(n, s, b, x):
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    return mid


def func_a8adc2744e004a1f828a09c84e5ce077(n, s, b, x):
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return y


def func_e0d48f34cbd246c38ab47c51fab55951(n, s, b, x):
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return mid


def func_d1cff6d6aaba4a20b061ea86151c1e64(n, s, b, x):
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return hi


def func_ec37af4c6c894950ba4a88ebe17f5969(n, s, b, x):
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return lo


def func_6ae642283e924cfc97864171f6e727ec(n, s, b, x):
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return f1(x[:s], y) * 36.0 / s - (f1(x[:s], y) + f1(x[s:], y + 1))


def func_774b404443274841a3a1f3703f0d3645(x):
    if len(x) < 37:
        x = x + [0] * (37 - len(x))
    x = sorted(x)
    lo = min(x)
    hi = max(x)
    return hi


def func_b386aea9a37d4a559019a3f26a72c65e(x):
    if len(x) < 37:
        x = x + [0] * (37 - len(x))
    x = sorted(x)
    lo = min(x)
    hi = max(x)
    return lo


def func_d9bcd2a71caa4aeb94d01b5eced27a7b(x):
    if len(x) < 37:
        x = x + [0] * (37 - len(x))
    x = sorted(x)
    lo = min(x)
    hi = max(x)
    return x


def func_e235afadecf34dd6be0a3f3533b0f8f2(n, s, b, x):
    x = sorted(x)
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    return lo


def func_f302128ef55a4d2584b21d20cb8cdcea(n, s, b, x):
    x = sorted(x)
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    return mid


def func_a284247d232848b2811304fb78e5674e(n, s, b, x):
    x = sorted(x)
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    return hi


def func_10982bccfe184fe5990feddd628eb987(n, s, b, x):
    x = sorted(x)
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    return x


def func_e9e971f4b7d743ecb28c2ab6cd4eaef3(n, s, b, x):
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return y


def func_6e97e1b754af43779abd92d873fc6132(n, s, b, x):
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return lo


def func_68574e401c5b49408352f84fbd2f3159(n, s, b, x):
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return mid


def func_d7eb76a4b3b34c1f8641a4a12a0c2ed3(n, s, b, x):
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return hi


def func_2bc97ec91ddb43969c3ca08e1a15226a(n, s, b, x):
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return f1(x[:s], y) * 36.0 / s - (f1(x[:s], y) + f1(x[s:], y + 1))


def func_f737a2a5856c487982c2b888e0762838(n, s, b, x):
    if len(x) < 37:
        x = x + [0] * (37 - len(x))
    x = sorted(x)
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    return lo


def func_8c5a44c9fac64d53b3180740a70a7779(n, s, b, x):
    if len(x) < 37:
        x = x + [0] * (37 - len(x))
    x = sorted(x)
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    return hi


def func_2bd4397a4b2f41f1bcabeddf6686dfa7(n, s, b, x):
    if len(x) < 37:
        x = x + [0] * (37 - len(x))
    x = sorted(x)
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    return x


def func_cb4d6843399a4822a826a0b2ec2c48e4(n, s, b, x):
    if len(x) < 37:
        x = x + [0] * (37 - len(x))
    x = sorted(x)
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    return mid


def func_05303aabccd04dad92763b2a58f0fdb1(n, s, b, x):
    x = sorted(x)
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return y


def func_d1b1163061af4f88aacc5a0de624412a(n, s, b, x):
    x = sorted(x)
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return x


def func_8b93731958e743cea911fc145bc2acf9(n, s, b, x):
    x = sorted(x)
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return lo


def func_4b311ade0a964126af93b8cd88c87e33(n, s, b, x):
    x = sorted(x)
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return mid


def func_b34ed897e9314793885083c17ce70390(n, s, b, x):
    x = sorted(x)
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return hi


def func_af103061d6a5452bb9faa1b06eec3635(n, s, b, x):
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return f1(x[:s], y) * 36.0 / s - (f1(x[:s], y) + f1(x[s:], y + 1))


def func_a7fb2effe43c46999358554945da3649(n, s, b, x):
    if len(x) < 37:
        x = x + [0] * (37 - len(x))
    x = sorted(x)
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return y


def func_1ea2edac273a4d109cf104bca5e3dc45(n, s, b, x):
    if len(x) < 37:
        x = x + [0] * (37 - len(x))
    x = sorted(x)
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return lo


def func_5c2df4559a8c4d199790698bf7498707(n, s, b, x):
    if len(x) < 37:
        x = x + [0] * (37 - len(x))
    x = sorted(x)
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return x


def func_3d68793b43ff4169a81f2930f380dc54(n, s, b, x):
    if len(x) < 37:
        x = x + [0] * (37 - len(x))
    x = sorted(x)
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return hi


def func_70d06905979c46808b0fa4d3098a94bc(n, s, b, x):
    if len(x) < 37:
        x = x + [0] * (37 - len(x))
    x = sorted(x)
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return mid


def func_7bcbccd3c59f493bb73767e26cae396f(n, s, b, x):
    x = sorted(x)
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return f1(x[:s], y) * 36.0 / s - (f1(x[:s], y) + f1(x[s:], y + 1))


def func_ce7f3ad9907e4c46ad33c613715ca552(n, s, b, x):
    if len(x) < 37:
        x = x + [0] * (37 - len(x))
    x = sorted(x)
    lo = min(x)
    hi = max(x)
    while lo < hi:
        mid = (lo + hi + 1) / 2
        if ok(b, n, x, s, mid):
            lo = mid
        else:
            hi = mid - 1
    y = lo
    return f1(x[:s], y) * 36.0 / s - (f1(x[:s], y) + f1(x[s:], y + 1))


def func_d3b9d02cda954f5cbb5acd1c48cc7a1e(n, b, x, s):
    currAns = go(b, n, x, s)
    ans = max(ans, currAns)
    return ans


def func_8549d9cd901c4c82a6a05ed00b3438bb(n, b, x, s):
    currAns = go(b, n, x, s)
    ans = max(ans, currAns)
    return currAns


def func_c2e72d9d7cad40e7b65af8164636d334(n, b, x):
    ans = 0.0
    for s in range(1, 37):
        currAns = go(b, n, x, s)
        ans = max(ans, currAns)
    return ans


def func_f8d92077e0ea4547b6fe4e33cc5cd5f7(n, b, x):
    ans = 0.0
    for s in range(1, 37):
        currAns = go(b, n, x, s)
        ans = max(ans, currAns)
    return s


def func_1598553191fa46cd8e7fb9e82b04318a(n, b, x):
    ans = 0.0
    for s in range(1, 37):
        currAns = go(b, n, x, s)
        ans = max(ans, currAns)
    return currAns


def func_1ca240d7b89c45029e653e35a18956b2(n, b, x):
    for s in range(1, 37):
        currAns = go(b, n, x, s)
        ans = max(ans, currAns)
    return ans


def func_4c177fd760f44376bd051c1e7c00650a(n, b, x):
    ans = 0.0
    for s in range(1, 37):
        currAns = go(b, n, x, s)
        ans = max(ans, currAns)
    return ans


def func_e67ac93084de4c3aba3756fe47fd276d(infile):
    b, n = rl(infile)
    x = rl(infile)
    return x


def func_b9c4d6616d8a4bbf9590210df76ed73c(infile):
    b, n = rl(infile)
    x = rl(infile)
    return n


def func_3a0a23add872440f950c74a8ec7dca72(infile):
    b, n = rl(infile)
    x = rl(infile)
    return b


def func_0d01af8c633b4a158aa5087ec59cda1c(n, infile, b):
    x = rl(infile)
    ans = solve(b, n, x)
    return ans


def func_33de68d91ad143698ee3b58d69d11eb6(n, infile, b):
    x = rl(infile)
    ans = solve(b, n, x)
    return x


def func_b388bec759d544eaaa6a00fb85accfdd(t, n, x, b):
    ans = solve(b, n, x)('Case #%d: %.10f' % (t, ans))
    return ans


def func_4f040f8d81ab4da09b278855738e7209(infile):
    b, n = rl(infile)
    x = rl(infile)
    ans = solve(b, n, x)
    return ans


def func_75078162262f44bca659b87dc9749bd2(infile):
    b, n = rl(infile)
    x = rl(infile)
    ans = solve(b, n, x)
    return x


def func_d5c9856838e84c9bbef1dfe1bc2ff01c(infile):
    b, n = rl(infile)
    x = rl(infile)
    ans = solve(b, n, x)
    return b


def func_09193e91c8da4150bb7544cbd3f72d24(infile):
    b, n = rl(infile)
    x = rl(infile)
    ans = solve(b, n, x)
    return n


def func_599d619b5d374f3da21a818ad719d0e6(t, n, infile, b):
    x = rl(infile)
    ans = solve(b, n, x)('Case #%d: %.10f' % (t, ans))
    return x


def func_dfa00ec767d84795bf2e8fc85ddcbe66(t, n, infile, b):
    x = rl(infile)
    ans = solve(b, n, x)('Case #%d: %.10f' % (t, ans))
    return ans


def func_4c5bc211ff604c1b86de308060bfd065(t, infile):
    b, n = rl(infile)
    x = rl(infile)
    ans = solve(b, n, x)('Case #%d: %.10f' % (t, ans))
    return x


def func_625db57f0b624b67911993143fd743d0(t, infile):
    b, n = rl(infile)
    x = rl(infile)
    ans = solve(b, n, x)('Case #%d: %.10f' % (t, ans))
    return b


def func_bf56b4678aa645ddbcb25ba0e43bc895(t, infile):
    b, n = rl(infile)
    x = rl(infile)
    ans = solve(b, n, x)('Case #%d: %.10f' % (t, ans))
    return ans


def func_de8a635c3e244078b84d7fa42fd7c327(t, infile):
    b, n = rl(infile)
    x = rl(infile)
    ans = solve(b, n, x)('Case #%d: %.10f' % (t, ans))
    return n


def func_398213b241464874b071a11e87bd462e():
    infile = open('test_files/Y13R5P1/A.in')
    T, = rl(infile)
    return T


def func_7b719bb6090e4caaa954baec51001fb9():
    infile = open('test_files/Y13R5P1/A.in')
    T, = rl(infile)
    return infile


def func_16777ab5e20f4cb08ef608301257d26c(infile):
    T, = rl(infile)
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    return t


def func_b34b1cf1955045448027c15006014bf3(infile):
    T, = rl(infile)
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    return ans


def func_207e2ede9cde4230b5f336fb6c077cd3(infile):
    T, = rl(infile)
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    return n


def func_8f7f966331884295a6e54f324f392fd5(infile):
    T, = rl(infile)
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    return T


def func_d93cbeda1c344322a4229c226f2057e3(infile):
    T, = rl(infile)
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    return x


def func_76ffc28f7aaf4be2815aac2a9e6654d2(infile):
    T, = rl(infile)
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    return b


def func_81008dcf89574419a6cf40a0687974ba(T, infile):
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    infile.close()
    return ans


def func_9d73dee698684a00916242f3f1597174(T, infile):
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    infile.close()
    return t


def func_b34a6ef9c40c47c8b4c68f4666183643(T, infile):
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    infile.close()
    return b


def func_ff59c0c10fe14bac824c6661be427b6a(T, infile):
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    infile.close()
    return n


def func_0d83e2e493bf42b4b1753652151bdcf5(T, infile):
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    infile.close()
    return x


def func_f110a3b4550444848e626bb504382d10():
    infile = open('test_files/Y13R5P1/A.in')
    T, = rl(infile)
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    return t


def func_b3cea022f3f74bf3b536a68214566b8c():
    infile = open('test_files/Y13R5P1/A.in')
    T, = rl(infile)
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    return infile


def func_ac6fe90af7aa49afa23e64f274d403eb():
    infile = open('test_files/Y13R5P1/A.in')
    T, = rl(infile)
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    return ans


def func_1c53e7ffc8914731a0b99ad2a7999aea():
    infile = open('test_files/Y13R5P1/A.in')
    T, = rl(infile)
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    return b


def func_bc0e435f963a4302b5d200b0e82d1766():
    infile = open('test_files/Y13R5P1/A.in')
    T, = rl(infile)
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    return x


def func_ff64964f761d4dd4b339334ae7bf16a7():
    infile = open('test_files/Y13R5P1/A.in')
    T, = rl(infile)
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    return n


def func_fadadec41eb846798c4bbef4ca650833():
    infile = open('test_files/Y13R5P1/A.in')
    T, = rl(infile)
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    return T


def func_eb02ffef50834f35b6906bb117ec7e08(infile):
    T, = rl(infile)
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    infile.close()
    return b


def func_93e863b46dd14dec8a0968b7eaadcbff(infile):
    T, = rl(infile)
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    infile.close()
    return n


def func_78a70f3b2080465280d6adaa799a34d4(infile):
    T, = rl(infile)
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    infile.close()
    return t


def func_f13bb18861164e91bf545a91a606c969(infile):
    T, = rl(infile)
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    infile.close()
    return ans


def func_5d683f6844df4747a56123e38278cf75(infile):
    T, = rl(infile)
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    infile.close()
    return x


def func_11c54e0444bf496aa2d894c52c16f8d4(infile):
    T, = rl(infile)
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    infile.close()
    return T


def func_114d52483be4409b908d21d83d7a10b2():
    infile = open('test_files/Y13R5P1/A.in')
    T, = rl(infile)
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    infile.close()
    return ans


def func_ee32c7d85b79403baf2759ba4eb9b12c():
    infile = open('test_files/Y13R5P1/A.in')
    T, = rl(infile)
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    infile.close()
    return n


def func_283a4654fe0f40ef9f05d992cee2573b():
    infile = open('test_files/Y13R5P1/A.in')
    T, = rl(infile)
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    infile.close()
    return b


def func_0fee1d8d3c7e449fab1dc1744b0a7dfc():
    infile = open('test_files/Y13R5P1/A.in')
    T, = rl(infile)
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    infile.close()
    return x


def func_8f96736a1b9d4771a853198c678d9c9f():
    infile = open('test_files/Y13R5P1/A.in')
    T, = rl(infile)
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    infile.close()
    return t


def func_4b29adaed6134f1ca05f05c006b16fe7():
    infile = open('test_files/Y13R5P1/A.in')
    T, = rl(infile)
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    infile.close()
    return infile


def func_dc42418db0514c0988f955c64432dc45():
    infile = open('test_files/Y13R5P1/A.in')
    T, = rl(infile)
    for t in range(1, T + 1):
        b, n = rl(infile)
        x = rl(infile)
        ans = solve(b, n, x)
        print 'Case #%d: %.10f' % (t, ans)
    infile.close()
    return T

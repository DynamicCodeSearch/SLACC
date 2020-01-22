import sys
sys.path.append('/home/george2/Raise/ProgramRepair/CodeSeer/projects/src/main/python')
from CodeJam.Y13R5P1.kmod.a2 import *

def func_3d9dd718518d49439297ced3533f0ee4(size, bets, num_min):
    t = 0
    for i in xrange(num_min):
        assert size >= bets[i]
        t += size - bets[i]
    return t


def func_3f02c79efdc749babe8297716bcc9ce2(size, bets, num_min):
    t = 0
    for i in xrange(num_min):
        assert size >= bets[i]
        t += size - bets[i]
    return i


def func_1012dc0cd8d346e28f5dd53e931a68ea(size, bets, num_min):
    for i in xrange(num_min):
        assert size >= bets[i]
        t += size - bets[i]
    for i in xrange(num_min, 37):
        if bets[i] <= size:
            t += size + 1 - bets[i]
    return i


def func_432223161d6f4794bd7157cf65353647(size, bets, num_min):
    for i in xrange(num_min):
        assert size >= bets[i]
        t += size - bets[i]
    for i in xrange(num_min, 37):
        if bets[i] <= size:
            t += size + 1 - bets[i]
    return t


def func_422f3a21b924419da4d5611b98bb5483(size, bets, num_min):
    for i in xrange(num_min, 37):
        if bets[i] <= size:
            t += size + 1 - bets[i]
    if bets[i] <= size:
        t += size + 1 - bets[i]
    return t


def func_6ce921bfa277490b9a7fdb6e7730d40a(size, bets, num_min):
    for i in xrange(num_min, 37):
        if bets[i] <= size:
            t += size + 1 - bets[i]
    if bets[i] <= size:
        t += size + 1 - bets[i]
    return i


def func_092bd20115f4487c8f442049ebd12112(size, i, bets):
    if bets[i] <= size:
        t += size + 1 - bets[i]
    return t


def func_cb9729025d904b27aac432c0b69833eb(size, bets, num_min):
    t = 0
    for i in xrange(num_min):
        assert size >= bets[i]
        t += size - bets[i]
    for i in xrange(num_min, 37):
        if bets[i] <= size:
            t += size + 1 - bets[i]
    return t


def func_4b30eb7009794840b38add0dd241a49c(size, bets, num_min):
    t = 0
    for i in xrange(num_min):
        assert size >= bets[i]
        t += size - bets[i]
    for i in xrange(num_min, 37):
        if bets[i] <= size:
            t += size + 1 - bets[i]
    return i


def func_5e72dd9753e64978b3a8e1bea4912e42(size, bets, num_min):
    for i in xrange(num_min):
        assert size >= bets[i]
        t += size - bets[i]
    for i in xrange(num_min, 37):
        if bets[i] <= size:
            t += size + 1 - bets[i]
    if bets[i] <= size:
        t += size + 1 - bets[i]
    return i


def func_e308743ec04a4492a22d944b9d5e67c4(size, bets, num_min):
    for i in xrange(num_min):
        assert size >= bets[i]
        t += size - bets[i]
    for i in xrange(num_min, 37):
        if bets[i] <= size:
            t += size + 1 - bets[i]
    if bets[i] <= size:
        t += size + 1 - bets[i]
    return t


def func_a7974a6ebe5245769a35adc78a8d8648(size, bets, num_min):
    for i in xrange(num_min, 37):
        if bets[i] <= size:
            t += size + 1 - bets[i]
    if bets[i] <= size:
        t += size + 1 - bets[i]
    return t


def func_3782cdb933294a159116c2f4ae6ae035(size, bets, num_min):
    t = 0
    for i in xrange(num_min):
        assert size >= bets[i]
        t += size - bets[i]
    for i in xrange(num_min, 37):
        if bets[i] <= size:
            t += size + 1 - bets[i]
    if bets[i] <= size:
        t += size + 1 - bets[i]
    return t


def func_45d4659d9139428f98a6931ad250a11e(size, bets, num_min):
    t = 0
    for i in xrange(num_min):
        assert size >= bets[i]
        t += size - bets[i]
    for i in xrange(num_min, 37):
        if bets[i] <= size:
            t += size + 1 - bets[i]
    if bets[i] <= size:
        t += size + 1 - bets[i]
    return i


def func_4c592ab6c5fe446cae537fae2bde328d(size, bets, num_min):
    for i in xrange(num_min):
        assert size >= bets[i]
        t += size - bets[i]
    for i in xrange(num_min, 37):
        if bets[i] <= size:
            t += size + 1 - bets[i]
    if bets[i] <= size:
        t += size + 1 - bets[i]
    return t


def func_1783254f4b5e47248a8757a08a25f6ff(size, bets, num_min):
    t = 0
    for i in xrange(num_min):
        assert size >= bets[i]
        t += size - bets[i]
    for i in xrange(num_min, 37):
        if bets[i] <= size:
            t += size + 1 - bets[i]
    if bets[i] <= size:
        t += size + 1 - bets[i]
    return t


def func_78b6d1b5ea1c47b381613f4356a6d00c(g, bets, num_min):
    low = g
    amount_bet = g * num_min - sum(bets[:num_min])
    return low


def func_4cf9fd57327342f6a2e7dfa99ddd6882(g, bets, num_min):
    low = g
    amount_bet = g * num_min - sum(bets[:num_min])
    return amount_bet


def func_45d0d1be32c849cd81f6b34ba953c85d(g, c, bets, num_min):
    amount_bet = g * num_min - sum(bets[:num_min])
    best = max(amount_bet * 36.0 / num_min - c, best)
    return best


def func_4a965d04e7874dccbc28fa11fb188682(g, c, bets, num_min):
    amount_bet = g * num_min - sum(bets[:num_min])
    best = max(amount_bet * 36.0 / num_min - c, best)
    return amount_bet


def func_f53559f8231846d89c92f34ce0e4fbdd(g, c, bets, num_min):
    low = g
    amount_bet = g * num_min - sum(bets[:num_min])
    best = max(amount_bet * 36.0 / num_min - c, best)
    return amount_bet


def func_c29c418058da4e6f909a1b120b30109f(g, c, bets, num_min):
    low = g
    amount_bet = g * num_min - sum(bets[:num_min])
    best = max(amount_bet * 36.0 / num_min - c, best)
    return low


def func_1114878412194b02930fd9238375fd83(g, c, bets, num_min):
    low = g
    amount_bet = g * num_min - sum(bets[:num_min])
    best = max(amount_bet * 36.0 / num_min - c, best)
    return best


def func_b2dcbfcc402144e0aadbb1837abbbef2(low, high):
    g = (high + low + 1) / 2
    c = cost(g)
    return g


def func_93961475b23e480e934a60c2d924afaa(low, high):
    g = (high + low + 1) / 2
    c = cost(g)
    return c


def func_36a2c3d37dde4e489f00272baff153dc(g, B, bets, num_min):
    c = cost(g)
    if c > B:
        high = g - 1
    else:
        low = g
        amount_bet = g * num_min - sum(bets[:num_min])
        best = max(amount_bet * 36.0 / num_min - c, best)
    return c


def func_708799613058467cad08465c462be28a(g, B, bets, num_min):
    c = cost(g)
    if c > B:
        high = g - 1
    else:
        low = g
        amount_bet = g * num_min - sum(bets[:num_min])
        best = max(amount_bet * 36.0 / num_min - c, best)
    return amount_bet


def func_925d31e8e98947109d6a5144bd4d6a6d(g, B, bets, num_min):
    c = cost(g)
    if c > B:
        high = g - 1
    else:
        low = g
        amount_bet = g * num_min - sum(bets[:num_min])
        best = max(amount_bet * 36.0 / num_min - c, best)
    return low


def func_b52d8ed38da8421892e04c1d3fe511ea(g, B, bets, num_min):
    c = cost(g)
    if c > B:
        high = g - 1
    else:
        low = g
        amount_bet = g * num_min - sum(bets[:num_min])
        best = max(amount_bet * 36.0 / num_min - c, best)
    return high


def func_2b104eeab1294683ab1bc55c61b5787f(g, B, bets, num_min):
    c = cost(g)
    if c > B:
        high = g - 1
    else:
        low = g
        amount_bet = g * num_min - sum(bets[:num_min])
        best = max(amount_bet * 36.0 / num_min - c, best)
    return best


def func_91c54914929848b1b1ad7343ce5bab11(B, bets, num_min):
    g = (high + low + 1) / 2
    c = cost(g)
    if c > B:
        high = g - 1
    else:
        low = g
        amount_bet = g * num_min - sum(bets[:num_min])
        best = max(amount_bet * 36.0 / num_min - c, best)
    return high


def func_c41fa5550f5b42558b387da8893d78be(B, bets, num_min):
    g = (high + low + 1) / 2
    c = cost(g)
    if c > B:
        high = g - 1
    else:
        low = g
        amount_bet = g * num_min - sum(bets[:num_min])
        best = max(amount_bet * 36.0 / num_min - c, best)
    return low


def func_2dc686966e004878adc6664e099fc4a9(B, bets, num_min):
    g = (high + low + 1) / 2
    c = cost(g)
    if c > B:
        high = g - 1
    else:
        low = g
        amount_bet = g * num_min - sum(bets[:num_min])
        best = max(amount_bet * 36.0 / num_min - c, best)
    return best


def func_db20a428715c4c869e37c63aca1d0658(B, bets, num_min):
    g = (high + low + 1) / 2
    c = cost(g)
    if c > B:
        high = g - 1
    else:
        low = g
        amount_bet = g * num_min - sum(bets[:num_min])
        best = max(amount_bet * 36.0 / num_min - c, best)
    return c


def func_260be3f56ae3426fad30781361fa8da0(B, bets, num_min):
    g = (high + low + 1) / 2
    c = cost(g)
    if c > B:
        high = g - 1
    else:
        low = g
        amount_bet = g * num_min - sum(bets[:num_min])
        best = max(amount_bet * 36.0 / num_min - c, best)
    return g


def func_39d90e0ba32243b08987f36c182447bd(B, bets, num_min):
    g = (high + low + 1) / 2
    c = cost(g)
    if c > B:
        high = g - 1
    else:
        low = g
        amount_bet = g * num_min - sum(bets[:num_min])
        best = max(amount_bet * 36.0 / num_min - c, best)
    return amount_bet


def func_75d93cea4dac4f07b3a036d484218e41(_bets, num_min):
    bets = list(_bets)

    def cost(size):
        t = 0
        for i in xrange(num_min):
            assert size >= bets[i]
            t += size - bets[i]
        for i in xrange(num_min, 37):
            if bets[i] <= size:
                t += size + 1 - bets[i]
        return t
    return bets


def func_5663f85f8e1140cd93900eaa4c2ab666(bets, num_min):

    def cost(size):
        t = 0
        for i in xrange(num_min):
            assert size >= bets[i]
            t += size - bets[i]
        for i in xrange(num_min, 37):
            if bets[i] <= size:
                t += size + 1 - bets[i]
        return t
    low = max(bets[:num_min]) - 1
    return low


def func_e519fb5bd9d1427fbfc0a9a3a39e1635(bets, num_min):
    low = max(bets[:num_min]) - 1
    high = 10000000000000
    return high


def func_7d1a127ce4fd4adf9193a8e7772ac40d(bets, num_min):
    low = max(bets[:num_min]) - 1
    high = 10000000000000
    return low


def func_b09d0cde67d64c0e8c9784814392c87f(B, bets, num_min):
    high = 10000000000000
    while high > low:
        g = (high + low + 1) / 2
        c = cost(g)
        if c > B:
            high = g - 1
        else:
            low = g
            amount_bet = g * num_min - sum(bets[:num_min])
            best = max(amount_bet * 36.0 / num_min - c, best)
    return low


def func_9239696145784741a6aac31e936c24d9(B, bets, num_min):
    high = 10000000000000
    while high > low:
        g = (high + low + 1) / 2
        c = cost(g)
        if c > B:
            high = g - 1
        else:
            low = g
            amount_bet = g * num_min - sum(bets[:num_min])
            best = max(amount_bet * 36.0 / num_min - c, best)
    return g


def func_2f3520fd4f294bc99a4c9015eb975e28(B, bets, num_min):
    high = 10000000000000
    while high > low:
        g = (high + low + 1) / 2
        c = cost(g)
        if c > B:
            high = g - 1
        else:
            low = g
            amount_bet = g * num_min - sum(bets[:num_min])
            best = max(amount_bet * 36.0 / num_min - c, best)
    return high


def func_b17dd37e58594a24b438751c5b4ae04d(B, bets, num_min):
    high = 10000000000000
    while high > low:
        g = (high + low + 1) / 2
        c = cost(g)
        if c > B:
            high = g - 1
        else:
            low = g
            amount_bet = g * num_min - sum(bets[:num_min])
            best = max(amount_bet * 36.0 / num_min - c, best)
    return amount_bet


def func_c52393c8f1d24bb7b6863670f03ee077(B, bets, num_min):
    high = 10000000000000
    while high > low:
        g = (high + low + 1) / 2
        c = cost(g)
        if c > B:
            high = g - 1
        else:
            low = g
            amount_bet = g * num_min - sum(bets[:num_min])
            best = max(amount_bet * 36.0 / num_min - c, best)
    return best


def func_8586c52b68b34245a36b0310189f3924(B, bets, num_min):
    high = 10000000000000
    while high > low:
        g = (high + low + 1) / 2
        c = cost(g)
        if c > B:
            high = g - 1
        else:
            low = g
            amount_bet = g * num_min - sum(bets[:num_min])
            best = max(amount_bet * 36.0 / num_min - c, best)
    return c


def func_320f340e00ea4c73975617839c211163(_bets, num_min):
    bets = list(_bets)

    def cost(size):
        t = 0
        for i in xrange(num_min):
            assert size >= bets[i]
            t += size - bets[i]
        for i in xrange(num_min, 37):
            if bets[i] <= size:
                t += size + 1 - bets[i]
        return t
    low = max(bets[:num_min]) - 1
    return bets


def func_98d683b4b66d48e2a241f692ca21895e(_bets, num_min):
    bets = list(_bets)

    def cost(size):
        t = 0
        for i in xrange(num_min):
            assert size >= bets[i]
            t += size - bets[i]
        for i in xrange(num_min, 37):
            if bets[i] <= size:
                t += size + 1 - bets[i]
        return t
    low = max(bets[:num_min]) - 1
    return low


def func_fba2c27ba2bf445593e430fdc38fefb8(bets, num_min):

    def cost(size):
        t = 0
        for i in xrange(num_min):
            assert size >= bets[i]
            t += size - bets[i]
        for i in xrange(num_min, 37):
            if bets[i] <= size:
                t += size + 1 - bets[i]
        return t
    low = max(bets[:num_min]) - 1
    high = 10000000000000
    return low


def func_87184c9feac849f0be690e5c3aae6555(bets, num_min):

    def cost(size):
        t = 0
        for i in xrange(num_min):
            assert size >= bets[i]
            t += size - bets[i]
        for i in xrange(num_min, 37):
            if bets[i] <= size:
                t += size + 1 - bets[i]
        return t
    low = max(bets[:num_min]) - 1
    high = 10000000000000
    return high


def func_6b6f2098ac7a40b7bb98913e3cd65af8(B, bets, num_min):
    low = max(bets[:num_min]) - 1
    high = 10000000000000
    while high > low:
        g = (high + low + 1) / 2
        c = cost(g)
        if c > B:
            high = g - 1
        else:
            low = g
            amount_bet = g * num_min - sum(bets[:num_min])
            best = max(amount_bet * 36.0 / num_min - c, best)
    return high


def func_04748f5c2bd64210af2d01d4411844e7(B, bets, num_min):
    low = max(bets[:num_min]) - 1
    high = 10000000000000
    while high > low:
        g = (high + low + 1) / 2
        c = cost(g)
        if c > B:
            high = g - 1
        else:
            low = g
            amount_bet = g * num_min - sum(bets[:num_min])
            best = max(amount_bet * 36.0 / num_min - c, best)
    return low


def func_9a8b3bf67eeb4ab3938eeb87b9a6046d(B, bets, num_min):
    low = max(bets[:num_min]) - 1
    high = 10000000000000
    while high > low:
        g = (high + low + 1) / 2
        c = cost(g)
        if c > B:
            high = g - 1
        else:
            low = g
            amount_bet = g * num_min - sum(bets[:num_min])
            best = max(amount_bet * 36.0 / num_min - c, best)
    return best


def func_313ad493e1e24040b8a8487e2890f7ab(B, bets, num_min):
    low = max(bets[:num_min]) - 1
    high = 10000000000000
    while high > low:
        g = (high + low + 1) / 2
        c = cost(g)
        if c > B:
            high = g - 1
        else:
            low = g
            amount_bet = g * num_min - sum(bets[:num_min])
            best = max(amount_bet * 36.0 / num_min - c, best)
    return amount_bet


def func_b7d1089c0a77460cadd3aa4483a74541(B, bets, num_min):
    low = max(bets[:num_min]) - 1
    high = 10000000000000
    while high > low:
        g = (high + low + 1) / 2
        c = cost(g)
        if c > B:
            high = g - 1
        else:
            low = g
            amount_bet = g * num_min - sum(bets[:num_min])
            best = max(amount_bet * 36.0 / num_min - c, best)
    return c


def func_d1a1bd978f9548049e83f6970ea187ac(B, bets, num_min):
    low = max(bets[:num_min]) - 1
    high = 10000000000000
    while high > low:
        g = (high + low + 1) / 2
        c = cost(g)
        if c > B:
            high = g - 1
        else:
            low = g
            amount_bet = g * num_min - sum(bets[:num_min])
            best = max(amount_bet * 36.0 / num_min - c, best)
    return g


def func_ba53bc87f6df4bc097288575fb871940(_bets, num_min):
    bets = list(_bets)

    def cost(size):
        t = 0
        for i in xrange(num_min):
            assert size >= bets[i]
            t += size - bets[i]
        for i in xrange(num_min, 37):
            if bets[i] <= size:
                t += size + 1 - bets[i]
        return t
    low = max(bets[:num_min]) - 1
    high = 10000000000000
    return low


def func_a35a606d83cd4998b8f5b311b2862b4f(_bets, num_min):
    bets = list(_bets)

    def cost(size):
        t = 0
        for i in xrange(num_min):
            assert size >= bets[i]
            t += size - bets[i]
        for i in xrange(num_min, 37):
            if bets[i] <= size:
                t += size + 1 - bets[i]
        return t
    low = max(bets[:num_min]) - 1
    high = 10000000000000
    return bets


def func_d96291d81e1942fbb1de75aa983de632(_bets, num_min):
    bets = list(_bets)

    def cost(size):
        t = 0
        for i in xrange(num_min):
            assert size >= bets[i]
            t += size - bets[i]
        for i in xrange(num_min, 37):
            if bets[i] <= size:
                t += size + 1 - bets[i]
        return t
    low = max(bets[:num_min]) - 1
    high = 10000000000000
    return high


def func_449877c2a62641cc9b758b3497187178(B, bets, num_min):

    def cost(size):
        t = 0
        for i in xrange(num_min):
            assert size >= bets[i]
            t += size - bets[i]
        for i in xrange(num_min, 37):
            if bets[i] <= size:
                t += size + 1 - bets[i]
        return t
    low = max(bets[:num_min]) - 1
    high = 10000000000000
    while high > low:
        g = (high + low + 1) / 2
        c = cost(g)
        if c > B:
            high = g - 1
        else:
            low = g
            amount_bet = g * num_min - sum(bets[:num_min])
            best = max(amount_bet * 36.0 / num_min - c, best)
    return low


def func_f658f744918c494994a92e0af5244f81(B, bets, num_min):

    def cost(size):
        t = 0
        for i in xrange(num_min):
            assert size >= bets[i]
            t += size - bets[i]
        for i in xrange(num_min, 37):
            if bets[i] <= size:
                t += size + 1 - bets[i]
        return t
    low = max(bets[:num_min]) - 1
    high = 10000000000000
    while high > low:
        g = (high + low + 1) / 2
        c = cost(g)
        if c > B:
            high = g - 1
        else:
            low = g
            amount_bet = g * num_min - sum(bets[:num_min])
            best = max(amount_bet * 36.0 / num_min - c, best)
    return g


def func_bc167a40800747c28ddbcadfe9be5a47(B, bets, num_min):

    def cost(size):
        t = 0
        for i in xrange(num_min):
            assert size >= bets[i]
            t += size - bets[i]
        for i in xrange(num_min, 37):
            if bets[i] <= size:
                t += size + 1 - bets[i]
        return t
    low = max(bets[:num_min]) - 1
    high = 10000000000000
    while high > low:
        g = (high + low + 1) / 2
        c = cost(g)
        if c > B:
            high = g - 1
        else:
            low = g
            amount_bet = g * num_min - sum(bets[:num_min])
            best = max(amount_bet * 36.0 / num_min - c, best)
    return best


def func_7e12299ef33741cf958af614d32a294b(B, bets, num_min):

    def cost(size):
        t = 0
        for i in xrange(num_min):
            assert size >= bets[i]
            t += size - bets[i]
        for i in xrange(num_min, 37):
            if bets[i] <= size:
                t += size + 1 - bets[i]
        return t
    low = max(bets[:num_min]) - 1
    high = 10000000000000
    while high > low:
        g = (high + low + 1) / 2
        c = cost(g)
        if c > B:
            high = g - 1
        else:
            low = g
            amount_bet = g * num_min - sum(bets[:num_min])
            best = max(amount_bet * 36.0 / num_min - c, best)
    return c


def func_e6e76528ee6641e3b4cf724f836c35e6(B, bets, num_min):

    def cost(size):
        t = 0
        for i in xrange(num_min):
            assert size >= bets[i]
            t += size - bets[i]
        for i in xrange(num_min, 37):
            if bets[i] <= size:
                t += size + 1 - bets[i]
        return t
    low = max(bets[:num_min]) - 1
    high = 10000000000000
    while high > low:
        g = (high + low + 1) / 2
        c = cost(g)
        if c > B:
            high = g - 1
        else:
            low = g
            amount_bet = g * num_min - sum(bets[:num_min])
            best = max(amount_bet * 36.0 / num_min - c, best)
    return amount_bet


def func_1019148265f04188b4cb2d6d448ead39(B, bets, num_min):

    def cost(size):
        t = 0
        for i in xrange(num_min):
            assert size >= bets[i]
            t += size - bets[i]
        for i in xrange(num_min, 37):
            if bets[i] <= size:
                t += size + 1 - bets[i]
        return t
    low = max(bets[:num_min]) - 1
    high = 10000000000000
    while high > low:
        g = (high + low + 1) / 2
        c = cost(g)
        if c > B:
            high = g - 1
        else:
            low = g
            amount_bet = g * num_min - sum(bets[:num_min])
            best = max(amount_bet * 36.0 / num_min - c, best)
    return high


def func_7fc259086cd44975aa9b08c46c78a923(_bets, B, num_min):
    bets = list(_bets)

    def cost(size):
        t = 0
        for i in xrange(num_min):
            assert size >= bets[i]
            t += size - bets[i]
        for i in xrange(num_min, 37):
            if bets[i] <= size:
                t += size + 1 - bets[i]
        return t
    low = max(bets[:num_min]) - 1
    high = 10000000000000
    while high > low:
        g = (high + low + 1) / 2
        c = cost(g)
        if c > B:
            high = g - 1
        else:
            low = g
            amount_bet = g * num_min - sum(bets[:num_min])
            best = max(amount_bet * 36.0 / num_min - c, best)
    return amount_bet


def func_1ea0371c4bc9423cbc54d7b7aa83f272(_bets, B, num_min):
    bets = list(_bets)

    def cost(size):
        t = 0
        for i in xrange(num_min):
            assert size >= bets[i]
            t += size - bets[i]
        for i in xrange(num_min, 37):
            if bets[i] <= size:
                t += size + 1 - bets[i]
        return t
    low = max(bets[:num_min]) - 1
    high = 10000000000000
    while high > low:
        g = (high + low + 1) / 2
        c = cost(g)
        if c > B:
            high = g - 1
        else:
            low = g
            amount_bet = g * num_min - sum(bets[:num_min])
            best = max(amount_bet * 36.0 / num_min - c, best)
    return best


def func_978f2409877c4285bac6ebf9158164bd(_bets, B, num_min):
    bets = list(_bets)

    def cost(size):
        t = 0
        for i in xrange(num_min):
            assert size >= bets[i]
            t += size - bets[i]
        for i in xrange(num_min, 37):
            if bets[i] <= size:
                t += size + 1 - bets[i]
        return t
    low = max(bets[:num_min]) - 1
    high = 10000000000000
    while high > low:
        g = (high + low + 1) / 2
        c = cost(g)
        if c > B:
            high = g - 1
        else:
            low = g
            amount_bet = g * num_min - sum(bets[:num_min])
            best = max(amount_bet * 36.0 / num_min - c, best)
    return bets


def func_7e6244dd311546a7a578f95a5a504604(_bets, B, num_min):
    bets = list(_bets)

    def cost(size):
        t = 0
        for i in xrange(num_min):
            assert size >= bets[i]
            t += size - bets[i]
        for i in xrange(num_min, 37):
            if bets[i] <= size:
                t += size + 1 - bets[i]
        return t
    low = max(bets[:num_min]) - 1
    high = 10000000000000
    while high > low:
        g = (high + low + 1) / 2
        c = cost(g)
        if c > B:
            high = g - 1
        else:
            low = g
            amount_bet = g * num_min - sum(bets[:num_min])
            best = max(amount_bet * 36.0 / num_min - c, best)
    return c


def func_f3ee6778cec240c3b0b3bed92cb5cd22(_bets, B, num_min):
    bets = list(_bets)

    def cost(size):
        t = 0
        for i in xrange(num_min):
            assert size >= bets[i]
            t += size - bets[i]
        for i in xrange(num_min, 37):
            if bets[i] <= size:
                t += size + 1 - bets[i]
        return t
    low = max(bets[:num_min]) - 1
    high = 10000000000000
    while high > low:
        g = (high + low + 1) / 2
        c = cost(g)
        if c > B:
            high = g - 1
        else:
            low = g
            amount_bet = g * num_min - sum(bets[:num_min])
            best = max(amount_bet * 36.0 / num_min - c, best)
    return high


def func_691db77c429c4f558f268b29ac049dd1(_bets, B, num_min):
    bets = list(_bets)

    def cost(size):
        t = 0
        for i in xrange(num_min):
            assert size >= bets[i]
            t += size - bets[i]
        for i in xrange(num_min, 37):
            if bets[i] <= size:
                t += size + 1 - bets[i]
        return t
    low = max(bets[:num_min]) - 1
    high = 10000000000000
    while high > low:
        g = (high + low + 1) / 2
        c = cost(g)
        if c > B:
            high = g - 1
        else:
            low = g
            amount_bet = g * num_min - sum(bets[:num_min])
            best = max(amount_bet * 36.0 / num_min - c, best)
    return low


def func_d7389b78bf0f42b99293b43c1a0b1a38(_bets, B, num_min):
    bets = list(_bets)

    def cost(size):
        t = 0
        for i in xrange(num_min):
            assert size >= bets[i]
            t += size - bets[i]
        for i in xrange(num_min, 37):
            if bets[i] <= size:
                t += size + 1 - bets[i]
        return t
    low = max(bets[:num_min]) - 1
    high = 10000000000000
    while high > low:
        g = (high + low + 1) / 2
        c = cost(g)
        if c > B:
            high = g - 1
        else:
            low = g
            amount_bet = g * num_min - sum(bets[:num_min])
            best = max(amount_bet * 36.0 / num_min - c, best)
    return g


def func_727bca909dfe4e0ca6a484972f7ef96e(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())
    return N


def func_44c520a0e8bd4722879cc649df39d43a(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())
    return B


def func_f03964c4f843445ab4808660c796e60a(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())
    return _bets


def func_f25159af2d8e424f87d5aa1d45ff155b(N, f):
    _bets = map(int, f.readline().split())(len(_bets) == N)
    return _bets


def func_840f98f7c20845c79a8941de494353e1(_bets):
    _bets.sort()
    best = 0.0
    return best


def func_0f5db8bd4df242c3b5f1aa9ba04016c6(_bets, B):
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return high


def func_4f4d4a8000be443185ad093e5a5b94fa(_bets, B):
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return best


def func_e82db4becb3e4004b63297e13d1df99a(_bets, B):
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return bets


def func_1a70129307aa4b39bf38ef6fa9e38499(_bets, B):
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return low


def func_98a648ce00ed48899e782e3b0fae0bb9(_bets, B):
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return g


def func_be1aee4dde9543a7bd74816003fa3e45(_bets, B):
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return c


def func_0a8587e672ee4c83b311a102c2edbc85(_bets, B):
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return num_min


def func_062bb03a37c04a04853c818ea395ebad(_bets, B):
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return amount_bet


def func_b95ff0debb7642c19361709e052d8a41(_T, _bets, B):
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return c


def func_dbc51835198e429f93be6c6bdd00a6f1(_T, _bets, B):
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return high


def func_d3adac96a81142ae98281fca9d25ba95(_T, _bets, B):
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return g


def func_d2f2f415530d49589c24e6a2021191ae(_T, _bets, B):
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return num_min


def func_583d4c539ceb4d12a9ba26661849b6a2(_T, _bets, B):
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return amount_bet


def func_f9a21bb6f4e94920a99e3519ba88771b(_T, _bets, B):
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return best


def func_fc01df97af8f4fefb3ac994b0df38ffc(_T, _bets, B):
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return low


def func_fa0d8f6175794430a616944069930240(_T, _bets, B):
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return bets


def func_15cc28adea884d0e8049b385c19a87f0(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    return B


def func_bb64eb5584ce4570b31699ceb7e56313(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    return _bets


def func_7349fb2b848449f7a787ea4bd151ff3e(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    return N


def func_1b6dd171b5ab4c23aca995474293def0(N, f):
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    return _bets


def func_6b40c8c2782d45758f1926bdd8d3da89(_bets):
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    return best


def func_b7f749fa603149b9b0230c2e8f86ccfb(_bets, B):
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return g


def func_826dd2368a4e4a07be34e81556cafbe9(_bets, B):
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return high


def func_a48da3743b274e87a1434c5f9617a15b(_bets, B):
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return best


def func_e3d0103e5249415b80c7c8808eb3c48a(_bets, B):
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return c


def func_dc5ae13afbe7424fb853c0e09ff605ca(_bets, B):
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return low


def func_6412c60cf87f4d1ebac91f6c6efe498f(_bets, B):
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return num_min


def func_986daca903724076908329d693bd80d6(_bets, B):
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return amount_bet


def func_1d2f5836068a474799dc557797dca95f(_bets, B):
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return bets


def func_5b05e0b77cb940f298ee891f9d91474d(_T, _bets, B):
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return c


def func_03967d29af974fdd8c6423d29e221684(_T, _bets, B):
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return g


def func_11ca43c648ab4a53b822a0b3bdc1f06e(_T, _bets, B):
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return amount_bet


def func_74794b74d6474dadadb374290caa642c(_T, _bets, B):
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return num_min


def func_61b752ad62d243c7b57218f5357cd499(_T, _bets, B):
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return bets


def func_6a7c1ed7b48d40918f599c02291c7950(_T, _bets, B):
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return low


def func_236b22797bfb4bb5a48734d3886cfb7e(_T, _bets, B):
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return best


def func_026d06bc29e946c0a376994877278ce8(_T, _bets, B):
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return high


def func_6e018ebe7c784e2ebc2777d799ea6987(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    return _bets


def func_9b205833b9904fe4a2ab713619cbd372(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    return B


def func_f9400915dc994b90a5514803f3e7ad5f(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    return N


def func_d3c6223a70cf45d1a16df360a92397e3(N, f):
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    return _bets


def func_2c46fc21c1c5473e804bf3f071046c8b(_bets, B):
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return amount_bet


def func_78341f781df34fe58c4f367ab7aa32c5(_bets, B):
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return best


def func_ab26ae6e61234142b39029bfb0207eab(_bets, B):
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return g


def func_501ae02a6dfc4e7c8551ac8834ec2f4b(_bets, B):
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return bets


def func_3379f690f0114994a0c4aad00502514f(_bets, B):
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return num_min


def func_09d50d245d154281b64e12a951ac2890(_bets, B):
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return high


def func_f083b6a748e744929aff4f8baa009dad(_bets, B):
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return low


def func_35a6bb764de64640b89f37a076ab5001(_bets, B):
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return c


def func_316c2c4ed0eb49dfacb1a34497499345(_T, _bets, B):
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return c


def func_92287a61158646bcab358d72650fbe6d(_T, _bets, B):
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return amount_bet


def func_2573bc095a214777bea86e248585070d(_T, _bets, B):
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return g


def func_b25462df60c54225ac642bd42579055a(_T, _bets, B):
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return best


def func_ba80a4aa8ca54ed28fb299debfd4ad8c(_T, _bets, B):
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return bets


def func_9e76757feb02401a972ff8b94d673f51(_T, _bets, B):
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return low


def func_b4a967fcf8d84e0eabe931c2ab25870a(_T, _bets, B):
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return high


def func_d097c9e3e8eb49359919a2d5c71bc37e(_T, _bets, B):
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return num_min


def func_3030d4fdd9e146e5905460275f832ad8(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    return _bets


def func_487606ce8d4742a3bcd2859742337d21(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    return B


def func_39c9cc91c11a4248bf20091d0927ebb4(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    return N


def func_8765616cee4942828d789153d784af45(N, f):
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    return best


def func_754693ecf12648f0a9284ca1e1755d9c(N, f):
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    return _bets


def func_2f0349d859b543c59965aaa7ad8a092e(_T, _bets, B):
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return num_min


def func_8cb70c7a97ca4593ab99874a4c9547e9(_T, _bets, B):
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return high


def func_b025cea98a3d4d4e8040d97f4e63fc8c(_T, _bets, B):
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return bets


def func_d987fd1657e14f7abd8a9c42874c8145(_T, _bets, B):
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return low


def func_65766f34089a4611b8d862c894ffdd02(_T, _bets, B):
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return amount_bet


def func_4b6e5fe840664c2daac813c9c0de1a04(_T, _bets, B):
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return g


def func_eb1dbaa21db64c9d98345f5ccb74a8b6(_T, _bets, B):
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return best


def func_35dd9754b2dc4bad9ca8d6ebf8714ddf(_T, _bets, B):
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return c


def func_4ec7888b4599443fa2c020c1798a8778(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    return best


def func_a90ea1a8325e49a9b7509ae39e8110f1(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    return _bets


def func_d324fe7a1f6f4fa48fc8816652df2041(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    return B


def func_b3201356fc4242be8d003d4aaadab561(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    return N


def func_f6273375ea364a39b2b66cb6cbdbd745(N, B, f):
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return bets


def func_0dba1d98cee349eea795a236d9b390ef(N, B, f):
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return _bets


def func_c57b8ccb0f394b63a8c5ab32377ae80b(N, B, f):
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return c


def func_06628867e2f34cf0aaad2c8584913b0c(N, B, f):
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return high


def func_0be6c8ef4511427a993e8e87afd75409(N, B, f):
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return low


def func_d389776ad1df44688ba145ae31bc0a46(N, B, f):
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return num_min


def func_a31c054d3ffa4b97baa4ebb36341dd69(N, B, f):
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return g


def func_9dc944427d0e44cca76fa4c603897573(N, B, f):
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return best


def func_bc6ad087d2d34e0c982039efed5676bc(N, B, f):
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return amount_bet


def func_0480209fee3140f89356f69d60f52f9b(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return N


def func_28f15419b25e4f2bb66a0105d377877a(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return best


def func_aff90a820fb8428194fef51c91f0dcc9(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return B


def func_6682adacfd7b473b9c7f00f3143a3f41(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return c


def func_b255ee83b9c34f449766c69ad4a99190(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return g


def func_920df53cf11445458c5cb481eafc3850(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return high


def func_26a39c76c87c46f984ab38f8726f409a(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return low


def func_b9feea8fe3584558892836ddf7cb7394(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return _bets


def func_605b42cdd1f14b46a57f458b4b1a0607(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return bets


def func_d697465a78ec4907b56b9e2e55e0c23f(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return num_min


def func_5ee113e7f9e24be6b552368e50ebd3e0(f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)
    return amount_bet


def func_56fc17ca26094ca297f8ab613adf33c6(N, _T, B, f):
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return best


def func_e4557d3765f34d1ab3878f64cb7de51e(N, _T, B, f):
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return low


def func_ae0c76a45c7d41d4a0dba61afcd4513b(N, _T, B, f):
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return amount_bet


def func_0397080bb81f4f3db43a05c87a89a86f(N, _T, B, f):
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return c


def func_7ee1f75992b04a27b04496eb956197b3(N, _T, B, f):
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return high


def func_c5f55de4461944c2ad2ab2aa5f4d158a(N, _T, B, f):
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return _bets


def func_b3765e3a3ab242458ec247aeec925fd8(N, _T, B, f):
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return num_min


def func_ba281b0671284fad98ae68a8f56e5044(N, _T, B, f):
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return bets


def func_d7167e4f4428431db873f7f98f84e34c(N, _T, B, f):
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return g


def func_65eb5b5aaeb44c5d822fb9525a12503f(_T, f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return N


def func_cf76fa60c799423f82351e4a323dca6a(_T, f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return B


def func_69a1a17aa0544d3cbe7723afe6caab5f(_T, f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return c


def func_feaad3d565224194810aa5bf20a20aa4(_T, f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return amount_bet


def func_c2844f80aff749f4a013a3c59e1d8c0d(_T, f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return low


def func_b8310711263547aebfa98c9d971a7a87(_T, f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return g


def func_b7d1f9b38b684a71b6891921a660f130(_T, f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return high


def func_9f3bcba50f764ef5931d09207e19aa8a(_T, f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return bets


def func_75e5e7b9eef548268b85f87e82fbdd7a(_T, f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return _bets


def func_5a862c7bf78748dcbadfcc57391c199c(_T, f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return best


def func_d7635f041a1d4b8e81189788dd36a842(_T, f):
    B, N = map(int, f.readline().split())
    _bets = map(int, f.readline().split())(len(_bets) == N)
    while len(_bets) < 37:
        _bets.append(0)
    _bets.sort()
    best = 0.0
    for num_min in xrange(1, 37):
        bets = list(_bets)

        def cost(size):
            t = 0
            for i in xrange(num_min):
                assert size >= bets[i]
                t += size - bets[i]
            for i in xrange(num_min, 37):
                if bets[i] <= size:
                    t += size + 1 - bets[i]
            return t
        low = max(bets[:num_min]) - 1
        high = 10000000000000
        while high > low:
            g = (high + low + 1) / 2
            c = cost(g)
            if c > B:
                high = g - 1
            else:
                low = g
                amount_bet = g * num_min - sum(bets[:num_min])
                best = max(amount_bet * 36.0 / num_min - c, best)(
                    'Case #%d: %.9f' % (_T + 1, best))
    return num_min


def func_fc5082ff40e2426eb01a6aee38543e23():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    return T


def func_d9316e3b5799497c87d2f3b4ea4ab7ea():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    return f


def func_2cbdcdcc8095433ea8dbd12c435688c3(f):
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return _T


def func_f333f4a6c9b1410e9a0c5d1c41ae2283(f):
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return best


def func_e15fa21a8a1b410f8c42e3a26a7aeca1(f):
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return amount_bet


def func_05248891e2f44f09aa91ac8f30ec2f81(f):
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return N


def func_09a92d9412c34b7ea08b9656384bb4a5(f):
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return B


def func_ae903db222324bf58733fe6e477f8fdc(f):
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return c


def func_5f9f38ada79e4fe5aeff6279f1ddf3e7(f):
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return g


def func_87dcad1164e64843adf734cdb634fe1e(f):
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return num_min


def func_c5e7da5ffc164f08ae28cbcecfc00fc9(f):
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return T


def func_761452cab993482b8ddd597e9be14f17(f):
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return high


def func_d57938ea8a224ffc8e8e626db9612699(f):
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return bets


def func_ee0ee4b6e33441deb137def9664c5769(f):
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return _bets


def func_8dc730a8befc4b8c92bc3af0a72ee4b8(f):
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return low


def func_ba2dddde800f499ca3029b5fab9dd98f(T, f):
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return num_min


def func_cf05fd6fc5b64611a26d7cc2054fb3d2(T, f):
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return N


def func_c3123de708ae4f72a59651b4b81a7fc8(T, f):
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return amount_bet


def func_9d2c42770a8a4a158e4aa2944c039bdc(T, f):
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return high


def func_c78e6f4a0fb34f8f88939276aa0f1962(T, f):
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return _T


def func_a97939587ee549e4919047d8782318ae(T, f):
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return bets


def func_f99d57cee47c434db30ac480712a90f3(T, f):
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return g


def func_339bf15b73e548e3946980734c454b58(T, f):
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return B


def func_efe218e6ca5e40389a1a47febe619fae(T, f):
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return low


def func_7021b69504514d95bac5122ec0822dd5(T, f):
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return c


def func_765200b006a641559160667fb7820160(T, f):
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return _bets


def func_6b5bf51461ca4adaa0d0b2c54538c2b4(T, f):
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return best


def func_a90fb60d7cb7491780b754680292730b():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return _bets


def func_8c428665047a4b318aca506431455dea():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return num_min


def func_5ec85a40a8a1426788a90958838efebf():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return amount_bet


def func_a12e65eca90540af85d66754322c71ab():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return bets


def func_c85ec9db35044845ad2596824894f864():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return low


def func_4658d4a3fd96487d979c27f6e329f831():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return _T


def func_e4fc46f6dff24cbf8cb11f1ce74db9f1():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return g


def func_6c06fa486630457084de096ed6d71d74():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return c


def func_b417e4151c084f39a941a3bab7e62023():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return high


def func_a7e99567131140d6918ad65e086d9766():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return N


def func_3b07cc37131b4bd79343593057f82a8a():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return f


def func_01b21115c2c54a1e9678b25e1b77f830():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return B


def func_900697b0a66f482797d145682846d0ba():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return T


def func_8ba0e6eb0572494a9221d34d86745981():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    return best


def func_dbf7635cd95348d09f96134e10729b6b(f):
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return amount_bet


def func_b7d8723cae624d59b746fa06e524a294(f):
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return g


def func_a2f48932c1dc40f4b6908ae8116a5ee1(f):
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return best


def func_c352e6c8ad8846e8b81a3f21d7695a45(f):
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return N


def func_0fd29ad8ad324aa785317032a3261b34(f):
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return _bets


def func_25bfdb0b6b8b452980a8a7dc519589df(f):
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return T


def func_f8a7e86eded440f08d4f636e1c342cf0(f):
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return _T


def func_7f89cb85fe424db3bf034d97f7cafae4(f):
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return c


def func_6cd2ad40a3584fc49c74a08d82fafe36(f):
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return low


def func_130bef190d764cf0bf83fa25597d0928(f):
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return B


def func_1187302ee2ab436085e39f29ee083e23(f):
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return bets


def func_df79a33427054a73bbe61e8591cab123(f):
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return high


def func_f5b9185d39d94dc9bda64b6b30ae2f27(f):
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return num_min


def func_9ea5f1df5b5a460ab6c71769d3b62b6e():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return bets


def func_7fafeb4db77a45bf9513b0da67c50c2a():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return g


def func_9fd694c30b4d49ca8b7b4842e5557497():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return amount_bet


def func_dc4669eb563f4855b5c65cf07376cb7f():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return c


def func_c978e198b3f543719f33b1c38122502c():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return high


def func_b3ebe423c82e426bbb129d8d0ead0f24():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return T


def func_5b74ec91f334416ea05add897d835190():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return _T


def func_2dcd59061dc84dfc9d43d3c5215bbcb2():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return best


def func_85bfdbe12d424657a05d0f2444c84e75():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return f


def func_e072464a32b24071871a2e20896bf6c0():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return num_min


def func_6a27defa5e3246ab956fe128edff11a5():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return low


def func_1f6d994959eb409aaaf4c8f2deb4d4ec():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return N


def func_7fab6683752642089111ce4c18e6086c():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return B


def func_6541d0d9d24a488bae54223134ba2812():
    f = open('codejam/test_files/Y13R5P1/A.in')
    T = int(f.readline())
    for _T in xrange(T):
        B, N = map(int, f.readline().split())
        _bets = map(int, f.readline().split())
        assert len(_bets) == N
        while len(_bets) < 37:
            _bets.append(0)
        _bets.sort()
        best = 0.0
        for num_min in xrange(1, 37):
            bets = list(_bets)

            def cost(size):
                t = 0
                for i in xrange(num_min):
                    assert size >= bets[i]
                    t += size - bets[i]
                for i in xrange(num_min, 37):
                    if bets[i] <= size:
                        t += size + 1 - bets[i]
                return t
            low = max(bets[:num_min]) - 1
            high = 10000000000000
            while high > low:
                g = (high + low + 1) / 2
                c = cost(g)
                if c > B:
                    high = g - 1
                else:
                    low = g
                    amount_bet = g * num_min - sum(bets[:num_min])
                    best = max(amount_bet * 36.0 / num_min - c, best)
        print 'Case #%d: %.9f' % (_T + 1, best)
    f.close()
    return _bets

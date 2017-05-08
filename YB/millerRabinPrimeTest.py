from random import *
from config import *

primeList = [2, 3, 5, 7, 11]
testList = [x for x in range(3, 1000, 2)]

def QuickPow(b, e, p):
    if e == 0:
        return 1
    if e % 2 == 0:
        return QuickPow(b * b % p, e // 2, p)
    elif e % 2 == 1:
        return b % p * QuickPow(b * b % p, e // 2, p) % p


def primeTest(p):
    if p < 10:
        if p in primeList:
            return True
        else: return False
    if p == 1:
        return False
    if p % 2 == 0:
        return False

    t = 0
    u = p - 1
    while(u % 2 == 0):
        u /= 2
        t += 1
    # p-1 = (2^t) * u
    #print(t, u)
    for times in range(TEST_TIMES):
        a = testList[times]
        if (a >= p):continue
        ignore = False
        remain = QuickPow(a, u, p)
        if remain == 1 or remain == p - 1:
            ignore = True
        for i in range(0, t):
            remain = QuickPow(remain, 2, p)
            #print("case {}: remain: {}, ignore: {}".format(str(i), str(remain), str(ignore)))
            if (i != t-1):
                if remain == 1 and not ignore:
                    #print("invalid 1")
                    return False
                if remain == 1 or remain == p - 1:
                    ignore = True
            elif (remain != 1):
                #print("invalid 2")
                return False
    return True


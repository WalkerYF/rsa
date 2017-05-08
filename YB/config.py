from math import *
unit =  3/4
confidence = 0.99
TEST_TIMES = ceil(log(1 - confidence, 2) / log(unit, 2))


bmin = 2**511
bmax = 2**512 - 1

wid_min = log(bmin, 10)
wid_max = log(bmin, 10)


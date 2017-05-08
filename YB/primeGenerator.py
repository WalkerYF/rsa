from config import *
from random import *
from millerRabinPrimeTest import * 
import sys
bit = int(sys.argv[1])
Min = 2**(bit - 1)
Max = 2**bit - 1

f = open("makePrime", 'a')
for i in range(10):
    num = randint(Min, Max)
    while primeTest(num) == False:
        num = randint(Min, Max)
    print(num)
    f.write(str(num) + '\n')
#    print(str(primeTest(11)))

"""
BUilding the Sparse Table for range queries minimum

import math
d = {}
nums = [1,8,6,2,3,3,4,1,2,3,45,3]
def construct(a, b):
    if (a,b) in d:
        return d[(a,b)]
    if a == b:
        d[(a,b)] = nums[a]
        return nums[a]

    d[(a, b)] = min(construct(a, a+((b-a+1)/2)-1),construct(a+((b-a+1)/2), b))
    return d[(a,b)]
N = len(nums)

x = 0
i = 1
while x < 2**(int(math.log(N,2))):
    for a in range(N):
        if a + x >= N:
            break
        construct(a, a+x)
    x = 2**(i)-1
    i += 1
print(d)
"""
""" #MAXIMUM THreading recurssion UPDATED
import threading
from sys import stdin,stdout,setrecursionlimit
from collections import defaultdict
setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
def main():
# Enter your code here
pass
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
"""
"""
##PRIME FACTORIZATION OF A NUMBER
nums = defaultdict(int)
got = [0]
def primefactorization(n):
    d = 2
    mn = n
    while d*d <= mn:
        while not n%d:
            got[0] = 1
            nums[d] += 1
            n = n//d
        d += 1
"""
"""
NUMBER OF CO PRIMES TO A NUMBER
def primefactorization(n):
    got = [0]
    nums = defaultdict(int)
    d = 2
    mn = n
    while d*d <= mn:
        while not n%d:
            got[0] = 1
            nums[d] += 1
            n = n//d
        d += 1
    return [nums, got]
def numerOfCoprimesTo(n):
    m = primefactorization(n)
    if not m[1][0]:
        return n-1
    rx = 1
    for j in m[0]:
        rx *= ((j**(m[0][j]-1))*(j-1))
    return rx
"""
"""
MOD INVERSE
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
"""
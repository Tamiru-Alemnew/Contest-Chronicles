import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

def sieve(n):
    spf = list(range(n + 1))  
    for i in range(2, int(math.sqrt(n)) + 1):
        if spf[i] == i:  
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

def prime_factors(n, spf):
    factors = []
    while n != 1:
        factors.append(spf[n])
        n //= spf[n]

    return factors

spf = sieve(10**4 + 4)

n = ip()
arr = lip()
query = []
ps = [0]*(n+2)

mp = defaultdict(list)

for i in range(n):
    fcts = prime_factors(arr[i], spf)
    mp[arr[i]] = heapify([-jj for jj in fcts])

    ps[i + 1] += ps[i] + sum(fcts)

for i in range(ip()):
    query.append(lip())

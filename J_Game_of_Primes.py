import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

def sieve(n):
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n, p):
                if is_prime[i] == True:
                    is_prime[i] = (p , i)
        p += 1
    return is_prime

def sievve(n):
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return is_prime

primes = sievve(10**6 + 10)
valuees = sieve(10**6 + 10)

for i in range(ip()):
    n = ip()
    arr = lip()
    ans = 0
    possible = 0 
    for c in arr:
        if primes[c] or c ==1:
            ans += 1
        else:
            a , b = valuees[c]
            b //= a
            if primes[a] and primes[b]:
                ans += 1
            elif primes[a]  or primes[b] :
                possible += 1

    ans +=math.ceil(possible / 2)

    print(ans)


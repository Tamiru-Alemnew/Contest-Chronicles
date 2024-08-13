import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

def factors(n):
    if n <= 1:
        return 0
    
    sum_factors = 1  
    sqrt_n = int(n**0.5)
    
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            sum_factors += i
            if i != n // i:
                sum_factors += n // i
    
    return sum_factors

mp = defaultdict(int)
for i in range(10**5 + 1):
    mp[i] = factors(i)
    
for i in range(ip()):
    c = ip()

    if mp[c] == c:
        print(c ,"perfecto")
    elif mp[mp[c]] == c:
        if mp[c] > c:
            print(c , "romantico abundante")

        else:
            print(c , "romantico")

    elif mp[c] > c:
        print(c , "abundante")

    else:
        print(c , "complicado")
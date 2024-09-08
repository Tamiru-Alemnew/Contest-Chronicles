import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

mod = 10**9 + 7

def mod_inverse(a, m):
    return pow(a, m - 2, m)


t = ip()

results = []

for _ in range(t):
    n = ip()  
    arr = lip() 
    
    ps = [0] * n
    ps[0] = arr[0]

    for i in range(1, n):
        ps[i] = ps[i - 1] + arr[i]

    total = 0

    for i in range(n):
        total += arr[i] * (ps[-1] - ps[i])
        total %= mod

    Q = (n * (n - 1) // 2) % mod

    P = total % mod
    Q_inv = mod_inverse(Q, mod)
    
    answer = (P * Q_inv) % mod
    results.append(answer)

print("\n".join(map(str, results)))

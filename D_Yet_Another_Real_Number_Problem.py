import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

def lt_sh(x, y, z):
    return z > 30 or x < y * (1 << z)


md = 10**9 + 7

for _ in range(ip()):
    ne = ip()
    el = lip()
    stk = []
    ans = 0
    pw = [1] * (ne * 32 + 1)
    result = []
    for i in range(1, ne * 32 + 1):
        pw[i] = pw[i - 1] * 2 % md
    
    for i in range(ne):
        x = el[i]
        y = 0
        
        while x % 2 == 0:
            x //= 2
            y += 1
        
        while stk and lt_sh(stk[-1][0], x, y):
            tv, tp = stk.pop()
            ans = (ans - tv * pw[tp] % md + md) % md
            ans = (ans + tv) % md
            y += tp
        
        stk.append((x, y))
        ans = (ans + stk[-1][0] * pw[stk[-1][1]]) % md
        result.append(ans)
    print(*result)


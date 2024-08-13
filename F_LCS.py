import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

a = cip()
b = cip()

def dp(l , r ):
    if l < 0 and r < 0:
        return 0
    next = 0
    if a[1] == b[r]:
        next += 1 + dp( l-1 , r -1)

    else:
        if l > 0 :
            next = max(dp(l- 1 , r ) , next)
        if r > 0:
            next = max(dp(l , r - 1) , next)

    return next

print(dp(len(a) -1 , len(b) -1))
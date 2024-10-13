import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;


for _ in range(ip()):
    n = ip()

    arr = lip()
    if n in [1 , 2]:
        print(-1)
        continue

    tt = sum(arr)
    m = n / 2

    def check(x):
        tm = tt + x 
        av = tm / n 
        av /= 2 

        cnt = 0 

        for a in arr :
            if a < av: cnt += 1

        return cnt > m

    l , r = 0 , 10**18

    ans = inf

    while l <= r :
        md = (l + r) // 2

        if check(md):
            ans = md 
            r = md - 1

        else: 
            l = md + 1

    print( -1 if ans == inf else ans)


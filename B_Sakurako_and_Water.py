import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;



for _ in range(ip()):
    n = ip()
    grid = []
    for i in range(n):
        grid.append(lip())


    mp = defaultdict(int)
    for r in range(n):
        for c in range(n):
            if grid[r][c] <  0:
                mp[r-c] = max( mp[r-c]  , abs(grid[r][c]))

    ans = 0 
   
    for key , val in mp.items():
        ans += val


    print(ans)

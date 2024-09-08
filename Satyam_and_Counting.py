import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;
for _ in range(ip()):
    b1 = ip()
    c1 = set()
    d1 = set()
    
    for _ in range(b1):
        x, y = map(int, input().split())
        if y == 0:
            c1.add(x)
        else:
            d1.add(x)
    
    ans = 0
    
    for i1 in c1:
        if i1 in d1:
            ans += len(d1) + len(c1) - 2
    
    for j1 in c1:
        if (j1 + 1 in d1) and (j1 + 2 in c1):
            ans += 1
    
    for k1 in d1:
        if (k1 - 1 in c1) and (k1 - 2 in d1):
            ans += 1
    
    print(ans)


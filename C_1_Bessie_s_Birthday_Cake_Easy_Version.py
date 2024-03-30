import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0

t = ip()
for _ in range(t):
    n, x, y = tip()
    arr = sorted(lip())
    arr.append(n + arr[0])
    gap = 0 

    for i in range(1 ,x +1):
        if arr[i] - arr[i-1] == 2:
            gap += 1

    print(x - 2 + gap)

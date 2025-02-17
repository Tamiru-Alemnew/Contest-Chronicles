import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for _ in range(ip()):
    n = ip()
    arr = lip()
    ps = [0]*(n)
    ps[0] = arr[0]
    for i in range(1 , n ):
        ps[i] += ps[i-1] + arr[i]

    l = -1
    check = {}
    check[0] = -1
    ans = 0 

    for i in range(n):
        if ps[i] in check and check[ps[i]]  >= l:
            ans += 1
            l = i 

        check[ps[i]] = i

    print(ans)

        
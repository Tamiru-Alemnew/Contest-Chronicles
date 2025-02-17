import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for _ in range(ip()):
    n = ip()
    arr = lip()

    total = sum(arr)

    if even(total):
        print(0)

    else:
        ans = float("inf")
        for i in range(n):
            cur = arr[i]
            temp = 0 
            while cur > 0 :
                temp += 1
                cur = cur // 2
                if even(arr[i]) != even(cur):
                    ans = min(ans , temp)
                    break
        print(ans)
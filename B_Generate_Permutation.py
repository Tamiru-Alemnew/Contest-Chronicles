import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for _ in range(ip()):
    n = ip()

    if n == 1 :
        print("1")
    else:
        if even(n):
            print(-1)
        else:
            mid = n // 2 
            left = [i for i in range(n , mid + 1 , -1)]
            right = [i for i in range(1 , mid + 2)]

            total = left + right

            print(*total)
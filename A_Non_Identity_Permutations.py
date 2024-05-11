import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for _ in range(ip()):
    n = ip()
    if even(n):
        arr = [i+1 for i in range(n)]
        arr.sort(reverse=True)
        print(*arr)

    else:
        arr = arr = [i+1 for i in range(n)]
        arr.sort(reverse=True)

        md = n // 2 
        arr[md] , arr[-1] = arr[-1] , arr[md]

        print(*arr)
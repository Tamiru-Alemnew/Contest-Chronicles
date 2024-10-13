import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;


for _ in range(ip()):
    n , k = lip()

    # ps = [0]*n
    # ps[0] += 1

    # if k < n:
    #     ps[k] -= 1


    # for i in range(1,n):
    #     ps[i] += ps[i-1] + (i+1)**(i+1)
    #     if i + k < n:
    #         ps[i+k] -= (i+1)**(i+1)


    # print("YES" if even(ps[-1]) else "NO")

    tt = k * n - (k * (k - 1)) // 2

    print("YES" if tt % 2 == 0 else "NO")


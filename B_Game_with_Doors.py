import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for _ in range(ip()):
    l , r = tip()
    L , R = tip()

    if L >= r or l >= R:
        print(1)

    else:
        left = max(l , L)
        right = min(r , R)

        if left > min(l , L):
            left -= 1

        if right < max(r , R):
            right += 1

        if min(l , L) == max(R , L):
            left -= 1

        print(right - left)

        


        
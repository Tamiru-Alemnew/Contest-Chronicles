import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;


for _ in range(ip()):
    n , x , m = tip()
    query = []

    for _ in range(m):
        query.append(lip())

    flag = False

    for a , b in query :
        if not flag :
            if a <= x <= b:
                l , r = a , b 
                flag = True

        else:
            if l<= a <= r or l<= b <= r or( b >= r and l >= a):
                l = min(l , a)
                r = max(r , b)

    if flag:
        print(r-l + 1)

    else:
        print(1)
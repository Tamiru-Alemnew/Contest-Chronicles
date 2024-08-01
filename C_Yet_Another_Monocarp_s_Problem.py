import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for i in range(ip()):
    n , h = tip()
    arr = lip()

    def check(k):
        cur = k
        for i in range(n - 2 , -1 , -1 ):
            cur += min(k , arr[i+1] - arr[i] )
        return cur >= h

    l = 0 
    r = h 

    while l < r :
        md = (l + r) // 2

        if check(md):
            r = md
        else:   
            l = md + 1

    print(r)

    


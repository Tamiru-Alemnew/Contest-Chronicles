import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for _ in range(ip()):
    n , k = lip()

    kk = k -1
    h = n+k - 1

    def check(l):

        left = kk*(kk+1) // 2
        lf = l*(l+1) // 2
        rr = h*(h+1) // 2

        lff = lf - left 
        rt = rr - lf

        return rt - lff
    

    l , r = k-1 , h

    ans = inf

    while l <= r :
        md = (l +r) // 2

        cur = check(md)
        ans = min(abs(cur) , ans)

        if cur == 0:
            break
        elif cur > 0:
            l = md + 1
        else:
            r = md -1

    print(ans)


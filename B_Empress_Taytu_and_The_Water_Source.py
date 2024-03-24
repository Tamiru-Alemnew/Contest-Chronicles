import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()


for _ in range(ip()):
    n , k = tip()

    d = lip()
    t = lip()

    def check(x):
        c = 0 
        for i ,  j in enumerate(d):
            c += math.ceil(j / x) * t[i]
            
        return c <= k
            
    if n > k or sum(t) > k:
        print(-1)
    else:
        l  , r = 1 , max(d)

        while l < r :
            md = (l + r) //2 

            if check(md):
                r = md
            else:
                l = md + 1

        print(r)

        

    
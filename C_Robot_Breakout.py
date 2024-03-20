import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()

# lurd

x = ip()

for i in range(x):
    limits = {}
    n = ip()
    for i in range(n):
        x ,y , l , u , r , d = tip()
        if not l:
            if "l" in limits:
                limits["l"] = max(limits["l"] , x)
            else:
                limits["l"] = x
        if not u :
            if "U" in limits:
                limits["U"] = min(limits["U"] , y)
            else:
                limits["U"] = y
        if not r :
            if "r" in limits:
                limits["r"] = min(limits["r"] , x)
            else:
                limits["r"] = x
        if not d :
            if "d" in limits:
                limits["d"] = max(limits["d"] , y)
            else:
                limits["d"] = y

    if ("U" in limits and "d" in limits) and   limits["U"] <  limits["d"] or ( "l" in limits and "r" in limits) and limits["l"] >   limits["r"]:
        print(0)
    else:
        ans = [0 , 0]
        if "l" not in limits:
            if "r" in limits:
                ans[0] = limits["r"]
        else:
            ans[0] = limits["l"]

        if "U" not in limits:
            if "d" in limits:
                ans[1] = limits["d"]
        else:
            ans[1] = limits["U"]
        
        
        print(1 ,*ans)



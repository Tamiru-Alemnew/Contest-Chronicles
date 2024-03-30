import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()

n = ip()
ans = 0 

for i in range(2,n+1):
    cur = i

    d =  2 
    fac =set()
    while d*d <= cur:
        while cur % d == 0 :
            fac.add(d)
            cur //= d

        d += 1

    if cur > 1:
        fac.add(cur)

    ans += len(fac) == 2

print(ans)





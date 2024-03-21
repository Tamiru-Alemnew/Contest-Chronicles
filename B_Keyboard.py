import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()

n , m , k= tip()

pos = {}
S =[]
for i in range(n):
    temp = cip()
    for j ,  t in enumerate(temp):
        if t =="S":
            S.append((i , j))
        else:
            pos[t] = (i , j)
            
_ = ip()
ar = cip()
ans = 0 
for c in ar:
    if c.lower() not in pos:
        print(-1)
        break
    else:
        if c.upper() == c:
            if len(S) == 0:
                print(-1)
                break

            mn = inf 
            x1 , y1 = pos[c.lower()]
            for x , y in S: 
                    mn = min(mn , ((x - x1)**2 + (y1 - y)**2)**0.5)
            if mn > k:
                ans += 1
else:
    print(ans)
                


    






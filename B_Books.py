import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()

n , t = tip()

a = lip()

r = 0
sm = 0
ans = 0
for i in range(n):
    while r < n and sm + a[r] <= t:
        sm += a[r]
        r += 1
    ans = max(ans, r - i)
    sm -= a[i]

print(ans)

    

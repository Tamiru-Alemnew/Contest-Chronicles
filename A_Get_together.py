import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;
x =[]
v = []
for _ in range(ip()):
    a , b = lip()
    x.append(a)
    v.append(b)


def check(t):
    left = -inf
    right = inf

    for i in range(len(x)):
        cur_l = x[i] - (t*v[i])
        cur_r = x[i] + (t*v[i])

        if cur_l > right or cur_r < left:
            return False

        left = max(cur_l , left)
        right = min(cur_r , right)

    return True

l , r = 0 , 10**18+ 19

ans = 0

while r - l > 0.0000006:

    md = (l + r) / 2

    if check(md):
        ans = md 
        r = md
    else:
        l = md 

print(ans)




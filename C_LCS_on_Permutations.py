import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n = ip()

a = lip()
b = lip()

pos = [0]*(n+1)


for i in range(n):
    pos[a[i]] = i + 1

cn = [0]*n

for i, bb in enumerate(b) :
    cn[i] = pos[bb]



seg = []
ans = 0

for c in cn:

    ind = bisect_right(seg , c)

    if ind == len(seg):
        ans += 1
        seg.append(c)
    else:
        seg[ind] = c

print(ans)

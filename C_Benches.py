import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;


n = ip()
m = ip()
bench = []
mx = 0
for i in range(n):
    cur = ip()
    mx = max(mx , cur)
    bench.append(cur)

dif = sum(bench) + m
mxx = n*mx
ans2 = mx + m

if dif > mxx:
    ans1 = mx + math.ceil(((dif) - mxx) / n)
else:
    ans1 = mx

print(ans1 , ans2)



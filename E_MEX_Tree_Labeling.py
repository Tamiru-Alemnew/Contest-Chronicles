import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n = ip()
v = defaultdict(list)
ans = [-1] * n

for i in range(1, n):
    a, b = lip()
    v[a].append(i)
    v[b].append(i)

mx = (0, 0)

for i in range(1, n + 1):
    mx = max(mx, (len(v[i]), i))

cur = 0
for i in v[mx[1]]:
    ans[i] = cur
    cur += 1

for i in range(1, n):
    if ans[i] == -1:
        ans[i] = cur
        cur += 1
    print(ans[i])
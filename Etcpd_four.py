import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n , m = tip()
a = lip()
b = lip()
k = ip()
kk = lip()

dc = {}

for i in range(n):
    dc[a[i]] = b[i]

sorted_dc = sorted(dc)

md = n // 2

ans = 0
print(sorted_dc[md])
for num in kk:
    if sorted_dc[md] <= num <= dc[sorted_dc[md]]:
        ans += 1


print(ans)
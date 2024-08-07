import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;
n = ip()
a = []
b = []
c = []
for i in range(n):
    aa , bb , cc = tip()
    a.append(aa)
    b.append(bb)
    c.append(cc)

dpa = [0]*n
dpb = [0]*n
dpc = [0]*n

dpa[0] = a[0]
dpb[0] = b[0]
dpc[0] = c[0]
for i in range(1 , n):
    dpa[i] = a[i] + max(dpb[i-1] , dpc[i-1])
    dpb[i] = b[i] + max(dpa[i-1] , dpc[i-1])
    dpc[i] = c[i] + max(dpa[i-1] , dpb[i-1])

print(max(dpa[-1] , dpb[-1] , dpc[-1]))
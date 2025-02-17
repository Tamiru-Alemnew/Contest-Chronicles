import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;


houses = [5, 10, 17]
stores = [1, 5, 20, 11, 16]

stores.sort()
ans = [-1]*len(houses)

for i in range(len(houses)):
    ind = bisect_left(stores , houses[i])
    dist = inf
    if ind < len(stores):
        dist = stores[ind]
    if ind > 0 :
        if abs(houses[i] - stores[ind -1]) <= dist - houses[i]:
            dist = stores[ind-1]

    ans[i] = dist

print(ans)



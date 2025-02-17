import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

heap = []
arr = []
ip()
for _ in range(ip()):
    arr.append(lip())

ans = []
arr.sort()

for s , e in arr:
    if not heap:
        heappush(heap , (e , 1))
        ans.append(1)

    elif heap and heap[0][0] <= s:
        cur , pos = heappop(heap)
        ans.append(pos)
        heappush(heap , (e , pos))

    else:

        heappush(heap , (e , len(heap)+1))
        ans.append(len(heap))

print(*ans)




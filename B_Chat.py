import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n , k , q = tip()
arr = lip()
min_heap = []
heapify(min_heap)

for i in range(q):
    f , s = tip()

    if f == 1 :   
        heappush(min_heap ,arr[s-1])
        while len(min_heap) > k:
            heappop(min_heap)
            

    if f == 2:
        if arr[s-1] in min_heap:
            print("YES")

        else:
            print("NO")

            
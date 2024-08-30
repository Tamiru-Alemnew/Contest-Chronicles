import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for _ in range(ip()):
    n = ip()
    arr = lip()
    cnt = defaultdict(int)

    for a in arr:
        cnt[a] += 1

    ans = []
    inc = True
    ans.append(arr[0])
    
    seen = set()
    seen.add(arr[0])
    for i in range(1 , n):
        if arr[i] not in visite

        if arr[i] > ans[-1] and inc or arr[i] < ans[-1] and not inc :


    print(*ans)
            

        







import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for i in range(ip()):
    n = ip()
    arr = lip()
    mp = defaultdict(int)
    ans = True
    mp[arr[0]] += 1
    for j in range(1 , n):
        if mp[arr[j] - 1] == 0 and mp[arr[j]+1] == 0:
            ans = False

        mp[arr[j] ] = 1

    if ans :
        print("YES")
    else:
        print("NO")

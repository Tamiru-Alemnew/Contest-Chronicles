import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n = ip()

arr = cip()
dp = [-1]*(n)
dp[0] = 0 
for i in range(n):
    if arr[i] == "W": continue

    for c in [1 , 3 , 5]:
        if i + c < n and arr[i] !="W":
            cur = 0 
            cur += arr[i] == '"'
            dp[i+c] = max(dp[i+c] , dp[i] + cur)

print(dp[-1])
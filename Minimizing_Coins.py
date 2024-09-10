import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n , x = tip()

dp = [float("inf") for i in range(x+1)]
arr = lip()
dp[0] = 0

for i in range(x):
    if dp[i] == float("inf"):
        continue
    
    for a in arr:
        if i + a <= x :
            dp[i+a] = min(dp[i] +1 , dp[i+a])

    
print(dp[x] if dp[x] != float("inf") else -1)

import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n , k = tip()
cost = lip()
dp = [inf]*n
dp[0] = 0

for i in range(1 , n):
    for j in range(1 , min(k , i) +1):
        dp[i] = min(dp[i] , abs(cost[i] - cost[i - j]) + dp[i-j])

print(dp[-1])
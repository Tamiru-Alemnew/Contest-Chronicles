import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

N , W = tip()

arr = []
for i in range(N):
    arr.append(lip())

dp = [0]*(W + 1) 

for i in range(1 , N + 1):
    cur = [0]*(W + 1) 
    for j in range(1 , W +1):
        cur[j] = dp[j]

        if j - arr[i-1][0] >= 0 :
            cur[j] = max(dp[j] , arr[i-1][1] + dp[j - arr[i-1][0]])

    dp = cur[:]
    
print(dp[W])
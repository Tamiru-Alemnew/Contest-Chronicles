import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n , m , c = tip()

M = lip()

graph = [0 for i in range(m)]

for i in range(m):
    a , b = lip()
    graph[a-1] = b - 1

dp = [0]*10000

cur = graph[0]
ans = 0 


for i in range(1, 10000):
    dp[i] = max(dp[i] , dp[i-1] + M[cur])

    if cur== 0:
        ans = max(ans , dp[i] - c*((i)**2))

    cur = graph[cur]


print(ans)
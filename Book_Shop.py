import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n , x = lip()

dp = [0 for i in range(x+1)]
v = lip()
p = lip()

for j ,  pr in enumerate(v) :
    pg = p[j]

    for i in range(x , -1 , -1):
        if i - pr>= 0 :
            dp[i] = max(dp[i - pr] + pg , dp[i])


print(dp[x])
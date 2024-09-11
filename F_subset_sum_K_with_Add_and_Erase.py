import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n , k = tip()
mod = 998244353
dp = [0 for i in range(k+1)]
dp[0]= 1

for _ in range(n):
    op , x = input().split()
    x = int(x)

    if op == "+":
        for i in range(k , x-1, -1):
            dp[i] += dp[i-x]
            dp[i] %= mod 

    else:
        for i in range(x , k+1):
            dp[i] -= dp[i-x]
            dp[i] %= mod 


    print(dp[k])
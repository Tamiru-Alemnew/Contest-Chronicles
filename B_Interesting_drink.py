import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n = ip()
arr = lip()
# arr.sort()

# for i in range(ip()):
#     cur = ip()
#     print(bisect_right(arr , cur))

dp = [0]*(100000 + 1)

for a in arr:
    dp[a] += 1


for i in range(1 , 100000 + 1):
    dp[i] += dp[i-1]


for  i in range(ip()):
    cur = ip()

    if cur >= 100000 :
        print(dp[100000])
    else:
        print(dp[cur])

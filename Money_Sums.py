import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n = ip()

arr = lip()
x = sum(arr)

dp = [False for i in range(x+1)]

dp[0] = True

for c in arr:
    for i in range(x , -1 , -1):
        if i -c >= 0 :
            dp[i] = dp[i-c] or dp[i]


ans = []

for i in range(1 , x+1):
    if dp[i]: 
        ans.append(i)

print(len(ans))
print(*ans)
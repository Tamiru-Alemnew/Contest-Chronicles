import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n = ip()

arr = lip()
mx = max(arr)
dp = defaultdict(int)

ln = 1

for a in arr:
    dp[a] = max(dp[a] , dp[a-1] + 1)
    ln = max(dp[a] , ln)


for key , value in dp.items():
    if value == ln :
        ans = [i for i in range(key-ln+1 , key +1 , 1)]

print(ln)

result = [0]*len(ans)

l = len(result) - 1

for i in range(n -1 , -1 , -1):
    if arr[i] == ans[l]:
        ans[l] = i +1
        l -= 1 

    if l < 0 :
        break

print(*ans)
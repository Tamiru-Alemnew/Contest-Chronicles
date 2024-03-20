import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right as br, bisect_left as bl; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()
 
n , k = lip()
arr = lip()
arr.sort()
x = arr[n-k] + 1

cnt=[]

for i in range(x):
    temp = []
    for j in range(n):
        cur = 0 
        t = arr[j]
        while t > i and len(temp) < k:
            t = t //2
            cur += 1
        
        if t == i:
            temp.append(cur)
    if len(temp) >= k:
        cnt.append([sum(temp),i])


cnt.sort(key=lambda x : x[0])
print(cnt[0][0])
            

import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0

def checker(arr):
    stack = [arr[0]]
 
    c = 0
    for a in reversed(arr):
        t = abs(a - stack[-1])
        c += min(a , stack[-1])
        stack.append(t)

    return c 


n = ip()
arr = lip()
arr.sort()
cur = sum(arr)

for i in range(n):
    for j in range(i + 1 , n):
        
        cur += min(arr[i] , arr[j]) + abs(arr[i] - arr[j])

        if i != j and n > 3:
            cur += checker(arr[i:j+1])

if n == 2:
    cur = min(arr[0] , arr[1]) + abs(arr[1] - arr[1])
if n == 3:
    cur += 2
if n > 3:
    cur += 3
if n >= 5:
    cur += checker(arr[:])
print(cur % 998244353)

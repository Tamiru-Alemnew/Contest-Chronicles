import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n, k = tip()
arr = lip()
 
def check(s):
    temp = [0] * n
    for i in range(n):
        temp[i] = arr[i] + (i + 1) * s
    temp.sort()
    total = 0
    for i in range(s):
        total += temp[i]

    return total <= k
 
 
l, r = 0 , n +1

while l + 1 < r:
    mid =(l + r) // 2

    if check(mid):
        l = mid

    else:
        r = mid
 
s = l
temp = [0] * n
for i in range(n):
    temp[i] = arr[i] + (i + 1) * s

temp.sort()

total = 0
for i in range(s):
    total += temp[i]

print(s, total)
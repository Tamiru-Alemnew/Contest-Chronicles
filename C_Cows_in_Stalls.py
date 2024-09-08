import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;
n , k = tip()

arr = lip()

def check(n):
    prev = arr[0]
    count = 0 

    for a in arr:
        if a - prev >= n :
            count += 1
            prev = a 

    return count >= k -1

l , r = 0 , 10**18

ans = 0

while l <= r:

    md = (l + r) // 2

    if check(md):
        ans = md 
        l = md + 1
    else:
        r = md  - 1

print(ans)
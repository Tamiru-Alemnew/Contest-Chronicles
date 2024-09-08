import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n , d = tip()
arr = lip()
"""
[-5e+17, -1e+18, -1.5e+18, -2e+18, -2.5e+18, -3e+18, -3.5e+18]
"""
def check(x):
    ps =[0]*(n+1)
    for i in range(n):
        ps[i+1] = ps[i] + arr[i] 

    l = 0 
    for r in range(d , n + 1):
        if ps[r-d]- ((r-d) * x) < ps[l] - l*x:
            l = r-d

        if ps[l] - l*x <= ps[r] - r*x:
            return l+1 , r
        
    return -1 , -1


l , r = 0 , 10**18

ans = [0,0]

while r - l >= 0.0000006:

    md = (l + r) / 2

    ll , rr = check(md)

    if ll != -1 :
        ans = [ll , rr]
        l = md 

    else:
        r = md 

print(*ans)
import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n = ip()

def check(k):
    t = n
    ans = 0

    while t >= 10 :
        tp = t 
        t -= k
        ans += tp - t
        d = t // 10 
        t -= d

    return ans + t 

l = 0 
r = n // 2 + 1
mdd = n // 2

while l < r :
    md = (l + r) // 2

    if  check(md) >= mdd:
        r = md 
    else:
        l = md + 1

print(r)


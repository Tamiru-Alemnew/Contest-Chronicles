import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right as br, bisect_left as bl; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()
 
n , k  = tip()
l  , r = 0 , n*k

def check(y):
    c = 0 
    c += y 
    lp = 1000

    while y >= 1:
        c += y // k
        y //= k

    return c >= n


while l < r : 
    md = (l + r) //2 
    if check(md):
        r = md 
    else:
        l = md + 1 

print(r)
    


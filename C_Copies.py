import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n  , k , y = tip()

l , r = 0 , n*min(k ,y) + 1

def check(num):
    num -= min(k , y)
    one = num // k
    two = num // y

    return one + two  + 1>= n

while l < r :
    md =( l + r) // 2

    if check(md):
        r = md
    else:
        l = md + 1

print(l)

print( 6 & 1)

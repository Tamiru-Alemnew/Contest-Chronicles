import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;
n , k = tip()
"""
1 3 2 4 10 8 4 2 5 3
       |  | |  
"""
arr = lip()

def check(t):
    cur = k
    temp = 0

    for a in arr:
        if a > t:
           return False
       
        if temp + a > t:
           temp = a
           cur -= 1
        else:
           temp += a
    
    return cur > 0 and temp <= t



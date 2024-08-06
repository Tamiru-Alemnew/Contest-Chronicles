import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for i in range(ip()):
    n , s , m = tip()
    pl , pr = 0 , 0
    flag = True
    for i in range(n):
        l , r = tip()

        if l - pr >= s :
            print("YES")
            flag = False
        pl = l 
        pr = r
        
    if m - pr >= s :
        print("YES")
        flag = False
    if flag:
        print("NO")
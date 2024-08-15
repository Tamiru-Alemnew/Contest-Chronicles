import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for i in range(ip()):
    cur = input()

    if len(cur) < 3:
        print("NO")
    
    else:
        rr = cur[2:]
        ten = int(cur[:2])
        rest = int(cur[2:])

        if ten != 10 or rest < 2 or rest < (10**(len(rr)-1)):
            print("NO")

        else:
            
            print("YES")
import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for j in range(ip()):
    n , k = tip()
    arr = lip()

    arr.sort()

    A = 0 
    B = 0 

    cur = True
    diff = 0 
    for i in range(n -1 , -1 , -1):
        if cur:
            A += arr[i]
            cur = False
        else:
            B += arr[i]
            diff += arr[i+1] - arr[i]
            cur = True

    B = min(min(k , diff) + B , A)
    print(A-B)

        

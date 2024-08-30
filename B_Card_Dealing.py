import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for _ in range(ip()):
    n = ip() 
    tot = n
    cur = 2
    A = 1
    Alice = False
    n -= 1
    
    while  n > 0 :
        # print(n , cur , cur+ 1 , Alice)
        add = min(cur + cur+1 , n)

        if Alice :
            A += add

        Alice = not Alice

        n -= add
        
        cur += 2
        

    print(A , tot - A)

import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;
for _ in range(ip()):
    n, k = tip()
    
    ans = 0 

    if k == 1:
        ans = n
    else:
        for i in range(31, -1, -1):
            cur = pow(k, i)
            
            if cur > n:
                continue
            
            count = n // cur
            ans += count
            n -= count * cur
            
            if n == 0:
                break
    
        ans += n
    
    print(ans)

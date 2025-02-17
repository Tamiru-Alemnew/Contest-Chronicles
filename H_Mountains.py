import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for _ in range(ip()):
    n , k = tip()
    arr = [i for i in range(1 , n + 1)]
    count = 0 

    cur = 2 
    
    if n <= 2 :
        if k == 0 :
            print(*[i for i in range(1 , n+1)])
        else:
            print(-1)
        continue

    
    while cur < n:
        arr[cur] , arr[cur-1] = arr[cur-1] , arr[cur]
        count += 1
        cur += 2

    if count < k :
        print(-1)
    else:
        print(*arr)
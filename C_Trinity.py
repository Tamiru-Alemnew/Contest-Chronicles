import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for _ in range(ip()):
    n = ip()
    arr = lip()
    arr.sort()
    ans = n
    l , r = 1 ,  n
    print(arr)

    
    while r >= l:
        mid = (l + r) // 2
        flag = False


        if mid == 1:
            ans = min(n - 1, ans)
            l = mid + 1
            continue
        
        for i in range(n - mid + 1):
            x = arr[i] + arr[i + 1]
            if x > arr[i + mid - 1]:
                flag = True
                break
        
        if flag:
            ans = min(n - mid, ans)
            l = mid + 1
        else:
            r = mid - 1
    
    print(ans)
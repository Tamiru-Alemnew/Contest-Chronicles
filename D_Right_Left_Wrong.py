import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;
for i in range(ip()):
    n = ip()
    dir = lip()
    arr = cip()
    l = 0 
    
    r = n -1 
    ps = [0]*(n+1)

    for i in range( n):
        ps[i+1] = dir[i] + ps[i]

    ans = 0

    while l < r :
        if arr[l] =="L" and arr[r] == "R":
            ans += ps[r+1] - ps[l]
            l += 1

            r -= 1

        elif arr[l] =="L" and arr[r] != "R":
            r -=1

        elif arr[l] !="L" and arr[r] == "R":
            l += 1

        else:
            l += 1
            r -= 1


    print(ans)

        


    

import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for _ in range(ip()):
    n , r = tip()

    arr = lip()

    ans = 0 


    left = 0 
    used = 0 

    for i in range(n):
        if even(arr[i]):
            ans += arr[i]
        else:
            ans += arr[i] - 1
            left += 1

        r -= arr[i] // 2


    if not even(left):
        ans += 1
        r -= 1

        left -= 1

    hv = left // 2
    tm = hv 

    for i in range(hv , r):

        if tm > 0 :
            ans += 2
            tm -= 1


    print(ans)
            

    
        






    
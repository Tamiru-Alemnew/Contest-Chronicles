import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;


for _ in range(ip()):
    w1 = cip()
    w2 = cip()

    l , r = 0 , 0 

    while l < len(w1) and r < len(w2) and w1[l] == w2[r]:
        l += 1
        r += 1


    rem = len(w1) - l 
    remm = len(w2) - r

    ans  = rem + remm 

    if l :
        ans += l + 1 
    

    print(ans)

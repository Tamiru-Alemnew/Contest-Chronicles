import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for i in range(ip()):
    mx = []
    n , k = tip()

    for j in range(n):
        a , b = tip()
        heappush(mx , (min(a , b) , -max(a , b)))

    ans =  True
    cur = 0 
    op = 0 

    while k > 0 and mx :
        a , b = heappop(mx)
        b = - b

        mt = a * (b-a) + a*2
        if k > mt:
            k -= mt
            op += a*b
        else:
            while k > 0 and a > 0 and b > 0 :
                if a == 1 and b == 1:
                    

    



    if k > 0 :
        print(-1)
    else:
        print(op)
            
            






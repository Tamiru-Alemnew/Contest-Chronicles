import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for i in range(ip()):
        b , c , d = tip()
        a = 0
        borrow = 0
        ok = True
        
        for i in range(61): 
            bi = (b >> i) & 1
            ci = (c >> i) & 1
            di = (d >> i) & 1
            
            found = False
            

            cc0 = bi - borrow
            if cc0 >= 0:
                tmp = cc0 - di
                if tmp >= 0 and tmp % 2 == 0 and tmp // 2 <= 1:
                    ai = 0
                    borrow = tmp // 2
                    a |= (ai << i)
                    found = True
            
            if not found:
                cc1 = 1 | bi
                a1_and_c = ci
                tmp1 = cc1 - a1_and_c - borrow
                if tmp1 >= 0:
                    tmp = tmp1 - di
                    if tmp >= 0 and tmp % 2 == 0 and tmp // 2 <= 1:
                        ai = 1
                        borrow = tmp // 2
                        a |= (ai << i)
                        found = True
            
            if not found:
                ok = False
                break
        
        if ok and borrow == 0:
            print(a)
        else:
            print(-1)
    

import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;



for _ in range(ip()):
    a , b , c = tip()
    arra  = lip()
    arrb = lip()
    arrc = lip()

    arra.sort()
    arrb.sort()
    arrc.sort()
    
    # h , i , j = 0 , 0 , 0 

    # answer = inf
    # flag = False
    # while h < len(arra) and i < len(arrb) and j < len(arrc) and not flag:
    #     current = (arra[h] - arrb[i])**2 + (arrb[i] - arrc[j])** 2 + (arrc[j] - arra[h])**2

    #     next = []
    #     next.append((inf if h + 1 >= len(arra) else arra[h+1] , 0))
    #     next.append((inf  if i + 1 >= len(arrb) else arrb[i+1], 1))
    #     next.append((inf if j + 1 >= len(arrc) else arrc[j+1] , 2))


    #     heapify(next)
    #     answer = min(current , answer)

    #     for _ in range(3):
    #         cur  , idx = heappop(next)

    #         if idx == 0 and h + 1 < len(arra):
    #             h += 1
    #             break
    #         if idx == 1 and i + 1 < len(arrb):
    #             i += 1
    #             break
    #         if idx == 2 and j + 1 < len(arrc):
    #             j += 1
    #             break

    #     else:
    #         flag = True

    for i in range(a):
        b1 = bisect_left(arrb , arra[i])
        b2 = -1 if b1 == b  else b1 + 1
        idx2 = bisect_(arrc , arra[i])
        idx3 = bisect_right(arrc , arrb[idx2-1] if idx2 ==b else arrb[idx2])

        current = (arra[i] - arrb[])**2 + (arrb[i] - arrc[j])** 2 + (arrc[j] - arra[h])**2

    print(answer)

            





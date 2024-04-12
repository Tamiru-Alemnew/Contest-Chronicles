import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0

for _ in range(ip()):
    x = lsip()
    
    y = lsip()
    cur_y = y[0]
    cur_x = x[0]

    for i in range(1 ,len(x)):

        if y[i] > x[i]:
            if cur_y > cur_x:
                cur_x = y[i]  + (10)*cur_x
                cur_y = x[i]  + (10)*cur_y

            else:
                cur_x = x[i]  + (10)*cur_x
                cur_y = y[i]  + (10)*cur_y
          
        else:
            if cur_y < cur_x:
                cur_x = y[i]  + (10)*cur_x
                cur_y = x[i]  + (10)*cur_y

            else:
                cur_x = x[i]  + (10)*cur_x
                cur_y = y[i]  + (10)*cur_y
            
    print(cur_x)
    print(cur_y)

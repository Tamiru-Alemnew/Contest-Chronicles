import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for i in range(ip()):
    n , k , x = tip()
    path = []
    def bt(cur_sum):
        global n , x , k
        if cur_sum == n:
            return True
        if cur_sum > n :
            return False
        
        for i in range(1 , k +1):
            if i == x:
                continue
            
            path.append(i)
            if bt( cur_sum+i):
                return True
            path.pop()

    if bt(0):
        print("YES")
        print(len(path))
        print(*path)
    else:
        print("NO")
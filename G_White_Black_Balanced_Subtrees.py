import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0

for _ in range(ip()):
    n = ip()
    arr =["Tamiru"] + lip()
    color = ["Alemnew"] + cip()
    tree = [["Abebe"] ,["hhh"]] +[[0 , 0] for _ in range(n)]

    for i in range(2 , n):
        if tree[arr[i]][0] == 0:
            tree[i][0] = i 
        
        else:
            tree[i][1] = i

    print(tree)



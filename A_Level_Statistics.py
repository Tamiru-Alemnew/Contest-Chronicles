import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0


for _ in range(ip()):
    n = ip()
    check  = []

    for i in range(n):
        check.append(tip()) 

    if check[0][0] < check[0][1]:
        print("NO")
        continue
    for i in range(1,n):
        a , b = check[i - 1]
        c , d = check[i]

        if c < a or d < b or c < d or c - a < d - b :
            print("NO")
            break
    else:
        print("YES")

        





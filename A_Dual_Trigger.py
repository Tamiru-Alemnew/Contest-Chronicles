import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0

for _ in range(ip()):
    n = ip()
    a = cip()
    b =  a.count("1")
    if b == 2 :
        for i in range(1 ,n):
            if a[i] == a[i-1] == "1":
                print("NO")
                break
        else:
            print("YES")
    else:
        if n == 1:
            if a[0]== "1":
                print("NO")
            else:
                print("YES")
        elif n ==2 :
            if b > 0 :
                print("NO")
            else:
                print("YES")    
        elif even(b):
            print("YES")
        else:
            print("NO")
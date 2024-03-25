import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()

for _ in range(ip()):
    n , x = tip()
    arr = lip()
    odd = 0 
    even = 0 
    for b in arr:
        odd += b % 2 ==1 
        even += b % 2 == 0 

    for i in range(1,min(odd , x)+1):
        if i % 2 and even >= x - (i):
            print("Yes")
            break
    else:
        print("No")

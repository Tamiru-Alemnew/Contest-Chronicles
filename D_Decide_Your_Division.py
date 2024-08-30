import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;


results = []

index = 1
for _ in range(ip()):
    n = ip()
    index += 1
    
    two= 0
    three = 0
    five = 0
    
    while n % 2 == 0:
        n //= 2
        two+= 1
    
    while n % 3 == 0:
        n //= 3
        three += 1
    
    while n % 5 == 0:
        n //= 5
        five += 1

        
    
    if n != 1:
        print(-1)
    else:
        print(two+ three * 2 + five * 3)


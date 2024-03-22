import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()


for z in range( ip()):
    a , b , l = tip()

    seen = set()

    for i in range(20):
        x = l 
        for _ in range(i):
            if x % a :
                break
            x = x// a
        else:
            while True:
                seen.add(x)
                if x % b:
                    break
                x = x // b

    print(len(seen))







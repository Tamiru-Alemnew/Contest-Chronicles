import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()

for _ in range(ip()):
    n , k = tip()

    ha = cip()
    need = cip()
    inc = 0 
    dec = 0 

    y = sum([ord(l) for l in need])

    x = 0 
    
    for i in range(k):
        x += ord(ha[i])
    if x == y:
        print("YES")
    else:
        for j in range(k , n):
            x += ord(ha[j])
            x -= ord(ha[j-k])

            if x == y:
                print("YES")
                break

        else:
            print("NO")
        




        



import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()


n , a , b , c = tip()

ans = 0
for x in range(a + 1):
    for y in range(b + 1):
        z = n - 0.5 * x - y
        if z >= 0 and z %2 ==0 and z <= c*2 :
            ans += 1

print(ans)
                    


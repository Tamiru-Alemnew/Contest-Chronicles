import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()
from itertools import permutations

n = ip()

if set(str(n)) == set(('4', '7')) or set(str(n)) == set(('7')) or set(str(n)) == set(('4')):
    print("YES")
else:
    for i in range(1, n):
        if (set(str(i)) == set(('4', '7')) or set(str(i)) == set(('7')) or set(str(i)) == set(('4'))) and (n % i == 0):
            print("YES")
            break
    else:
        print("NO")






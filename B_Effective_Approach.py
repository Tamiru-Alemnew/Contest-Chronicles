import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()

n = ip()
arr = lip()
q = ip()
b = lip()

vs = 0 
sa = 0 

seen = {}

for j in range(n):
    seen[arr[j]] = j + 1

for l in b:
    vs += seen[l]
    sa += n - seen[l] + 1

print(vs , sa)
                

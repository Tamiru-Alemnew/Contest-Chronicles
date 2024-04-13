import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0

#  "chest" exercises, "biceps" exercises and "back"
n = ip()

arr = lip()
c = 0 
b = 0
bk = 0
for i in range(n):
    if i % 3 == 0:
        c += arr[i]
    elif i % 3 == 1:
        b += arr[i]
    else:
        bk += arr[i]

l = max(c , b  , bk)

if l == c:
    print("chest")
elif l == b:
    print("biceps")
else:
    print("back")



    





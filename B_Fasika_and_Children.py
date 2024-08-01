import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n , m = tip()

arr = lip()

check = []

for i in range(n):
    check.append((arr[i] , i +1))

l = 0 
r = n-1


while  r - l >= 1:
    cur , pos = check[l]

    if cur > m:
        check.append((cur - m , pos))
        r += 1

    l += 1
    
print(check[l][1])
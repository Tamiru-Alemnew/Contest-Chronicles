import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n = ip()

a = lip()
b = lip()

checker = [0]*n
cur = n-1
for i in range(n //2 ):
    checker[i] = cur
    cur -= 2

cur = n

for i in range(n-1 , n//2-1 ,-1):
    checker[i] = cur
    cur -= 2

ans_a = 0
ans_b = 0 

for i in range(n):
    if a[i] != checker[i]:
        ans_a += 1

    if b[i] != checker[i]:
        ans_b += 1

if ans_a > ans_b:
    print("Team B")
elif ans_a < ans_b:
    print("Team A")
else:
    print("Tie")
import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n = ip()

arr  = lip()

dp = [1 for i in range(n)]

min_endings = []
for i in arr:
    pos = bisect_left(min_endings, i)
    if pos == len(min_endings):  
        min_endings.append(i)
    else:  
        min_endings[pos] = i

print(len(min_endings))



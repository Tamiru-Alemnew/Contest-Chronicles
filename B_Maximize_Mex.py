import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;
import random

for _ in range(ip()):
    n , x = tip()
    arr = lip()
    freq = defaultdict(int)
    rn = random.randint(0, 10**5)
    for a in arr:
        freq[a ^rn] += 1


    for i in range(n):
        if freq[(i-x) ^ rn] > 1 :
            freq[i^rn] += freq[(i-x) ^ rn] - 1

        if not freq[i^rn]:
            print(i)
            break
    else:
        print(n)


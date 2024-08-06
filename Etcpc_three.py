import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n = ip()
q = ip()

mpp = defaultdict(int)

av = [i for i in range(1 , n + 1)]

heapify(av)

for i in range(q):
    cur , id = lcp()

    if cur == "E":
        if len(av)== 0:
            print("Sorry sir, no available slots")
        else:
            pos = heappop(av)
            mpp[id] = pos
            print("Good morning sir, please proceed to slot number" , pos)
    else:
        heappush(av , mpp[id])
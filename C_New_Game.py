import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;
import random 
for _ in range(ip()):
    n , k = tip()
    arr = lip()

    arr.sort()
    l = 0 
    ans = 0
    cur = 0
    freq = defaultdict(int)
    xx = random.randint(1 , 10**9)
    for r in range(n):
        if r > 0 and arr[r] > arr[r-1] + 1:
            cur = 0
            freq = defaultdict(int)
            l = r

        freq[arr[r] ^ xx] += 1
        if freq[arr[r] ^ xx] == 1:
            cur += 1

        while cur > k:
            freq[arr[l] ^ xx] -= 1
            if freq[arr[l] ^ xx] == 0:
                cur -= 1
            l += 1

        ans = max(r - l + 1, ans)

    print(ans)

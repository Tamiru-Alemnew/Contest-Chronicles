import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

def findK(arr):
    k = 0
    for i in range(1, len(arr) + 1):
        if i % 2 == 1:
            k = k & arr[i - 1]
        else:
            k = k | arr[i - 1]
    return k

for _ in range(ip()):
    n = ip()

    if n == 5:
        ans = [2, 1, 3, 4, 5]
    elif n == 6:
        ans = [1, 2, 4, 6, 5, 3]
    elif n == 7:
        ans = [2, 4, 5, 1, 3, 6, 7]
    elif n == 8:
        ans = [2, 4, 5, 1, 3, 6, 7, 8]
    elif n == 9:
        ans = [2, 4, 5, 6, 7, 1, 3, 8, 9]
    elif n == 10:
        ans = [1, 2, 3, 4, 5, 6, 8, 10, 9, 7]
    else:
        ans = list(range(1, n + 1))

    print(findK(ans))
    print(*ans)
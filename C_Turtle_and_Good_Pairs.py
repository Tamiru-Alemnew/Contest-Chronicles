import sys
from collections import Counter, defaultdict, deque
from bisect import bisect_right, bisect_left
from math import inf, ceil
import math
from heapq import *

# Input functions
ip = lambda: int(sys.stdin.readline().strip())
lip = lambda: list(map(int, sys.stdin.readline().strip().split()))
tip = lambda: tuple(map(int, sys.stdin.readline().strip().split()))
lcp = lambda: sys.stdin.readline().strip().split()
lsip = lambda: list(map(int, sys.stdin.readline().strip()))
cip = lambda: list(sys.stdin.readline().strip())
sip = lambda: sys.stdin.readline().strip()
even = lambda x: x & 1 == 0

def alternate_chars():
    n = ip()
    chars = cip()
    chars.sort()
    result = []
    left, right = 0, n - 1

    while left <= right:
        result.append(chars[right])
        right -= 1
        if left > right:
            break
        result.append(chars[left])
        left += 1

    return "".join(result)

for _ in range(ip()):
    print(alternate_chars())
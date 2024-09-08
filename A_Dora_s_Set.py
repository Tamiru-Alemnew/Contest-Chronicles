import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

def max_operations(l, r):
    # Generate the set s containing all integers from l to r
    s = list(range(l, r + 1))
    
    # Count the number of integers that are coprime with each other
    count = 0
    n = len(s)
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if math.gcd(s[i], s[j]) == 1 and math.gcd(s[j], s[k]) == 1 and math.gcd(s[i], s[k]) == 1:
                    count += 1
    
    # Calculate the maximum number of operations
    return count // 3

for _ in range(ip()):
    l , r = lip()
    print(max_operations(l , r))
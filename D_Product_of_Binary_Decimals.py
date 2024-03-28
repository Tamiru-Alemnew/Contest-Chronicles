import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0


def help(n, binary_decimals):
    if n == 1:
        return True
    for i in binary_decimals:
        if n % i == 0:
            if help(n // i, binary_decimals):
                return True
    return False

check = []
for i in range(2, 10**5 + 7):
    if all(digit in {'0', '1'} for digit in str(i)):
        check.append(i)

for _ in range(ip()):
    n = ip()
    print("YES" if help(n, check) else "NO")



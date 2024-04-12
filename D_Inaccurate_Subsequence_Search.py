import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0
import random 
for _ in range(ip()):
    n , m , k = tip()
    a = lip()
    b = lip()
    freq_a = defaultdict(int)
    freq_b = defaultdict(int)
    x = random.randint(1, 10 ** 6 )
    count = 0

    for j in b:
        freq_b[j^x] += 1

    for i in range(m):
        freq_a[a[i]^x] += 1
        if freq_a[a[i]^x] <= freq_b[a[i]^x]:
            count += 1

    ans = 0
    if count >= k:
        ans += 1

    for i in range(m, n):
        freq_a[a[i]^x] += 1
        if freq_a[a[i]^x] <= freq_b[a[i]^x]:
            count += 1

        freq_a[a[i-m]^x] -= 1
        if freq_a[a[i-m]^x] < freq_b[a[i-m]^x]:
            count -= 1

        if count >= k:
            ans += 1

    print(ans)



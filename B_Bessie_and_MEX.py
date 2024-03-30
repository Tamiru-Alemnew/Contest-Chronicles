import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0

for _ in range(ip()):
    num = ip()
    arr = lip()
    res = [0]* num
    used_set = set()

    if arr[0] == 1 or arr[0] == 0:
        max_val = 1
        res[0] = 0
        used_set.add(0)
    else:
        max_val = 0
        res[0] = -arr[0]
        used_set.add(-arr[0])

    for i in range(1, num):
        if max_val - arr[i] >= 0 and max_val - arr[i] not in used_set:
            res[i] = max_val - arr[i]
            used_set.add(max_val - arr[i])
            max_val += res[i] == max_val
        else:
            res[i] = max_val
            used_set.add(max_val)
            max_val += 1
            while max_val in used_set:
                max_val += 1
    print(*res)
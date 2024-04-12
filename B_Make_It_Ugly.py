import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0


for _ in range(ip()):
    n =  ip()
    arr = lip()
    count = Counter(arr)
    a = count.most_common()
    b = a[0][0]
    min_streak = inf
    current_streak = 0
    for num in arr:
        if num == b:
            current_streak += 1
        else:
            if current_streak > 0:
                min_streak = min(min_streak, current_streak)
            current_streak = 0
    
    if current_streak > 0:
        min_streak = min(min_streak, current_streak)

    if min_streak == n or min_streak== inf:
        print(-1)
    else:
        print(min_streak)


    
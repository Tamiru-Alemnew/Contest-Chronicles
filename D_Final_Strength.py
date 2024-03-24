import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()


for _ in range(ip()):
    n = ip()
    arr = lip()
    for i in range(1, n+1):
        for j in range(0, len(arr), 2**i):
            inc = defaultdict(int)
            cur = sorted(arr[j: j * 2])
            l = 0
            for k in range(1, len(cur)):
                if cur[k] > cur[k - 1]:
                    l = k
                inc[cur[k]] += l
            for k in range(j, min(j * 2, len(arr))):
                arr[k] += inc[arr[k]]
    print(*arr)




            








    

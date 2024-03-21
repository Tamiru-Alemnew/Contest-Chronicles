import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()

n = ip()
t =[0] + lip()
answer = [0] * (n + 1)

for low in range(1, n + 1):
    cnt = [0] * (n + 1)
    best = 0
    for i in range(low, n + 1):
        val = t[i]
        cnt[val] += 1
        if cnt[val] > cnt[best] or (cnt[val] == cnt[best] and val < best):
            best = val
        answer[best] += 1

        
print(' '.join(map(str, answer[1:])))





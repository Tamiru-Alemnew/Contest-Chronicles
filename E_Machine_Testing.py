import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()

for _ in range(ip()):
    n = ip()
    health = lip()
    power = lip()

    stack = [(inf, power[0])]
    ans = 0
    for i in range(1, n):
        duration = 0
        while health[i] - (stack[-1][0] - duration)*stack[-1][-1] > 0:
            t, p = stack.pop()

            health[i] -= (t-duration)*p
            duration += (t-duration)
       
        duration += ceil(health[i]/stack[-1][-1])
        stack.append((duration, power[i]))
        ans = max(ans, duration)
        print(stack)
    print(ans)





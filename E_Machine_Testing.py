import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()

for _ in range(ip()):
    n = ip()
    health = lip()
    power = lip()
    if n <= 1 :
        print(0)
        continue

    stack = []
    prev_time = math.ceil(health[1] / power[0])
    stack.append((prev_time, power[1]))


    for idx in range(2, n):
        curr_time = math.ceil(health[idx] / power[idx - 1])

        if curr_time < prev_time:
            stack.append((curr_time, power[idx]))

        else:
            prev_time, prev_power = stack.pop()
            curr_health = health[idx] - prev_time * prev_power

            while stack and curr_health > 0:
                cur_time , cur_power = stack.pop()
                curr_health -=(cur_time - prev_time ) * cur_power
                prev_time = cur_time
            
            if not stack:
                if curr_health > 0 :
                    stack.append((cur_time + math.ceil(cur_time / power[0]) , power[idx]))
            else:
                stack.append((cur_time , power[idx]))

        print(stack)


    print(max(stack))





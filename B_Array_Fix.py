import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()


for _ in range(ip()):
    n = ip()
    arr = lcp()
    stack = [0]
    for i in range(n):
        if int(arr[i]) >= stack[-1]:
            if int(arr[i][0]) >= stack[-1] and len(arr[i]) >1 and int(arr[i][0]) <= int(arr[i][1]): 
                stack.append(int(arr[i][0]))
                stack.append(int(arr[i][1]))
            else:
                stack.append(int(arr[i]))
        else:
            print("NO")
            break
    else:
        print("YES")
        
            

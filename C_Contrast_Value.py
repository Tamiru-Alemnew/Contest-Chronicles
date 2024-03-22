import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()

x = ip()

for j in range(x):
    n = ip()
    arr = lip()
    ans = n 
    temp =[arr[0]]
    if n > 1:

        for i in range(1,n):
            if arr[i] == arr[i - 1] :
                ans -= 1
            else:
                temp.append(arr[i])

        for i in range(len(temp)-2):
            if temp[i] > temp[i + 1] > temp[i + 2]:
                ans -= 1

        for i in range(len(temp)-2):
            if temp[i] < temp[i + 1] < temp[i + 2]:
                ans -= 1

    print(ans)



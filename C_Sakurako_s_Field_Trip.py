import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for _ in range(ip()):
    n = ip()
    arr = lip()
    temp = arr[::-1]
    for i in range(n//2):
        if i < n and arr[i] == arr[i+1] or i > 0 and arr[i] == arr[i-1]:
            if (i > 0 and arr[n-i-1] == arr[i-1]) or( i !=n-1 and arr[n-i-1] == arr[i+1]):
                # print((i > 0 and arr[n-i-1] == arr[i-1]) , i)
                continue

            arr[i] , arr[n-i-1] = arr[n-i-1] , arr[i]
  
    ans = 0

    for i in range(n//2):
        if i < n and arr[i] == temp[i+1] or i > 0 and temp[i] == arr[i-1]:
            if (i > 0 and [n-i-1] == arr[i-1]) or( i !=n-1 and temp[n-i-1] == temp[i+1]):
                # print((i > 0 and arr[n-i-1] == arr[i-1]) , i)
                continue

            arr[i] , arr[n-i-1] = arr[n-i-1] , arr[i]

    # 3 1 3 2 2 3 3
    print(arr)
    for i in range(1 , n):
        ans += arr[i] == arr[i-1]

    print(ans)
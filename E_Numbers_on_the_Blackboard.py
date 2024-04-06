import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0

for _ in range(ip()):
    n , k = tip()
    arr = lip()
    arr.sort()
    for i in range(n):
        arr[i] -= k
    
    if arr[0] == arr[n-1]:
        print(0)

    elif arr[0] <= 0 <= arr[n-1] :
        print(-1)
    
    else:
        if arr[n-1] < 0 :
            arr = [-arr[i] for i in range(n)]
        gd = arr[0]

        for num in arr:
            gd = math.gcd(num , gd)

        ans = 0 

        for num in arr:
            ans += num//gd - 1
    
        print(ans)

    
2
    
    

    


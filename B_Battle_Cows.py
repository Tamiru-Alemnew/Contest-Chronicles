import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0


for _ in range(ip()):
    n , k = tip()
    a = lip()
    c = a[k-1]
    ans = 0 
    l = 0
    for i in range(n):
        if a[i] < c:
            ans += 1
        elif a[i] == c:
            continue
        else:
            if k - 1 < i:
                break
            a[k-1] , a[i] = a[i] , a[k-1]
            l = i
            break
    ans1 = 0

    for j in range(l +1 , n):

        if a[j] < c:
            ans1 += 1
        else:
            break
    
    ans1 += l > 0
    ans -= 0< l < (k -1)
    print(max(ans , ans1))

    

    

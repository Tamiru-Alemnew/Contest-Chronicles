import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0

def k_smallest_elements(arr, s):
    so = sorted(arr)
    chk = set(so[:s])

    res = []
    mx = max(chk)
    for b in arr :
        if b in chk:
            res.append(b)
            if len(res) == k :
                break
    return res , mx
    

for _ in range(ip()):
    n , m , k = tip()
       
    a = lip()
    if k <= m:
        print(min(a)*k)
        continue
    s = ceil(k / m)

    arr , mx = k_smallest_elements(a , s)
    ans = 0 
    cur = 0
    mm = k % m
    flag = True

    for i in range(s):
        if k % m == 0 :
            ans += (arr[i] + cur)*m
            cur += m
        else:
            if arr[i] == mx and flag:
                ans += (arr[i] + cur)*(mm)
                cur += mm
                flag = False
            else:
                ans += (arr[i] + cur)*m
                cur += m


    print(ans)


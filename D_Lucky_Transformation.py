import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0


n , k = tip()
t =cip()
i = 1
 
i = 0
 
while k and i < n - 1:
 
    if t[i] == '4' and t[i + 1] == '7':
        k -= 1
 
        if even(i):
            t[i + 1] = '4'
 
        else:
            if i > 0 and t[i - 1] == '4':
                if even(k): 
                    t[i] = '7'
                break
 
            t[i] = '7'
            i -= 2
    i += 1
 
print(''.join(t))
    
    






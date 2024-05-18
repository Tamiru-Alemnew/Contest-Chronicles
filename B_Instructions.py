import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    for _ in range(ip()):
        n = ip()
        arr =lip()
        memo = {}

        def bt(i ):
            
            if i >= n :
                return 0
                
            if i in memo:
                return memo[i]

            memo[i] = arr[i] +  bt(i + arr[i])

            return memo[i]
        
        ans = 0 

        for i in range(0 , n):
            ans = max(ans , bt(i ))

        print(ans)
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()




        

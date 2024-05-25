import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;
import threading
from sys import stdin, stdout, setrecursionlimit
from collections import defaultdict
setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

def main():

    mod = 10**9+7
    memo = {}



    def dp(j , target):
        if (j , target ) in memo :
            return memo[(j , target )]
        
        if j > target  or target < 0:
            return 0
        
        if target == 0 :
            return 1
        
        nxt = 0 

        for i in range(j , target + 1):
            cur = str(i)
            if cur == cur[::-1]:
                nxt += dp(i , target - i) % mod

        memo[(j , target )] = nxt

        return nxt
    
    dp(1 , 40000 )

    for _ in range(ip()):
        n = ip()
        print((1, memo[n]))


main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()





        
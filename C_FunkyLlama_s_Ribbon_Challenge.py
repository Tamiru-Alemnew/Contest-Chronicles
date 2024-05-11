import sys; import threading ; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

input = lambda: sys.stdin.readline().strip()

def main():
    n , a , b ,c = tip()
    memo = {}

    def bt(cur):
        if cur == 0 :
            return 0 

        if cur <  0 :
            return float("-inf")

        if cur in memo:
            return memo[cur]

        nxt = float("-inf")

        for st in [a , b , c]:
            nxt = max(1 + bt(cur - st) , nxt)

        memo[cur] = nxt

        return nxt

    ans = bt(n)

    print(ans)
            
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()




        



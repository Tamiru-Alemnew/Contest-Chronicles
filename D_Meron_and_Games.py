import sys; import threading ; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

input = lambda: sys.stdin.readline().strip()

def main():
    zz= ip()
    arr = [0]*100001
    arr2= lip()

    for x in arr2:
        arr[x] += x

    memo = {}

    def dp(i):
        if i >= len(arr):
            return 0
        
        if i in memo:
            return memo[i]
        
        include = arr[i] + (dp(i + 2) if i + 2 < len(arr) else 0)
        exclude = dp(i + 1)

        memo[i] = max(include, exclude)

        return memo[i]

    print(dp(0))
            
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()




        



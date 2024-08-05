import threading
from sys import stdin, stdout, setrecursionlimit
import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
def main():

    n = ip()
    arr = tip()

    memo = {}
    def dp(i , cur):

        if cur < 0 or i >= n:  return 0

        if i in memo:
            return memo[i]

        memo[i] = max(dp(i + 1 , cur + arr[i]) + 1 , dp(i + 1 , cur))

        return memo[i] 

    print(dp(0 , 0))

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
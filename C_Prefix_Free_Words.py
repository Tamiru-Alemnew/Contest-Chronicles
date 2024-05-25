import threading
from sys import stdin, stdout, setrecursionlimit
from collections import defaultdict
import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
def main():

    n = ip()

    arrr = lip()
    trie = {}

    def insert(word):
        node = trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = True

    def search(word):
        node = trie
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return '#' in node

    def startsWith(prefix):
        node = trie
        for char in prefix:
            if char not in node:
                return False
            node = node[char]

        return True
    arr = sorted(arrr)
    mx = arr[-1]

    possible = set()
    ans = []
    
    def bt(cur_len , ct ,  path):
        check = "".join(path)

        if check in possible:
            return False
        
        if cur_len == 0 and not startsWith(check):
            possible.add((check))
            ans.append(check)
            insert(check)
            return True
        
        if cur_len < 0:
            return False
        
        path.append("0")
        left =  bt(cur_len - 1 , ct ,path )
        path.pop()
        right = False
        if not left:
            path.append("1")
            right = bt(cur_len - 1 ,ct ,path)
            path.pop()

        return left or right


    cur_pos = 2**mx

    for n in arr:
        cur_pos -= 1 / n

    if cur_pos < 0 :
        print("NO")
    else:
        flag = True
        for a in arrr:
            flag = bt(a ,a, [])

        if not flag:
            print("NO")
        else: 
            print("YES")
            for w in ans:
                print(w)
                
    
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
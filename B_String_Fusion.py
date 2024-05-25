import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;
def insert(trie, word):
    node = trie
    for char in word:
        if char not in node:
            node[char] = {'count': 0}
        node = node[char]
        node['count'] += 1


def search(trie, word):
    node = trie
    for char in word:
        if char not in node:
            return 0
        node = node[char]
    return node['count']

N = ip()
arr = []

for _ in range(N):
    arr.append(cip())

trie = {}
total_length = 0

for word in arr:
    insert(trie, word)
    total_length += len(word)

result = 0

for word in arr:
    cur_node = trie
    cnt = []

    for char in reversed(word):
        if char not in cur_node:
            cnt.append(0)
            break
        
        cur_node = cur_node[char]
        cnt.append(cur_node['count'])

    s = len(word) * N + total_length
    s -= 2 * sum(cnt)
    result += s

print(result)


import sys
import math

INF = int(1e9)

def read():
    global n, c, a
    try:
        n, c = map(int, input().split())
    except:
        return False
    
    a = list(map(int, input().split()))
    return True



def get_cnt(l, r):
    return cntC[r] - cntC[l]

def max_segment(s):
    mx = -INF
    bal = 0
    for i in range(len(s)):
        bal = max(0, bal + s[i])
        mx = max(mx, bal)
    return mx



def solve():
    global cntC, segs, lst
    cntC = [0] * (n + 1)
    for i in range(n):
        cntC[i + 1] = cntC[i] + (a[i] == c)

    cntDif = max(a) + 1

    segs = [[] for _ in range(cntDif)]
    lst = [-1] * cntDif

    for i in range(n):
        segs[a[i]].append(-get_cnt(lst[a[i]] + 1, i))
        lst[a[i]] = i
        segs[a[i]].append(1)
        
    for v in range(cntDif):
        segs[v].append(-get_cnt(lst[v] + 1, n))
    
    ans = 0
    for v in range(cntDif):
        if v == c:
            continue
        ans = max(ans, max_segment(segs[v]))

    print(get_cnt(0, n) + ans)


if __name__ == "__main__":
    if read():
        solve()

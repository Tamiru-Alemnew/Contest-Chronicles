import math
 
 
def solve():
    n, m, q = map(int, input().split())
    arr = []
    dist = dict()
    S = []
    for _ in range(n):
        arr.append(input())
 
    _ = int(input())
    s = input().strip()
 
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 'S':
                S.append((i, j))
            else:
                dist[arr[i][j]] = 0
 
    if len(S) > 0:
        for i in range(n):
            for j in range(m):
                if arr[i][j] != 'S':
                    # sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))
                    mn = min(math.sqrt((pow(i - shift[0], 2) + pow(j - shift[1], 2))) for shift in S)
                    cap = arr[i][j].upper()
                    if mn <= q:
                        dist[cap] = 0
                    elif cap not in dist:
                        dist[cap] = 1
    res = 0
    for el in s:
        if el not in dist:
            print(-1)
            return
        else:
            res += dist[el]
    print(res)
 
    return
 
 
def main():
    # test = int(input())
    # for t in range(test):
    #     solve()
 
    solve()
 
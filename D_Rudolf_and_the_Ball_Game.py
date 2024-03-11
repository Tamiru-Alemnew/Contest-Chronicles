
t = int(input())

for _ in range(t):
    n, m, x = map(int, input().split())
    dxn = []
    d = set([x])
    for _ in range(m):
        r, c = input().split()
        r = int(r)
        dxn.append([r, c])
        
    l = 0
    while d and l < m:
        next_d = set()
        for x in d:
            if dxn[l][1] in {"?", "0"}:
                next_d.add((x + dxn[l][0] - 1) % n + 1)
            if dxn[l][1] in {"?", "1"}:
                next_d.add((x - dxn[l][0] - 1) % n + 1)
        d = next_d
        l += 1
    print(len(d))
    print(*sorted(d))
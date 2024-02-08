x = int(input())

for _ in range(x):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [sorted(r) for r in a]
    s = []
    
    if a == b:
        print("1 1")
    else:
        for j in range(m):
            if any(a[i][j] != b[i][j] for i in range(n)):
                s.append(j)
        if len(s) > 2 :
            print("-1")
        else:
            i, j = s
            for r in a:
                r[i], r[j] = r[j], r[i]
            if a == b:
                print(i + 1, j + 1)
            else:
                print("-1")
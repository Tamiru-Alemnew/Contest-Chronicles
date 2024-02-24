x = int(input())

for _ in range(x):
    n = int(input())
    c = list(map(int, input().split()))
    o = list(map(int, input().split()))
    ans = 0
    mc = min(c)
    mo = min(o)

    for i in range(n):
        temp = max((c[i]-mc) ,(o[i]-mo))
        ans += temp

    print(ans)
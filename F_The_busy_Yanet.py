def help():
    n = int(input())
    a = list(map(int, input().split()))

    mn = 10**9 + 1

    for i in range(n):
        mn = min(mn, a[i])

    ok = False
    c = None

    for i in range(n):
        if a[i] == mn and not ok:
            ok = True
            c = i + 1

        if ok and (a[i] > a[i + 1] if i != n - 1 else False):
            print("-1")
            return

    print(c - 1)


x = int(input())
for _ in range(x):
    help()


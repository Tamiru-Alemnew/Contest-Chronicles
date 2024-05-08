for _ in range(int(input())):
    n , z = map(int , input().split())
    arr = [*map(int , input().split())]

    ans = 0 

    for nm in arr:
        c = nm | z
        ans = max( c, ans)

    print(ans)


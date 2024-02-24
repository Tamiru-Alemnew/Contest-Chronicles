
t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    total0 = sum(1 for x in b if x == 0)
    total1 = n - total0
    ans = 0
    left0 = 0
    for i in range(n):
        if b[i] == 0:
            left0 += 1
        else:
            ans += total0 - left0
    maxi = ans
    left0 = 0
    left1 = 0
    for i in range(n):
        if b[i] == 0:
            newinv = ans - left1 + (total0 - left0 - 1)
            maxi = max(maxi, newinv)
            left0 += 1
        else:
            newinv = ans - (total0 - left0) + left1
            maxi = max(maxi, newinv)
            left1 += 1
    print(maxi)



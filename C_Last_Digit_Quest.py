def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = [0]*10
    for i in range(n):
        cnt[arr[i] % 10] += 1
    vn = []
    for i in range(10):
        for j in range(1, min(cnt[i], 3) + 1):
            vn.append(i)
    s = len(vn)
    for i in range(s):
        for j in range(i + 1, s):
            for k in range(j + 1, s):
                if (vn[i] + vn[j] + vn[k]) % 10 == 3:
                    print("YES")
                    return
    print("NO")

x = int(input())
for _ in range(x):
    solve()
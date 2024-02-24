
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int , input().split()))
    a = [0] * k

    for i in range(n):
        x = arr[i]
        a[i % k] = max(a[i % k], x)

    print(sum(a))


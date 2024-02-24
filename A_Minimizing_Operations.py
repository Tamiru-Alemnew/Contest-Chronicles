x = int(input())

for i in range(x):
    n = int(input())
    arr = list(map(int , input().split()))

    mn = min(arr)
    mx = max(arr)

    print(mx - mn)
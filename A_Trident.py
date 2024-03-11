
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    mini = 0
    for i in range(1, n - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            mini = 1
            print("YES")
            print(i, i + 1, i + 2)
            break
    if not mini:
        print("NO")
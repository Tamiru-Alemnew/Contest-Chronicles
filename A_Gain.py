x = int(input())

for i in range(x):
    n = int(input())

    arr = list(map(int, input().split()))
    sorArr = sorted(arr)

    ans = [0]*n
    for i in range(n):
        if arr[i] == sorArr[-1]:    
            ans[i] = arr[i] - sorArr[-2]
        else:
            ans[i] = arr[i] - sorArr[-1]

    print(*ans)



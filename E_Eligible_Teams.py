x = int(input())

for i in range(x):
    m, n = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    ans = 0 
    l = 1

    for i in range(m):
        if arr[i]*l >= n:
            ans += 1
            l = 1
        else:
            l += 1
    print(ans)

        

        
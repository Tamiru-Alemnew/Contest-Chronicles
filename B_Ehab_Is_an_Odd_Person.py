x = int(input())
arr = list(map(int,input().split()))
for i in range(x):
    for j in range(i+1,x):
        if ((arr[i] + arr[j])/ 2 != 0 )and arr[i] > arr[j]:
            arr[i] , arr[j] = arr[j] , arr[i]

print(*arr)
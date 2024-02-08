x = int(input())
for i in range(x):
    n = int(input())
    arr = list(map(int,input().split()))
    idx = -1
    for j in range(n):
        if arr.count(arr[j]) == 1:
            idx = j
            break
    print(idx+1)
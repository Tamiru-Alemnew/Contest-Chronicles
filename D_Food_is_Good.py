x = int(input())

def kidan (arr):
    n= len(arr)
    mx = 0 
    cur_sum = 0
    flag = False

    for i in range(n):
        if cur_sum <=  0:
            cur_sum = 0  
        cur_sum +=arr[i]
        mx = max(cur_sum , mx)
    return mx


for i in range(x):

    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    ans = 0

    ans = max(kidan(arr[:n-1]),kidan(arr[1:]))


    if total > ans:
        print("YES")
    else:
        print("NO")

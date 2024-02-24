x = int(input())

for i in range(x):
    n =  int(input())
    arr = list(map(int , input().split()))
    l , r = 0 , n -1 

    while l < r:
        if arr[l] == 1 and arr[r] != 1:
            r -= 1

        elif arr[r] == 1 and arr[l] != 1:
            l += 1
        
        elif arr[r] == 1 and arr[l] == 1:
            break
        else:
            l += 1 
            r -= 1

    print(r- l + 1 - sum(arr))




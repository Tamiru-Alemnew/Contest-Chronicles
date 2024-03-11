x = int(input())

for i in range(x):
    n = int(input())
    arr = list(map(int, input().split()))
    
    if arr[0] > arr[1] or arr[n-1] > arr[n-2]:
        print("NO")
        continue

    for i in range(1,n-1):
        if arr[i-0] == 0 :
            continue

        val = arr[i-1] 
        arr[i-1] -= val
        arr[i] -= 2 * val
        arr[i+1] -= val

        if arr[i] < 0 or arr[i+1] < 0:
            print("NO")
            break
    
    else:
        if any(n != 0 for n in arr):
            print("NO")
        else:
            print("YES")


        
        
        
        



            
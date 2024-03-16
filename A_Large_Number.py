x = int(input())
for j in range(x):
    n , m = map(int , input().split())
    arr = list( input())
    l = 0 
    for i in range(n):
        if int(arr[i]) < m:
            new = arr[:i] + [str(m)] + arr[i:]
            print("".join(new))
            break
    
    else:
        arr.append(str(m))
        print("".join(arr))


x = int(input())

for i in range(x):
    n = int(input())
    arr = list(map(int,input().split())) 
    arr.sort()
    cur_sum =0 
    ps = [0]*(n)
    flag = False
    if arr[0] != 1:
        print("NO")
    else:
        for i in range(n):
            cur_sum += arr[0]
            ps[i] += cur_sum


        for i in range(1,n):
            if arr[i] < ps[i-1]:
                print("No")
                break
        else:
            print("YES")

    

        
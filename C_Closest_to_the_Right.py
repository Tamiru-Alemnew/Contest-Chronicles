from bisect import bisect_left
n , m = map(int, input().split())
arr = list(map(int, input().split()))
q = list(map(int, input().split()))

for b in q:
    l , r = 0 ,  n - 1

    while l <= r : 
        md = (l + r )// 2

        if arr[md] < b:
            if  md < n - 1 and arr[md + 1] >= b:
                print(md + 1)
                break
            if md == n-1:
                print(n + 1)
                break
            l = md + 1

        else:
            r = md -1
        

    else:
        print(l+1)



    # print(bisect_left(arr , b) + 1)

from bisect import bisect_left , bisect_right

n , m = map(int , input().split())
arr = list(map(int , input().split()))
q = list(map(int , input().split()))

for b in q :
    # ind = bisect_left(arr , b)
    # if ind < n and arr[ind] == b:
    #     print(bisect_right(arr , b))
    # else:
    #     print(ind)

    l , r = 0 , n-1 

    while l <= r :
        md =(l + r ) // 2 

        if arr[md] > b:
            r = md - 1
        else:
            l = md + 1 

    print(l)







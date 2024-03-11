x = int(input())

for i in range(x):
    a , b , k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort(reverse = True)

    ans = 0 

    l  = 0 

    for n in a:
        if l >= len(b):
            break

        if n + b[l] <= k:
            ans += len(b) - l
        else:
            while l < len(b) and n + b[l] > k:
                l += 1
            ans += len(b) - l

    print(ans)



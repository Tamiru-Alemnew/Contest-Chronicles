n , s = map(int, input().split())
arr = list(map(int,input().split()))

l = 0
cur = 0 
ans = 0 
for r in range(n):
    cur += arr[r]

    while cur > s:
        cur -= arr[l]
        l += 1
    ans += r -l +1

print(ans)
n = int(input())
arr = list(map(int, input().split()))
ans = 0 
arr.sort()
sm = sum(arr)

i = 0 
while sm / n < 4.5:
    ans += 1 
    sm += 5 - arr[i]
    i += 1 

print(ans)



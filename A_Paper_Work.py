x = int(input())
arr = list(map(int,input().split()))
c = 0 
l = 0 
f = 1
ans = []
for i in range(x):
    if arr[i] < 0:
        c += 1 

    if c == 3:
        ans.append(i-l)
        l = i
        f += 1
        c = 0 
    elif i == len(arr) + 1:
        ans.append(i-c)
        f += 1

print(f)
print(*ans)

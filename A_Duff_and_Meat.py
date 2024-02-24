x = int(input())
ans = 0
min_p = 1000000000
for i in range(x):
    m , p = map(int, input().split())
    min_p = min(min_p , p)
    ans += m * min_p

print(ans)


    
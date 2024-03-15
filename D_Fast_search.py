from bisect import bisect_left , bisect_right
x = int(input())
arr = list(map(int , input().split()))
n = int(input())
ans = []
arr.sort()

for i in range(n):
    n , m = map(int , input().split())
    l = bisect_left(arr , n)
    r = bisect_right(arr , m)
    ans.append(r - l )

print(*ans)
n , m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
count = 0
l , r = 0 , 0
while l < n and r < m :
    if a[l] < b[r]:
        l += 1
    elif a[l] > b[r]:
        r += 1
    else:
        count_a = 0
        while l < n and a[l] == a[l - count_a]:
            count_a += 1
            l += 1
        count_b = 0
        while r < m and b[r] == b[r - count_b]:
            count_b += 1
            r += 1
        count += count_a * count_b
print(count)
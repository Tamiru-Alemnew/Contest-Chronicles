from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
f = defaultdict(int)
j = n - 1

while j >= 0:
    if f[a[j]] >= 1:
        break
    f[a[j]] += 1
    j -= 1

m = float('inf')
for i in range(n):
    m = min(m, j - i + 1)
    f[a[i]] += 1

    while f[a[i]] >= 2 and j < n - 1:
        j += 1
        f[a[j]] -= 1

    if f[a[i]] >= 2:
        break

print(m)

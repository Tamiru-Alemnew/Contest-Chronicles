from collections import defaultdict

x  = int(input())

for _ in range(x):
    n = int(input())
    t = [int(x) for x in input().split()]
    diff_counts = defaultdict(int)
    for i in range(n):
        diff = i - t[i]
        diff_counts[diff] += 1
    count = sum(val * (val - 1) // 2 for val in diff_counts.values())
    print(count)
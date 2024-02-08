n = int(input())
arr = list(map(int, input().split()))
 
counter = {}
ans, itr = 0, 0

for v in arr:
    counter[v] = counter.get(v, 0) + 1

while len(counter) > 1:
    itr += 1
    counter = {k: v - 1 for k, v in counter.items()}
    ans += len(counter)
    counter = {k: v for k, v in counter.items() if v > 0}

print(ans - itr)
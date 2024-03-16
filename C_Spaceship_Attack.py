from bisect import bisect_right
from collections import defaultdict
n , m = map(int , input().split())
arr = list(map(int , input().split()))

ps = {}

for i in range(m):
    d , g = map(int , input().split())
    if d not in ps:
        ps[d] = 0
    ps[d] += g

keys = sorted(ps.keys())
for i in range(1, len(keys)):
    ps[keys[i]] += ps[keys[i-1]]

ans = []

for a in arr:
    if a in ps:
        ans.append(ps[a])
    else:
        ind = bisect_right(keys , a)
        if ind == 0:
            ans.append(0)
        else:
            ans.append(ps[keys[ind-1]])
        
print(*ans)
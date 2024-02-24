from collections import defaultdict
n , s = map(int , input().split())
arr = list(map(int , input().split()))

freq = defaultdict(int)
unique = 0 
l = 0 
ans = 0 

for r in range(n):
    if freq[arr[r]] == 0 :
        unique += 1
    freq[arr[r]] += 1

    while unique > s :
        if freq[arr[l]] == 1:
            unique -= 1
        
        freq[arr[l]] -= 1
        l += 1

    ans += r - l +1 

print(ans )



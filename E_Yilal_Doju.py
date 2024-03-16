from collections import defaultdict

def calculate_ta(h, l):
    t1 = max(h , l)
    t2 = min(h, l)
    ta = 0
    while t1 > (t2 // 2):
        t1 -= 2
        t2 -= 1
        ta += 1
    ta += t2 // 2
    return ta

n = int(input())
arr = list(map(int , input().split()))
ind = defaultdict(int)
ans = float("inf")

for i in range(0 ,n-2):
    ta = calculate_ta(arr[i], arr[i+1])
    ans = min(ta , ans)
    ta = calculate_ta(arr[i], arr[i+2])
    ans = min(ta , ans)
    ta = calculate_ta(arr[i+1], arr[i+2])
    ans = min(ta , ans)


t1 = max(arr[0] , arr[1])
t2 = min(arr[0] , arr[1])
ta = calculate_ta(t1, t2)
ans = min(ta , ans)

t1 = max(arr[-1] , arr[-2])
t2 = min(arr[-1] , arr[-2])
ta = calculate_ta(t1, t2)
ans = min(ta , ans)
arr.sort()
t1 = arr[0]
t2 = arr[1]

ta = 0 

ta += t1 //2 
ta += t2 // 2
ta += t1 % 2
ta += t2 % 2

ans = min(ta , ans)

print(ans)
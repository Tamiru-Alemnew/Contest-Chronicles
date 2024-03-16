x = int(input())
arr = list(map(int , input().split()))
m =  int(input())
ps = []
for i in range(len(arr)):
    for j in range(arr[i]):
        ps.append(i)

w = list(map(int , input().split()))

for p in w:
    print(ps[p-1]+1)
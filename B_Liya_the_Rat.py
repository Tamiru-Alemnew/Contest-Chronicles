w = input()
n = int(input())
ps=[0]*(len(w)+1)

for j in range(1,len(w)):
    ps[j] += w[j-1] == w[j] 
    ps[j] += ps[j-1]


for l in range(n):
    s , e = map(int , input().split())
    c = 0 
    c = ps[e-1] - ps[s-1]
    print(c)
        


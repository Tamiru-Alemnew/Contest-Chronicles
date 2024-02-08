from collections import defaultdict
x = int(input())

for i in range(x):
    n , m = map(int , input().split())
    matr = []
    right = defaultdict(int)
    left = defaultdict(int)
    ma = 0 
    for i in range(n):
        matr.append(list(map(int , input().split())))
    for i in range(n):
        for j in range(m):
            right[i + j ] += matr[i][j]
    for i in range(n):
        for j in range(m):
            left[i - j ] += matr[i][j]
    for i in range(n):
        for j in range(m):
            ma = max(right[i + j] + left[i-j] - matr[i][j] , ma)
    
    print(ma)
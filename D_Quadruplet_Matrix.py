from collections import defaultdict
from collections import Counter
x = int(input())


for i in range(x):
    n = int(input())
    matr = []
    ans = defaultdict(list)
    for i in range(n):
        matr.append(list(input()))
    for i in range(n):
        for j in range(n):
            ans[(i , j )].append(matr[i][j])
    # 90 degree
    nine  = list(zip(*matr[::-1]))
    for i in range(n):
        for j in range(n):
            ans[(i , j )].append(nine[i][j])

    # 180 degree
    one = list(zip(*nine[::-1]))
    for i in range(n):
        for j in range(n):
            ans[(i , j )].append(one[i][j])
    # 270 degree
    three= list(zip(*one[::-1]))
    for i in range(n):
        for j in range(n):
            ans[(i , j )].append(three[i][j])
    
    c = 0 
    for i in range(n):
        for j in range(n):
            for i , j , k , m in  zip(*ans[(i , j )]):
                count = Counter(list((i , j , k , m )))
                print(count[0])
                c += min(count[0],count[1])
    
    print(c)

     


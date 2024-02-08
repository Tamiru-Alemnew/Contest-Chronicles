
x = int(input())
matrix = []
for i in range(x):
    matrix.append(list(map(int, input().split())))

total = 0
mid = x // 2

for i in range(x):
    total += matrix[i][i] 
    total += matrix[i][x - i - 1]  
    total += matrix[mid][i]  
    total += matrix[i][mid]  

if x % 2 == 1:
    total -= 3 * matrix[mid][mid]

print(total)
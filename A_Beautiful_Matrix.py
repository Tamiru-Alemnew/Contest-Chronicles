matrix = []

for _ in range(5):
    single_line = list(map(int, input().split())) 
    matrix.append(single_line)

for r in range(5):
    for c in range(5):
        if matrix[r][c] == 1:
            print(abs(r - 2) + abs(c -2))

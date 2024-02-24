x = int(input())

for i in range(x):
    n = int(input())
    grid = []
    for i in range(n):
        row = list(input())
        grid.append(row)
    flag = False
    found = False
    for r in range(n-1):
        for c in range(len(grid[0])-1):
            if grid[r][c] == "1":
                if grid[r+1][c]=="1" and grid[r][c+1]=="1":
                    flag = True
                found = True
                break
        if found:
            break
    if flag:
        print("SQUARE")
    else:
        print("TRIANGLE")


    
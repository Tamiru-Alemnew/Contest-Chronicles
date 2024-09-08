def min_moves(x, y, k):
    moves_x = (x + k - 1) // k  
    moves_y = (y + k - 1) // k  
    if moves_x > moves_y:
        return 2*moves_x -1
    return 2*moves_y


t = int(input())
for _ in range(t):
    x, y, k = map(int, input().split())
    print(min_moves(x, y, k))

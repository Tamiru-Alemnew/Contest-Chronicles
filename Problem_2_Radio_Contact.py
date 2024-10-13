
INF = int(1e9) + 7
MX = 1001

# Directions: N, E, S, W
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# Movement map
md = {'N': 0, 'E': 1, 'S': 2, 'W': 3}

# Square of a number
def sq(a):
    return a * a

# Distance squared between two points
def dist(a, b):
    return sq(a[0] - b[0]) + sq(a[1] - b[1])

# Main function
def main():
    # Read input
    with open("radio.in", "r") as f:
        N, M = map(int, f.readline().split())
        fx, fy = map(int, f.readline().split())
        bx, by = map(int, f.readline().split())
        jS = f.readline().strip()
        bS = f.readline().strip()

    # Locations for Farmer John and Bessie
    jl = [(fx, fy)]  # Farmer John's initial position
    bl = [(bx, by)]  # Bessie's initial position

    # Calculate Farmer John's path
    for i in range(N):
        move = md[jS[i]]
        new_pos = (jl[-1][0] + dx[move], jl[-1][1] + dy[move])
        jl.append(new_pos)

    # Calculate Bessie's path
    for i in range(M):
        move = md[bS[i]]
        new_pos = (bl[-1][0] + dx[move], bl[-1][1] + dy[move])
        bl.append(new_pos)

    # DP table
    dp = [[INF] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 0

    # Fill the DP table
    for i in range(N + 1):
        for j in range(M + 1):
            if i < N:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + dist(jl[i + 1], bl[j]))
            if j < M:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + dist(jl[i], bl[j + 1]))
            if i < N and j < M:
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + dist(jl[i + 1], bl[j + 1]))

    # Output the result
    with open("radio.out", "w") as f:
        f.write(f"{dp[N][M]}\n")

# Entry point
if __name__ == "__main__":
    main()

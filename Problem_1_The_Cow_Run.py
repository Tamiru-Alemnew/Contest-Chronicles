# Read input
n = int(input())
positions = [int(input()) for _ in range(n)]

# Sort the positions of the cows
positions.sort()


dp = [[[float('inf')] * 2 for _ in range(n)] for _ in range(n)]

# Fill the base cases where there is only one cow in the range
for i in range(n):
    dp[i][i][0] = abs(positions[i]) * n  # If we visit only the i-th cow from the start
    dp[i][i][1] = abs(positions[i]) * n  # Same, but ending at the same position

for length in range(1, n):  # length is the size of the range
    for i in range(n - length):
        j = i + length  # j is the right endpoint

        # Calculate the number of cows left to visit
        remaining_cows = n - (j - i)

        # Transition if we come from the left side (positions[i])
        dp[i][j][0] = min(dp[i + 1][j][0] + (positions[i + 1] - positions[i]) * remaining_cows,  # Going left to left
                          dp[i + 1][j][1] + (positions[j] - positions[i]) * remaining_cows)    # Going right to left

        # Transition if we come from the right side (positions[j])
        dp[i][j][1] = min(dp[i][j - 1][1] + (positions[j] - positions[j - 1]) * remaining_cows,  # Going right to right
                          dp[i][j - 1][0] + (positions[j] - positions[i]) * remaining_cows)    # Going left to right

result = min(dp[0][n - 1][0], dp[0][n - 1][1])

print(result)


# 1. Read a single integer
n = int(input())  # Example: 5

# 2. Read multiple space-separated integers
a, b, c = map(int , input().split())  # Example: 3 4 5


# 3. Read a list of space-separated integers
arr = list(map(int, input().split()))  # Example: 1 2 3 4 5


# 4. Read multiple lines of input
m = int(input())  # Read first integer
arr2 = list(map(int, input().split()))  # Read m integers

# 5. Read multiple test cases
t = int(input())  # Number of test cases
for _ in range(t):
    x = int(input())  
    arr3 = list(map(int, input().split())) 


# 6. Read a string input
s = input()  # Example: hello


# 7. Read a tuple (same as multiple integers)
x, y = map(int, input().split())  # Example: 10 20


# 8. Read a matrix (grid of numbers)
r, c = map(int, input().split())  
matrix = [list(map(int, input().split())) for _ in range(n)]  # Read n lines

matrix = []
for _ in range(r):
    single_line = list(map(int, input().split())) 
    matrix.append(single_line)

# fast input
import sys
data = sys.stdin.read().split()

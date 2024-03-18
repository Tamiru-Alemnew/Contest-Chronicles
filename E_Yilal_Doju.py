import math

N = int(input())
arr = list(map(int, input().split()))

def smallest(arr):
    i = j = float('inf')
    for num in arr:
        if num < i:
            j = i
            i = num
        elif num < j:
            j = num

    return i, j

a, b = smallest(arr)
cost = math.ceil(a / 2) + (math.ceil(b / 2))

def do(a, b):
    if math.ceil(b / 2) >= a:
        return math.ceil(b / 2)
    
    x = math.ceil((2*a - b) / 3)
    return x + abs(math.ceil((b - x) / 2))

def check(idx):
    l_m = m_r = l_r = float("inf")
    
    if idx - 1 >= 0:
        l_m = do(arr[idx], arr[idx - 1])
    
    if idx + 1 < N:
        m_r = do(arr[idx], arr[idx + 1])
        
    if idx - 1 >= 0 and idx + 1 < N:
        a, b = sorted([arr[idx - 1], arr[idx + 1]])
        l_r = a + math.ceil((b - a) / 2)
        
    return min(l_m, m_r, l_r)

for idx, num in enumerate(arr):
    cost = min(cost, check(idx))

print(cost)
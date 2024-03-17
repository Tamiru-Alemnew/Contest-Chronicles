num_cases = int(input())

for i in range(num_cases):
    total, limit = map(int , input().split())
    if limit >= total-1:
        print(1)
    else:
        print(total)
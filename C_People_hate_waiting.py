x = int(input())
arr = list(map(int , input().split()))
n = len(arr)
cur_sum = 0 
arr.sort()
num = 0 

for i in range(n):
    if cur_sum > arr[i]:
        pass
    else:
        cur_sum += arr[i]
        num +=1

print(num)


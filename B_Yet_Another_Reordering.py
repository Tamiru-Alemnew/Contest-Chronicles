N = int(input())
arr = list(map(int, input().split()))
arr.sort()
left = 0

for right in range(N):
    if arr[right] > arr[left]:
        left += 1
       
print(left)
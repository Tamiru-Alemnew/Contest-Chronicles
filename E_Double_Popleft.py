from collections import deque

n, q = map(int, input().split())
nums = list(map(int, input().split()))

queue = deque(nums)
max_num = max(nums)
max_index = nums.index(max_num)
ans = []

while True:
    a = queue.popleft()
    b = queue.popleft()
    if a > b:
        queue.append(b)
        queue.appendleft(a)
    else:
        queue.append(a)
        queue.appendleft(b)
    ans.append((a, b))
    if queue[0] == max_num:
        break

for _ in range(q):
    x = int(input())
    if x <= len(ans):
        print(ans[x - 1][0], ans[x - 1][1])
    else:
        val = (x - len(ans)) % (n - 1)
        if val == 0:
            print(max_num, queue[-1])
        else:
            print(max_num, queue[val])


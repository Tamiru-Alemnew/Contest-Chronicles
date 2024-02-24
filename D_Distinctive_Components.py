t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))


    count = 0
    for num in a:
        left = 0
        run_sum = 0
        for right in range(n):
            run_sum += a[right]
            while run_sum > num:
                run_sum -= a[left]
                left += 1           
            if run_sum == num and left < right:
                count += 1
                break
   
    print(count)
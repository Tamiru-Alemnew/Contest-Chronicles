t = int(input().strip())

for _ in range(t):

    n, k = map(int, input().strip().split())
    
    result = ['a'] * n
    

    start = 1
    summation = 1
    while summation < k:
        start += 1
        summation += start
        if summation >= k:
            summation -= start
            break
    
    k -= summation
    
    result[start] = 'b'
    
    ind2 = 0
    if k > 0:
        ind2 = k - 1
    result[ind2] = 'b'
    
    final = ''.join(result[::-1])
    print(final)


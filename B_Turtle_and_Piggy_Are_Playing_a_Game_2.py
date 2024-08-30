def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        a.sort()
        # turn = 0 
        
        # while len(a) > 1:
        #     if turn == 0:
        #         a[0] = max(a[0], a[1])
        #     else:
        #         a[0] = min(a[0], a[1])
        #     a.pop(1)
        #     turn = 1 - turn
        
        results.append(a[n//2])
    
    for result in results:
        print(result)


solve()
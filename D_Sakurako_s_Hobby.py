def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        p = list(map(int, data[index:index + n]))
        index += n
        s = data[index]
        index += 1
        
        p = [x - 1 for x in p]

        visited = [False] * n
        f = [0] * n
        
        for i in range(n):
            if not visited[i]:

                cycle = []
                x = i
                

                while not visited[x]:
                    visited[x] = True
                    cycle.append(x)
                    x = p[x]
                

                black_count = sum(1 for idx in cycle if s[idx] == '0')
                

                for idx in cycle:
                    f[idx] = black_count
        
        results.append(' '.join(map(str, f)))
    

    print('\n'.join(results))

solve()
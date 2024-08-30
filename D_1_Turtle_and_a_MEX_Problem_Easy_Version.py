def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    results = []
    index = 1
    t = int(data[0])
    
    for _ in range(t):
        n, m = map(int, data[index].split())
        index += 1
        
        mex_set = set()
        for i in range(n):
            li = list(map(int, data[index].split()))
            index += 1
            mex_set.add(min(set(range(li[0]+1)) - set(li[1:])))
        
        mex_list = sorted(mex_set)
        sum_f = 0
        current_f_value = 0
        
        for mex_value in mex_list:
            if mex_value > m:
                break
            sum_f += current_f_value * (mex_value - current_f_value)
            current_f_value = mex_value
            
        if current_f_value <= m:
            sum_f += current_f_value * (m - current_f_value + 1)
        
        results.append(sum_f)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')
solve()
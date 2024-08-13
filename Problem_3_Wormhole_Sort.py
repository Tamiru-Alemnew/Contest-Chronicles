import sys
from collections import defaultdict
from math import inf

def main():
    with open('wormsort.in', 'r') as fin:
        data = fin.read().split()
    
    index = 0
    n = int(data[index])
    m = int(data[index + 1])
    index += 2
    
    arr = list(map(int, data[index:index + n]))
    index += n
    
    graph = defaultdict(list)
    
    for i in range(m):
        a = int(data[index])
        b = int(data[index + 1])
        w = int(data[index + 2])
        index += 3
        graph[a].append((b, w))
        graph[b].append((a, w))
    
    query = set()
    for i, v in enumerate(arr):
        if i + 1 != v:
            if (v, i + 1) not in query:
                query.add((i + 1, v))
    
    ans = inf
    
    for a, b in query:
        visited = set()
        
        def dfs(s, e):
            if s == e:
                return True
            
            if s in visited:
                return False
            
            visited.add(s)
            cur = -inf
            
            for neighbor, w in graph[s]:
                if dfs(neighbor, e):
                    cur = max(cur, w)
            
            return cur
        
        ans = min(dfs(a, b), ans)
    
    with open('wormsort.out', 'w') as fout:
        if ans == inf:
            fout.write('-1\n')
        else:
            fout.write(f'{ans}\n')

if __name__ == "__main__":
    main()
import heapq

def min_mean_path(n, m, edges):
    
    low, high = 0.0, 100.0
    epsilon = 1e-7
    answer_path = []
    
    def is_valid_path(mid):
        
        pq = [(0.0, 1, 0, [])]
        
        dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]
        dist[1][0] = 0.0
        
        while pq:
            d, node, edge_count, path = heapq.heappop(pq)
            path = path.copy()
            path.append(node)
            
            if node == n:
                nonlocal answer_path
                answer_path = path
                return True

            for nei, cost in graph[node]:
                new_dist = d + (cost - mid)
                new_edge_count = edge_count + 1

                if new_edge_count <= n and new_dist < dist[nei][new_edge_count]:
                    dist[nei][new_edge_count] = new_dist
                    heapq.heappush(pq, (new_dist, nei, new_edge_count, path))
        
        return False


    graph = [[] for _ in range(n + 1)]
    for a, b, c in edges:
        graph[a].append((b, c))


    while high - low > epsilon:
        mid = (low + high) / 2
        answer_path = []
        if is_valid_path(mid):
            high = mid
        else:
            low = mid

    k = len(answer_path) - 1
    print(k)
    print(' '.join(map(str, answer_path)))


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]


min_mean_path(n, m, edges)

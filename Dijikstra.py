import heapq

def dijikstra(graph, src, n):
    dist = [float('inf')] *n
    dist[src] = 0
    pq = [(0, src)]

    while pq:
        
        d,u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, weight in graph[u]:
            if dist[u]+weight<dist[v]:
                dist[v] = dist[u]+weight
                
                    
n =5
graph = {
    0: [(1, 10), (3, 5)],
    1: [(2, 1),  (3, 2)],
    2: [(4, 4)],
    3: [(1, 3),  (2, 9), (4, 2)],
    4: [(2, 6),  (0, 7)]
}

distance = dijikstra(graph, 0, n)
for i, d in enumerate(distance):
    print(f"vertex 0 -> {i} : {d}")
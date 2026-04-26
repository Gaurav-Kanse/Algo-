import heapq

def prim(g, n):
    vis = [0]*n
    pq = [(0, 0)]
    total = 0
    
    while pq:
        w,u = heapq.heappop(pq)
        
        if vis[u]:
            continue
        vis[u] =1
        total+=w
        
        for v, wt in g[u]:
            if not vis[v]:
                heapq.heappush(pq, (wt,v))
                
    return total

g = {
    0: [(1,2),(3,6)],
    1: [(0,2),(2,3),(3,8),(4,5)],
    2: [(1,3),(4,7)],
    3: [(0,6),(1,8),(4,9)],
    4: [(1,5),(2,7),(3,9)]
}

print("Total Cost:", prim(g, 5))
        
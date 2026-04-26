def kruskals(n, edges):
    edges.sort()
    parent = list(range(n))
    rank = [0]*n
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union (x,y):
        px,py = find(x), find(y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        
        if rank[px] ==rank[py]:
            rank[px] +=1
        return True
            
    mst = []
    total = 0
    for w,u,v in edges:
        if union(u,v):
            mst.append((u,v,w))
            total +=1
    return mst, total

n = 4
edges = [(10, 0, 1), (6, 0, 2), (5, 0, 3), (15, 1, 3), (4, 2, 3)]
mst, cost = kruskals(n, edges)
print("MST Edges:")
for u, v, w in mst:
    print(f"  {u} - {v} : {w}")
print("Total Cost:", cost)
def dfs_connected(graph, n):
    visited = [False] *n
    
    def dfs(v):
        visited[v] = True
        for nei in graph.get(v, []):
            if not visited[nei]:
                dfs(nei)
    dfs(0)
    return all(visited)

g1 = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}     # connected
g2 = {0: [1],    1: [0],    2: [3], 3: [2]}      # disconnected
print("Graph 1 connected:", dfs_connected(g1, 4))
print("Graph 2 connected:", dfs_connected(g2, 4))
    
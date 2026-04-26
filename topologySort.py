def topoSort(graph, n):
    visited = [False] *n
    result=[]
    
    def dfs(node):
        visited [node] = True
        for nie in graph.get(node, []):
            if not visited[nie]:
                dfs(nie)
        result.append(node)
                
    for i in range(n):
        if not visited[i]:
            dfs(i)
    return result[::-1]

graph = {5:[2,0], 4:[0,1], 2:[3], 3:[1]}
print(topoSort(graph, 6))
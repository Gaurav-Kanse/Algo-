from collections import deque

def bfs(graph ,start, n):
    visited = [False] *n
    visited[start] = True
    queue = deque([start])
    reachable =[]
    
    while queue:
        node  = queue.popleft()
        reachable.append(node)
        for nei in graph.get(node,[]):
            if not visited[nei]:
                visited[nei] = True
                queue.append(nei)
    return reachable

graph = {0: [1, 2], 1: [0, 3], 2: [0, 4], 3: [1], 4: [2]}
print("BFS Reachable from 0:", bfs(graph, 0, 5))
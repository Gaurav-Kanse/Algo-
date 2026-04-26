def subset_sum(S,target):
    res = []
    
    def dfs(i,path,total):
        if total == target:
            res.append(path[:])
            return
        if i == len(S) or total > target:
            return
        
        dfs(i+1, path + [S[i]], total+S[i])
        dfs(i+1, path, total)
        
    dfs(0, [], 0)
    return res

print(subset_sum([1,2,5,6,8], 9))
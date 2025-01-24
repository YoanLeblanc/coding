class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        s = set()
        m = [0]*n
        def dfs(i):
            if m[i] == 1 or len(graph[i]) == 0:
                m[i] = 1
                return True
            elif m[i] == -1 or i in s:
                m[i] = -1
                s.add(i)
                return False
            else:
                s.add(i)
                if all([dfs(j) for j in graph[i]]):
                    m[i] = 1
                    return True
                else:
                    m[i] = -1
                    return False
        for i in range(n):
            dfs(i)
        return [i for i in range(n) if m[i] == 1]
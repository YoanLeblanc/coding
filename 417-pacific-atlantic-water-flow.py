class Solution:
    def voisin_non_visite(self, i, j, n, m, visited, heights):
        h = heights[i][j]
        r = []
        if i > 0 and (i-1,j) not in visited and h <= heights[i-1][j]:
            r.append((i-1,j))
        if j > 0 and (i,j-1) not in visited and h <= heights[i][j-1]:
            r.append((i,j-1))
        if i < n-1 and (i+1,j) not in visited and h <= heights[i+1][j]:
            r.append((i+1,j))
        if j < m-1 and (i,j+1) not in visited and h <= heights[i][j+1]:
            r.append((i,j+1))
        return r
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pacific = {(i,j) for i,j in zip([int(i/m) for i in range(n*m)], list(range(m))*n) if i == 0 or j == 0}
        atlantic = {(i,j) for i,j in zip([int(i/m) for i in range(n*m)], list(range(m))*n) if i == n-1 or j == m-1}
        visited_atlantic = set()
        queue_atlantic = list(atlantic)
        while len(queue_atlantic) > 0:
            x = queue_atlantic.pop()
            if x not in visited_atlantic:
                queue_atlantic += self.voisin_non_visite(x[0],x[1], n, m, visited_atlantic, heights)
            visited_atlantic.add(x)
        visited_pacific = set()
        queue_pacific = list(pacific)
        while len(queue_pacific) > 0:
            x = queue_pacific.pop()
            if x not in visited_pacific:
                queue_pacific += self.voisin_non_visite(x[0],x[1], n, m, visited_pacific, heights)
            visited_pacific.add(x)
        return [x for x in visited_pacific if x in visited_atlantic] 
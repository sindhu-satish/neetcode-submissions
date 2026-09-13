class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        visited = set()


        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r, c))
            res = 1

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (nr < 0 or nr == rows or nc < 0 or nc == cols or grid[nr][nc] == 0 or (nr, nc) in visited):
                        continue
                    
                    visited.add((nr,nc))
                    q.append((nr, nc))
                    res += 1
            return res
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_area = max(max_area, bfs(r,c))

        return max_area
                
                
        
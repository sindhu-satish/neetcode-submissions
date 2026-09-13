class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr in range(rows) and nc in range(cols) and ((nr, nc) not in visited and grid[nr][nc] == "1"):
                        q.append((nr,nc))
                        visited.add((nr, nc))


        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    visited.add((r,c))
                    bfs(r,c)
                    islands += 1


        return islands


        
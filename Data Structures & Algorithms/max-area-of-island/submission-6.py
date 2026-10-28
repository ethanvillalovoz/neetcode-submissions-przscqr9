class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        visit = set()

        def bfs(r, c):
            visit.add((r, c))
            q = collections.deque()
            q.append((r, c))
            area = 1
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 and (nr, nc) not in visit:
                        visit.add((nr, nc))
                        q.append((nr, nc))
                        area += 1

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = bfs(r, c)
                    maxArea = max(maxArea, area)

        return maxArea
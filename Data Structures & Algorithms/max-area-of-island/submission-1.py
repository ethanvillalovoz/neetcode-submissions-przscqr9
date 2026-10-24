class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        res = 0

        def bfs(r, c) -> int:
            visit.add((r, c))
            q = collections.deque()
            q.append((r, c))
            area = 1

            while q:
                row, col = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 and (nr, nc) not in visit:
                        q.append((nr, nc))
                        visit.add((nr, nc))
                        area += 1

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = bfs(r, c)
                    res = max(res, area)

        return res
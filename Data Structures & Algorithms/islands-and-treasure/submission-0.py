class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        q = collections.deque()
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dist = 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] != 0 and grid[nr][nc] != -1 and grid[nr][nc] > dist:
                        grid[nr][nc] = dist
                        q.append((nr, nc))

            dist += 1

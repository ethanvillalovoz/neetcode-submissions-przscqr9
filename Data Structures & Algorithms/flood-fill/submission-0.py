class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if image[sr][sc] == color:
            return image

        m, n = len(image), len(image[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c, org):
            if not (0 <= r < m) or not (0 <= c < n) or image[r][c] != org:
                return

            image[r][c] = color

            for dr, dc in directions:
                dfs(r+dr, c+dc, org)

        dfs(sr, sc, image[sr][sc])

        return image
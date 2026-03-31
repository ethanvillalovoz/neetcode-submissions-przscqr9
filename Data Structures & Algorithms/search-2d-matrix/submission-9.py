class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix:
            return False
        
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS*COLS - 1

        while l <= r:
            m = (l+r) // 2

            i = m // COLS
            j = m % COLS

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                l = m + 1
            else:
                r = m - 1

        return False
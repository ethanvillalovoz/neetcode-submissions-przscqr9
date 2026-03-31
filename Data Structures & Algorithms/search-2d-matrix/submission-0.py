class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, (m*n)-1

        while l <= r:
            m  = (l + r) // 2
            i = m // n
            j = m % n

            mid = matrix[i][j]

            if target == mid:
                return True
            elif target < mid:
                r = m - 1
            else:
                l = m + 1

        return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = m * n - 1

        while i <= j:
            mid = (i + j) // 2
            x = mid // n
            y = mid % n
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                i = mid + 1
            else:
                j = mid - 1
        return False

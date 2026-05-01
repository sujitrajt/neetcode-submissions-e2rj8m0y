class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        left = 0 
        right = (row * col) - 1
        while left <= right:
            middle = (left + right ) // 2
            i = middle // col
            j = middle % col 

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                right = middle - 1
            else:
                left = middle + 1
        return False
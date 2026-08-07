class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, cols = len(matrix), len(matrix[0])

        for r in range(rows):
            if target in matrix[r]:
                for c in range(cols):
                    if matrix[r][c] == target:
                        return True
            if matrix[r][0] > target:
                return False
        return False
                    

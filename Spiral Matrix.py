class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        
        m, n = len(matrix), len(matrix[0])
        result = []
        top, bottom, left, right = 0, m - 1, 0, n - 1
        
        while top <= bottom and left <= right:
            # Traverse from left to right along the top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            
            # Traverse from top to bottom along the right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                # Traverse from right to left along the bottom row
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                # Traverse from bottom to top along the left column
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result

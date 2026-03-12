class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        
        while matrix:
            # top
            ans += matrix.pop(0)

            # right
            if matrix and matrix[0]:
                for row in matrix:
                    ans.append(row.pop())
            
            # bottom
            if matrix:
                ans += matrix.pop()[::-1]
            
            # left
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ans.append(row.pop(0))

        return ans

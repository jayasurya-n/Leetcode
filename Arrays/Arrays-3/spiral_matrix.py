class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m =  len(matrix)
        n = len(matrix[0])
        ans = []
        top = 0
        bottom = m-1
        left = 0
        right = n-1
        
        while(top<=bottom and left<=right):
            # right
            for j in range(left,right+1):
                ans.append(matrix[top][j])
            top+=1

            # bottom
            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right-=1

            if(top<=bottom):
                # left
                for j in range(right,left-1,-1):
                    ans.append(matrix[bottom][j])
                bottom-=1
            
            if(left<=right):
                # top
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])
                left+=1
        return ans
            



m,n = [int(i) for i in input().strip().split()]
matrix = [[int(i) for i in input().strip().split()] for i in range(m)]
obj = Solution()
print(obj.spiralOrder(matrix))

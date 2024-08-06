class Solution:
    
    
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        
        i = 0
        j = n-1

        while(i<=m-1 and j>=0):
            if(matrix[i][j]==target):return True
            if(matrix[i][j]>target):j-=1
            else:i+=1

        return False
        pass
        



m,n, target = [int(i) for i in input().strip().split()]
matrix = []
for i in range(n):
    matrix.append([int(i) for i in input().strip().split()])
obj = Solution()
print(obj.searchMatrix(matrix,target))

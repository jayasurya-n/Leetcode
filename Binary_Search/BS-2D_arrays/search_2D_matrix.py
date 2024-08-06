class Solution:
    
    
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m*n-1

        while(low<=high):
            mid = (low+high)//2
            i,j = mid//n,mid%n
            if(matrix[i][j]==target):return True
            if(matrix[i][j]<target):low = mid+1
            else:high = mid-1
        
        return False

        pass
        



m,n, target = [int(i) for i in input().strip().split()]
matrix = []
for i in range(n):
    matrix.append([int(i) for i in input().strip().split()])
obj = Solution()
print(obj.searchMatrix(matrix,target))

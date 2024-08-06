class Solution:

    def findMax(self,matrix,m,mid):
        max = -1
        index = -1
        for i in range(m):
            if(max<matrix[i][mid]):
                max = matrix[i][mid]
                index = i
        
        return index

    def findPeakGrid(self, matrix: list[list[int]]) -> list[int]:
        
        m = len(matrix)
        n = len(matrix[0])

        low = 0
        high = n-1

        while(low<=high):
            mid = (low+high)//2
            row = self.findMax(matrix,m,mid)

            left = matrix[row][mid-1] if mid-1>=0 else -1
            right = matrix[row][mid+1] if mid+1<n else -1
            middle = matrix[row][mid]

            if(middle > left and middle > right):
                return [row,mid]
            
            if(middle<left):high = mid-1
            else:low = mid+1

            
        pass
        



m,n = [int(i) for i in input().strip().split()]
matrix = []
for i in range(n):
    matrix.append([int(i) for i in input().strip().split()])
obj = Solution()
print(obj.findPeakGrid(matrix))

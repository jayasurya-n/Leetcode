class Solution:

    def upperBound(self,arr,target):
        n = len(arr)
        low = 0 
        high = n-1
        ans = n
        while(low<=high):
            mid = (low+high)//2

            if(arr[mid]>target):
                ans = mid
                high = mid-1
            else:low = mid+1

        return ans


    def findElementsLesser(self,matrix,R,C,target):
        cnt = 0
        for i in range(R):
            cnt += self.upperBound(matrix[i],target)
        return cnt


    def median(self, matrix, R, C):
        low = float('inf')
        high = float('-inf')

        for i in range(R):
            low = min(low,matrix[i][0])
            high = max(high,matrix[i][C-1])

        required = R*C//2

        
        ans = -1
        while(low<=high):
            mid = (low+high)//2
            elements = self.findElementsLesser(matrix,R,C,mid)

            if(elements<=required):low = mid+1
            else:high = mid-1
        
        return low

        pass
        



m,n = [int(i) for i in input().strip().split()]
matrix = []
for i in range(n):
    matrix.append([int(i) for i in input().strip().split()])
obj = Solution()
print(obj.median(matrix,m,n))

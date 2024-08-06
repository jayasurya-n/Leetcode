class Solution:

    def lowerBound(self,arr,m,target):
        low = 0
        high = m-1
        ans = m

        while(low<=high):
            mid = (low+high)//2

            if(arr[mid]>=target):
                ans = mid
                high = mid-1
            else:low = mid+1
        
        return ans
    
    
    def rowWithMax1s(self,matrix, n, m):
        
        max_ones = 0
        row = -1
        for i in range(n):
            cnt_ones = m - self.lowerBound(matrix[i],m,1)
            if(cnt_ones > max_ones):
                max_ones = cnt_ones
                row = i

        return row
        pass
        



n,m = [int(i) for i in input().strip().split()]

matrix = []
for i in range(n):
    matrix.append([int(i) for i in input().strip().split()])
obj = Solution()
print(obj.rowWithMax1s(matrix,n,m))

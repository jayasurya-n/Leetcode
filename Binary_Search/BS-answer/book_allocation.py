class Solution:


    def canMaxPages(self,arr,n,m,maxSum):
        
        student = 1
        sum = 0
        for i in range(n):
            if(sum+arr[i]>maxSum):
                student+=1
                sum = 0
            sum+=arr[i]
        
        if(student<=m):
            return True
        return False
              
            




    def findPages(self,arr: [int], n: int, m: int) -> int:

    # Write your code here
    # Return the minimum number of pages
        low = max(arr)
        high = sum(arr)

        if(m>n):return -1

        ans = 1e9+1
        while(low<=high):
            mid = (low+high)//2

            if(self.canMaxPages(arr,n,m,mid)):
                ans = min(ans,mid)
                high = mid-1
            else:low = mid+1

        return ans
        pass
        




            


       



n,m = [int(i) for i in input().strip().split()]
arr = [int(i) for i in input().strip().split()]
obj = Solution()
print(obj.findPages(arr,n,m))
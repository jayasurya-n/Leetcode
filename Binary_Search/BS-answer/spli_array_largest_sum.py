class Solution:


    def canMaxSum(self,arr,k,maxSum):
        
        subarray = 1
        sum = 0
        for i in range(len(arr)):
            if(sum+arr[i]>maxSum):
                subarray+=1
                sum = 0
            sum+=arr[i]
        
        if(subarray<=k):
            return True
        return False
              
            

    def splitArray(self, arr: list[int], k: int) -> int:

        low = max(arr)
        high = sum(arr)

        if(k>len(arr)):return -1

        ans = 1e9+1
        while(low<=high):
            mid = (low+high)//2

            if(self.canMaxSum(arr,k,mid)):
                ans = min(ans,mid)
                high = mid-1
            else:low = mid+1

        return ans
        pass
        




            


       



k = int(input())
arr = [int(i) for i in input().strip().split()]
obj = Solution()
print(obj.splitArray(arr,k))
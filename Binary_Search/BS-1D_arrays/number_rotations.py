class Solution:
    def findKRotation(self,arr,n):
        # code here
        
        low = 0
        high = n-1
        ans = 1e8
        index = -1
        while(low<=high):
            mid = (low+high)//2

            # left sorted
            if(arr[low]<=arr[mid]):
                ans = min(ans,arr[low])
                if(ans==arr[low]):index=low
                low = mid+1
            elif(arr[mid]<=arr[high]):
                ans = min(ans,arr[mid])
                if(ans==arr[mid]):index=mid
                high = mid-1
                
        return index


    
nums = [int(x) for x in input().strip().split()]
obj = Solution()
print(obj.findKRotation(nums,len(nums)))
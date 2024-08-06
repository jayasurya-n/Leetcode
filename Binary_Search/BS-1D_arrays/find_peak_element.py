class Solution:
    def findPeakElement(self, arr: list[int]) -> int:
        
        n = len(arr)
        
        if(n==1):return 0
        if(arr[0]>arr[1]):return 0
        if(arr[n-1]>arr[n-2]):return n-1

        low = 1
        high = n-2

        while(low<=high):
            mid = (low+high)//2
            if(arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]):
                return mid
            
            # left side
            elif(arr[mid]>arr[mid-1]):
                low = mid+1
            # right side
            else:
                high = mid-1
                


    
nums = [int(x) for x in input().strip().split()]
obj = Solution()
print(obj.findPeakElement(nums))
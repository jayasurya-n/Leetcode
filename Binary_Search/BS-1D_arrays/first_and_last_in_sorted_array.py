class Solution:
    def searchRange(self, arr: list[int], x: int) -> list[int]:
        
        n = len(arr)
        low = 0
        high = n-1
        first = -1
        
        while(low<=high):
            mid = (low+high)//2
            if(arr[mid]==x):
                first = mid
                high = mid-1
            elif(arr[mid]>x):
                high = mid-1
            else:
                low = mid+1

        
        low = 0
        high = n-1
        second = -1
        while(low<=high):
            mid = (low+high)//2 
            if(arr[mid]==x):
                second = mid
                low = mid+1
            elif(arr[mid]>x):
                high = mid-1
            else:
                low = mid+1
        
        if(first==-1):return [-1,-1]
        return first,second
    
    pass


        


            




x = int(input())
nums = [int(x) for x in input().strip().split()]
obj = Solution()
print(obj.searchRange(nums,x))
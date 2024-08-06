class Solution:
    def singleNonDuplicate(self, arr: list[int]) -> int:
        
        n = len(arr)
        low = 0
        high = n-1

        if(n==1):return arr[0]
        if(arr[0]!=arr[1]):return arr[0]
        if(arr[n-1]!=arr[n-2]):return arr[n-1]

        while(low<=high):
            mid = (low+high)//2
            # left side
            if(arr[mid]!=arr[mid-1] and arr[mid]!=arr[mid+1]):
                return arr[mid]
            
            # if(mid%2==0):
            #     if(arr[mid]==arr[mid-1]):
            #         high = mid-1
            #     else:
            #         low = mid+1
            
            # else:
            #     if(arr[mid]==arr[mid-1]):
            #         low = mid+1
            #     else:
            #         high = mid-1

            if ((mid%2==0 and arr[mid]==arr[mid+1]) or (mid%2==1 and arr[mid]==arr[mid-1])):
                low = mid+1
            
            else:high = mid-1


    
nums = [int(x) for x in input().strip().split()]
obj = Solution()
print(obj.singleNonDuplicate(nums))
class Solution:
    def search(self, arr: list[int], x: int) -> int:
        
        
        n = len(arr)
        low = 0
        high = n-1
        ans = -1
        
        while(low<=high):
            mid = (low+high)//2
            if(arr[mid]==x):
                ans = mid 
                break
            

            if(arr[mid]==arr[low] and arr[mid]==arr[high]):
                low = low+1
                high = high-1
                continue
            # left sorted
            if(arr[mid]>=arr[low]):
                if(arr[low]<=x<=arr[mid]):
                    high = mid-1
                
                else:
                    low = mid+1
                pass
            
            # right sorted
            if(arr[mid]<=arr[high]):
                if(arr[mid]<=x<=arr[high]):
                    low = mid+1
                else:
                    high = mid-1
                pass
        
        return ans!=-1


        


            




x = int(input())
nums = [int(x) for x in input().strip().split()]
obj = Solution()
print(obj.search(nums,x))
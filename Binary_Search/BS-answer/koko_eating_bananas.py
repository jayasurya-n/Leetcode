import math
class Solution:

    def time(self,piles,mid):
        ans = 0
        for i in piles:
            ans+=math.ceil(i/mid)
        return ans

    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        low = 1
        high = max(piles)
        ans = 1e8

        while(low<=high):
            mid = (low+high)//2
            
            if(self.time(piles,mid)<=h):
                ans = min(mid,ans)
                high = mid-1
            else:
                low = mid+1

        return ans    



    
h = int(input())
nums = [int(i) for i in input().strip().split()]
obj = Solution()
print(obj.minEatingSpeed(nums,h))
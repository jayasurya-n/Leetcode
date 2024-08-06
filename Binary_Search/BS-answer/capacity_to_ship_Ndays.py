import math
class Solution:

    def daysRequired(self,weights,maxWeight):
        days = 1
        sum = 0
        for i in weights:
            if(sum+i>maxWeight):
                sum = i
                days+=1
            else:sum+=i    
        return days

    def shipWithinDays(self, weights: list[int], days: int) -> int:

        low = max(weights)
        high = sum(weights)
        
        ans = 1e8

        while(low<=high):
            mid = (low+high)//2
            print(self.daysRequired(weights,mid),mid)
            if(self.daysRequired(weights,mid)<=days):
                ans = min(mid,ans)
                high = mid-1
            else:
                low = mid+1

        return ans  


    

days = int(input())
weights = [int(i) for i in input().strip().split()]
obj = Solution()
print(obj.shipWithinDays(weights,days))
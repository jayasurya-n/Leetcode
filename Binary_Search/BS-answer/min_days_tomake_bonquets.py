class Solution:
    
    def m_bouquets(self,bloomDay,m,k,mid):
        
        bouquets = 0
        cnt = 0

        for i in range(0,len(bloomDay)):
            if(bloomDay[i]<=mid):cnt+=1
            else:cnt=0

            if(cnt==k):
                bouquets+=1
                cnt = 0

        if(bouquets>=m):return True
        else: return False 

        
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:

        if(m*k>len(bloomDay)):
            return -1
         
        low = min(bloomDay)
        high = max(bloomDay)
        ans = 1e9+1

        while(low<=high):
            mid = (low+high)//2
            if(self.m_bouquets(bloomDay,m,k,mid)):
                ans = min(ans,mid)
                high = mid-1
            else:
                low = mid+1
            

        return ans    



    

m,k = [int(i) for i in input().strip().split()]
nums = [int(i) for i in input().strip().split(",")]
obj = Solution()
print(obj.minDays(nums,m,k))
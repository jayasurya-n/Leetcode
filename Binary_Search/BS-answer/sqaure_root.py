
#Complete this function
class Solution:
    def floorSqrt(self, n): 
    #Your code here
        low = 1
        high = n
        ans = -1

        while(low<=high):
            mid = (low+high)//2

            if(mid*mid<=n):
                ans = mid
                low = mid+1
            else:
                high = mid-1

        return ans    



    
num = int(input())
obj = Solution()
print(obj.floorSqrt(num))
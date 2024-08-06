class Solution:
    
    def power(self,mid,n,m):
        ans = 1
        for i in range(1,n+1):
            if(ans>m):
                return m+1
            ans*=mid
        return ans


    
    def NthRoot(self, n, m):
        # Code here
        low = 1
        high = m
        ans = -1

        while(low<=high):
            mid = (low+high)//2

            value = self.power(mid,n,m)
            if(value==m):
                ans = mid
                break
            elif(value<m):
                low = mid+1
            else:
                high = mid-1
        
        return ans

n,m = [int(x) for x in input().strip().split()]
obj = Solution()
print(obj.NthRoot(n,m))
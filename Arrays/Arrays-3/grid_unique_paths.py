class Solution:

    def combination(self,n,r):
        ans = 1
        for i in range(1,r+1):
            ans*=n-i+1
            ans/=i
        return int(ans)
        
    def uniquePaths(self, m: int, n: int) -> int:
        # m-1+n-1 C n-1
        if(m<n):
            return self.combination(m+n-2,m-1)
        return self.combination(m+n-2,n-1)
        



m,n = [int(i) for i in input().strip().split()]
obj = Solution()
print(obj.uniquePaths(m,n))

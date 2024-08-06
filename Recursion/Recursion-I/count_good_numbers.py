class Solution:
    mod = int(1e9+7)

    def binaryExponent(self,x,y,mod):
        ans = 1
        while(y):
            if(y%2==1):
                ans = (x*ans)%mod
                y-=1
            x = (x*x)%mod
            y//=2
        return ans

    def countGoodNumbers(self, n: int) -> int:
        odd = n//2
        even = (n+1)//2
        
        ans = (self.binaryExponent(4,odd,self.mod)*self.binaryExponent(5,even,self.mod))%self.mod
        return ans







n = int(input())
print(Solution().countGoodNumbers(n))
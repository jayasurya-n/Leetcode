class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if(n==0):return 1
        elif(n<0):
            x = 1/x
            n = -n

        ans = 1
        while(n>0):
            if(n%2==1):
                ans = ans*x
                n-=1
            else:
                x = x*x 
                n//=2
        
        return ans

        
        pass




x,n = [int(i) for i in input().strip().split()]
obj = Solution()
print(obj.myPow(x,n))
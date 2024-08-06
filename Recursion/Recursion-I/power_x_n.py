class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if(n==0):return 1
        elif(n<0):
            x = 1/x
            n = -n

        ans = 1
        while(n):
            if(n%2==1):
                ans = x*ans
                n-=1
            x = x*x 
            n//=2
        return ans



x,n = list(map(float,input().strip().split()))
print(Solution().myPow(x,n))
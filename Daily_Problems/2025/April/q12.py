from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

def factorial(n):
    fac = [1]*(n+1)
    for i in range(1,n+1):
        fac[i] = fac[i-1]*i
    return fac[n]

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # def rec(i,num):
        #     if(i==(n+1)//2):
        #         s = "".join(num)
        #         if(n%2==0):s+=s[::-1]
        #         else:s+=s[::-1][1:]
        #         if(int(s)%k==0):self.hash.add("".join(sorted(s)))
        #         return 
            
        #     if(i==0):
        #         for digit in range(1,10):
        #             num.append(str(digit))
        #             rec(i+1,num)
        #             num.pop()
        #     else:       
        #         for digit in range(0,10):
        #             num.append(str(digit))
        #             rec(i+1,num)
        #             num.pop()
        
        # self.hash = set()
        # rec(0,[])
        # ans = 0
        
        # for s in self.hash:
        #     freq = [0]*10
        #     for ch in s:freq[int(ch)]+=1
        #     cnt = (n-freq[0])*factorial(n-1)
        #     for i,f in enumerate(freq):cnt//=factorial(f)
        #     ans+=cnt
        # return ans
        
        start = 10**((n-1)//2)
        hash = set()
        
        for num in range(start,10*start):
            s = str(num)
            if(n%2==0):s+=s[::-1]
            else:s+=s[::-1][1:]
            if(int(s)%k==0):hash.add("".join(sorted(s)))

        ans = 0    
        for s in hash:
            freq = [0]*10
            for ch in s:freq[int(ch)]+=1
            cnt = (n-freq[0])*factorial(n-1)
            for i,f in enumerate(freq):cnt//=factorial(f)
            ans+=cnt
        return ans

# time complexity: O(nlogn*10^(n/2)),O(nlogn*10^(n/2))
# space complexity: O(n*10^(n/2)),O(n*10^(n/2))
if __name__ == "__main__":
    for _ in range(ii()):
        n,k = lii()
        print(Solution().countGoodIntegers(n,k))
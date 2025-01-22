from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def sieve(self):
        n = 10**6
        #smallest prime factor dividing i(spf)
        self.spf = list(range(n+1)) 
        for i in range(2,int(n**0.5)+1):
            if(self.spf[i]==i):  
                for j in range(i*i,n+1,i):
                    if(self.spf[j]==j):self.spf[j] = i 
        
    def findPrimeFactors(self, n):
        prime_factorization = []
        while(n!=1):
            spf = self.spf[n]
            prime_factorization.append(spf)
            n//=spf
        return prime_factorization

# time complexity: O(nloglogn+q*logn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))
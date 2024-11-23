from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def isPrime(n):
            if(n<=1):return False
            for i in range(2,int(n**0.5)+1):
                if(n%i==0):return False
            return True
        
        prevPrimes = [0]*(max(nums)+1)
        for i in range(2,len(prevPrimes)):
            if(isPrime(i)):prevPrimes[i]=i
            else:prevPrimes[i] = prevPrimes[i-1]
        
        for i in range(len(nums)):
            limit = nums[i]
            if(i>0):limit-=nums[i-1]
            if(limit<=0):return False
            nums[i]-= prevPrimes[limit-1]
        return True
                
# time complexity: O(n+m^1.5)
# space complexity: O(m)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))
from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def countPrimes(self, n: int) -> int:
        if(n<=1):return 0
        primes = [True]*(n+1)
        primes[0]=primes[1]=False
        for i in range(2,int(n**0.5)+1):
            if(primes[i]):  
                for j in range(i*i,n+1,i):primes[j] = False            
        return sum([1 for num in primes if num==True])

# time complexity: O(nloglogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))
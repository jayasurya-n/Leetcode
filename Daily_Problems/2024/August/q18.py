from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    # def nthUglyNumber(self, n: int):
    #     min_heap = []
    #     hash = set()
        
    #     heapq.heappush(min_heap,1)
    #     hash.add(1)
        
    #     primes = [2,3,5]
    #     ugly = 1
        
    #     for i in range(n):
    #         ugly = heapq.heappop(min_heap)
    #         for p in primes:
    #             next_ugly = ugly*p
    #             if(next_ugly not in hash):
    #                 hash.add(next_ugly)
    #                 heapq.heappush(min_heap,next_ugly)
        
    #     return ugly

    def nthUglyNumber(self, n: int):
        ugly_numbers = [0]*n
        ugly_numbers[0] = 1
        
        # index multiple of 2,3,5
        i2,i3,i5 = 0,0,0
        
        # next multiple of 2,3,5
        n2,n3,n5 = 2,3,5
        
        for i in range(1,n):
            next_ugly = min(n2,n3,n5)
            ugly_numbers[i] = next_ugly
            
            if(next_ugly==n2):
                i2+=1
                n2 = ugly_numbers[i2]*2
            
            if(next_ugly==n3):
                i3+=1
                n3 = ugly_numbers[i3]*3
            
            if(next_ugly==n5):
                i5+=1
                n5 = ugly_numbers[i5]*5
        
        return ugly_numbers[-1]

# time complexity: O(nlogn), O(n)
# space complexity: O(m), O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))
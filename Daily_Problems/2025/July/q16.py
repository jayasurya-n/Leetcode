from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd_zero = odd_one = 0
        even_zero = even_one = 0

        for num in nums:
            if(num%2==1):
                odd_zero+=1
                odd_one = even_one+1
            else:
                even_zero+=1
                even_one = odd_one+1
        
        return max(odd_one,odd_zero,even_one,even_zero)

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))
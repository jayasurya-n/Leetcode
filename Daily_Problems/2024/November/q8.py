from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor = 0
        for num in nums:xor^=num
        maxi = (1<<maximumBit)-1
        ans = []
        
        for i in range(n-1,-1,-1):
            ans.append(maxi^xor)
            xor^=nums[i]
        return ans

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))
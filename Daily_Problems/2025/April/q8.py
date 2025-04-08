from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n+2)//3
        rem = n%3
        
        hash = set()
        for i in range(rem):
            if(nums[n-i-1] in hash):return total
            hash.add(nums[n-i-1])
        
        cnt = 1 if rem else 0
        
        for i in range(n-1-rem,-1,-3):
            for j in range(3):
                if(nums[i-j] in hash):return total-cnt
                hash.add(nums[i-j])
            cnt+=1
        return total-cnt

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))
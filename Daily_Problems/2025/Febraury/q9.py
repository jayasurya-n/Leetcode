from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        hash = defaultdict(int)
        for i,num in enumerate(nums):
            hash[num-i]+=1
        
        ans = n*(n-1)//2
        for val in hash.values():ans-=(val*(val-1))//2
        return ans

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))
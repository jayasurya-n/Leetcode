from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # hash =defaultdict(int)
        # for num in nums:hash[num]+=1
        
        # for num,freq in hash.items():
        #     if(freq%2==1):return False
        # return True
        
        nums.sort()
        for i in range(0,len(nums),2):
            if(nums[i]!=nums[i+1]):return False
        return True

# time complexity: O(n),O(nlogn)
# space complexity: O(n),O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))
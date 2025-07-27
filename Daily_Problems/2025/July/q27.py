from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        temp = [nums[0]]
        for i in range(1,n):
            if(nums[i]==nums[i-1]):continue
            temp.append(nums[i])
        
        ans = 0
        for i in range(1,len(temp)-1):
            if(temp[i]>temp[i-1] and temp[i]>temp[i+1]):ans+=1
            elif(temp[i]<temp[i-1] and temp[i]<temp[i+1]):ans+=1
        
        return ans

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))
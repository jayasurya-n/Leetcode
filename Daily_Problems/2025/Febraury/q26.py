from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # pos = [0] 
        # neg = [0]
        
        # ans = curr = 0
        # for num in nums:
        #     curr+=num
        #     if(curr>=0):ans = max(ans,curr-neg[0])
        #     if(curr<=0):ans = max(ans,abs(curr+pos[0]))
        #     if(curr>0):heapq.heappush(pos,-curr)
        #     elif(curr<0):heapq.heappush(neg,curr)
        
        # return ans
        
        pos = neg = 0
        ans = curr = 0
        for num in nums:
            curr+=num
            if(curr>=0):ans = max(ans,curr-neg)
            if(curr<=0):ans = max(ans,abs(curr-pos))
            pos = max(pos,curr)
            neg = min(neg,curr)
        return ans

# time complexity: O(nlogn),O(n)
# space complexity: O(n),O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))
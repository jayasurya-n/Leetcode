from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        hash = set(nums)
        ans = 0
        for ele in nums:
            temp = ele
            cnt = 0
            while(temp in hash):
                cnt+=1
                temp *= temp
            ans = max(ans,cnt)
        return ans if ans>=2 else -1

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))
from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def longestSubsequence(self, n, nums):
        ans = []
        for num in nums:
            pos = bisect.bisect_left(ans,num)
            if(pos==len(ans)):ans.append(num)
            else:ans[pos]=num
        return len(ans)
    
# time complexity: O(nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))
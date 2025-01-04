from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxi_left = values[0]
        ans=0
        
        for j in range(1,len(values)):
            ans = max(ans,maxi_left+values[j]-j)
            maxi_left = max(maxi_left,values[j]+j)
        return ans

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))
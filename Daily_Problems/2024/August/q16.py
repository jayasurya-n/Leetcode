from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def maxDistance(self, arrays: List[List[int]]):
        n = len(arrays)
        maxi = arrays[0][-1]
        mini = arrays[0][0]
        
        ans = -1
        for i in range(1,n):
            small,large = arrays[i][0],arrays[i][-1] 
            ans = max(ans,abs(large-mini),abs(maxi-small))
            mini = min(mini,small)
            maxi = max(maxi,large)
        return ans


# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arrays = [list(map(int,input().strip().split())) for _ in range(n)]
        print(Solution().maxDistance(arrays))
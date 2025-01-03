from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        prefix_max = arr[:]
        suffix_min = arr[:]
        
        for i in range(1,n):prefix_max[i] = max(prefix_max[i-1],arr[i])
        for i in range(n-2,-1,-1):suffix_min[i] = min(suffix_min[i+1],arr[i])
        
        chunks = 0
        for i in range(n-1):
            if (suffix_min[i+1]>prefix_max[i]):chunks+=1
        return chunks+1
        
        # n = len(arr)
        # stack = []
        # for i in range(n):
        #     if(not stack or stack[-1]<arr[i]):stack.append(arr[i])
        #     else:
        #         maxi = stack[-1]
        #         while stack and stack[-1]>arr[i]:stack.pop()
        #         stack.append(maxi)
        # return len(stack)
            
# time complexity: O(n),O(n)
# space complexity: O(n),O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))
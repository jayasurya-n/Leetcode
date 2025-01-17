from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque([root])
        
        ans = []
        while q:
            size = len(q)
            sum = 0
            for _ in range(size):
                node = q.popleft()
                sum+=node.val
                if(node.left):q.append(node.left)
                if(node.right):q.append(node.right)
            ans.append(sum)
        
        ans.sort(reverse=True)
        return ans[k-1]
                
# time complexity: O(n+logn(loglogn))
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))
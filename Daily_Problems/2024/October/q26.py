from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        height = defaultdict(int)
        depth = defaultdict(int)
        maxHeight1 = defaultdict(int)
        maxHeight2 = defaultdict(int)
        
        def dfs(node,d):
            if(node==None):return 0
            l = dfs(node.left,d+1)
            r = dfs(node.right,d+1)
            depth[node.val] = d
            h = 1+max(l,r)
            height[node.val] = h
            if(maxHeight1[d]<h):
                maxHeight2[d] = maxHeight1[d]
                maxHeight1[d] = h
            else:
                maxHeight2[d] = max(maxHeight2[d],h)
            return h
        
        dfs(root,0)
        ans = []
        for val in queries:
            d = depth[val]
            if(maxHeight1[d]==height[val]):ans.append(d-1+maxHeight2[d])
            else:ans.append(d-1+maxHeight1[d])
        return ans
            
# time complexity: O(n+q)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))
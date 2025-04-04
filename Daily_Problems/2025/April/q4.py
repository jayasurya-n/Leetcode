from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # def depth(node):
        #     if(not node):return 0
        #     l = depth(node.left)
        #     r = depth(node.right)
        #     return 1+max(l,r)

        # maxd = depth(root)
        
        # def dfs(node,d):
        #     if(not node or d==maxd):return node
        #     l = dfs(node.left,d+1)
        #     r = dfs(node.right,d+1)
        #     if(l and r):return node
        #     return l if not r else r
        
        # return dfs(root,1) 
        
        def dfs(node):
            if(not node):return 0,None
            l = dfs(node.left)
            r = dfs(node.right)
            if(l[0]>r[0]):return l[0]+1,l[1]
            elif(l[0]<r[0]):return r[0]+1,r[1]
            else:return l[0]+1,node
        return dfs(root)[1]
            

# time complexity: O(n),O(n)
# space complexity: O(n),O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))
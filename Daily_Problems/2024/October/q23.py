from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depths = [0]*(10**5)
        def dfs(node,d):
            if(node==None):return
            depths[d]+=node.val
            dfs(node.left,d+1)
            dfs(node.right,d+1)
        dfs(root,0)
        
        def modify(node,d,childSum):
            if(node==None):return 
            node.val = depths[d]-childSum
            sum = 0
            if(node.left):sum+=node.left.val
            if(node.right):sum+=node.right.val
            modify(node.left,d+1,sum)
            modify(node.right,d+1,sum)
        
        modify(root,0,root.val)
        return root
        
# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))
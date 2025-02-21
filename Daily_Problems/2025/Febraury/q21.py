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
        
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.hash = set()
        self.dfs(root,0)
    
    def dfs(self,node,val):
        self.hash.add(val)
        if(node.left):self.dfs(node.left,2*val+1)
        if(node.right):self.dfs(node.right,2*val+2)

    def find(self, target: int) -> bool:
        return target in self.hash

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))
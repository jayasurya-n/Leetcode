from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def check(node1,node2):
            if(node1==None and node2==None):return True
            if(not node1 or not node2 or (node1.val!=node2.val)):return False
            
            return ((check(node1.left,node2.left) and check(node1.right,node2.right)) or 
                    (check(node1.left,node2.right) and check(node1.right,node2.left)))
        
        return check(root1,root2)
                
# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))
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
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        def create(start,end,post_start):
            if(start>end):return None
            
            node = TreeNode(preorder[start])
            if(start==end):return node
            
            left = preorder[start+1]
            left_nodes = 1
            while(postorder[post_start+left_nodes-1]!=left):left_nodes+=1
            
            node.left = create(start+1,start+left_nodes,post_start)
            node.right = create(start+1+left_nodes,end,post_start+left_nodes)
            return node
        
        return create(0,n-1,0)

# time complexity: O(n^2)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))
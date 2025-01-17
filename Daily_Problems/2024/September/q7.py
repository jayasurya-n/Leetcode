from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(node,temp):
            if(temp==None):return True
            if(node==None):return False
            if(node.val!=temp.val):return False
            return dfs(node.left,temp.next) or dfs(node.right,temp.next)
            
        def check(node,temp):
            if(node==None):return False
            if(dfs(node,temp)):return True
            return check(node.left,temp) or check(node.right,temp)
        
        return check(root,head)
            
# time complexity: O(n*m)
# space complexity: O(n(stack space))
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))
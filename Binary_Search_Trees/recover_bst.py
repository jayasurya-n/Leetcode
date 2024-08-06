from typing import List,Optional
from collections import deque
import sys

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while(root):
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        if(self.stack==[]):return None
        node = self.stack.pop()
        temp = node.right

        while(temp):
            self.stack.append(temp)
            temp = temp.left
        return node
        

class Solution:
    # def recoverTree(self, root: Optional[TreeNode]):
    #     obj = BSTIterator(root)
    #     cur = obj.next()

    #     node1,node2 = None,None
    #     prev = None
    #     while(cur):
    #         prev = cur
    #         cur = obj.next()
    #         if(cur):
    #             if(node1==None and cur.val<prev.val):
    #                 node1 = prev
    #                 node2 = cur
    #             elif(node1 and cur.val<prev.val):
    #                 node2 = cur
    #     node1.val,node2.val = node2.val,node1.val

    def recoverTree(self, root):
        self.node1,self.node2 = None,None
        def dfs(node):
            if(node==None):return
            dfs(node.left)
            if(self.node1==None and node.val<self.prev.val):
                self.node1 = self.prev
                self.node2 = node
            elif(self.node1 and node.val<self.prev.val):self.node2 = node
            self.prev = node
            dfs(node.right)

        self.prev = TreeNode(-sys.maxsize)
        dfs(root)
        self.node1.val,self.node2.val = self.node2.val,self.node1.val
            
        
# time complexity: O(n),O(n)
# space complexity: O(h),O(n(stack space))
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))
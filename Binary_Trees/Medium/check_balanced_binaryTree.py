from typing import List,Optional
from collections import deque
import sys
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def createBinrayTree(self,i,root,arr):
        if(i>=len(arr)):return None

        if(arr[i]=='None'): return None
        root = TreeNode(arr[i])
        root.left = self.createBinrayTree(2*i+1,root.left,arr)
        root.right = self.createBinrayTree(2*i+2,root.right,arr)
        return root

    def printBinaryTree(self,root):
        if(root!=None):
            print(root.val)
            self.printBinaryTree(root.left)
            self.printBinaryTree(root.right)

class Solution:
    def dfs(self,root):
        if(root==None):return 0

        lh = self.dfs(root.left)
        if(lh==-1):return -1

        rh = self.dfs(root.right)
        if(rh==-1):return -1
        
        if(abs(lh-rh)>1):return -1
        return 1+max(lh,rh)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)!=-1

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = input().strip().split()
        for i in range(len(arr)):
            if(arr[i]!="None"):arr[i]=int(arr[i])
        root = BinaryTree().createBinrayTree(0,None,arr)
        print(Solution().isBalanced(root))
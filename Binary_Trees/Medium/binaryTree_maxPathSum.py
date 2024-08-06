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
    def pathSum(self,root,ans):
        if(root==None):return 0
        lpath = self.pathSum(root.left,ans)
        rpath = self.pathSum(root.right,ans)
        ans[0] = max(ans[0],root.val+max(0,lpath,rpath,lpath+rpath))
        return root.val+max(0,lpath,rpath)
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [-sys.maxsize]
        self.pathSum(root,ans)
        return ans[0]


# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = input().strip().split()
        for i in range(len(arr)):
            if(arr[i]!="None"):arr[i]=int(arr[i])
        root = BinaryTree().createBinrayTree(0,None,arr)
        print(Solution().maxPathSum(root))
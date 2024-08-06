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
    def isSumProperty(self, root):
        if(root.left==None and root.right==None):
            return 1
            
        sum = 0
        if(root.left):sum+=root.left.val
        if(root.right):sum+=root.right.val
        if(root.val!=sum):return 0

        if(root.left):
            if(self.isSumProperty(root.left)==0):return 0

        if(root.right):
            if(self.isSumProperty(root.right)==0):return 0

        return 1


# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = input().strip().split()
        for i in range(len(arr)):
            if(arr[i]!="None"):arr[i] = int(arr[i])
        root = BinaryTree().createBinrayTree(0,None,arr)
        print(Solution().isSumProperty(root))
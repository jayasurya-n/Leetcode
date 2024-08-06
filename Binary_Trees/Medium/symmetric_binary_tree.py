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
    # def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    #     if(root==None):return True

    #     q = deque([root])
    #     while(q):
    #         size = len(q)
    #         temp = []
    #         for _ in range(size):
    #             node = q.popleft()
    #             if(node==None):temp.append("None")
    #             else:temp.append(node.val)
    #             if(node):
    #                 q.append(node.left)
    #                 q.append(node.right)
    #         if(temp!=temp[::-1]):return False
    #     return True
    def checkSymmetric(self,left,right):
        if(left==None or right==None):return (left==right)

        if(left.val!=right.val):return False

        return (self.checkSymmetric(left.left,right.right) and 
        self.checkSymmetric(left.right,right.left))

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return (root==None or self.checkSymmetric(root.left,root.right))
        

# time complexity: O(n),O(n)
# space complexity: O(n),O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = input().strip().split()
        for i in range(len(arr)):
            if(arr[i]!="None"):arr[i]=int(arr[i])
        root = BinaryTree().createBinrayTree(0,None,arr)
        print(Solution().rightSideView(root))
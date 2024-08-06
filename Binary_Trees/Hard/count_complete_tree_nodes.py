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
    def leftHeight(self,node):
        lh = 0
        while(node):
            node = node.left
            lh+=1
        return lh    
    
    def rightHeight(self,node):
        rh = 0
        while(node):
            node = node.right
            rh+=1
        return rh   

    def countNodes(self, node: Optional[TreeNode]):
        lh = self.leftHeight(node)
        rh = self.rightHeight(node)
        if(lh==rh):return 2**lh-1
        return 1+self.countNodes(node.left)+self.countNodes(node.right)


# time complexity: O((logn)**2)
# space complexity: O(logn(stack space))
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))
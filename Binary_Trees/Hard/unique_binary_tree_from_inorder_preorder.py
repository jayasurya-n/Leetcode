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
    def buildTree(self, preorder: List[int], inorder: List[int]):
        map = dict()
        for i in range(len(inorder)):
            map[inorder[i]] = i

        def build(preorder,inorder,p1,p2,i1,i2):
            if(p1>p2):return None
            node = TreeNode(preorder[p1])
            ind = map[preorder[p1]]
            l = ind-i1
            node.left = build(preorder,inorder,p1+1,p1+l,i1,ind-1)
            node.right = build(preorder,inorder,p1+l+1,p2,ind+1,i2)
            return node
        
        root = build(preorder,inorder,0,len(preorder)-1,0,len(inorder)-1)
        return root

# time complexity: O(n)
# space complexity: O(n+n(stack space))
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        preorder = list(map(int,input().strip().split()))
        inorder = list(map(int,input().strip().split()))
        root = Solution().buildTree(preorder,inorder)
        BinaryTree().printBinaryTree(root)
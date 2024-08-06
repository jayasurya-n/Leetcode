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
    # def findPath(self,root,node,path):
    #     if(root==None):return False
    #     path.append(root.val)
    #     if(root.val==node):
    #         return True
        
    #     if(self.findPath(root.left,node,path) or 
    #        self.findPath(root.right,node,path)):
    #         return True

    #     path.pop()
    #     return False

    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
    #     a,b = [],[]
    #     self.findPath(root,p,a)
    #     self.findPath(root,q,b)

    #     for i in range(min(len(a),len(b))):
    #         if(a[i]!=b[i]):return a[i-1]

    #     return a[-1] if(len(a)<len(b)) else b[-1]

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        if(root==None or root==p or root==q):
            return root

        l = self.lowestCommonAncestor(root.left,p,q)
        r = self.lowestCommonAncestor(root.right,p,q)

        if(l==None):return r
        elif(r==None):return l
        return root
        

# time complexity: O(n), O(n)
# space complexity: O(n), O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = input().strip().split()
        for i in range(len(arr)):
            if(arr[i]!="None"):arr[i] = int(arr[i])
        root = BinaryTree().createBinrayTree(0,None,arr)
        p,q = list(map(int,input().strip().split()))
        print(Solution().lowestCommonAncestor(root,p,q))
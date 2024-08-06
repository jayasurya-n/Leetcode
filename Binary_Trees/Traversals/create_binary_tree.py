from typing import List,Optional
import sys

class TreeNode:
    def __init__(self, val, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

class Solution:
    def createTree(self,i,root,arr):
        if(i>=len(arr)):return None

        root = TreeNode(arr[i])
        root.left = self.createTree(2*i+1,root.left,arr)
        root.right = self.createTree(2*i+2,root.right,arr)
        return root

    def printTree(self,root):
        if(root!=None):
            print(root.val)
            self.printTree(root.left)
            self.printTree(root.right)
        

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = list(map(int,input().strip().split()))
        root = None
        root = Solution().createTree(0,root,arr)
        Solution().printTree(root)
from typing import List,Optional
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
    def postorder(self,root,ans):
        if(root==None):return 
        self.postorder(root.left,ans)
        self.postorder(root.right,ans)
        ans.append(root.val)
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.postorder(root,ans)
        return ans



# time complexity: O(n)
# space complexity: O(n(max height of the tree))
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = input().strip().split()
        for i in range(len(arr)):
            if(arr[i]!="None"):arr[i] = int(arr[i]) 
        root = BinaryTree().createBinrayTree(0,None,arr)
        print(Solution().postorderTraversal(root))
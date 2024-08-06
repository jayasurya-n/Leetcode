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

    def createBinrayTree(self,arr):
        if(arr==[] or arr[0]=='None'):return None
        root = TreeNode(int(arr[0]))
        q = deque([root])
        i = 1
        while(q):
            node = q.popleft()
            if(i<len(arr)):
                if(arr[i]!='None'):
                    node.left = TreeNode(int(arr[i]))
                    q.append(node.left)
                i+=1
            if(i<len(arr)):
                if(arr[i]!='None'):
                    node.right = TreeNode(int(arr[i]))
                    q.append(node.right)
                i+=1
        return root

def printBinaryTree(root):
    if(root==None):return
    print(root.val)
    printBinaryTree(root.left)
    printBinaryTree(root.right)


class Solution:
    # def isValidBST(self, root: Optional[TreeNode]):
    #     inorder = []
    #     def dfs(node):
    #         if(node==None):return
    #         dfs(node.left)
    #         inorder.append(node.val)
    #         dfs(node.right)
        
    #     dfs(root)
    #     for i in range(1,len(inorder)):
    #         if(inorder[i]<=inorder[i-1]):
    #             return False
    #     return True

    def isValidBST(self, root: Optional[TreeNode]):
        def dfs(node,l,r):
            if(node==None):return True
            if(l>=node.val or node.val>=r):return False
            return dfs(node.left,l,node.val) and dfs(node.right,node.val,r)
        
        return dfs(root,-sys.maxsize,sys.maxsize)


# time complexity: O(n),O(n)
# space complexity: O(n),O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = input().strip().split()
        root = BinaryTree().createBinrayTree(arr)
        print(Solution().isValidBST(root))
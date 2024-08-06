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
    def insertIntoBST(self, root: Optional[TreeNode], val: int):
        if(root==None):return TreeNode(val)
        temp = root
        while(True):
            if(temp.val<val):
                if(temp.right==None):
                    temp.right = TreeNode(val)
                    break
                temp = temp.right
            elif(temp.val>val):
                if(temp.left==None):
                    temp.left = TreeNode(val)
                    break
                temp = temp.left
        return root
        
            
# time complexity: O(logn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = input().strip().split()
        root = BinaryTree().createBinrayTree(arr)
        # printBinaryTree(root)
        x = int(input().strip())
        root = Solution().insertIntoBST(root,x)
        printBinaryTree(root)
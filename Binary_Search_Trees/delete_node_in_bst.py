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
    def deleteNode(self, root: Optional[TreeNode], key: int):
        parent = None
        cur = root
        while(cur and cur.val!=key ):
            parent = cur
            if(cur.val<key):cur=cur.right
            else:cur=cur.left
        if(cur==None):return root

        if(cur.left and cur.right):
            temp = cur.left
            while(temp.right):temp = temp.right
            temp.right = cur.right
            if(parent==None):
                newroot = cur.left
                cur.left = None
                cur.right = None
                return newroot
            else:
                if(parent.left==cur):parent.left = cur.left
                else:parent.right = cur.left
                cur.left = None
                cur.right = None
                return root
        
        child = cur.left if cur.left else cur.right
        if(parent==None):return child
        if(parent.left==cur):parent.left = child
        else:parent.right = child
        cur.left = None
        cur.right = None
        return root

# time complexity: O(logn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = input().strip().split()
        root = BinaryTree().createBinrayTree(arr)
        # printBinaryTree(root)
        x = int(input().strip())
        root = Solution().deleteNode(root,x)
        printBinaryTree(root)
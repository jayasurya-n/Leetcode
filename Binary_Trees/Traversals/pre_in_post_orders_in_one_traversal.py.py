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
    def allTraversals(self, root):
        if(root==None):return None
        preorder = []
        inorder = []
        postorder = []
        stack = [(root,1)]

        while(stack):
            cur,i = stack.pop()
            if(i==1):
                preorder.append(cur.val)
                stack.append((cur,2))
                if(cur.left):stack.append((cur.left,1))
            elif(i==2):
                inorder.append(cur.val)
                stack.append((cur,3))
                if(cur.right):stack.append((cur.right,1))
            elif(i==3):
                postorder.append(cur.val)
        return preorder,inorder,postorder 
            
        
# time complexity: O(n)
# space complexity: O(n(max height of the tree))
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = input().strip().split()
        root = BinaryTree().createBinrayTree(arr)
        print(Solution().allTraversals(root))
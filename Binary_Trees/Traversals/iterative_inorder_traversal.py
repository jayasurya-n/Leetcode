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
    def inorderTraversal(self, root) -> List[int]:
        stack = []
        ans = []
        cur = root
        while(True):
            if(cur!=None):
                stack.append(cur)
                cur = cur.left
            else:
                if(stack==[]):break
                cur = stack.pop()
                ans.append(cur.val)
                cur = cur.right
        return ans
            

# time complexity: O(n)
# space complexity: O(n(max height of the tree))
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = input().strip().split()
        root = BinaryTree().createBinrayTree(arr)
        print(Solution().inorderTraversal(root))
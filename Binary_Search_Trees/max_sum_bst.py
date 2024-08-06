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
    def maxSumBST(self, root: Optional[TreeNode]):
        self.ans = -sys.maxsize
        def findmaxSum(node):
            if(node==None):
                return 0,-sys.maxsize,sys.maxsize
            sum1,largest1,smallest1 = findmaxSum(node.left)
            sum2,largest2,smallest2 = findmaxSum(node.right)
            
            if(largest1<node.val and node.val<smallest2):
                self.ans= max(self.ans,sum1+sum2+node.val)
                return sum1+sum2+node.val,max(largest2,node.val),min(smallest1,node.val)
            
            return sum1+sum2+node.val, sys.maxsize,-sys.maxsize

        findmaxSum(root)
        return max(self.ans,0)


# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = input().strip().split()
        root = BinaryTree().createBinrayTree(arr)
        print(Solution().maxSumBST(root))
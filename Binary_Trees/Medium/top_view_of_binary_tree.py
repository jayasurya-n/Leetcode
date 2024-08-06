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
       def topView(self,root):
        if(root==None):return []
        map = dict()
        q = deque([(root,0,0)])

        while(q):
            size = len(q)
            for _ in range(size):
                node,i,j = q.popleft()
                if(j not in map):map[j] = node.val
                
                if(node.left):q.append((node.left,i+1,j-1))
                if(node.right):q.append((node.right,i+1,j+1))
        
        return [x[1] for x in sorted(map.items())]
        

# time complexity: O(nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = input().strip().split()
        for i in range(len(arr)):
            if(arr[i]!="None"):arr[i]=int(arr[i])
        root = BinaryTree().createBinrayTree(0,None,arr)
        print(Solution().topView(root))
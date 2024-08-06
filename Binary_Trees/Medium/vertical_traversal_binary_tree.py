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
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root==None):return None
        map = dict()
        q = deque([(root,0,0)])

        while(q):
            size = len(q)
            temp = dict()
            for _ in range(size):
                node,i,j = q.popleft()
                if(j in temp):temp[j].append(node.val)
                else:temp[j] = [node.val]
                
                if(node.left):q.append((node.left,i+1,j-1))
                if(node.right):q.append((node.right,i+1,j+1))
            
            for key in temp:
                temp[key].sort()
                if(key in map):map[key].extend(temp[key])
                else:map[key] = temp[key]
        
        return [x[1] for x in sorted(map.items())]
        

# time complexity: O(nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = input().strip().split()
        for i in range(len(arr)):
            if(arr[i]!="None"):arr[i]=int(arr[i])
        root = BinaryTree().createBinrayTree(0,None,arr)
        print(Solution().verticalTraversal(root))
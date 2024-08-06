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

class BSTIterator:
    
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while(root):
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        temp = node.right

        while(temp):
            self.stack.append(temp)
            temp = temp.left
        return node.val

    def hasNext(self):
        return self.stack!=[]

# time complexity: O(1(n elements/n 'next' calls))
# space complexity: O(h)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = input().strip().split()
        root = BinaryTree().createBinrayTree(arr)
        ope = list(map(int,input().strip().split()))
        ans = []
        for i in ope:
            if(i=='BSTIterator'):
                obj = BSTIterator(root)
                ans.append('null')
            elif(i=='next'):ans.append(obj.next())
            elif(i=='hasNext'):ans.append(obj.hasNext())
        print(ans)
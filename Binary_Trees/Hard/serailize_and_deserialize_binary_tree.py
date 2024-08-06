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
    def serialize(self, root):
        q = deque([root])
        data = []
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if(node):data.append(str(node.val))
                else:data.append('#')
                if(node):
                    q.append(node.left)
                    q.append(node.right)
        return ",".join(data)
        

    def deserialize(self, data):   
        if(data=="#"):return None  
        data = data.split(',')

        root = TreeNode(int(data[0]))
        q=deque([root])

        i = 1
        while(q):
            node = q.popleft()
            if(i<len(data)):
                if(data[i]!='#'):
                    node.left = TreeNode(int(data[i]))
                    q.append(node.left)
                i+=1

                if(data[i]!='#'):
                    node.right = TreeNode(int(data[i]))
                    q.append(node.right)
                i+=1
        return root


# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        data = input().strip()
        root = Solution().deserialize(data)
        printBinaryTree(root)
        print()
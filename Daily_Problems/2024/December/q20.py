from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

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
    q = deque([root])
    print("Binary Tree:", end=" ")
    while q:
        node = q.popleft()
        print(node.val,end=" ")
        if(node.left):q.append(node.left)
        if(node.right):q.append(node.right)
    print()


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # level = 0
        # q = deque([root])
        
        # while(q):
        #     curr = []
        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         curr.append(node)
        #         if(node.left):q.append(node.left)
        #         if(node.right):q.append(node.right)

        #     if(level%2==1):
        #         values = [node.val for node in curr][::-1]
        #         for i,node in enumerate(curr):node.val = values[i]
        #     level+=1
        # return root
        def reverse(left,right,level):
            if(left==None or right==None):return 
            if(level%2==0):
                temp = left.val
                left.val = right.val
                right.val = temp
            
            reverse(left.left,right.right,level+1)
            reverse(left.right,right.left,level+1)
        reverse(root.left,root.right,0)
        return root
        
# time complexity: O(n),O(n)
# space complexity: O(n),O(logn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = list(map(int,input().strip().split()))
        root = BinaryTree().createBinrayTree(arr)
        printBinaryTree(root)
        root = Solution().reverseOddLevels(root)
        printBinaryTree(root)
        
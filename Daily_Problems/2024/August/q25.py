from typing import List,Optional
from collections import deque
import sys, math, heapq

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
    print(root.val,end = " ")
    printBinaryTree(root.left)
    printBinaryTree(root.right)


class Solution:
    # def postorderTraversal(self, root: Optional[TreeNode]):
    #     ans = []
    #     def dfs(node):
    #         if(node==None):return 
    #         dfs(node.left)
    #         dfs(node.right)
    #         ans.append(node.val)
    #     dfs(root)
    #     return ans
    
    # def postorderTraversal(self, root: Optional[TreeNode]):
    #     if(root==None):return []
    #     stack = [root]
    #     ans = []
    #     while stack:
    #         node = stack.pop()
    #         ans.append(node.val)
    #         if(node.left):stack.append(node.left)
    #         if(node.right):stack.append(node.right)
    #     return ans[::-1]
    
    def postorderTraversal(self, root: Optional[TreeNode]):
        if(root==None):return []
        stack1 = [root]
        stack2 = []
        ans = []
        
        while(stack1):
            root = stack1[-1]
            
            if stack2 and stack2[-1]==root:
                ans.append(root.val)
                stack1.pop()
                stack2.pop()
            
            else:
                stack2.append(root)
                if(root.right):stack1.append(root.right)
                if(root.left):stack1.append(root.left)
        return ans
                
# time complexity: O(n),O(n),O(n)
# space complexity: O(h),O(h),O(2h)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = input().strip().split()
        root = BinaryTree().createBinrayTree(arr)
        print(Solution().postorderTraversal(root))
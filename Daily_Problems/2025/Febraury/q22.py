from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # n = len(traversal)
        # def dfs(depth):
        #     if(self.ind>=n):return None
            
        #     cnt = 0
        #     while(self.ind+cnt<n and traversal[self.ind+cnt]=='-'):cnt+=1

        #     if(cnt!=depth):return None
        #     self.ind+=cnt
            
        #     digit = 0
        #     while(self.ind<n and traversal[self.ind].isdigit()):
        #         digit=10*digit+int(traversal[self.ind])
        #         self.ind+=1
            
        #     node = TreeNode(digit)
        #     node.left = dfs(depth+1)
        #     node.right = dfs(depth+1)
        #     return node
    
        # self.ind = 0
        # return dfs(0)
        
        n = len(traversal)
        stack = []
        i = 0
        while i<n:
            depth = 0
            while(i<n and traversal[i]=='-'):
                depth+=1
                i+=1
            
            digit = 0
            while(i<n and traversal[i].isdigit()):
                digit = 10*digit+int(traversal[i])
                i+=1
            
            while(len(stack)>depth):stack.pop()
            
            node = TreeNode(digit)
            if(stack):
                parent = stack[-1]
                if(parent.left==None):parent.left = node
                else:parent.right = node
            
            stack.append(node)
        return stack[0]
        
# time complexity: O(n),O(n)
# space complexity: O(n),O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        traversal = si()
        print(Solution().recoverFromPreorder(traversal))
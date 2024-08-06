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
    def distanceK(self, root: TreeNode, target: TreeNode, k: int):
        parent = dict()
        def dfs(node,par):
            if(node==None):return 
            parent[node] = par
            dfs(node.left,node)
            dfs(node.right,node)

        dfs(root,None)

        q = deque([target])
        visited = set([target])
        dist = 0
        while q:
            if(dist==k):
                return [x.val for x in q]
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                neighbour = [node.left,node.right,parent.get(node)]
                for i in neighbour:
                    if i and i not in visited:
                        q.append(i)
                        visited.add(i)
            dist+=1
        return []


# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = input().strip().split()
        for i in range(len(arr)):
            if(arr[i]!="None"):arr[i] = int(arr[i])
        root = BinaryTree().createBinrayTree(0,None,arr)
        target,k = list(map(int,input().strip().split()))
        print(Solution().distanceK(root,target,k))
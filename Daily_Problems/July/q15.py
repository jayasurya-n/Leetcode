# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List,Optional
import sys
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodeMap = dict()
        children = set()

        for i in range(len(descriptions)):
            parent = descriptions[i][0]
            child = descriptions[i][1]
            left = bool(descriptions[i][2])

            if parent not in nodeMap:
                nodeMap[parent] = TreeNode(parent)
            if child not in nodeMap:
                nodeMap[child] = TreeNode(child)
            
            if left:nodeMap[parent].left = nodeMap[child]
            else:nodeMap[parent].right = nodeMap[child]

            children.add(child)
        
        for node in nodeMap:
            if node not in children:
                return nodeMap[node]

            
# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))
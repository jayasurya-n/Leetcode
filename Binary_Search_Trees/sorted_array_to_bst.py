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
    def sortedArrayToBST(self, nums: List[int]):
        def createbst(nums,l,r):
            if(l>r):return None

            mid = (l+r)//2
            node = TreeNode(nums[mid])
            node.left = createbst(nums,l,mid-1)        
            node.right = createbst(nums,mid+1,r)
            return node 

        return createbst(nums,0,len(nums)-1)       

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        nums = list(map(int,input().strip().split()))
        root = Solution().sortedArrayToBST(nums)
        printBinaryTree(root)
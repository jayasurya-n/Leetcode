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
    # def bstFromPreorder(self, preorder: List[int]):
        # def getIndex(l,r):
        #     low,high = l+1,r
        #     while(low<=high):
        #         mid = (low+high)//2
        #         if(preorder[mid]>preorder[l]):high = mid-1
        #         else: low = mid+1
        #     return low

        # def createbst(l,r):
        #     if(l>r):return None
        #     elif(l==r):return TreeNode(preorder[l])

        #     node = TreeNode(preorder[l])
        #     index = getIndex(l,r)
        #     node.left = createbst(l+1,index-1)
        #     node.right = createbst(index,r)
        #     return node
        
        # return createbst(0,len(preorder)-1)
        
    def bstFromPreorder(self, preorder: List[int]):
        self.index = 0
        def createbst(lower,upper):
            if(self.index==len(preorder)):return None
            node = TreeNode(preorder[self.index])
            if(node.val<lower or node.val>upper):return None

            self.index+=1
            node.left = createbst(lower,node.val)
            node.right = createbst(node.val,upper)
            return node
        
        return createbst(-sys.maxsize,sys.maxsize)
        

# time complexity: O(nlogn),O(n)
# space complexity: O(1),O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        preorder = list(map(int,input().strip().split()))
        root = Solution().bstFromPreorder(preorder)
        printBinaryTree(root)
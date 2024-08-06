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
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     cur = root
    #     cnt = 0
    #     while(cur):
    #         if(cur.left==None):
    #             cnt+=1
    #             if(cnt==k):return cur.val
    #             cur = cur.right
    #         else:
    #             temp = cur.left
    #             while(temp.right and temp.right!=cur):
    #                 temp = temp.right

    #             if(temp.right==None):
    #                 temp.right = cur
    #                 cur = cur.left
    #             else:
    #                 temp.right = None
    #                 cnt+=1
    #                 if(cnt==k):return cur.val
    #                 cur = cur.right 

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node,cnt):
            if(node==None):return
            inorder(node.left,cnt)
            cnt[0]+=1
            if(cnt[0]==k):
                cnt[1] = node.val
            inorder(node.right,cnt)
        
        cnt = [0,None]
        inorder(root,cnt)
        return cnt[1]            

# time complexity: O(n),O(n)
# space complexity: O(1),O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = input().strip().split()
        root = BinaryTree().createBinrayTree(arr)
        x = int(input().strip())
        print(Solution().kthSmallest(root,x))
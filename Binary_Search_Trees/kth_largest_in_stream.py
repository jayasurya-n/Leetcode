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


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.root = None
        self.k = k
        for i in range(len(nums)):
            self.root = self.insert(self.root,nums[i])

        
    def insert(self,root,x):
        if(root==None):return TreeNode(x)
        
        node = root
        while(True):
            if(node.val>x):
                if(node.left==None):
                    node.left = TreeNode(x)
                    break
                node = node.left
            else:
                if(node.right==None):
                    node.right = TreeNode(x)
                    break
                node = node.right
        return root
                
    def getKthlargest(self,root,k):
            cur = root
            cnt = 0
            while(cur):
                if(cur.right==None):
                    cnt+=1
                    if(cnt==k):ans = cur.val
                    cur = cur.left
                else:
                    temp = cur.right
                    while(temp.left and temp.left!=cur):
                        temp = temp.left

                    if(temp.left==None):
                        temp.left = cur
                        cur = cur.right
                    else:
                        temp.left = None
                        cnt+=1
                        if(cnt==k):ans = cur.val
                        cur = cur.left
            return ans

    def add(self, val: int):
        self.root = self.insert(self.root,val)
        return self.getKthlargest(self.root,self.k)


# time complexity: O(nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        obj = KthLargest(2,[3,4,5,8,2])
        k = 2
        arr = list(map(int,input().strip().split()))

        for x in arr:
            root = obj.insert(obj.root,x)
            print("kth largest:",obj.getKthlargest(obj.root,k))
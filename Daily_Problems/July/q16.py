class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        lca = self.findLCA(root, startValue, destValue)
        
        startPath = []
        self.findPath(lca, startValue, [], startPath)
        
        destPath = []
        self.findPath(lca, destValue, [], destPath)
        
        startPath = ['U'] * len(startPath[0])        
        return ''.join(startPath + destPath[0])
    
    def findLCA(self, root: TreeNode, p: int, q: int) -> TreeNode:
        if not root:
            return None
        if root.val == p or root.val == q:
            return root
        left = self.findLCA(root.left, p, q)
        right = self.findLCA(root.right, p, q)
        if left and right:
            return root
        return left if left else right
    
    def findPath(self, root: TreeNode, target: int, path: list, result: list) -> bool:
        if not root:
            return False
        if root.val == target:
            result.append(path.copy())
            return True
        path.append('L')
        if self.findPath(root.left, target, path, result):
            return True
        path.pop()
        
        path.append('R')
        if self.findPath(root.right, target, path, result):
            return True
        path.pop()
        
        return False



# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        root = list(map(int,input().strip().split()))
        startValue, destValue = list(map(int,input().strip().split()))
        print(Solution().getDirections(root,startValue,destValue))
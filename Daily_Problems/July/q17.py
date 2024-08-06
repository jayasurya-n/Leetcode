from typing import List,Optional
import sys
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        forest = []

        def dfs(node, is_root):
            if not node:
                return None
            root_deleted = node.val in to_delete_set
            if is_root and not root_deleted:
                forest.append(node)
            node.left = dfs(node.left, root_deleted)
            node.right = dfs(node.right, root_deleted)
            return None if root_deleted else node

        dfs(root, True)
        return forest


# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        root = list(map(int,input().strip().split()))
        to_delete = list(map(int,input().strip().split()))
        print(Solution().delNodes(root,to_delete))
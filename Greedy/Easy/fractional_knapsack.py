from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        pass
        
            

# time complexity: O(nlogn+mlogm+n+m)
# space complexity:  
if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        g = list(map(int,input().strip().split()))
        s = list(map(int,input().strip().split()))
        print(Solution().findContentChildren(g,s))
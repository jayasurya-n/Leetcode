from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans=0
        i,j=0,0
        while(i<len(g) and j<len(s)):
            if(g[i]<=s[j]):
                ans+=1
                i+=1
                j+=1
            else:j+=1
        return ans
        
            

# time complexity: O(nlogn+mlogm+n+m)
# space complexity:  
if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        g = list(map(int,input().strip().split()))
        s = list(map(int,input().strip().split()))
        print(Solution().findContentChildren(g,s))
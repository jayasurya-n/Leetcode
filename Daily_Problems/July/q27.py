from typing import List,Optional
from collections import deque
import sys
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]):
        cost_data = [[sys.maxsize]*26 for _ in range(26)]
        for i in range(26):cost_data[i][i] = 0
        for i in range(len(cost)):
            cost_data[ord(original[i])-97][ord(changed[i])-97] = min(cost[i],
                                        cost_data[ord(original[i])-97][ord(changed[i])-97])
        
        for k in range(26):
            for i in range(26):
                    for j in range(26):
                        cost_data[i][j] = min(cost_data[i][j],cost_data[i][k]+cost_data[k][j])

        ans = 0
        for i in range(len(source)):
            if(cost_data[ord(source[i])-97][ord(target[i])-97]==sys.maxsize):return -1
            ans+=cost_data[ord(source[i])-97][ord(target[i])-97]
        return ans

# time complexity: O(m+n+26**3)
# space complexity: O(26**2)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))
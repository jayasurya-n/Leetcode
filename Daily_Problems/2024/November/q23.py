from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m,n = len(box),len(box[0])
        ans = []
        
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(box[j][i])
            ans.append(temp[::-1])
        
        for j in range(m):
            temp = n-1
            for i in range(n-1,-1,-1):
                if(ans[i][j]=='#'):
                    ans[i][j]='.'
                    ans[temp][j] = '#'
                    temp-=1
                elif(ans[i][j]=='*'):temp = i-1
        return ans

# time complexity: O(mn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))